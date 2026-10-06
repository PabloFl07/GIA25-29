from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def area(): ...


class Circulo(Figura):
    PI = 3.141592

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return self.PI * self.radio**2


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado**2


class Triangulo(Rectangulo):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    

    def area(self):
        return (self.base * self.altura) / 2
