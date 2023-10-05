import shutil #using make_archive and rmtree
import os
import pickle
from Credentials import UserInfo
import EncryptUserData
from GLOBAL_VARIABLES import *

def pullData(username):
    with open(WORKING_DIR + username + '/data/websiteCredentials.dat', 'rb') as websiteCredentialsFile:
        return pickle.load(websiteCredentialsFile)

def initDump(user):
    os.mkdir(user.getUserFolder())
    os.mkdir(user.getUserFolder() + 'data/')
    dumpData(user)

def dumpData(user):
    #User = UserInfo()
    with open(user.getUserFolder() + 'data' + '/websiteCredentials.dat', 'wb') as websiteCredentialsFile:
        pickle.dump(user, websiteCredentialsFile)

def zipAndEncrypt(username):
    extension = 'zip'
    '''
    path = WORKING_DIR + username + '/data'
    if (os.path.exists(path + extension)):
        return
    shutil.make_archive(path, extension, path)
    shutil.rmtree(path)
    '''

    path = WORKING_DIR + username + '/data'
    path += '.' + extension

    EncryptUserData.encrypt_file('./users/mikeH23/data.zip', EncryptUserData.get_public_key(username))

'''
x = UserInfo('mikeH23')
x.addCredentials(name='Google', url='https://www.Google.com', email1='holycarton@gmail.com', username='holycarton', password='1234')
x.addCredentials(name='Amazon', url='https://www.Amazon.com', email1='porter.dalton2@gmail.com', username='porterd1', password='qwerty')
x.addCredentials(name='Tennis Warehouse', url='https://www.Tennis-Warehouse.com', email1='porter.dalton2@gmail.com', username='porterd', password='fh4$%F')
x.addCredentials(name='Piano Studio', url='https://app.pianostudio.com', email1='porter.dalton2@gmail.com', username='porterdalton', password='nfeuiuy43', notes='Secret key: 45237')

dumpData(x)

y = pullData('mikeH23')
y.printData()

y.addCredentials(name='topSpin', url='https://www.topSpin.com', email1='BigAss69@gmail.com', username='fatassery', password='sugarmomma')
y.addCredentials(name='jimmyWhat', url='https://www.JimmyWhat.com', email1='porter.dalton2@gmail.com', username='jimmy', password='lshbfy6682jsghsyuywu7z')

dumpData(y)

z = pullData('mikeH23')
'''
zipAndEncrypt('mikeH23')