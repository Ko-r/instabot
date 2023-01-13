from instabot import Bot
bot = Bot()
bot.login(username="",password="")

bot.upload_photo("",caption="")
#insert message in blank and input username in user1,user2 
bot.send_message("blank",['user1','user2'])

#list of followers insert username you want a list of followers from
bot.get_user_followers("blank")