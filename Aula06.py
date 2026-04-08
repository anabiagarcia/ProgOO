from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message: str, reciver: str) -> None:
        ...

class SmsNotification(Notification):
    def send(self, message, reciver) -> None:
        print(f"SMS: {message} To: {reciver}")

class EmailNotification(Notification):
    def send(self, message, reciver) -> None:
        print(f"Email: {message} To: {reciver}")

class PushNotification(Notification):
    def send(self, message, reciver) -> None:
        print(f"Push: {message} To: {reciver}")

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

    def _new_(cls):
        if cls._instance is None:
            cls.instance = super().new_(cls)
            cls._instance._initialized = False
        return cls._instance

    def CreateInstance(self):
        if not self._initialized:
            self.EmailNotification = NotificationFactory._create("email")()
            self.SmsNotification = NotificationFactory._create("sms")()
            self.PushNotification = NotificationFactory._create("push")()
            self._initialized = True

    def getInstance(self, notification_type: str):
        self.CreateInstance()
        if notification_type == "email":
            return self.EmailNotification
        elif notification_type == "sms":
            return self.SmsNotification
        elif notification_type == "push":
            return self.PushNotification
       


