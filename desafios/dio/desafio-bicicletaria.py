
#Aula de classes e objetos.

class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor


    def buzinar(self):
        print("Plim, plim .. ") 

    def parar(self):
        print("Parando a bicicleta ...")
        print("Bicicleta parada.")

    def correr(self):
        print("Vrummm")


b1 = bicicleta("Amarela","Caloi", 1994, 200)

b1.buzinar()
b1.parar()
b1.correr()

print(b1.cor, b1.modelo, b1.valor,b1.ano)  #acessando os atributos da classe.

def __str__(self):
    return f"bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"





        










    