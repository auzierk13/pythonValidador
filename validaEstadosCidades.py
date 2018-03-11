import re
import splitEstados
#Entrada de dados
estadosCidadesErrados  = open('Estados+CIdades(erro).txt','r',encoding='UTF8')
estadosCidadesCorretos = open('Estados+CIdades.txt','r', encoding='UTF8')
log = open("log.txt", 'w', encoding='UTF8')


print("Metodo read () : \n")

#buscaformat = re.compile(r'\w[a-zA-Z0-9]{1,} ?\|[a-zA-Z0-9]{1,}\|[a-zA-Z0-9]{1,}')
buscaformat = re.compile(r'.{1,}\|.{1,}\|.{1,}')
#arqErrados = estadosCidadesErrados.readlines()

indexLinha=0
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
    #*** Fim de povoar dicionario


        
povoarDicionario()
print(len(dicEstados))
splitEstados.povoar3ArquivoEstados(dicEstados)



estadosCidadesCorretos.close()
estadosCidadesErrados.close()

log.close()
