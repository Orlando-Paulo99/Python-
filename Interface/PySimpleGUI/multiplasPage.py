import PySimpleGUI as sg
#Formato da tela de login
def tela_login():
	sg.theme("DarkBrown")
	layout=[
			[sg.Text("Login"),sg.Input("",key="login",size=(15,0))],
			[sg.Text("Senha"),sg.Input(key="senha",size=(15,0))],
			[sg.Button("Entrar",key="enter")],
			[sg.Text("",key="mensagem")]
			
	
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
					[sg.Button("Voltar",size=(5,0))],
					[sg.Text("Nome do Produto"),sg.Input("",key="dados",size=(10,5))],
					[sg.Text("Valor"),sg.Input(key="valor_p",size=(10,5))],
					[sg.Button("Resetar"),sg.Button("Confirmar")],
					

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
				
 
		
			
		
		
		
		
