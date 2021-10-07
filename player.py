from time import sleep

class Player:
    """Your game character"""
    def __init__(self, hp, potion, hunt, user):
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

        # Object user
        self.user = user

    def auto_rpg(self):
        """Auto hunt, farm, work"""
        i = 0
        count = 2
        while True:
            if i % 5 == 0:
                self.user.send_message(self.msg['work'])
                if count == 2:
                    sleep(1.5)
                    self.user.send_message(self.msg['farm'])
                    count = 0
                count += 1
                sleep(1.5)
            if self.potion == 0:
                self.user.send_message(self.msg['buy'])
                self.potion = 10
                sleep(1.5)
            if self.hp > self.hunt:
                self.user.send_message(self.msg['hunt'])
                self.hp -= self.hunt
                sleep(61.5)
            else:
                self.user.send_message(self.msg['heal'])
                self.hp = self.ihp
                self.potion -= 1
                sleep(1.5)
                self.user.send_message(self.msg['hunt'])
                self.hp -= self.hunt
                sleep(61.5)
            i += 1