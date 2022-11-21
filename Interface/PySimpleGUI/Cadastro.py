from PySimpleGUI import PySimpleGUI as sg
#editando o tema
sg.theme ('black')

#criando o formato
layout=[
	[sg.Text("Nome Completo"), sg.Input(key="nome", size=(20,1))],
	[sg.Text("Telefone"), sg.Input(key="tel", size=(15,1))],

	[sg.Text("Endereço"),sg.Input(key="end", size=(15,1))],
	[sg.Text("CPF"),sg.Input(key="n_cpf", size=(15,1))],
	[sg.Text("Login"),sg.Input(key="lg", size=(15,1))],

	
	

	[sg.Text("Senha"),
	sg.Input(key="senha",password_char='*', size=(15,1))],
	

	[sg.Button("Entar")]

]
#criando a tela
tela=sg.Window("cadastro", layout)

#loopo 
while True:
	event,values=tela.read()
	#se caso o usuario queira sair a pagina irá sair sem erro
	if event==sg.WIN_CLOSED:
		break
