import math

# 1. Classe Circulo
class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * (self.raio ** 2)

# 2. Classe Livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def detalhes(self):
        return f'Título: {self.titulo}, Autor: {self.autor}'

# 3. Classe Retangulo
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

# 4. Classe ContaBancaria
class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor

# 5. Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(f'Olá, meu nome é {self.nome}.')

# 6. Classe Produto
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_total(self):
        return self.preco * self.quantidade

# 7. Classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def detalhes(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}'

# 8. Classe Aluno
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

# 9. Classe Triangulo
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# 10. Classe Funcionario
class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumentar_salario(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento

# Classe
if __name__ == "__main__":
    # classe Circulo
    c = Circulo(5)
    print(f'Área do círculo: {c.calcular_area()}')

    # classe Livro
    l = Livro("1984", "George Orwell")
    print(l.detalhes())

    # classe Retangulo
    r = Retangulo(10, 5)
    print(f'Área do retângulo: {r.calcular_area()}')

    # classe ContaBancaria
    conta = ContaBancaria(1000, "João")
    conta.depositar(500)
    conta.sacar(300)
    print(f'Saldo da conta: {conta.saldo}')

    # classe Pessoa
    p = Pessoa("Maria", 30)
    p.falar()

    # classe Produto
    prod = Produto("Camiseta", 20.0, 3)
    print(f'Valor total do produto: {prod.calcular_total()}')

    # classe Carro
    carro = Carro("Toyota", "Corolla", 2022)
    print(carro.detalhes())

    # classe Aluno
    aluno = Aluno("Ana", [8.5, 9.0, 7.5])
    print(f'Média das notas do aluno: {aluno.calcular_media()}')

    # classe Triangulo
    triang = Triangulo(3, 4, 5)
    print(f'Perímetro do triângulo: {triang.calcular_perimetro()}')

    # classe Funcionario
    func = Funcionario("Carlos", 3000, "Analista")
    func.aumentar_salario(10)
    print(f'Salário atualizado do funcionário: {func.salario}')