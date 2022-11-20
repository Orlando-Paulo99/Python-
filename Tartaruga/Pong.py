import turtle

wn=turtle.Screen()
wn.title("Snackers")
wn.bgcolor("aqua")
wn.setup(width=800, height=600)
wn.tracer(100)

#placar
placarA=0
placarB=0





#Jogador A
jogadorA=turtle.Turtle()
jogadorA.speed(0)
jogadorA.shape("square")
jogadorA.color("black")
jogadorA.shapesize(stretch_wid=5,stretch_len=1)
jogadorA.penup()
jogadorA.goto(-350,10)


#Jogador B
jogadorB=turtle.Turtle()
jogadorB.speed(0)
jogadorB.shape("square")
jogadorB.color("black")
jogadorB.shapesize(stretch_wid=5,stretch_len=1)
jogadorB.penup()
jogadorB.goto(350,0)

#Bola
bola=turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("black")
bola.penup()
bola.goto(0,0)
bola.dx=0.5
bola.dy=-0.7

#Criando o Placar
caneta=turtle.Turtle()
caneta.speed(0)
caneta.color("white")
caneta.penup()
caneta.hideturtle()
caneta.goto(0,260)
caneta.write(" jogadorA: 0 jogadorB: 0", align=("center"),font=("courier",20,("normal")))



#Função JogadorA
#Mover para cima
def jogadorA_up():
	y=jogadorA.ycor()
	y+=20
	jogadorA.sety(y)
		
#Mover pra baixo
def jogadorA_down():
	y=jogadorA.ycor()
	y-=20
	jogadorA.sety(y)
	
#Função jogadorB
#Move ora cima	
def jogadorB_down():
	y=jogadorB.ycor()
	y-=20
	jogadorA.sety(y)
#Move pra baixo	
def jogadorB_up():
	y=jogadorA.ycor()
	y+=20
	jogadorA.sety(y)
	
	
#Comandos
wn.listen()
wn.onkeypress(jogadorA_up,"w")
wn.onkeypress(jogadorA_down,"s")
wn.onkeypress(jogadorB_up,"1")
wn.onkeypress(jogadorB_down,"2")


	


#parte pr
while True:
	wn.update()
	
	#Movimento da bola
	bola.setx(bola.xcor()  +   bola.dx)
	bola.sety(bola.ycor()  +  bola.dy)
	
   
	#Limite da bola
	if bola.ycor() > 290:
		bola.sety(290)
		bola.dy *=-1
		
	if bola.xcor() < -290:
		bola.setx(-290)
		bola.dx *=-1
		
	#Limite Lateral
	if bola.xcor() > 390:
		bola.goto(0, 0)
		bola.dx *= -1
		placarA+=1
		caneta.clear()
		caneta.write("jogadorA: {} jogadorB: {}".format(placarA,  placarB),align="center",font=("courtier",20,"normal"))
		
	if bola.ycor() < -390:
		bola.goto(0, 0)
		bola.dx *= -1
		placarB+=1
		caneta.clear()
		caneta.write("jogadorA: {} jogadorB: {}".format(placarA,  placarB),align="center",font=("courtier",20,"normal"))

		
	#Colisão da bola com os jogadores
	if(bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < jogadorB.ycor +40 and bola.ycor() > jogadorB.ycor() -40):
		bola.setx(340)
		bola.dx *= -1
	
	if(bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < jogadorA.ycor +40 and bola.ycor() > jogadorA.ycor() -40):
		bola.setx(-340)
		bola.dx *= -1
