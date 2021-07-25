from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class User:
    """Your discord account"""
    def __init__(self, email, password, url):
        # Your username and password
        self.email = email
        self.password = password

        # Url of the website you want to automatically access
        self.url = url

        # Driver of the browser you use
        self.driver = webdriver.Chrome("C:/Users/T460/Downloads/chromedriver.exe")

        # Access to the website you want using the driver you want
        self.browse = self.driver.get(self.url)

    def login(self):
        """Login to discord"""
        self.driver.find_element_by_name('email').send_keys(self.email)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_name('password').send_keys(Keys.ENTER)

    def choose(self):
        """Choose where to send messages"""
        self.driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[3]/div[2]/div[2]').click()
        self.driver.find_element_by_xpath('//*[@id="channels"]/div/div[4]').click()

    def send_message(self, msg):
        """Send messages to text channel"""
        msg_xpath = '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div/div'
        self.driver.find_element_by_xpath(msg_xpath).send_keys(msg)
        self.driver.find_element_by_xpath(msg_xpath).send_keys(Keys.ENTER)