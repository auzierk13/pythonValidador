estadosCidadesErrados  = open('Estados+CIdades(erro1).txt','r',encoding='UTF8')
estadosCidadesCorretos = open('Estados+CIdades.txt','r', encoding='UTF8')


print("Metodo read () : \n")
#Entrada de dados
arqCorreto= estadosCidadesCorretos.readlines()
arqErrado= estadosCidadesErrados.readlines()

indexLinha=0
for linha in arqErrado:
    indexLinha+=1
    linha = linha.rstrip() #Limpa linha em branco
    
    ##*****Linha em branco *****##
    if(linha == ""):
        #print("Linha em branco")
        print("Erro na linha "+str(indexLinha) +":Linha em Branco")
        continue
    ##*****End Linha em branco *****##
    estado,sigla,cidade = linha.split("|")
    hasEstado = False
    hasSigla = False

    ##***** Sigla escrita errada *****##
    if(len(sigla)>2):
        print("Erro na linha "+str(indexLinha) +":"+sigla+" sigla escrita errada com > 2 letras")
        hasSigla=True
    if(len(sigla) <2):
        print("Erro na linha "+str(indexLinha) +":"+sigla+" sigla escrita errada com < 2 letras")
        hasSigla=True
    ##***** End Sigla escrita errada *****#
        
    for linhaCerta in arqCorreto:
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
            print("Erro na linha "+str(indexLinha) +":"+estado+ " Estado escrito errado com mais palavras. Talvez queira dizer ["+estadoCorreto+"]")
        
        if((not hasEstado) and estadoCorreto.find(estado)!= -1 ):
            hasEstado= True
            print("Erro na linha "+str(indexLinha) +":"+estado+ " Estado escrito com menos palavras. Talvez queira dizer ["+estadoCorreto+"]")
        


        ##***** Sigla não existe (Duas letra mais sigla não encontrado)*****##    
        if(sigla == siglaCorreta):
            hasSigla=True
        ##***** End Sigla não existe (Duas letra mais sigla não encontrado)*****##    

    
    estadosCidadesCorretos.seek(0) #Volta para o inicio do arquivo
    if(not hasEstado):
        print("Erro na linha "+str(indexLinha) +":"+estado+ " Estado nao exite")
        hasEstado = False
    if(not hasSigla):
        print("Erro na linha "+str(indexLinha) +":"+sigla+ " sigla nao encontrada")
        hasSigla = False
 

estadosCidadesErrados.close
estadosCidadesCorretos.close
