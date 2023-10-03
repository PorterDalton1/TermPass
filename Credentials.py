class _websiteCredentials:
    def __init__(self):
        self.name = ""
        self.url = ""
        self.email1 = ""
        self.email2 = ""
        self.username = ""
        self.password = ""
        self.notes = ""

    def __str__(self):
        tmp =  self.name + "\n"
        tmp += "---------------------------\n"
        tmp += "url: " + self.url + "\n"
        tmp += "email1: " + self.email1 + "\n"
        tmp += "email2: " + self.email2 + "\n"
        tmp += "username: " + self.username + "\n"
        tmp += "password: " + self.password + "\n"

        return tmp
        


class UserInfo:
    def __init__(self, username):
        '''inits secure notes and credentials '''
        self._username = username
        self.secure_notes = [] # List of tuples (note_name, file_name)
        self.credentials = [] # List of tuples containing the credentials. ID is the subscript of each item
        self._userFolder = './users/' + self._username

    def getUsername(self):
        return self._username
    
    def getUserFolder(self):
        return self._userFolder
    
    def addCredentials(self, name="", url="", email1="", email2="", username="", password="", notes=""):
        '''To add credentials given all the info'''
        tmp = _websiteCredentials()
        tmp.name = name
        tmp.url = url
        tmp.email1 = email1
        tmp.email2 = email2
        tmp.username = username
        tmp.password = password
        tmp.notes = notes

        self.credentials.append(tmp)

    def removeCredential(self, id):
        '''To remove a credential given the id'''
        if (id > len(self.credentials) or id < 0):
            raise IndexError("id not in list")
        del self.credentials[id]

    def getCredential(self, id):
        '''To get credentials based off id'''
        if (id > len(self.credentials) or id < 0):
            raise IndexError("id not in list")

        return self.credentials[id]
    
    def printData(self):
        '''Prints all the credentials'''
        for i in self.credentials:
            print(i)

    def addSecure_note(self, note):
        pass

'''
x = Credentials("mike")

x.addCredentials(name='Google', url='https://www.Google.com', email1='holycarton@gmail.com', username='holycarton', password='1234')
x.addCredentials(name='Amazon', url='https://www.Amazon.com', email1='porter.dalton2@gmail.com', username='porterd1', password='qwerty')
x.addCredentials(name='Tennis Warehouse', url='https://www.Tennis-Warehouse.com', email1='porter.dalton2@gmail.com', username='porterd', password='fh4$%F')
x.addCredentials(name='Piano Studio', url='https://app.pianostudio.com', email1='porter.dalton2@gmail.com', username='porterdalton', password='nfeuiuy43', notes='Secret key: 45237')

x.printData()
'''