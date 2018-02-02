# chosenBot.py

import praw
import re

# Reddit API login, creds via praw.ini
reddit = praw.Reddit("chosenBot", user_agent="The chosenBot by Lukas Horak v1.0")

# active Subs - switch out which one is commented-out for easy testing purposes
subreddit = reddit.subreddit("testingground4bots")
#subreddit = reddit.subreddit('prequelmemes')


# Phrase which triggers senateBot
keyword = 'men'

# Find phrase and inform them of who the Senate is
for comment in subreddit.stream.comments():
    if keyword in comment.body:
        try:
            reply = ''
            '''
            TODO - make it find the word 'men'
            '''
            hit = re.search(r"[^.]*?men[^.]*\.?", comment.body,)
            #comment.reply(reply)
            print(reply)

            print("posted")
        except Exception as e:
            print("The chosenBot fucked up...\n\n", e)
