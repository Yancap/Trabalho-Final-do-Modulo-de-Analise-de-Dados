def encontraLocalDownload():
    import os
    local = os.getcwd()
    localDownload = ""
    aux = 0
    for i in local:
        localDownload += i
        if (i == '\\'):
            aux += 1
        if aux == 3:
            localDownload += "Downloads"
            return(localDownload)
            
encontraLocalDownload()