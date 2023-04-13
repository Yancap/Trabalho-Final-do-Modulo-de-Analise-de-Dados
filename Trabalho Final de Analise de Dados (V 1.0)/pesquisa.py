from local import *

def pesquisaUsuario():
    import shutil
    import os
    #move o arquivo .txt da pasta downloads para a pasta do trabalho
    localArquivo = encontraLocalDownload() + "\pesquisa.txt"
    destino = os.getcwd()
    shutil.move(localArquivo,destino)

    #Abre o arquivo txt com o python
    with open("pesquisa.txt", "r", encoding="UTF-8") as arquivo:
        pesquisa = arquivo.readlines()


    
    if os.path.exists("pesquisa.txt"): 
        os.remove("pesquisa.txt")
    return pesquisa