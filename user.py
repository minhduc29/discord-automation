from selenium import webdriver

class User:
    def __init__(self, username, password, url):
        # Your username and password
        self.username = username
        self.password = password

        # Url of the website you want to automatically access
        self.url = url

        # Driver of the browser you use
        self.driver = webdriver.Chrome("/Users/T460/Downloads/chromedriver")

        # Access to the website you want using the driver you want
        self.browse = self.driver.get(self.url)