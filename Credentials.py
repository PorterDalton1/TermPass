import hashlib
import pickle

class Credentials:
    def __init__(self):
        '''inits secure notes and credentials '''
        self.secure_notes = [] # List of tuples (note_name, file_name)
        self.credentials = [] # List of tuples containing the credentials. ID is the subscript of each item

    def addCredentials(self, name=None, url=None, email1=None, email2=None, username=None, password=None, notes=None):
        '''To add credentials given all the info'''
        self.credentials.append((name, url, email1, email2, username, password, notes))

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


x = Credentials()

'''
x.addData(name='Google', url='https://www.Google.com', email1='holycarton@gmail.com', username='holycarton', password='1234')
x.addData(name='Amazon', url='https://www.Amazon.com', email1='porter.dalton2@gmail.com', username='porterd1', password='qwerty')
x.addData(name='Tennis Warehouse', url='https://www.Tennis-Warehouse.com', email1='porter.dalton2@gmail.com', username='porterd', password='fh4$%F')
x.addData(name='Piano Studio', url='https://app.pianostudio.com', email1='porter.dalton2@gmail.com', username='porterdalton', password='nfeuiuy43', notes='Secret key: 45237')
'''
