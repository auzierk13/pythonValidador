import re
#Entrada de dados
estadosCidadesErrados  = open('Estados+CIdades(erro1).txt','r',encoding='UTF8')
estadosCidadesCorretos = open('Estados+CIdades.txt','r', encoding='UTF8')
log = open("log.txt", 'w', encoding='UTF8')
aux = open("parse.txt", 'w', encoding='UTF8')


print("Metodo read () : \n")

#buscaformat = re.compile(r'\w[a-zA-Z0-9]{1,} ?\|[a-zA-Z0-9]{1,}\|[a-zA-Z0-9]{1,}')
buscaformat = re.compile(r'.{1,}\|.{1,}\|.{1,}')
arqCorretos = estadosCidadesCorretos.readlines()
arqErrados = estadosCidadesErrados.readlines()

indexLinha=0
for linha in estadosCidadesErrados:
    indexLinha+=1
    linha = linha.rstrip() #Limpa linha em branco

    
    ##*****Linha em branco *****##
    if(linha == ""):
        #print("Linha em branco")
        error = "Erro na linha "+str(indexLinha) +":Linha em Branco\n"
        print(error)
        log.write(error)
        continue
    ##*****End Linha em branco *****##


    ##*****Verifica formato do texto*****##
    resultado = buscaformat.search(linha)

    if (not resultado):
        print("Erro na linha "+str(indexLinha)+"["+ linha + "] Erro no formato. Formato esperado *|*|*\n")
        continue
        
    ##*****Verifica formato do texto*****##
    
    estado,sigla,cidade = linha.split("|")
    hasEstado = False
    hasSigla = False
    hasEstadoSigla = False
    
    ##***** Sigla escrita errada *****##
    if(len(sigla)>2):
        error ="Erro na linha "+str(indexLinha) +": Sigla["+sigla+"]  escrita errada com > 2 letras\n"
        print(error)
        log.write(error)
        hasSigla=True
    if(len(sigla) <2):
        error= "Erro na linha "+str(indexLinha) +": Sigla["+sigla+"] escrita errada com < 2 letras\n"
        print(error)
        log.write(error)
        hasSigla=True
    ##***** End Sigla escrita errada *****#
    
    print(len(arqCorretos))
    teste= "r'"+linha+ "'"
    print("Vai ")
    print(teste)
    """    
    for linhaCerta in estadosCidadesCorretos:
        #linhaCerta = linhaCerta.rstrip() #Limpa linha em branco
        ##******Estado Correto********##
        if(linha.find(linhaCerta)!= -1): #print("Estado correto")
            #print("Estado correto")
            #print(str(indexLinha) +" "+linha+": "+linhaCerta)
            hasEstadoSigla=True

            break
        ##******End Estado Correto ****##
    if(not hasEstadoSigla):
       aux.write(linha+"\n")
    estadosCidadesCorretos.seek(0) #Volta para o
    """
"""
        estadoCorreto,siglaCorreta,cidadeCorreta = linhaCerta.split("|")
        ##***** Estado encontrado *****##
        if(estado == estadoCorreto ):
            hasEstado= True
            if((not hasSigla) and sigla!= siglaCorreta):
                 hasSigla =True
                 error = "Erro na linha "+str(indexLinha) +":["+sigla+ "] nao pertence ao estado " +estadoCorreto+". Sigla esperada "+siglaCorreta +"\n"
                 print(error)
                 log.write(error)
            
        ##***** End encontrado *****#

        ##***** Erro na escrita estado *****##
        if((not hasEstado) and estado.find(estadoCorreto)!= -1):
            hasEstado= True
            error = "Erro na linha "+str(indexLinha) +":["+estado+ "] Estado escrito errado com mais palavras. Talvez queira dizer ["+estadoCorreto+"]\n"
            print(error)
            log.write(error)
        #Mato Grosso Mato Grosso do Sul

       
        if((not hasEstado) and estadoCorreto.find(estado)!= -1 ):
            hasEstado= True
            error="Erro na linha "+str(indexLinha) +":["+estado+ "] Estado escrito com menos palavras. Talvez queira dizer ["+estadoCorreto+"]\n"
            print(error)
            log.write(error)
        
       

        ##***** Sigla não existe (Duas letra mais sigla não encontrado)*****##    
        if(sigla == siglaCorreta):
            hasSigla=True
        ##***** End Sigla não existe (Duas letra mais sigla não encontrado)*****##    
"""
    
  

estadosCidadesErrados.close()
estadosCidadesCorretos.close()
log.close()
aux.close()
