from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pandas as pd
import os

class InstagramBot:
    def __init__(self, username, password, function, url, num_people=1):
        '''
        Bot that comment on photos on Instagram
        Args:
            username:string: username to an Instagram account
            password:string: password to an Instagram account
            function:string: 'comment' if only comment or 'get_comments' to get comments (scrapper)
            url:string/list: unique url if 'comment', list of url if 'get_comments'
            num_people(optional):int: number of people to tag, valid only if 'comment'
            
        Attributes:
            username:string: username given
            password:string: password given
            base_url:string: instagram website (https://www.instagram.com)
            driver:selenium.webdriver.Chrome: driver that performs actions in the browser
        '''

        self.username = username
        self.password = password
        self.function = function
        self.url = url
        self.num_people = num_people
        self.driver = webdriver.Chrome(executable_path = "D:\Códigos\Chrome Driver\chromedriver.exe")

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

        self.run_bot()

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

    def comment_on_post(self, num_people):
        '''
        Comment on the choosen URL post, choosing random strings on the people list, the number of times that were specified
        on "num_people"
        
        Args:
            num_people(optional):int: number of people to pick from the people list
        '''
        
        i = 0       # Counter

        driver = self.driver
        driver.get(self.url)
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
                cache = []

                for num in range(num_people):
                    person = random.choice(people)

                    if person not in cache:
                        cache.append(person)

                    elif person in cache:
                        check = True
                        while check:
                            person = random.choice(people)
                            if person not in cache:
                                check = False
                                cache.append(person)
                    
                    self.human_type(person, commentary_box)
                    time.sleep(random.randint(1,4)/4)

                time.sleep(random.randint(1, 4))
                publish = driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]")        # If your language is not portuguese, change the "Publicar" to "Publish" or similar
                publish.click()

                i += 1

                print("You published ", i, " commentaries")

                time.sleep(random.randint(45, 90))
            
                if i % 100 == 0:
                    time.sleep(60*5)
            
            except Exception as e:
                print(e)
                time.sleep(5)

    def scroll(self):
        """
        Scroll screen to show all comments

        Args:
            None
        """

        # Get scroll height
        try:
            driver = self.driver
            while True:
                # Click on "plus" sign
                print("Carregando mais comentários...")
                driver.find_element_by_xpath("//button[contains(@class, 'dCJp8')]").click()

                # Wait to load page
                time.sleep(1)
        except:
            pass

    def get_comments(self):
        """
        Get all the comments from Instagram URLs

        Args:
            None
        """     
        try:
            # Getting all the comments from the post
            all_comments = []
            for url in self.url:
                driver = self.driver
                driver.get(url)
                time.sleep(3)

                # Scroll to load all the comments
                self.scroll()

                comment = driver.find_elements_by_class_name('gElp9 ')
                for c in comment:
                    container = c.find_element_by_class_name('C4VMK')
                    content = container.find_elements_by_xpath('(.//span)')[1].text
                    content = content.replace('\n', ' ').strip().rstrip()
                    print(content)
                    all_comments.append(content)
                    time.sleep(5)

            # Exporting comments to csv
            df = pd.DataFrame({"comments" : all_comments})

            # Check if file already exists and export to csv
            i = 0
            exists = True

            while exists:
                filename = f'comments{i}.csv'
                filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
                if os.path.isfile(filepath):
                    i += 1
                else:
                    df.to_csv(filename, sep=';', index=False)
                    exists = False

        except Exception as e:
            print(e)
            time.sleep(5)


    def run_bot(self):
        if self.function == 'comment':
            self.comment_on_post(self.num_people)
            print('chegou')

        elif self.function == 'get_comments':
             self.get_comments()

