import PySimpleGUI as sg
class TelaPython:
	#cor
	sg.change_look_and_feel("Red")
	
	def __init__(self):
		#Criando o formato da tela
		layout=[
				[sg.Text("Nome"),sg.Input(key="nome_1",size=(10,0))],
				[sg.Text("Idade"),sg.Input(key="idade_1",size=(10,0))],
				[sg.Checkbox("Facebook",key="face"),sg.Checkbox("Instagram",key="insta"),sg.Checkbox("Gmail",key="email")],
				[sg.Text("Aceita Cartoes")],
				[sg.Radio("sim","cartoes",key="aceita_c"),sg.Radio("não","cartoes",key="nao_aceita")],
				[sg.Button("Enviar")],
				[sg.Output(size=(30,20))]
		]
		#criando a tela
		self.janela=sg.Window("Cadastro").layout(layout)
		self.event,self.values=self.janela.Read()
		
		#Método para inicar o que estaá dentro da tel.OBS:deixando dentro de uma variavel
	def iniciar():
		#loop
		while True:
			self.button,self.values=self.janela.Read()
		
			nome=self.values["nome_1"]
			idade=self.values["idade_1"]
			aceitar_face=self.values["face"]
			aceitar_insta=self.values["insta"]
			aceitar_gmail=self.values["email"]
			aceita_cartao=self.values["aceitq_c"]
			nao_aceita_cartao= selfvalues["nao_aceita"]
		
		print(f"nome {nome}")
		print(f"idade{idade}")
		print(f" Facebook {aceitar_face}")
		print(f"Instagram {aceitar_insta}")
		print(f"Gmail {aceitatar_gmail}")
		print(f"Aceita Cartão{aceita_cartao}")
		print(f"Não aceita Cartão{nao_aceita_cartao}")
		
		
		
		
tela=TelaPython()
tela.iniciar()

