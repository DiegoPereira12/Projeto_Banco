class Carros():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def imprime(self,marca,modelo):
        print("Esse carro é %s e o Modelo %s" %(self.marca,self.modelo))

carro1 = Carros('Chevete','Chevrolet')
carro2  = Carros('Ranger', 'Ford')

print(carro1.modelo)
print(carro1.marca)
print(carro2.modelo)
print(carro2.marca)

carro2.imprime("Ranger","Ford")