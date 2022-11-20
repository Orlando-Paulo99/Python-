import turtle


#criando a tela
wn=turtle.Screen()
wn.title("Snackers")
wn.bgcolor("yellow")
wn.setup(width=500, height=300)
wn.tracer(90)
#Priemira letro
nome=turtle.Turtle()
nome.shape("blank")
nome.pencolor("black")
nome.right(100)
nome.penup()



fonte1=("comic Sans",30,"italic")
nome.write("Orlando",True,"center",fonte1)
nome.forward(40)

fonte2=("comic sans",12,"normal")
nome.write("Ele tem 22 anos,atualmente está estudando Desenvolvimento de softwere",False,"center",fonte2)

nome.forward(60)

fonte3=("comic sans",12,"normal")
nome.write("O seu maior sonho como Dev é trabalhar na Amazon ou Google",False,"center",fonte3)
nome.forward
			
		
	

	



while True:
	wn.update()
