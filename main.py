from bot_instagram import InstagramBot
import config

username = config.username
password = config.password

url_comment = config.url_comment
url_get_comments = config.url_get_comments
function = 'get_comments'
num_people = config.num_people

instaBot = InstagramBot(username, password, function, url_get_comments)
instaBot.login()