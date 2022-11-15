import PySimpleGUI as sg
#editando o tema
sg.theme ('black')

#criando o formato
layout=[
	[sg.Text("Usuario"),sg.Input(key="usuario", size=(10,1))],
	[sg.Text("Senha"),
	sg.Input(key="senha",password_char='*', size=(10,1))],
	[sg.Checkbox("salvar login?")],
	[sg.Button("Entar")]

]
#criando a tela
tela=sg.Window("Login", layout)

#loopo 
while True:
	event,values=tela.read()
	#se caso o usuario queira sair a pagina irá sair sem erro
	if event==sg.WIN_CLOSED:
		break
