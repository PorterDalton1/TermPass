import shutil
import os
import pickle
from Credentials import UserInfo
from EncryptUserData import EncryptUserData

def pullData(username):
    with open('./users/' + username + '/websiteCredentials.dat', 'rb') as websiteCredentialsFile:
        return pickle.load(websiteCredentialsFile)

def initDump(user):
    os.mkdir(user.getUserFolder())
    dumpData(user)

def dumpData(user):
    #User = UserInfo()
    with open(user.getUserFolder() + '/websiteCredentials.dat', 'wb') as websiteCredentialsFile:
        pickle.dump(user, websiteCredentialsFile)

def zipAndEncrypt(username):
    if (os.path.exists('./users/' + username + '.zip')):
        return
    shutil.make_archive('./users/' + username, 'zip', './users/' + username)
    os.rmdir('./users/' + username, )


zipAndEncrypt('mikeH23')

'''
x = UserInfo('mikeH23')
x.addCredentials(name='Google', url='https://www.Google.com', email1='holycarton@gmail.com', username='holycarton', password='1234')
x.addCredentials(name='Amazon', url='https://www.Amazon.com', email1='porter.dalton2@gmail.com', username='porterd1', password='qwerty')
x.addCredentials(name='Tennis Warehouse', url='https://www.Tennis-Warehouse.com', email1='porter.dalton2@gmail.com', username='porterd', password='fh4$%F')
x.addCredentials(name='Piano Studio', url='https://app.pianostudio.com', email1='porter.dalton2@gmail.com', username='porterdalton', password='nfeuiuy43', notes='Secret key: 45237')

manageData(x).dumpData()

y = pullData('mikeH23')
y.printData()

y.addCredentials(name='topSpin', url='https://www.topSpin.com', email1='BigAss69@gmail.com', username='fatassery', password='sugarmomma')

manageData(y).dumpData()

z = pullData('mikeH23')

z.printData()
'''