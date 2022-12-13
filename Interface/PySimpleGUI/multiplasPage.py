import PySimpleGUI as sg
def tela_inicial():
		sg.theme("DarkRed")
		layout=[
			[sg.Text("Seja Bem-Vindo",size=(15,0))],
			[sg.Button("Cadastro",key="cadas",   size=(30,3))],
			[sg.Button("Informações",key="lg",size=(30,3))],
			[sg.Button("Contatos",key="cont",size=(30,3))],
			[sg.Button("Redes sociais",key="redes",size=(30,4))]
		
		]
		return sg.Window("principal",layout=layout,finalize=True,size=(600,800))
		
def tela_cadastro():
		sg.theme("DarkBlack")
		layout=[
				[sg.Text("Nome"),sg.Input(key="nome_1",size=(10,0))],
				[sg.Text("Idade"),sg.Input(key="idade_1",size=(10,0))],
				[sg.Text("CPF"),sg.Input(key="cpf",size=(10,0))],
				[sg.Text("Telefone"),sg.Input(key="tel",size=(10,0))],
				[sg.Text("Endereço"),sg.Input(key="ende",size=(10,0))],
				
				[sg.Button("Enviar")],
				[sg.Output(size=(30,10))],
				
				[sg.Button("Voltar")]
		]
		return sg.Window("Cadastro2",layout=layout,finalize=True)
		
def tela_info():
		layout=[
						[sg.Radio("Cidade","cartoes",key="ci"),sg.Radio("Informacao","cartoes",key="inf")],
				[sg.Radio("Pontos Históricos","ph",key="pont_h")],
				
				[sg.Button("Voltar"),sg.Button("Confirmar")]
		]
		return sg.Window("informacao1",layout=layout,finalize=True)
		
		

		

		
		
jan_inicial,janela_cadastro, jan_info=tela_inicial(),None,None
		
while True:
		window, event, values = sg.read_all_windows()
		#Se o usuario querer sair da pagina principal sem erro
		if window==tela_inicial and event==WIN_CLOSED :
			break
			
			
		##Eventos tela de Cadastro
		if window==tela_cadastro and event==WIN_CLOSED:
				break
				
		if window==jan_inicial and event=="cadas":
			janela_cadastro=tela_cadastro()
			jan_inicial.hide()
			
		if window==janela_cadastro and event=="Voltar":
		          janela_cadastro.hide()
		          jan_inicial.un_hide()

		#Eventos Tela de Informações
		if window==jan_info and event==WIN_CLOSED:
					break
			
		if window==jan_inicial and event=="lg":
			jan_info=tela_info()
			jan_inicial.hide()
			
		if window==jan_info and event=="Voltar":
			jan_info.hide()
			jan_inicial.un_hide()
