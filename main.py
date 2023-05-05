from abc import ABC, abstractmethod
#Задание 2.
#Рассмотрим принцип инверсии зависимостей. Исправьте следующий код таким
#образом, чтобы классы и верхних, и нижних уровней зависели от одних и тех же
#абстракций, а не от конкретных реализаций.
#class AnonymousAuthentication:
#def doAauthentication(self): pass
#class GithubAuthentication:
#def doAuthentication(self): pass
#class FacebookAuthentication:
#def doAuthentication(self): pass
#class Permissions:
#def __init__(self, auth: AnonymousAuthentication)
#self.auth = auth
#def getPermissions(self):
#self.auth.doAuthentication()
class Authentication(ABC):
    @abstractmethod
    def doAuthentication(self, name: str):
        pass
class AnonymousAuthentication(Authentication):
    def doAuthentication(self, name: str):
        print(f"{name}- вы прошли анонимную авторизацию.")
        pass
class GithubAuthentication(Authentication):
    def doAuthentication(self, name: str):
        print(f"{name}- вы прошли авторизацию в GitHub.")
        pass
class FacebookAuthentication(Authentication):
    def doAuthentication(self, name: str):
        print(f"{name}- вы прошли авторизацию в Facebook.")
        pass

class Permissions:
    def __init__(self, auth: Authentication):
        self.auth = auth

    def getPermissions(self, name:str):
        self.auth.doAuthentication(name)

def execute_application():
    facebook_auth = FacebookAuthentication()
    facebook_auth.doAuthentication("Константин")

    permissions = Permissions(facebook_auth)
    permissions.getPermissions("Konstantin")
if __name__ =="__main__":
    execute_application()
