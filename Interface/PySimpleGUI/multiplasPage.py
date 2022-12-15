import PySimpleGUI as sg
#Formato da tela de login
def tela_login():
	sg.theme("DarkBrown")
	layout=[
			[sg.Text("Login"),sg.Input(key="login_1",size=(15,0))],
			[sg.Text("Senha"),sg.Input(key="senha1",size=(15,0))],
			[sg.Button("Entrar",key="enter")]
	
	]
	return sg.Window("login",layout=layout,finalize=True)


#Formato da tela inicial
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
#Formato da tela de cadastro	
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

#Formato da tela de informações
def tela_info():
		layout=[
						[sg.Radio("Cidade","cartoes",key="ci"),sg.Radio("Informacao","cartoes",key="inf")],
				[sg.Radio("Pontos Históricos","ph",key="pont_h")],
				
				[sg.Button("Voltar"),sg.Button("Confirmar")]
		]
		return sg.Window("informacao1",layout=layout,finalize=True)
		
#Criando as janelas e deixando visivel de cara só atela de escilha
jan_login,jan_inicial,janela_cadastro, jan_info=tela_login(),None,None,None

#loop	
while True:
		#netodo para ler as janelas,eventos e valores.
		window, event, values = sg.read_all_windows()
		#Evento tela de Login
		if window==jan_login and event==sg.WIN_CLOSED:
			break
		#Evento para ir para ir a outra tela após a tela de login
		if window==jan_login and event=="enter":
			jan_inicial=tela_inicial()
			jan_login.hide()
			
		
		#Se o usuario querer sair da pagina principal sem erro
		if window==jan_inicial and event==sg.WIN_CLOSED :
			break
			
			
		##Eventos tela de Cadastro
		if window==janela_cadastro and event==sg.WIN_CLOSED:
				break
				
		if window==jan_inicial and event=="cadas":
			janela_cadastro=tela_cadastro()
			jan_inicial.hide()
			
		if window==janela_cadastro and event=="Voltar":
		          janela_cadastro.hide()
		          jan_inicial.un_hide()

		#Eventos Tela de Informações
		if window==jan_info and event==sg.WIN_CLOSED:
					break
			
		if window==jan_inicial and event=="lg":
			jan_info=tela_info()
			jan_inicial.hide()
			
		if window==jan_info and event=="Voltar":
			jan_info.hide()
			jan_inicial.un_hide()
			
		if window==jan_info and event=="Confirmar":
				if values["ci"]==True:
					sg.popup("Recife,a capital do nordeste")
				elif values["inf"]==True:
					sg.popup("Recife tem ... anos,é conhecida por sua linda cultura,oelo seu clima e seus pontos turisticos são os mais visitados do Brqsil")
				elif values["pont_h"]==True:
					sg.popup("Seus principais pontos turicos são Paço do Frevo,Cais do sertão e entre outros")
				
 
		
			
		
		
		
		
