# Instagram Bot
Bot that comments on Instagram posts using Selenium. Must have Chrome Driver installed.
Language: Portuguese/BR

Don't forget to install Chrome Driver and put the path on the code (download Chrome Driver according to your Google Chrome version)

## 1. Files

### 1.1. bot_instagram_comment.py

Contains InstagramBot class, which has, currently, two functions, to comment and to get comments on Instagram posts.

* **Arguments**:
    * username(string)
    * password(string)
    * function(string)
    * url("comment":string, "get_comments":list)
    * num_people(int, optional)

See next section to more information about the arguments

### 1.2. config.py

Contains pertinent information to the bot. Inside the file, you must provide:

* **username(string)**: username of Instagram account
* **password(string**: password of Instagram account
* **function(string)**: currenty, can receive two values: "comment" and "get_comments"
        * "comment": comment nonstop on Instagram post, needs to provide @s in the "people" list on "comment_on_post" function
        * "get_comments": scrapper to get all Instagram comments from one or more posts
* **url_comment(string)**: URL which will be commented
* **url_get_comments(list)**: list with one or more URLs to get the comments (scrapper)
* **num_people(int, optional)**: pertinent when using "comment" function, choose the number of people to tag in the same commentary see

### 1.3. main.py

Contains the main script, run it and be happy!

* **Outputs**: 
    * function "comment": no outputs, just comment nonstop on Instagram post
    * function "get_comments": returns a csv with all the Instagram comments in a post