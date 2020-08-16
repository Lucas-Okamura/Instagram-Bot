from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import stdiomask

class InstagramBot:
    def __init__(self, username, password):
        '''
        Bot that comment on photos on Instagram
        Args:
            username:string: username to an Instagram account
            password:string: password to an Instagram account
            
        Attributes:
            username:string: username given
            password:string: password given
            base_url:string: instagram website (https://www.instagram.com)
            driver:selenium.webdriver.Chrome: driver that performs actions in the browser
        '''

        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path = "INPUT CHROME DRIVE PATH HERE")

    def login(self):
        '''
        Logs into the Instagram account with the given username and password
        
        Args:
            None
        '''
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)

        user_box = driver.find_element_by_xpath("//input[@name = 'username']")
        user_box.click()
        user_box.clear()
        user_box.send_keys(self.username)

        password_box = driver.find_element_by_xpath("//input[@name = 'password']")
        password_box.click()
        password_box.clear()
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.RETURN)
        time.sleep(3)

        not_now_login = driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")     # If your language is not portuguese, change the "Agora não" to "Not now" or similar
        not_now_login.click()
        time.sleep(1)

        self.comment_on_post(url_target, num_people)

    @staticmethod
    def human_type(phrase, input_comment):
        '''
        Type letter by letter, with random intervals of time in between
        
        Args:
            phrase:string: text that will be written by the function
            input_comment:selenium.webdriver.Chrome.find_element_by_xpath: path to the comment box
        '''

        for letter in phrase:
            input_comment.send_keys(letter)
            time.sleep(random.randint(1,5)/30)
        input_comment.send_keys(" ")

    def comment_on_post(self, url, num_people = 1):
        '''
        Comment on the choosen URL post, choosing random strings on the people list, the number of times that were specified
        on "num_people"
        
        Args:
            url:string: URL of the post to comment
            num_people(optional):int: number of people to pick from the people list
        '''
        
        i = 0       # Counter

        driver = self.driver
        driver.get(url)
        time.sleep(3)

        people = [
            "@person1",
            "@person2",
            "@person3"
            ]

        while (1):
            try:
                driver.find_element_by_class_name("Ypffh").click()
                commentary_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(1, 10)/40)

                for num in range(num_people):
                    person = random.choice(people)
                    self.human_type(person, commentary_box)
                    time.sleep(random.randint(1,4)/4)

                time.sleep(random.randint(1, 4))
                publish = driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]")        # If your language is not portuguese, change the "Publicar" to "Publish" or similar
                publish.click()

                i += 1

                print("You published ", i, " commentaries")

                time.sleep(random.randint(45, 120))
            
                if i % 100 == 0:
                    time.sleep(60*5)
            
            except Exception as e:
                print(e)
                time.sleep(5)

username = str(input("Insert your Instagram username: "))
password = stdiomask.getpass(prompt = "Insert you Instagram password: ", mask = '*')

url_target = str(input("Insert the Instagram URL to be commented: "))
num_people = int(input("Insert the number of people you want to tag: "))

instaBot = InstagramBot(username, password)
instaBot.login()
