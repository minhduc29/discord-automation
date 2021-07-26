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
            'pickup': 'rpg ladder',
            'mine': 'rpg mine',
            'farm': 'rpg farm carrot',
            'upgrade': 'rpg guild upgrade'
        }

        # Object user
        self.user = user

    def progress(self):
        """Auto progress"""
        i = 0
        self.user.send_message(self.msg['farm'])
        sleep(1)
        while True:
            self.user.send_message(self.msg['chop'])
            if i == 2:
                sleep(1)
                self.user.send_message(self.msg['farm'])
                i = 0
            i += 1
            sleep(301)
            self.user.send_message(self.msg['fish'])
            if i == 2:
                sleep(1)
                self.user.send_message(self.msg['farm'])
                i = 0
            i += 1
            sleep(301)
            self.user.send_message(self.msg['pickup'])
            if i == 2:
                sleep(1)
                self.user.send_message(self.msg['farm'])
                i = 0
            i += 1
            sleep(301)
            self.user.send_message(self.msg['mine'])
            if i == 2:
                sleep(1)
                self.user.send_message(self.msg['farm'])
                i = 0
            i += 1
            sleep(301)

    def experience(self):
        """Auto experience"""
        while True:
            self.user.send_message(self.msg['upgrade'])
            for i in range(2):
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
                for j in range(60):
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
            self.user.send_message(self.msg['upgrade'])
            for i in range(2):
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
                count = 0
                self.user.send_message(self.msg['farm'])
                sleep(1)
                for j in range(60):
                    if j % 5 == 0:
                        self.user.send_message(self.msg['mine'])
                        if count == 2:
                            sleep(1)
                            self.user.send_message(self.msg['farm'])
                            count = 0
                        count += 1
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