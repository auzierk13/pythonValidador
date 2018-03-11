estadosCidadesCorretos = open('Estados+CIdades.txt','r', encoding='UTF8')
inicioCorreto1 = open("parse1.txt", 'w', encoding='UTF8')
meioCorreto2 = open("parse2.txt", 'w', encoding='UTF8')
fimCorreto3 = open("parse3.txt", 'w', encoding='UTF8')


def povoar3ArquivoEstados(dicEstados):
    for linhaCerta in estadosCidadesCorretos:
        #linhaCerta = linhaCerta.rstrip() #Limpa linha em branco
        estadoCorreto,siglaCorreta,cidadeCorreta = linhaCerta.split("|")
        listChavesEstados = list(dicEstados.keys())
        # print(listChavesEstados[0])

       #index =0 8
        if((estadoCorreto == listChavesEstados[0]) or
           (estadoCorreto == listChavesEstados[1]) or
           (estadoCorreto == listChavesEstados[2]) or
           (estadoCorreto == listChavesEstados[3]) or
           (estadoCorreto == listChavesEstados[4]) or
           (estadoCorreto == listChavesEstados[5]) or
           (estadoCorreto == listChavesEstados[6]) or
           (estadoCorreto == listChavesEstados[7]) or
           (estadoCorreto == listChavesEstados[8])):
            inicioCorreto1.write(linhaCerta)
            continue

        #index =9 17
        if((estadoCorreto==listChavesEstados[9]) or
           (estadoCorreto==listChavesEstados[10]) or
           (estadoCorreto==listChavesEstados[11]) or
           (estadoCorreto==listChavesEstados[12]) or
           (estadoCorreto==listChavesEstados[13]) or
           (estadoCorreto==listChavesEstados[14]) or
           (estadoCorreto==listChavesEstados[15]) or
           (estadoCorreto==listChavesEstados[16]) or
           (estadoCorreto==listChavesEstados[17])):
            meioCorreto2.write(linhaCerta)
            continue

        #index =18 26
        if((estadoCorreto==listChavesEstados[18]) or
           (estadoCorreto==listChavesEstados[19]) or
           (estadoCorreto==listChavesEstados[20]) or
           (estadoCorreto==listChavesEstados[21]) or
           (estadoCorreto==listChavesEstados[22]) or
           (estadoCorreto==listChavesEstados[23]) or
           (estadoCorreto==listChavesEstados[24]) or
           (estadoCorreto==listChavesEstados[25]) or
           (estadoCorreto==listChavesEstados[26])):
            meioCorreto2.write(linhaCerta)
            continue
        

    estadosCidadesCorretos.seek(0) #Volta para o
    estadosCidadesCorretos.close()
    inicioCorreto1.close()
    meioCorreto2.close()
    fimCorreto3.close()

