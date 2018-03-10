import re
#Entrada de dados
estadosCidadesErrados  = open('Estados+CIdades(erro1).txt','r',encoding='UTF8')
estadosCidadesCorretos = open('Estados+CIdades.txt','r', encoding='UTF8')
log = open("log.txt", 'w', encoding='UTF8')

print("Metodo read () : \n")

#buscaformat = re.compile(r'\w[a-zA-Z0-9]{1,} ?\|[a-zA-Z0-9]{1,}\|[a-zA-Z0-9]{1,}')
buscaformat = re.compile(r'.{1,}\|.{1,}\|.{1,}')

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
        
    for linhaCerta in estadosCidadesCorretos:
        linhaCerta = linhaCerta.rstrip() #Limpa linha em branco
        ##******Estado Correto********##
        if(linha.find(linhaCerta)!= -1): #print("Estado correto")
            #print("Estado correto")
            #print(str(indexLinha) +" "+linha+": "+linhaCerta)
            hasEstado = True #Existe Estado 
            hasSigla=True #Existe Sigla 
            break
        ##******End Estado Correto ****##

        estadoCorreto,siglaCorreta,cidadeCorreta = linhaCerta.split("|")
        ##***** Estado encontrado *****##
        if(estado == estadoCorreto ):
            hasEstado= True
        ##***** End encontrado *****#

        ##***** Erro na escrita estado *****##
        if((not hasEstado) and estado.find(estadoCorreto)!= -1):
            hasEstado= True
            error = "Erro na linha "+str(indexLinha) +":["+estado+ "] Estado escrito errado com mais palavras. Talvez queira dizer ["+estadoCorreto+"]\n"
            print(error)
            log.write(error)
        #Mato Grosso Mato Grosso do Sul
        """
        if((not hasEstado) and estadoCorreto.find(estado)!= -1 ):
            hasEstado= True
            error="Erro na linha "+str(indexLinha) +":["+estado+ "] Estado escrito com menos palavras. Talvez queira dizer ["+estadoCorreto+"]\n"
            print(error)
            log.write(error)
        
        """

        ##***** Sigla não existe (Duas letra mais sigla não encontrado)*****##    
        if(sigla == siglaCorreta):
            hasSigla=True
        ##***** End Sigla não existe (Duas letra mais sigla não encontrado)*****##    

    
    estadosCidadesCorretos.seek(0) #Volta para o inicio do arquivo
    if(not hasEstado):
        error = "Erro na linha "+str(indexLinha) +":Estado ["+estado+ "] nao exite\n" 
        print(error)
        log.write(error)
        hasEstado = False
    if(not hasSigla):
        error = "Erro na linha "+str(indexLinha) +":["+sigla+ "] sigla nao encontrada\n"
        print(error)
        hasSigla = False
 

estadosCidadesErrados.close()
estadosCidadesCorretos.close()
log.close()
