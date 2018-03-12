import re


#grupo 1
inicioCorreto1 = open("parseCorreto1.txt", 'r', encoding='UTF8')
inicioErrado1 = open("parseErrado1.txt", 'r', encoding='UTF8')


meioCorreto2 = open("parseCorreto2.txt", 'r', encoding='UTF8')
meioErrado2 = open("parseErrado2.txt", 'r', encoding='UTF8')


fimCorreto3 = open("parseCorreto3.txt", 'r', encoding='UTF8')
fimErrado3 = open("parseErrado3.txt", 'r', encoding='UTF8')

sobraErrado4 =open("parseErrado4.txt", 'a', encoding='UTF8')

log = open("log.txt", 'w', encoding='UTF8')

# arquivoErrado recebe o grupo de arquivos {certosX,erradoX} para busca de erros



def buscaErrosGenericosGrupo(arqCerto, arqErrado):
    arqCerto.seek(0)
    arqErrado.seek(0)

    
    for linhaErrada in arqErrado:
        #print(linhaErrada)
        linhaErrada = linhaErrada.rstrip() #Limpa linha em branco
        indexLinha,estadoErrado,siglaErrado,cidadeErrado = linhaErrada.split("|")
       

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
        if(not linhaSemErros):
            print(linhaErrada+"\n")
            linhaSemErros = False
            sobraErrado4.write(linhaErrada+"\n")
        
        
    print(arqCerto)
    print(arqErrado)

    arqCerto.seek(0)
    arqErrado.seek(0)
    
    arqCerto.close()
    arqErrado.close()



    
def mainErrosGenericos():
   #Busca em grupo 1 
   buscaErrosGenericosGrupo(inicioCorreto1,inicioErrado1)

   buscaErrosGenericosGrupo(meioCorreto2,meioErrado2)
   
   buscaErrosGenericosGrupo(fimCorreto3,fimErrado3)
   
   sobraErrado4.close()
   log.close()


    
    
    
