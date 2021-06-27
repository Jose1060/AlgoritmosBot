import datetime
from bson.objectid import ObjectId
import discord
import pymongo
import librerias.Libreria_lista as list


client = pymongo.MongoClient("mongodb+srv://admin:DSTecsup2@cluster0.m9azk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
TOKEN = 'ODU1NDU4MTMwODU4NDc1NTYw.YMyxeA.HS19XvUiGunajkumM9g6JkbkAP4'

id = "60d1f24576a0d47dcc185f52"


user = client.PostMyGame.users.find_one({"_id": ObjectId(id)})

print(user['name'])