
class Observer():
    def __init__(self):
        self.nome: str = "" 

    def update(self, id: int):
       print(f"Alerta {self.nome}: as condições foram alteradas, verifique o pcd {id} para mais informações.")

class PCD():
    """"
        Quando há uma mudança, todas as universidades cadastradas como Observers são avisadas.
        Assim, os Observers não controlam o fluxo, ou seja, não ficam verificando se houve mudança,
        mas são notificados pelo PCD quando uma alteração acontece. Desta forma, temos a inversão de 
        controle, o Sujeito controla.
    """
    def __init__(self):
        self.id = 0
        self.universidades = [] 
        self.temperatura = 0.0
        self.umidade = 0.0
        self.pressao = 0.0
        self.luminosidade = 0.0
    
    def setId(self, id: int):
        self.id = id
     
     #Aqui é a principal ponto da inversão de controle, aqui ele identifica quais observers serão notificados,
     #ao invés de esses observers ficarem consultando o PCD, o PDC avisará eles em caso de mudança
    def addUniversidade(self, universidade: Observer):
        self.universidades.append(universidade) 
    
    def notificationUni(self):
        for universidade in self.universidades:
            universidade.update(self.id)
    
    def setTemperatura(self, temperatura: float):
        self.temperatura = temperatura
        self.notificationUni()
    
    def setUmidade(self, umidade: float):
        self.umidade = umidade
        self.notificationUni()

    def setPressao(self, pressao: float):
        self.pressao = pressao
        self.notificationUni()
    
    def setLuminosidade(self, luminosidade: float):
        self.luminosidade = luminosidade
        self.notificationUni()


#Testes
if __name__ == "__main__":
    #Criar PCDs
    RioA = PCD()
    RioA.setId(1)
    RioB = PCD()
    RioB.setId(2)
    RioC = PCD()
    RioC.setId(3)

    #Criar Universidades
    UFRJ = Observer()
    UFRJ.nome = "UFRJ"
    Unifesp = Observer()
    Unifesp.nome = "Unifesp"
    USP = Observer()
    USP.nome = "USP"

    #Universidades se inscrevem nos PCDs
    RioA.addUniversidade(UFRJ)
    RioA.addUniversidade(Unifesp)
    RioB.addUniversidade(UFRJ)
    RioB.addUniversidade(USP)
    RioC.addUniversidade(Unifesp)
    RioC.addUniversidade(USP)

    #Alterar condições dos PCDs
    RioA.setTemperatura(25.0)
    RioB.setUmidade(80.0)
    RioC.setPressao(1013.0)
    RioA.setLuminosidade(50.0)





