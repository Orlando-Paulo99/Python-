import PySimpleGUI as sg

#CRIANDO O FORMATO DA TELA DE LOGIN
def tela_login():
	sg.theme("DarkBlue4")
	layout=[
			[sg.Text("Nome")],
			[sg.Input(key="user",size=(15,1))],
			[sg.Text("ID")],
			[sg.Input(key="ident",size=(15,1))],
			[sg.Button("Entrar")]
	]
	return sg.Window("login",layout=layout,finalize=True)

#FORMATO TELA DE OPÇÕES	
def tela_option():
	sg.theme("DarkBlue14")
	layout=[
			[sg.Button("Cadastrar Produto")],
			[sg.Button("Verificar Produtos")]
	]
	return sg.Window("Opção",layout=layout,finalize=True)

#FORMATO TELA DE CADASTRO DOS PRODUTOS
def tela_cadastroProdutos():
	sg.theme("DarkBlue5")
	layout=[
			[sg.Text("Produto")],
			[sg.Input(size=(20,1))],
			[sg.Text("Valor"),sg.Input(size=(10,1))],
			[sg.Button("Voltar"),sg.Button("Confirmar")]
	]
	return sg.Window("cadastro",layout=layout,finalize=True)

#FORMATO TELA DE VERIFICAÇÃO	
def verificar_produtos():
	sg.theme("DarkBrown")
	layout=[
			[sg.Output(size=(20,10))],
			[sg.Button("Voltar")]
	]
	return sg.Window("verificando",layout=layout,finalize=True)
	
	
	
	
#CRIANDO JANELAS
jan_login,jan_option,jan_cadastro,jan_verificar=tela_login(),None,None,None

while True:
	window,event,values=sg.read_all_windows()
	
	#EVENTO TELA LOGIN PARA ENCERRAR O PROGRAMA
	if window==jan_login and event==sg.WIN_CLOSED:
		break
	#EVENTO  PARA IR PARA JANELA DE OPÇÕES
	if window==jan_login and event=="Entrar":
		jan_option=tela_option()
		jan_login.hide()
		
	#EVENTO PARA FECHAR A TELA DE OPÇÕES
	if  window==jan_option and event==sg.WIN_CLOSED:
		break
		
	#EVENTO DA TELA DE OPCÕES
	if window==jan_option and event=="Cadastrar Produto":
		jan_cadastro=tela_cadastroProdutos()
		jan_option.hide()
		
	#VOLTANDO PARA TELA DE OPÇÕES
	if window==jan_cadastro and event=="Voltar":
		jan_option=tela_option()
		jan_cadastro.hide()
		jan_option.un_hide()
		
	#EVENTO PARA FECHAR A TELA DE PRODUTOS
	if window==jan_cadastro and event==sg.WIN_CLOSED:
		break
		
	#EVENTOS VERIFICAR PRODUTOS
	if window==jan_option and event=="Verificar Produtos":
		jan_verificar=verificar_produtos()
		jan_option.hide()
		
	#SAINDO DA TELA DE VERIFICAÇÃO PARA TELA OPTION
	if window==jan_verificar and event=="Voltar":
		jan_verificar.hide()
		jan_option.un_hide()
