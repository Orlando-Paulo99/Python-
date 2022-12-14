import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED


class TelaPython:
    # cor
    sg.theme('DarkTeal12')

    def __init__(self):
        # Criando o formato da tela
        layout = [
            [sg.Text("Nome"), sg.Input(key="nome_1", size=(10, 0))],
            [sg.Text("Idade"), sg.Input(key="idade_1", size=(10, 0))],
            [sg.Checkbox("Facebook", key="face"), sg.Checkbox("Instagram", key="insta"),
             sg.Checkbox("Gmail", key="email")],
            [sg.Text("Aceita Cartoes")],
            [sg.Radio("sim", "cartoes", key="aceita_c"), sg.Radio("não", "cartoes", key="nao_aceita")],
            [sg.Slider(range=(0, 300), default_value=0, orientation="h", size=(15, 20), key="slider_vel")],
            [sg.Button("Enviar")],
            [sg.Output(size=(30, 20))]
        ]
        # criando a tela
        self.janela = sg.Window("Cadastro").layout(layout)
        self.event, self.values = self.janela.Read()

    # Método para inicar o que estaá dentro da tel.OBS:deixando dentro de uma variavel
    def iniciar(self=None, velocidade_s=None):
        # loop
        while True:

            if self.event == WIN_CLOSED:
                break

            nome = self.values["nome_1"]
            idade = self.values["idade_1"]
            aceitar_face = self.values["face"]
            aceitar_insta = self.values["insta"]
            aceitar_gmail = self.values["email"]
            aceita_cartao = self.values["aceitq_c"]
            nao_aceita_cartao = self.values["nao_aceita"]
            velcidade_s = self.values["slider_vel"]

            print(f"nome {nome}")
            print(f"idade{idade}")
            print(f" Facebook {aceitar_face}")
            print(f"Instagram {aceitar_insta}")
            print(f"Gmail {aceitar_gmail}")
            print(f"Aceita Cartão{aceita_cartao}")
            print(f"Não aceita Cartão{nao_aceita_cartao}")
            print(f"Velocidade {velocidade_s}")


# Instanciando o objeto
tela = TelaPython()
tela.iniciar()
