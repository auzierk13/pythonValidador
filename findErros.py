import re


#grupo 1
inicioCorreto1 = open("parseCorreto1.txt", 'r', encoding='UTF8')
inicioErrado1 = open("parseErrado1.txt", 'r', encoding='UTF8')


meioCorreto2 = open("parseCorreto2.txt", 'r', encoding='UTF8')
meioErrado2 = open("parseErrado2.txt", 'r', encoding='UTF8')


fimCorreto3 = open("parseCorreto3.txt", 'r', encoding='UTF8')
fimErrado3 = open("parseErrado3.txt", 'r', encoding='UTF8')

spaceOfErrors =open("parseErrado4.txt", 'a+', encoding='UTF8')


log = open("log.txt", 'a', encoding='UTF8')

# arquivoErrado recebe o grupo de arquivos {certosX,erradoX} para busca de erros



def buscaErrosGenericosGrupo(arqCerto, arqErrado):
    arqCerto.seek(0)
    arqErrado.seek(0)

    print("Inicio da busca")
    for linhaErrada in arqErrado:
        #print(linhaErrada)
        linhaErrada = linhaErrada.rstrip() #Limpa linha em branco
        #print(linhaErrada)
        index,estadoErrado,siglaErrado,cidadeErrado = linhaErrada.split("|")
       

        linhaSemErros = False
        for linhaCerta in arqCerto:
            linhaCerta = linhaCerta.rstrip() #Limpa linha em branco
            estadoCorreta,siglaCorreta,cidadeCorreta = linhaCerta.split("|")
            #print("["+linhaErrada+"]["+linhaCerta+"]"+str((estadoErrado == estadoCorreta)) + str((siglaErrado == siglaCorreta))+ str((cidadeErrado == cidadeCorreta)))

            """
            if((estadoErrado != estadoCorreta) and (siglaErrado != siglaCorreta)):
                #print("Linha errrada "+linhaErrada+"\n")
                 break
            """

            if((estadoErrado == estadoCorreta) and (siglaErrado == siglaCorreta) and (cidadeErrado ==  cidadeCorreta)):
                #print("Não deveria imprimir no 4 ["+linhaErrada+"]["+linhaCerta+"]")
                linhaSemErros = True
                break
            
        arqCerto.seek(0)
        if(not linhaSemErros): #Foi encontrado algum erro
            print(linhaErrada)
            linhaSemErros = False
            spaceOfErrors.write(linhaErrada+"\n")
        
    print("Fim da busca") 
    #print(arqCerto)
    #print(arqErrado)

    arqCerto.seek(0)
    arqErrado.seek(0)
    
    arqCerto.close()
    arqErrado.close()


def erroSigla(dicEstados):
    print("Busca de erro nas siglas")
    #print(list(dicEstados.values()))
    listSiglas = list(dicEstados.values())
    listEstadosSigla = list(dicEstados.items())
    #print(listEstadosSigla)
    #print(len(listEstadosSigla))
    spaceOfErrors.seek(0)

    
    for siglaTest in spaceOfErrors:
        siglaTest = siglaTest.rstrip() #Limpa linha em branco
        index,estado,sigla,cidade = siglaTest.split("|")
        #print(index+" "+sigla)
        hasSiglaCorreta=False
        
        for siglaCorreta in listSiglas:
            if(siglaCorreta == sigla):
                hasSiglaCorreta=True #Sigla existe esta correta
                for estados in listEstadosSigla:
                    estadosValidos,siglaValidos = estados
                    if((estado==estadosValidos) and (sigla!=siglaValidos)):
                        error = index+"|Erro na linha "+index+"["+siglaTest+"]: Sigla "+sigla+" não confere com o estado deveria ser "+siglaValidos+"." 
                        print(error)
                        log.write(error+"\n")
                        break
    
                break #fim do loop listSiglas

        if(not hasSiglaCorreta):
            linhaSigla = estado+"|"+sigla+ "|"+cidade
            print(linhaSigla)
            if(len(sigla)!=2):
                if(len(sigla) < 2):
                    error = index+"|Erro na linha "+index+"["+linhaSigla+"]: Sigla "+sigla+" possui menos caracteres." 
                    print(error)
                    log.write(error+"\n")
                    
                else:
                    error= index+"|Erro na linha "+index+"["+linhaSigla+"]: Sigla "+sigla+" possui mais caracteres."
                    print(error)
                    log.write(error+"\n")
                    
            else:
                if(sigla.islower()):
                    error = index+"|Erro na linha "+index+"["+linhaSigla+"]: Sigla "+sigla+" estar em minusculo."
                    print(error)
                    log.write(error+"\n")
                else:
                    print("Erro "+index+" "+sigla)
                    error = index+"|Erro na linha "+index+"["+linhaSigla+"]:Sigla "+sigla+" nao existe." 
                    print(error)
                    log.write(error+"\n")
                    

            
        hasSiglaCorreta=False
        
    

    
    
def mainErrosGenericos(dicEstados):
   #Busca em grupo 1 
   buscaErrosGenericosGrupo(inicioCorreto1,inicioErrado1)

   #Busca em grupo 2
   #buscaErrosGenericosGrupo(meioCorreto2,meioErrado2)

   #Busca em grupo 3
   #buscaErrosGenericosGrupo(fimCorreto3,fimErrado3)

   erroSigla(dicEstados)
  

   
   spaceOfErrors.close()
   log.close()


    
    
    
