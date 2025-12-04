import PySimpleGUI as sg
import numpy as np

#Lista para guardar o layout da janela
layout = [
    [sg.Text("Digite a quantidade de números que deseja inserir")], 
    [sg.Input(key = 'N')],
    [sg.Button("Ok"), sg.Button("Cancelar")]
    
]

janela = sg.Window("Calculadora", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        janela.close()
        break
    if evento == "Ok":
        try:
            n = int(valores['N'])
            if n <=0:
                sg.popup("Insira somente números positivos")
                continue
            break
        except:
            sg.popup("Por favor, insira um valor válido")
janela.close()
numeros = [] #Outra Lista

for i in range(n):
    layout = [
        [sg.Text(f"Digite o {i+1}º número")], 
        [sg.Input(key='Campeao')],
        [sg.Button("Ok"), sg.Button("Cancelar")]
    ]
    janela = sg.Window("Entrada de números", layout)

    while True:
        eventos,valores = janela.read()
        if eventos == sg.WIN_CLOSED or eventos == "Cancelar":
            janela.close()
            break
        if eventos == 'Ok':
            try:
                num = float(valores['Campeao'])
                numeros.append(num)
                break
            except:
                sg.popup("Por favor, insira valores válidos")

janela.close() #Comando para fechar a janela

#Utilização do Numpy
vetor = np.array(numeros)
#soma = np.sum(np.array(numeros))
soma = np.sum(vetor)
#media = np.mean(np.array(numeros))
media = np.mean(vetor)

#Resultados
resultado_layout = [
    [sg.Text("Elementos do vetor")],
    [sg.Text(",".join(map(str,vetor)))],
    [sg.Text(f"Soma dos elementos = {soma}")],
    [sg.Text(f"Media dos elementos = {media}")]
    [sg.Button("Fechar")]
]

resultado_janela = sg.Window("Resultado", resultado_layout)

while True:
    eventoResultado = resultado_janela.read()
    print(eventoResultado)
    if eventoResultado == sg.WIN_CLOSED or "Fechar" in eventoResultado:
        resultado_janela.close()
        print("entrei if")
        break

resultado_janela.close()

if __name__ == "__main__":
    main()