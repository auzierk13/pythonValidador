import re

estadosCidadesCorretos = open('Estados+CIdades.txt','r', encoding='UTF8')
estadosCidadesErrados  = open('Estados+CIdades(erro).txt','r',encoding='UTF8')

inicioCorreto1 = open("parseCorreto1.txt", 'w', encoding='UTF8')
meioCorreto2 = open("parseCorreto2.txt", 'w', encoding='UTF8')
fimCorreto3 = open("parseCorreto3.txt", 'w', encoding='UTF8')

inicioErrado1 = open("parseErrado1.txt", 'w', encoding='UTF8')
meioErrado2 = open("parseErrado2.txt", 'w', encoding='UTF8')
fimErrado3 = open("parseErrado3.txt", 'w', encoding='UTF8')
sobraErrado4 =open("parseErrado4.txt", 'w', encoding='UTF8')

log = open("log.txt", 'w', encoding='UTF8')

#buscaformat = re.compile(r'\w[a-zA-Z0-9]{1,} ?\|[a-zA-Z0-9]{1,}\|[a-zA-Z0-9]{1,}')
buscaformat = re.compile(r'.{1,}\|.{1,}\|.{1,}')
def povoar3ArquivoEstadosCorretos(dicEstados):
    listChavesEstados = list(dicEstados.keys())
    # print(listChavesEstados[0])
    
    
    for linhaCerta in estadosCidadesCorretos:
        #linhaCerta = linhaCerta.rstrip() #Limpa linha em branco
        estadoCorreto,siglaCorreta,cidadeCorreta = linhaCerta.split("|")
        index=0
       #index =0 8
        
        for estado in listChavesEstados:
            if((estadoCorreto == estado) and (index>= 0 and index<= 8)):
                inicioCorreto1.write(linhaCerta)
                continue

            #index =9 17
            if((estadoCorreto == estado) and (index>= 9 and index<= 17)):
                meioCorreto2.write(linhaCerta)
                continue

            #index =18 26
            if((estadoCorreto == estado) and (index>= 18 and index<= 26)):
                fimCorreto3.write(linhaCerta)
                continue
            index+=1

    estadosCidadesCorretos.seek(0) #Volta para inicio
    estadosCidadesCorretos.close()
    inicioCorreto1.close()
    meioCorreto2.close()
    fimCorreto3.close()


def povoar3ArquivoEstadosErrados(dicEstados):
    listChavesEstados = list(dicEstados.keys())
    # print(listChavesEstados[0])
    
    indexLinha=0
    for linhaErrada in estadosCidadesErrados:
        #linhaErrada = linhaErrada.rstrip() #Limpa linha em branco
        if(linhaErrada == "\n"):
            #print("Linha em branco")
            error = str(indexLinha)+"|"+"Erro na linha "+str(indexLinha) +": Linha em Branco\n"
            print(error.rstrip())
            log.write(error)
            indexLinha+=1
            continue
        else:
            ##*****Verifica formato do texto*****##
            resultado = buscaformat.search(linhaErrada)

            if (not resultado):
                linhaErrada = linhaErrada.rstrip() #Limpa linha em branco
                error = str(indexLinha)+"|"+"Erro na linha "+str(indexLinha)+"["+ linhaErrada + "]: Erro no formato. Formato esperado *|*|*\n"
                print(error.rstrip())
                log.write(error)
                indexLinha+=1
                continue
        
        #print(linhaErrada)

        estadoErrado,siglaErrada,cidadeErrada = linhaErrada.split("|")
        indexEstado=0
        
            ##*****End Verifica formato do texto*****##
       #index =0 8
        hasEstado= False
        for estado in listChavesEstados: #Busca em lista de estados
            if((estadoErrado == estado) and (indexEstado>= 0 and indexEstado<= 8)):
                inicioErrado1.write(str(indexLinha)+"|"+linhaErrada)
                hasEstado= True #Estado encontrado
                continue

            #index =9 17
            if((estadoErrado == estado) and (indexEstado>= 9 and indexEstado<= 17)):
                meioErrado2.write(str(indexLinha)+"|"+linhaErrada)
                hasEstado= True #Estado encontrado
                continue

            #index =18 26
            if((estadoErrado == estado) and (indexEstado>= 18 and indexEstado<= 26)):
                fimErrado3.write(str(indexLinha)+"|"+linhaErrada)
                hasEstado= True #Estado encontrado
                continue
            indexEstado+=1
            
        if(not hasEstado): #Caso Estado não exite
            if(not (estadoErrado.istitle()) ): #Deve iniciar com maiusculo
                linhaErrada = linhaErrada.rstrip() #Limpa linha em branco
                error = str(indexLinha)+"|"+"Erro na linha "+str(indexLinha)+"["+ linhaErrada + "]: Erro na escrita. Estado deve iniciando com maiúsculo\n"
                sobraErrado4.write(str(indexLinha)+"|"+linhaErrada+"\n")
                print(error.rstrip())
                log.write(error)
            else:
                 sobraErrado4.write(str(indexLinha)+"|"+linhaErrada)
                 linhaErrada = linhaErrada.rstrip() #Limpa linha em branco
                 error = str(indexLinha)+"|"+"Erro na linha "+str(indexLinha)+"["+ linhaErrada + "]: Estado["+estadoErrado+"] Estado nao existe.\n"
                 print(error.rstrip())
                 log.write(error)
                 
        indexLinha+=1

    estadosCidadesErrados.seek(0) #Volta para inicio
    estadosCidadesErrados.close()
    inicioErrado1.close()
    meioErrado2.close()
    fimErrado3.close()
    sobraErrado4.close()
    log.close()
