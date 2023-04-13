from local import *
def criacaoPaginas(listaTexto, vetorIndice):
    import shutil
    
    #import os
    for num in range(0,len(vetorIndice)):
        nomePagina = str("pagina" + str(num) + ".html")
        
        pagina = open(nomePagina, "w", encoding="UTF-8")
        pagina.write("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta name="keywords" content="fbtech, Primesite, HTML, CSS, Javascript">
                <link rel="stylesheet" href="C:\\Users\\1227.332\\Desktop\\Trabalho final de Analise de Dados\\css\\styles.css">
                <title>FBIT - Texto</title>
            </head>
            <body>


            <nav>
                <a href="index.html">FB_IT</a>
                <a href="FB_Tech.html" target="_self" title="FB_Tech" >FB_Tech</a>
                <a href="">Base de Dados</a>
                <a href="creditos.html">Creditos</a>
                
            </nav>

            <div class="container-flex">
                <div class="leftbar">
                    <h1>Texto %d</h1>
                    

                </div>
                <div>
                    <div class="card">
                        <h2>Texto %d</h2>
                    <p>%s</p>
                    </div>
                </div>
            </div>
            <div class="bottom-bar">
            <footer>
                <a id="footercreditos">FBtech 2022. Todos os direitos reservados.</a>
            </footer>
            </div>

            </body>
            </html> 
        """ %(num + 1, num + 1, listaTexto[vetorIndice[num]-1]))
        pagina.close()
        localArquivo = os.getcwd() + "\pagina" + str(num) + ".html"
        destino = local = os.getcwd() + "\paginas-html"
        shutil.move(localArquivo,destino)

def criacaoResultados(listaTexto, vetorIndice):
    import shutil
    #import os
    
    nomePagina = str("resultado.html")
    
    pagina = open(nomePagina, "w", encoding="UTF-8")
    pagina.write("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="keywords" content="fbtech, Primesite, HTML, CSS, Javascript">
            <link rel="stylesheet" href="css/styles.css">
            <title>FBIT - Resultado</title>
            <script>
                for(var num; num<1; num++){
                    location. reload()
                    }
                </script>
        </head>
        <body>


        <nav>
            <a href="index.html">FB_BIT</a>
            <a href="FB_Tech.html" target="_self" title="FB_Tech" >FB_Tech</a>
            <a href="">Base de Dados</a>
            <a href="creditos.html">Creditos</a>
            
        </nav>

        <div class="container-flex">
            <div class="leftbar">
                <h1>Bem vindo ao Primesite da _FBtech</h1>
            </div>
        <div> 
    """)
    numPage = 0
    if vetorIndice == []:
        pagina.write("""
        <div class="card">
            <h3>NENHUM RESULTADO ENCONTRADO</h3>
            
        </div>
        """)
        pass
    for i in vetorIndice:
        
        pagina.write("""
            <div class="card">
            <h3><a href="paginas de texto html/%s" class="text">%s.....</a></h3>
            
            </div>
""" %("pagina" + str(numPage) + ".html", listaTexto[vetorIndice[numPage]-1][:120]))
        numPage += 1
    pagina.write("""
           </div>
            </div>
            <div class="bottom-bar">
            <footer>
                <a id="footercreditos">FBtech 2022. Todos os direitos reservados.</a>
            </footer>
            </div>

            </body>
            </html> 
    """)    
    #%(listaTexto[vetorIndice[num]-1]))
    pagina.close()
    #'''localArquivo = r"C:\Users\1227.332\Desktop\Trabalho final de Analise de Dados\resultado.html
    #destino = r"C:\Users\1227.332\Desktop\Trabalho final de Analise de Dados\paginas de texto html"
    #shutil.move(localArquivo,destino)'''