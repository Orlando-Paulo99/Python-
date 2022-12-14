import PySimpleGUI as sg

#CRIANDO O FORMATO DA TELA DE LOGIN
def tela_login():
	sg.theme("LightBrown10")
	layout=[
			[sg.Text("Nome")],
			[sg.Input(key="user",size=(15,1))],
			[sg.Text("ID")],
			[sg.Input(key="ident",size=(15,1))],
			[sg.Button("Entrar")],
			[sg.Text(' ',key="mensagem")]
	]
	return sg.Window("login",layout=layout,finalize=True)

#FORMATO TELA DE OPÇÕES	
def tela_option():
	sg.theme("DarkBlue14")
	layout=[
			[sg.Button("Cadastrar Produto")],
			[sg.Button("Verificar Produtos")],
			[sg.Button("Desconectar")]
	]
	return sg.Window("Opção",layout=layout,finalize=True,size=(415,250))

#FORMATO TELA DE CADASTRO DOS PRODUTOS
def tela_cadastroProdutos():
	sg.theme("DarkBlue5")
	layout=[
			[sg.Text("Produto")],
			[sg.Input(key="nome_produto",size=(20,1))],
			[sg.Text("Valor"),sg.Input(key="valor_produto",size=(10,1))],
			[sg.Button("Voltar"),sg.Button("Confirmar")]
	]
	return sg.Window("cadastro",layout=layout,finalize=True)

#FORMATO TELA DE VERIFICAÇÃO	
def verificar_produtos():
	sg.theme("DarkBrown")
	lista_produtos=[]
	layout=[
			[sg.Output(key="saida",size=(30,10))],
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
	#EVENTO TELA DE LOGIN
	if window==jan_login and event=="Entrar":
		user_1=values["user"]
		pin=values["ident"]
		user_2="orlando"
		pin_2="123"
		if user_1==user_2 and pin==pin_2:
			jan_option=tela_option()
			jan_login.hide()
		else:
			window["mensagem"].update("login ou senha invalido")
	#EVENTO PARA FECHAR A TELA DE OPÇÕES
	if  window==jan_option and event==sg.WIN_CLOSED:
		break
		
	#EVENTO DA TELA DE OPCÕES
	if window==jan_option and event=="Cadastrar Produto":
		jan_cadastro=tela_cadastroProdutos()
		jan_option.hide()
		
	#VOLTANDO PARA TELA DE LOGIN
	if window==jan_option and event=="Desconectar":
		jan_login=tela_login()
		jan_option.hide()
		jan_login.un_hide()
		
	#VOLTANDO PARA TELA DE OPÇÕES
	if window==jan_cadastro and event=="Voltar":
		jan_option=tela_option()
		jan_cadastro.hide()
		jan_option.un_hide()
		
	#EVENTO PARA FECHAR A TELA DE PRODUTOS
	if window==jan_cadastro and event==sg.WIN_CLOSED:
		break
	 	
	if window==jan_cadastro and event=="Confirmar":
			varif=tela_cadastroProdutos()
			
			window["saida"].update("")
			verif.get_tela_cadastroProdutos()
	
	#EVENTOS VERIFICAR PRODUTOS
	if window==jan_option and event=="Verificar Produtos":
			jan_verificar=verificar_produtos()
			jan_option.hide()
		
	#SAINDO DA TELA DE VERIFICAÇÃO PARA TELA OPTION
	if window==jan_verificar and event=="Voltar":
		jan_verificar.hide()
		jan_option.un_hide()


