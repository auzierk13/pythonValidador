estadosCidadesErrados  = open('Estados+CIdades(erro).txt','r',encoding='UTF8')
estadosCidadesCorretos = open('Estados+CIdades.txt','r', encoding='UTF8')


print("Metodo read () : \n")
#Entrada de dados
arqCorreto= estadosCidadesCorretos.readlines()
arqErrado= estadosCidadesErrados.readlines()

indexLinha=0
for linha in arqErrado:
    indexLinha+=1
    linha = linha.rstrip() #Limpa linha em branco
    for linhaCerta in arqCorreto:
        linhaCerta = linhaCerta.rstrip() #Limpa linha em branco
        ##******Estado Correto********##
        if(linha.find(linhaCerta)!= -1): #print("Estado correto")
            print("Estado correto")
            print(str(indexLinha) +" "+linha+": "+linhaCerta)
            break
        ##******End Estado Correto ****##
        ##*****Linha em branco *****##
        if(linha == ""):
            print("Linha em branco")
            print("Erro na linha "+str(indexLinha) +" :Linha em Branco")
            break
        ##*****End Linha em branco *****##
        else:
            if indexLinha > 50:
                break
    estadosCidadesCorretos.seek(0) #Volta para o inicio do arquivo
    """
    if indexLinha > 50:
        break
    """ 

estadosCidadesErrados.close
estadosCidadesCorretos.close
