from player import Player
from user import User
from time import sleep

with open('account.txt') as f:
    email = f.readline().strip()
    password = f.readline().strip()

user = User(email, password, 'https://discord.com/login')
player = Player(130, 91, 0, user)

user.login()
sleep(25)
# Instead of using user.choose(), you can put a longer sleep time and choose server and channel manually
# Note that the msg_xpath in user.send_message() may need to be changed if error occurs
player.auto_rpg()