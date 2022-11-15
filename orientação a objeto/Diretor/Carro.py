 class Carro:
		def __init__(self,marca,modelo,ano,status=False):
			self.marca=marca
			self.modelo=modelo
			self.ano=ano
			self.status=status
			
		def ligar(self):
			if self.status==False:
				self.status=True
			if self.status==True:
				print("O carro está ligado")
				
			else:
				print("Carro desligado")
		
		def andar(self):
				if self.status==False:
					self.status=True
				if self.status==True:
					cont=0
					while True:
						
						print(" A cada giro completo do pneu o carro anda 1km")
						break
						cont+=1
					print("O carro andou ",cont+cont,"km")
