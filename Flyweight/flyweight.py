from abc import ABC
import random

from abc import ABC

objetos = 0

class algarismo(ABC):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            global objetos 
            objetos = objetos + 1
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, digito: int):
        self._digito = digito

    def getdigito(self):
        return self._digito
    
class digito0(algarismo):
    def __init__(self):
        super().__init__(0)

class digito1(algarismo):
    def __init__(self):
        super().__init__(1)

class digito2(algarismo):
    def __init__(self):
        super().__init__(2)

class digito3(algarismo):
    def __init__(self):
        super().__init__(3)

class digito4(algarismo):
    def __init__(self):
        super().__init__(4)

class digito5(algarismo):
    def __init__(self):
        super().__init__(5)

class digito6(algarismo):
    def __init__(self):
        super().__init__(6)

class digito7(algarismo):
    def __init__(self):
        super().__init__(7)

class digito8(algarismo):
    def __init__(self):
        super().__init__(8)

class digito9(algarismo):
    def __init__(self):
        super().__init__(9)

class factoryalgarismo():
    _types = {
        0: digito0,
        1: digito1,
        2: digito2,
        3: digito3,
        4: digito4,
        5: digito5,
        6: digito6,
        7: digito7,
        8: digito8,
        9: digito9
    }

    def create(self, numero: int) -> algarismo:
        algarismo_class = factoryalgarismo._types.get(numero)

        if algarismo_class is None:
            raise ValueError("Algarismo inválido")

        return algarismo_class()

class buildnumber():
    fabrica = factoryalgarismo()

    def __init__(self):
        self._number = []

    def build(self):
        for i in range(9):
            numero = random.randint(0, 9)
            algarismo = self.fabrica.create(numero)
            self._number.append(algarismo)

        return self._number

def main():
    for i in range(9):
        numero = buildnumber().build()
        for alg in numero:
            print(alg.getdigito(), end="")
        print("\n")
    print(objetos)
if __name__ == "__main__":
    main()