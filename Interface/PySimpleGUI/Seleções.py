import PySimpleGUI as sg


def tela_um():
    sg.theme("DarkBrown1")
    layout = [
        [sg.Text("Nome")],
        [sg.Input(key="name_1",size=(10,0))],
        [sg.Button('Prox')]
    ]

    return sg.Window("login", layout=layout, finalize=True)


def tela_dois():
    layout = [
        [sg.Text("Escolha a informação")],
        [sg.Checkbox("Brasil", key="info_1"),sg.Checkbox("Argentina",key="infor_2")],
        [sg.Checkbox("Alemanha",key="info_3"),sg.Checkbox("França",key="infor_4")],
        [sg.Button("Voltar"),sg.Button("Confirmar")]

    ]
    return sg.Window("informações", layout=layout, finalize=True)


   # return sg.Window("informações",layout=layout,finaLize=True)

#ordenar todas as janelas
jan_1,jan_2=tela_um(),None


while True:
    window, event, values = sg.read_all_windows()
    # evento fechar

    if window == jan_1 and event == sg.WIN_CLOSED:
        break


    #  if window == tela_um and event == sg.WIN_CLOSED:
  # QUANDO FOR TROCAR DE JANELA SE USA O NOME DA JANELA E NAO A FUNÇAO DA JANELA

    if window == jan_2 and event == sg.WIN_CLOSED:
        break

    # evento  da janela 1 pra janela 2


    if window == jan_1 and event == 'Prox':
        # QUANDO FOR TROCAR DE JANELA SE USA O NOME DA JANELA E NAO A FUNÇAO DA JANELA
        jan_2= tela_dois()
        jan_1.hide()

    if window== jan_2 and event == "Voltar":
        jan_2.hide()
        jan_1.un_hide()
    if window==jan_2 and event=="Confirmar":
    	if values["info_1"]==True:
    		sg.popup(" A seleção brasileira é a maior seleção a ganhar uma copa do mundo.A mesma tem cinco(5) títulos e está em busca do HEXA.")
    	elif values["infor_2"]==True :
    		sg.popup("Uma das selacões mais conhecidas do mundo,os hermanos tem apenas dois(2) títulos mundiais")
    		
    	elif values["info_3"]==True:
    		sg.popup("A Alemanha conta com quatro(4) titulos,a segunda seleção com maior números títos em uma copa do mundo.Só perde para o Brasil que tem cinco(5)")
    		
    	elif values["infor_4"]==True:
    		sg.popup("A França,a atual campeã do mundo,tem dois(2) títulos em copa do mundo,a mesma ainda está na fase eliminatória indo em busca de mais um título")
