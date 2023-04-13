
from programa import *
from local import *
        
import os
import shutil



nomePagina = str("resultado.html")

pagina = open(nomePagina, "w", encoding="UTF-8")
pagina.write("""
    <!DOCTYPE html>
    <html lang="pt">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body> 
        <script>
            location. reload()
        </script>
        </body>
        </html>""")
pagina.close()
cond = 0
localPaginas = os.getcwd() + "\paginas-html"
paginas = os.listdir(localPaginas)
try:
    
    if ".html" in paginas[0][-5:]:
        
                
        for pagina in paginas:
            os.remove(localPaginas + "\\" + pagina)
except IndexError:
    pass
while(cond == 0):
    localDownload = encontraLocalDownload()
    arquivos = os.listdir(localDownload)
    
    localPaginas = os.getcwd() + "\paginas-html"
    paginas = os.listdir(localPaginas)
    if "index.txt" in arquivos:
        os.remove(localDownload + "\index.txt")
        nomePagina = str("resultado.html")

        pagina = open(nomePagina, "w", encoding="UTF-8")
        pagina.write("""
            <!DOCTYPE html>
            <html lang="pt">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                </head>
                <body> 
                <script>
                    location. reload()
                </script>
                </body>
                </html>""")
        pagina.close()

    for arquivo in arquivos:
        if arquivo == "index.html":
            os.remove(localDownload + "\index.txt")
            nomePagina = str("resultado.html")

            pagina = open(nomePagina, "w", encoding="UTF-8")
            pagina.write("""
                <!DOCTYPE html>
                <html lang="pt">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Document</title>
                    </head>
                    <body> 
                    <script>
                        location. reload()
                    </script>
                    </body>
                    </html>""")
            pagina.close()
        if "pesquisa.txt" not in arquivos:
            continue
        if arquivo == "pesquisa.txt":
            #from programa import *
            
            try:
                if ".html" in paginas[0][-5:]:
                    for pagina in paginas:
                        os.remove(localPaginas + "\\" + pagina)
            except IndexError:
                pass
            
            executar()
            
            
            

    '''if cont == 1:
    from programa import *
    executar()
    if os.path.exists("pesquisa.txt"): 
        os.remove("pesquisa.txt")
    '''