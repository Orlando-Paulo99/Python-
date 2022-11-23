import PySimpleGUI as sg
#criand a estrutura da tela
layout=[
	[sg.Text('Usuario')],
	[sg.Input(key='user', size=(10,1))],
	[sg.Text('Senha')],
	[sg.Input(key='passe', size=(10,1))],
	[sg.Button('Login')],
	[sg.Text(' ', key='mensagem')],
]
#criando a janela
window= sg.Window('Login' ,layout=layout)
#loop para a janela ficar sempre ativa
while True:
	event,values=window.read()
	#sevo usuario fechar atela ,a tela irá fechar sem erro
	if event==sg.WIN_CLOSED:
		break
		
	#como não está conectado ao banco de dados,essa condição se caso o login e senha for diferente dos valores definidos nas variaveis user_c e senha_c
	elif event=='Login':
		senha_c='123'
		user_c='orlando'
		usuario1=values['user']
		pin=values['passe']
		if usuario1==user_c and pin==senha_c:
			window['mensagem'].update('login feito com sucesso')
		else:
			window['mensagem'].update('login ou senha invalido')

	
