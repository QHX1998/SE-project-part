import pymongo
import os
import time
import random

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['newscomment']

class CommentInfo:
    def __init__(self, id:str, commentor:str, content:str, reply_count:int, like:int):
        self.id = id
        self.commentor = commentor
        self.content = content
        self.reply_count = reply_count
        self.like = like

class CommentPage:
    def __init__(self, comments:[CommentInfo for i in range(1000)], count:int):
        self.comments = comments
        self.count = count

class ReplyInfo:
    def __init__(self, id:str, replier:str, repliee:str, content:str, like:int):
        self.id = id
        self.replier = replier
        self.repliee = repliee
        self.content = content
        self.like = like

class ReplyPage:
    def __init__(self, replies:[ReplyInfo for i in range(100)], totalcount:int):
        self.replies = replies
        self.totalcount = totalcount

def checkcode():
    check_code = ''
    for i in range(7):
        num = random.randint(0, 9)
        letter = chr(random.randint(97, 122))
        Letter = chr(random.randint(65, 90))
        s = str(random.choice([num, letter, Letter]))
        check_code += s
    return(check_code)

def addcomment(token:str, news_id, content:str):
    mycol = mydb[str(news_id)]
    while True:
        code = checkcode()
        myquery = { "id": code }
        num = mycol.find(myquery).count()
        if num == 0:
            break
    localtime = time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
    mydict = { "type": "comment", "user": token, "object": str(news_id), "msg": content, "id": code, "time": localtime, "like": 0}
    x = mycol.insert_one(mydict)
    return("评论成功")

def addreply(token:str, news_id, comment_id:str, content:str):
    mycol = mydb[str(news_id)]
    while True:
        code = checkcode()
        myquery = { "id": code }
        num = mycol.find(myquery).count()
        if num == 0:
            break
    localtime = time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
    mydict = { "type": "reply", "user": token, "object": comment_id , "msg": content, "id": code, "time": localtime, "like": 0}
    x = mycol.insert_one(mydict)
    return("回复成功")

def remove_comment(token:str, news_id, comment_id:str):
    mycol = mydb[str(news_id)]
    x = { "id": comment_id}
    mycol.delete_one(x)
    x = { "object": comment_id}
    mycol.delete_many(x)
    num = mycol.find(x).count()
    if num == 0:
        return('删除成功')
    else:
        return('删除失败，请重新操作')

def remove_reply(token:str, news_id, reply_id):
    mycol = mydb[str(news_id)]
    x = { "id": reply_id}
    mycol.delete_one(x)
    num = mycol.find(x).count()
    if num == 0:
        return('删除成功')
    else:
        return('删除失败，请重新操作')

def get_comments(token, news_id):
    mycol = mydb[str(news_id)]
    myquery = { "type": "comment"}
    mydoc = mycol.find(myquery)
    comments = []
    i = 0
    for line in mydoc:
        num = mycol.find({"object": line["id"]}).count()
        comment = CommentInfo(line["id"], line["user"], line["msg"], num, line["like"])
        comments.append(comment)
        i += 1
    page = CommentPage(comments, i)
    return(page)

def get_replied(token, news_id, comment_id):
    mycol = mydb[str(news_id)]
    x = { "type": "reply", "object": comment_id }
    mydoc = mycol.find(x)
    replies = []
    i = 0
    for line in mydoc:
        y = mycol.find({"id": comment_id}).limit(1)
        for l in y:
            repliee = l["user"]
        reply = ReplyInfo(line["id"], line["user"], repliee, line["msg"], line["like"])
        replies.append(reply)
        i += 1
    page = ReplyPage(replies, i)
    return(page)

def like(token, news_id, id):
    mycol = mydb[str(news_id)]
    x = { "id": id }
    mydoc = mycol.find(x).limit(1)
    for line in mydoc:
        i = line["like"]
    newvalue = { "$set": { "like": i+1 }}
    mycol.update_one(x, newvalue)
    return('点赞成功')

def getcommentid(news_id, i:int):
    mycol = mydb[str(news_id)]
    myquery = { "type": "comment" }
    mydoc = mycol.find(myquery)
    num = mycol.find(myquery).count()
    if num < i:
        return('no such comment!')
    else:
        j = 1
        for line in mydoc:
            if j == i:
                return(line["id"])
            j += 1

def getreplyid(news_id, comment_id, i:int):
    mycol = mydb[str(news_id)]
    myquery = { "type": "reply", "object": comment_id }
    mydoc = mycol.find(myquery)
    num = mycol.find(myquery).count()
    if num < i:
        return('no such reply!')
    else:
        j = 1
        for line in mydoc:
            if j == i:
                return(line["id"])
            j += 1

def printit(type:str, id:str):
    if type.find('new')>=0:
        page = get_comments("user1", id)
        commentlist = page.comments
        for line in commentlist:
            print(line.commentor)
            print(line.content)
    else:
        page = get_replied("user1", 303, id)
        replylist = page.replies
        for line in replylist:
            print(line.replier, " to ", line.repliee)
            print(line.content)

'''
addcomment("user1", 303, "This news is fun")
addcomment("user2", 303, "Sure hope it will work")
addcomment("user3", 303, "I don`t believe it!")
addreply("user1", 303, getcommentid(303, 2), "I don`t think so")
addreply("user2", 303, getcommentid(303, 2), "I insist!")
remove_comment("user1", 303, getcommentid(303,3))
printit('news', '303')
'''
