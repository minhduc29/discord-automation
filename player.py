from time import sleep
from random import uniform
from message import send_message


class Player:
    """Your game character"""
    def __init__(self, hp, potion, hunt):
        # Your health point
        self.ihp = hp
        self.hp = hp

        # Number of life potion you currently have
        self.potion = potion

        # Hp lost per hunt
        self.hunt = hunt

        # Messages
        self.msg = {
            'hunt': 'rpg ascended hunt h',
            'heal': 'rpg heal',
            'buy': 'rpg buy life potion 10',
            'farm': 'rpg ascended farm',
            'work': 'rpg ascended dynamite'
        }

    def auto_rpg(self):
        """Auto hunt, farm, work"""
        i = 0
        while True:
            if i % 5 == 0:
                send_message(self.msg['work'])
                sleep(1)
            if i % 10 == 0:
                send_message(self.msg['farm'])
                sleep(1)
            if self.potion == 0:
                send_message(self.msg['buy'])
                self.potion = 10
                sleep(1)
            if self.hp > self.hunt:
                send_message(self.msg['hunt'])
                self.hp -= self.hunt
                sleep(40)
            else:
                send_message(self.msg['heal'])
                self.hp = self.ihp
                self.potion -= 1
                sleep(1)
                send_message(self.msg['hunt'])
                self.hp -= self.hunt
                sleep(40)
            sleep(uniform(0, 3))  # Make the program less suspicious
            i += 1
