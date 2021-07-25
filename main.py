from player import Player
from user import User
from time import sleep

with open('account.txt') as f:
    email = f.readline().strip()
    password = f.readline().strip()

user = User(email, password, 'https://discord.com/login')
player = Player(130, 25, 65, 15, user)

user.login()
sleep(7)
user.choose()

player.rpg()