from abc import ABC, abstractmethod

class Dispositivo(ABC):
    @abstractmethod
    def ligar(self) -> bool:
        pass

    @abstractmethod
    def desligar(self) -> bool:
        pass

class Tv(Dispositivo):
    def ligar(self):
        print("Televisão ligada")
        return True

    def desligar(self):
        print("Televisão desligada")
        return True

class Projetor(Dispositivo):
    def ligar(self):
        print("Projetor ligado")
        return True

    def desligar(self):
        print("Projetor desligado")
        return True
    
class Receiver(Dispositivo):
    def ligar(self):
        print("Receiver ligado")
        return True

    def desligar(self):
        print("Receiver desligado")
        return True
    
class Player(Dispositivo):
    def ligar(self):
        print("Player ligado")
        return True

    def desligar(self):
        print("Player desligado")
        return True

class Som(Dispositivo):
    def ligar(self):
        print("Som ligado")
        return True

    def desligar(self):
        print("Som desligado")
        return True
    
class Luz(Dispositivo):
    def ligar(self):
        print("Luz ligada")
        return True

    def desligar(self):
        print("Luz desligada")
        return True

class HomeTheater:
    def __init__(self):
        self._Tv = Tv()
        self._Projetor = Projetor()
        self._Receiver = Receiver()
        self._Player = Player()
        self._Som = Som()
        self._Luz = Luz()

    def assistir_filme(self):
        self._Luz.desligar()
        self._Tv.ligar()
        self._Projetor.ligar()
        self._Receiver.ligar()
        self._Player.ligar()
        self._Som.ligar()

    def ouvir_musica(self):
        self._Player.ligar()
        self._Som.ligar()
        self._Receiver.ligar()
        self._Projetor.desligar()
        self._Tv.desligar()
        self._Luz.ligar()