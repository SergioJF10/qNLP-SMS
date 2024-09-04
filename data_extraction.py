import pandas as pd
import json
import os
import shutil

def suma_uno(dic, conceptos):
    for concept in conceptos:
        # Preprocess
        concepto = concept.lower() if type(concept) == str else concept
        
        if type(concepto) == str and concepto.endswith(' '):
            concepto = concepto[:-1]
        elif type(concepto) == pd.Timestamp:
            concepto = str(concepto)

        # Suma 1
        if concepto in dic.keys():
            dic[concepto] += 1
        else:
            dic[concepto] = 1


class Digestor:
    def __init__(self, path='datos_sms.xlsx', sheet='Conteo'):
        self.df = pd.read_excel(path, sheet_name=sheet)
        self.len_code = self.df.loc[self.df['Ident.'] == 'T01'].index.tolist()[0]
        self.len_paper = self.df.shape[0] - self.len_code
        self.output = 'results\\'

        # Print Excel Info
        print(f'### FILE LOADED ###')
        print(f'\t- Name: {path}')
        print(f'\t- Sheet: {sheet}')
        print(f'\t- Num. Total Contributions: {self.df.shape[0]}')
        print(f'\t- Num. Code Contributions: {self.len_code}')
        print(f'\t- Num. Theoretical Contributions: {self.len_paper}')
        print(f'\t- Num. Features: {self.df.shape[1]}')

    def preg_inv(self):
        '''Conteos generales y partículares con el concepto/algoritmo utilizado'''
        features = ['Concepto (PI1)',
                    'Aplicación (PI2)',
                    'Lenguaje (PI3)',
                    'Tipo (DE1)',
                    'País (DE2)',
                    'Fecha (DE3)']

        for feature in features:
            print(f'> Procesando {feature}...')

            try:
                os.makedirs(f'.\\{self.output}{feature}')
            except FileExistsError:
                print(f'> Borrando archivos ya existentes en .\\{self.output}{feature}')
                shutil.rmtree(f'.\\{self.output}{feature}')
                os.makedirs(f'.\\{self.output}{feature}')

            feat_col = self.df[feature].tolist()

            conteos = {
                'general': dict(),
                'codigo': dict(),
                'papers': dict()
            }

            for i, item in enumerate(feat_col):
                try:
                    concepts = item.split(', ')
                except AttributeError:
                    if type(item) == pd.Timestamp:
                        concepts = [item]

                suma_uno(conteos['general'], concepts) # General
                if i < self.len_code: # Es código
                    suma_uno(conteos['codigo'], concepts)
                else: # Es teórico
                    suma_uno(conteos['papers'], concepts)

            for tipo in conteos.keys():
                tipo_file = open(f'{self.output}{feature}\\{tipo}.json', 'w', encoding='utf-8')
                sorted_tipo = dict(sorted(conteos[tipo].items(), key=lambda item: -item[1])) # Sort dictionary
                json.dump(sorted_tipo, tipo_file)
                print(f'\t* Conteo tipo {tipo} guardado en {self.output}{feature}\\{tipo}.json')


if __name__ == '__main__':
    print('>>>> DIGESTOR <<<<')
    digestor = Digestor()
    digestor.preg_inv()