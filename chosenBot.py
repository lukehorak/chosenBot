# chosenBot.py

import praw
import re

# Reddit API login, creds via praw.ini
reddit = praw.Reddit("chosenBot", user_agent="The chosenBot by Lukas Horak v1.0")

# active Subs - switch out which one is commented-out for easy testing purposes
subreddit = reddit.subreddit("testingground4bots")
#subreddit = reddit.subreddit('prequelmemes')

# Phrase which triggers the chosenBot
keyword = 'men'

# Find phrase and inform them of who the Senate is
for comment in subreddit.stream.comments():
    if (keyword in comment.body and getattr(comment.author, 'name', None) != "not_just_the_men"):
        print("comment: ", comment.body, "\n\n")
        try:
            reply = ''
            firstHit = re.search(r"[^.]*?men[^.]*\.?", comment.body, flags=re.I).group()

            men = re.search(r"[^ ]+men[^ ]+", hit, flags=re.I).group()
            women = men.replace("men", "*women*")
            children = men.replace("men", "*chldren*")

            case = re.compile(re.escape('men'), re.I) # to make sure "men" is replaced, case-independent
            reply += "> " + case.sub("***men***", hit) + "\n\n"
            reply += "Not just the " + men + ", but the " + women + " and " + children + " too!"
            comment.reply(reply)
            #print(reply)

            print("posted") # For logging purposes
        except Exception as e:
            print("The chosenBot fucked up... What have I done?!?! (hint, it's down there VV)\n\n", e)
