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
    server = user.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/nav/div[2]/div[3]/div[3]/div[2]')
    server.click()

    # Initialize and choose text channel
    channel = user.driver.find_element_by_xpath('//*[@id="channels-3"]')
    channel.click()

def send_messages(user):
    """Send messages"""
    # Initialize your messages
    chop_msg = 'rpg chop'
    fish_msg = 'rpg fish'

    # Send messages
    while True:
        progress(user, fish_msg)
        time.sleep(301)
        progress(user, chop_msg)
        time.sleep(301)

def progress(user, msg):
    msg_input = user.driver.find_element_by_xpath(
        '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div')
    msg_input.send_keys(msg)
    msg_input.send_keys(Keys.ENTER)

auto()
