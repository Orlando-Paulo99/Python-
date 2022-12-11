import PySimpleGUI as sg
def tela_inicial():
		sg.theme("DarkRed")
		layout=[
			[sg.Text("Seja Bem-Vindo",size=(15,0))],
			[sg.Button("Cadastro",key="cadas",size=(15,0))],
			[sg.Button("Informações",key="lg",size=(15,0))],
			[sg.Button("Contatos",key="cont",size=(15,0))],
			[sg.Button("Redes sociais",key="redes",size=(15,0))]
		
		]
		return sg.Window("principal",layout=layout,finalize=True)
		

def tela_cadastro():
		sg.theme("DarkGreen")
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
		pass
		
def tela_contatos():
		pass
		
def tela_redes():
		pass
		
		
jan_inicial,janela_cadastro=tela_inicial(),None
		
while True:
		window, event, values = sg.read_all_windows()
		#Se o usuario querer sair da pagina principal sem erro
		if window==tela_inicial and event==WIN_CLOSED :
			break
		#Se o usuario querer sair da tela de cadastro sem erro
		if window==tela_cadastro and event==WIN_CLOSED:
				break
		
		#Sair sem erro da tela informações
	
		#Sair sem erro da tela contatos
		#Sair sem erro da tela Redes Sociais
		
		#Eventos Tela de Cadastro
		if window==jan_inicial and event=="cadas":
			janela_cadastro=tela_cadastro()
			jan_inicial.hide()
			
		if window==janela_cadastro and event=="Voltar":
		          janela_cadastro.hide()
		          jan_inicial.un_hide()
		if window==janela_cadastro and event=="Enviar":
		          print(f"Nome {nome_1}")
		          print(f"Idade {idade_1}")
		          prinr(f"CPF {cpf}")
		          print(f"Telefone {tel}")
		          print(f" Endereço {ende}")
		          
		          
		
	
		
			
		
		
		
		
	
