import pymongo
import os
import time

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['newscomment']

def click_news(token:str, news_id:str):
    mycol = mydb[token]
    if mycol.find({ "news_id": news_id }).count() == 0:
        myquery = { "news_id": news_id, "clickcount": 1 }
        mycol.insert_one(myquery)
        return(1)
    else:
        mydoc = mycol.find({ "news_id": news_id }).limit(1)
        for line in mydoc:
            num = line["clickcount"]
            num += 1
            newvalue = { "$set": { "clickcount": num }}
            mycol.update_one({ "news_id": news_id }, newvalue)
            return(num)