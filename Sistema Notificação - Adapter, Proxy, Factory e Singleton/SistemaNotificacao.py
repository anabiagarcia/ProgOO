from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message: str, reciver: str) -> None:
        ...

class SmsNotification(Notification):
    def send(self, message, reciver):
        print(f"SMS: {message} To: {reciver}")

class EmailNotification(Notification):
    def send(self, message, reciver):
        print(f"Email: {message} To: {reciver}")

class PushNotification(Notification):
    def send(self, message, reciver):
        print(f"Push: {message} To: {reciver}")

class SmsAdapter(Notification):
    def __init__(self):
        self.servico = SmsNotification()

    def send(self, message, reciver):
        self.servico.disparar_sms(reciver, message)

class NotificationFactory:
    _types = {
        "sms": SmsNotification,
        "email": EmailNotification,
        "push": PushNotification,
    }

    @staticmethod
    def _create(notification_type: str) -> Notification:
        new = NotificationFactory._types.get(notification_type)
        return new


class CoreComponent():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def CreateInstance(self):
        if not self._initialized:
            self.Email = NotificationFactory._create("email")()
            self.Sms = NotificationFactory._create("sms")()
            self.Push = NotificationFactory._create("push")()
            self._initialized = True

    def getInstance(self, notification_type: str):
        if not hasattr(self, "Email"):
            self.CreateInstance()
        if notification_type == "email":
            return self.Email
        elif notification_type == "sms":
            return self.Sms
        elif notification_type == "push":
            return self.Push

    def send(self, notification_type: str, message: str, reciver: str):
        self.getInstance(notification_type).send(message, reciver)

class NotificationProxy:
    def __init__(self, adapter: CoreComponent):
        self.adapter = adapter

    def send(self, notification_type: str, message: str, reciver: str):
        print("Entrando no proxy")

        if notification_type == "email" and "@" not in reciver:
            print(f"Proxy bloqueou: '{reciver}' não é email válido")
        else:
            self.adapter.send(notification_type, message, reciver)

        print("Saindo do proxy")


class SmsNotification:
    def disparar_sms(self, numero: str, texto: str):
        print(f"SMS: {texto} To: {numero}")

class SmsAdapter(Notification):
    def __init__(self):
        self.servico = SmsNotification()

    def send(self, message, reciver):
        self.servico.disparar_sms(reciver, message)