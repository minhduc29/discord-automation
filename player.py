from time import sleep

class Player:
    """Your game character"""
    def __init__(self, hp, potion, adv, hunt, user):
        # Your health point
        self.ihp = hp
        self.hp = hp

        # Number of life potion you currently have
        self.potion = potion

        # Hp lost per adv, hunt
        self.adv = adv
        self.hunt = hunt

        # Messages
        self.msg = {
            'adv': 'rpg adv',
            'hunt': 'rpg hunt',
            'heal': 'rpg heal',
            'buy': 'rpg buy life potion 10',
            'chop': 'rpg axe',
            'fish': 'rpg net',
            'pickup': 'rpg pickup'
        }

        # Object user
        self.user = user

    def progress(self):
        """Auto progress"""
        while True:
            self.user.send_message(self.msg['chop'])
            sleep(301)
            self.user.send_message(self.msg['fish'])
            sleep(301)
            self.user.send_message(self.msg['pickup'])
            sleep(301)

    def experience(self):
        """Auto experience"""
        while True:
            if self.potion == 0:
                self.user.send_message(self.msg['buy'])
                self.potion = 10
                sleep(1)
            if self.hp > self.adv:
                self.user.send_message(self.msg['adv'])
                self.hp -= self.adv
                sleep(1)
            else:
                self.user.send_message(self.msg['heal'])
                self.hp = self.ihp
                self.potion -= 1
                sleep(1)
                self.user.send_message(self.msg['adv'])
                self.hp -= self.adv
                sleep(1)
            for i in range(60):
                if self.potion == 0:
                    self.user.send_message(self.msg['buy'])
                    self.potion = 10
                    sleep(1)
                if self.hp > self.hunt:
                    self.user.send_message(self.msg['hunt'])
                    self.hp -= self.hunt
                    sleep(61)
                else:
                    self.user.send_message(self.msg['heal'])
                    self.hp = self.ihp
                    self.potion -= 1
                    sleep(1)
                    self.user.send_message(self.msg['hunt'])
                    self.hp -= self.hunt
                    sleep(61)

    def rpg(self):
        """Auto both progress and experience"""
        while True:
            if self.potion == 0:
                self.user.send_message(self.msg['buy'])
                self.potion = 10
                sleep(1)
            if self.hp > self.adv:
                self.user.send_message(self.msg['adv'])
                self.hp -= self.adv
                sleep(1)
            else:
                self.user.send_message(self.msg['heal'])
                self.hp = self.ihp
                self.potion -= 1
                sleep(1)
                self.user.send_message(self.msg['adv'])
                self.hp -= self.adv
                sleep(1)
            for i in range(60):
                if i % 15 == 0:
                    self.user.send_message(self.msg['chop'])
                    sleep(1)
                elif i % 15 == 5:
                    self.user.send_message(self.msg['fish'])
                    sleep(1)
                elif i % 15 == 10:
                    self.user.send_message(self.msg['pickup'])
                    sleep(1)
                if self.potion == 0:
                    self.user.send_message(self.msg['buy'])
                    self.potion = 10
                    sleep(1)
                if self.hp > self.hunt:
                    self.user.send_message(self.msg['hunt'])
                    self.hp -= self.hunt
                    sleep(61)
                else:
                    self.user.send_message(self.msg['heal'])
                    self.hp = self.ihp
                    self.potion -= 1
                    sleep(1)
                    self.user.send_message(self.msg['hunt'])
                    self.hp -= self.hunt
                    sleep(61)