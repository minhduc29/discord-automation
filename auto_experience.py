from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from user import User
import time

def auto():
    # Initialize your account
    username = 'email'
    password = 'password'
    url = 'https://discord.com/'
    user = User(username, password, url)

    login(user)

    # Wait for the web to load
    time.sleep(7)

    choose(user)
    send_messages(user)

def login(user):
    """Login to discord"""
    # Initialize and access to login section
    open_button = user.driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[1]/header[2]/nav/div[2]/a')
    open_button.click()

    # Initialize and input email
    username_input = user.driver.find_element_by_name('email')
    username_input.send_keys(user.username)

    # Initialize and input password
    password_input = user.driver.find_element_by_name('password')
    password_input.send_keys(user.password)

    # Initialize and login 
    login_button = user.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
    login_button.click()

def choose(user):
    """Choose where you want to automatically send messages"""
    # Initialize and choose discord server
    server = user.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/nav/div[2]/div[3]/div[5]/div[2]')
    server.click()

    # Initialize and choose text channel
    channel = user.driver.find_element_by_xpath('//*[@id="channels-2"]')
    channel.click()

def send_messages(user):
    """Send messages"""
    # Initialize your messages
    adv_msg = 'rpg adv'
    hunt_msg = 'rpg hunt'
    heal_msg = 'rpg heal'
    buy_potion_msg = 'rpg buy life potion 10'

    # Your health point
    hp = 140

    # Your life potion
    potion = 10

    # Hp lost per adv, hunt
    adv = 60
    hunt = 10

    # Send messages
    while True:
        if potion == 0:
            experience(user, buy_potion_msg)
            potion = 10
            time.sleep(1)
        if hp > adv:
            experience(user, adv_msg)
            hp -= adv
            time.sleep(1)
        else:
            experience(user, heal_msg)
            hp = 140
            potion -= 1
            time.sleep(1)

            experience(user, adv_msg)
            hp -= adv
            time.sleep(1)
        for i in range(60):
            if potion == 0:
                experience(user, buy_potion_msg)
                potion = 10
                time.sleep(1)
            if hp > hunt:
                experience(user, hunt_msg)
                hp -= hunt
                time.sleep(61)
            else:
                experience(user, heal_msg)
                hp = 140
                potion -= 1
                time.sleep(1)

                experience(user, hunt_msg)
                hp -= hunt
                time.sleep(61)

def experience(user, msg):
    msg_input = user.driver.find_element_by_xpath(
        '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div')
    msg_input.send_keys(msg)
    msg_input.send_keys(Keys.ENTER) 

auto()
