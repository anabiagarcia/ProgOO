from abc import ABC, abstractmethod

class Bebida(ABC):
    @abstractmethod
    def descricao(self) -> str:
        pass

    @abstractmethod
    def custo(self) -> float:
        pass

class CafeExpresso(Bebida):
    def descricao(self):
        return "Café expresso"

    def custo(self):
        return 5.0


class Cappuccino(Bebida):
    def descricao(self):
        return "Cappuccino"

    def custo(self):
        return 6.0


class Cha(Bebida):
    def descricao(self):
        return "Chá"

    def custo(self):
        return 4.0


class Decorador(Bebida):
    def __init__(self, bebida: Bebida):
        self._bebida = bebida  

class Leite(Decorador):
    def descricao(self):
        return self._bebida.descricao() + " + Leite"

    def custo(self):
        return self._bebida.custo() + 1.0


class Chantilly(Decorador):
    def descricao(self):
        return self._bebida.descricao() + " + Chantilly"

    def custo(self):
        return self._bebida.custo() + 1.5


class Canela(Decorador):
    def descricao(self):
        return self._bebida.descricao() + " + Canela"

    def custo(self):
        return self._bebida.custo() + 0.5


class CaldaDeChocolate(Decorador):
    def descricao(self):
        return self._bebida.descricao() + " + Calda de chocolate"

    def custo(self):
        return self._bebida.custo() + 2.0
