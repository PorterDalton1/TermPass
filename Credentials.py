import random
import urllib.parse
from GLOBAL_VARIABLES import *

class _websiteCredentials:
    def __init__(self):
        self._name = ""
        self._id = 0 #Is defined by a random number when called by UserInfo
        self._url = ""
        self._email1 = ""
        self._email2 = ""
        self._username = ""
        self._password = ""
        self._notes = ""


    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name

    def getId(self):
        return self._id
    
    def setId(self, id):
        self._id = id

    def getUrl(self):
        return self._url
    
    def setUrl(self, url):
        full_url = url # TODO make this into a full url
        self._url = full_url

    def getEmail1(self):
        return self._email1
    
    def setEmail1(self, email1):
        self._email1 = email1
    
    def getEmail2(self):
        return self._email2
    
    def setEmail2(self, email2):
        self._email2 = email2

    def getUsername(self):
        return self._username
    
    def setUsername(self, username):
        self._username = username

    def getPassword(self):
        return self._password
    
    def setPassword(self, password):
        self._password = password

    def getNotes(self):
        return self._notes
    
    def setNotes(self, notes):
        self._notes = notes

    def __str__(self):
        tmp =  self.getName() + "\n"
        tmp += "---------------------------\n"
        tmp += "id: " + str(self.getId()) + "\n"
        tmp += "url: " + self.getUrl() + "\n"
        tmp += "email1: " + self.getEmail1() + "\n"
        tmp += "email2: " + self.getEmail2() + "\n"
        tmp += "username: " + self.getUsername() + "\n"
        tmp += "password: " + self.getPassword() + "\n"

        return tmp
        


class UserInfo:
    def __init__(self, username):
        '''inits secure notes and credentials '''
        self._username = username
        self.secure_notes = [] # List of tuples (note_name, file_name)
        self.credentials = [] # List of tuples containing the credentials. ID is the subscript of each item
        self._userFolder = WORKING_DIR + self._username + '/'

    def getUsername(self):
        return self._username
    
    def getUserFolder(self):
        return self._userFolder
    
    def addCredentials(self, name="", url="", email1="", email2="", username="", password="", notes=""):
        '''To add credentials given all the info'''

        tmpInt = random.randint(1000000, 9999999) #Generate random 7 digit number

        while (tmpInt in [i.getId() for i in self.credentials]):
            tmpInt = random.randint(1000000, 9999999)

        tmp = _websiteCredentials()
        tmp.setName(name)
        tmp.setId(tmpInt)
        tmp.setUrl(url)
        tmp.setEmail1(email1)
        tmp.setEmail2(email2)
        tmp.setUsername(username)
        tmp.setPassword(password)
        tmp.setNotes(notes)
        
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
x = UserInfo("mike")

x.addCredentials(name='Google', url='google.com', email1='holycarton@gmail.com', username='holycarton', password='1234')
x.addCredentials(name='Amazon', url='https://www.Amazon.com', email1='porter.dalton2@gmail.com', username='porterd1', password='qwerty')
x.addCredentials(name='Tennis Warehouse', url='https://www.Tennis-Warehouse.com', email1='porter.dalton2@gmail.com', username='porterd', password='fh4$%F')
x.addCredentials(name='Piano Studio', url='https://app.pianostudio.com', email1='porter.dalton2@gmail.com', username='porterdalton', password='nfeuiuy43', notes='Secret key: 45237')

x.printData()
'''
