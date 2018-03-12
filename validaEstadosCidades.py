import findErros
import splitEstados
#Entrada de dados

estadosCidadesCorretos = open('Estados+CIdades.txt','r', encoding='UTF8')




print("Metodo read () : \n")

#cria dicionario de estados_Cidades
dicEstados = {}

def povoarDicionario():
    for linhaCerta in estadosCidadesCorretos:
        linhaCerta = linhaCerta.rstrip() #Limpa linha em branco
        estadoCorreto,siglaCorreta,cidadeCorreta = linhaCerta.split("|")
        dicHasEstado=False
        #print("Adicionando estados: "+ str(len(estados)))
   
        if(len(dicEstados)== 0): #primeiro termo
            dicEstados[estadoCorreto]=siglaCorreta
            continue
        for estados in dicEstados:
            if(estadoCorreto == estados):
                dicHasEstado=True
                break

        if(not dicHasEstado):
            dicEstados[estadoCorreto]=siglaCorreta
    estadosCidadesCorretos.seek(0) #Volta para inicio do arquivo
    estadosCidadesCorretos.close()
    #*** Fim de povoar dicionario


        
povoarDicionario()
#print(len(dicEstados))
splitEstados.povoar3ArquivoEstadosCorretos(dicEstados)
splitEstados.povoar3ArquivoEstadosErrados(dicEstados)

findErros.mainErrosGenericos(dicEstados)



