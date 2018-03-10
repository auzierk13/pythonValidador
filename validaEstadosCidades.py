#manipulador= open('Enunciado.txt','r')
manipulador= open('Estados+CIdades.txt','r', encoding='UTF8')

print("Metodo read () : \n")
a= manipulador.readlines()
#print(manipulador.readlines())
indexLinha=0
for linha in a:
    indexLinha+=1
    linha = linha.rstrip()
    print(str(indexLinha) +": "+linha)
    if indexLinha > 50:
        break

manipulador.seek(0) #Volta para o inicio do arquivo

"""
for linha in manipulador:
    linha = linha.rstrip()
    print(linha)
"""
manipulador.close
