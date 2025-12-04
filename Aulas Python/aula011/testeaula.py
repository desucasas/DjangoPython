import PySimpleGUI as sg

# Definindo o tema da interface (opcional)
sg.theme('Reddit')

# --- Definição do Layout da Janela ---
# O layout é uma lista de listas, onde cada lista interna representa uma linha na janela
layout = [
    [sg.Text('Formulário de Cadastro de Usuários')],
    [sg.Text('Nome:'), sg.InputText(key='-NOME-')],
    [sg.Text('Idade:'), sg.InputText(key='-IDADE-')],
    [sg.Text('Altura:'), sg.InputText(key='-ALTURA-')],
    [sg.Button('Ler os Dados'), sg.Button('Cancelar')]
]

# --- Criação da Janela ---
window = sg.Window('Cadastro de Usuários', layout)

# --- Loop de Eventos ---
# O loop lê eventos e valores da janela
while True:
    event, values = window.read()

    # Se o usuário fechar a janela ou clicar em Cancelar, o loop é interrompido
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    
    # Se o usuário clicar em Cadastrar
    elif event == 'Ler os dados':
        nome = values['-NOME-']
        idade = values['-IDADE-']
        altura = values['-ALTURA-']

        # Validação simples dos dados
        if not nome or not idade or not altura:
            sg.popup_error('Todos os campos devem ser preenchidos.')
        else:
            # Aqui você pode adicionar a lógica para salvar o usuário em um banco de dados ou arquivo (ex: JSON, CSV)
            # Por enquanto, apenas exibiremos um popup de sucesso
            mensagem = f'Nome {nome} cadastrado com sucesso!\nIdade: {idade}'
            sg.popup_ok('Cadastro Realizado', mensagem)
            
            # Limpar os campos após o cadastro (opcional)
           # window['-USUARIO-'].update('')
           # window['-EMAIL-'].update('')
           # window['-SENHA-'].update('')
           # window['-CONFIRMAR_SENHA-'].update('')
           # window['-TERMOS-'].update(False)


# --- Fechamento da Janela ---
window.close()