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
        break
    ##*****End Linha em branco *****##
    estado,sigla,cidade = linha.split("|")
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
            hasSigla=True #Existe Sigla 
            break
        ##******End Estado Correto ****##

        estadoCorreto,siglaCorreta,cidadeCorreta = linhaCerta.split("|")
        if(sigla == siglaCorreta):
            hasSigla=True
            


        


        
        ##***** Sigla não existe (Duas letra mais sigla não encontrado)*****##
            
            
        ##***** Sigla não existe (Duas letra mais sigla não encontrado)*****##


        

    
    estadosCidadesCorretos.seek(0) #Volta para o inicio do arquivo
    if(not hasSigla):
        print("Erro na linha "+str(indexLinha) +":"+sigla+ " sigla nao encontrada")
        hasSigla = False
    """
    if indexLinha > 50:
        break
    """ 

estadosCidadesErrados.close
estadosCidadesCorretos.close
