from math import hypot
# Retorna a norma eucliana. Este é o comprimento do vetor desde a origem
# ate o ponto indicado pelas coordenadas
# sqrt(sum(x**2 for x in coordinates))
# Para um ponto bidimensional, isso equivale a calcular a hipotenusa de um
# triangulo retangulo usando Pitagoras.

class Vector:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    # "Difference between __str__ and __repr__ in Python"
    # http://bit.ly/1Vm7j1N)
    # É uma pergunta do Stack Overflow com excelentes contrinuições
    # dos pythonistas Alex Martelli e Martijin Pieters

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
    # Retornara False se a magnitude do vetor for zero
    # e True caso contrario

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    # Multiplicamos um vetor por um escalar
    # mas nao vale a comutativa. Esse problema sera corrigido no cap13
