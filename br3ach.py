import requests


url = "https://breachdirectory.p.rapidapi.com/"
import os

# get the size of file
a = os.path.getsize('config.txt')
b = 1
if ( a < b ):
 x = input("Api_Key : ")
 y = open('config.txt', 'w')
 #z = ('username ='' "' + str(x) + '"')
 z= (x)
 #z = ('"' + str(x) + '"')
 y.write(z)
 y.close()
 import config 
 file1 = open("config.txt","r+") 
 M = (file1.read())
 val = input("Enter your username,email or phone: ")
 headers = {
    'x-rapidapi-host': "breachdirectory.p.rapidapi.com",
    'x-rapidapi-key': (M)
    }
 querystring = {"func":"auto","term":{val}}

 response = requests.request("GET", url, headers=headers, params=querystring)
 print(response.text)
else : 
 import config 
 file1 = open("config.txt","r+") 
 M = (file1.read())
 val = input("Enter your username,email or phone: ")
 headers = {
    'x-rapidapi-host': "breachdirectory.p.rapidapi.com",
    'x-rapidapi-key': (M)
    }
 querystring = {"func":"auto","term":{val}}

 response = requests.request("GET", url, headers=headers, params=querystring)
 print(response.text)
 
 

 
