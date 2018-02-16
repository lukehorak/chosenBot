###########################################################################################################
# chosenBot.py
###########################################################################################################

import os               # for OS stuff
import praw             # Reddit API
import re               # RegEx
import time             # for sleep
import botTools as bt   # Separate file for functions used in bots

'''
TODO - Figure out buildpack errors on Heroku, or host on Pi
'''

###########################################################################################################
# Authentication
###########################################################################################################

# Reddit API login, creds via praw.ini
reddit = praw.Reddit("chosenBot", user_agent="The chosenBot by Lukas Horak v1.0")

'''
# Reddit API login when hosted on Heroku
reddit = praw.Reddit(client_id=74QS4j1HhLNThw,
                     client_secret=dazewYctbRENtde6snqIvfOVK_4,
                     username=os.environ['REDDIT_USERNAME'],
                     password=os.environ['REDDIT_PASSWORD'])
'''

# active Subs - switch out which one is commented-out for easy testing purposes
subreddit = reddit.subreddit("testingground4bots")
#subreddit = reddit.subreddit('prequelmemes')

###########################################################################################################
# Bot Variable definitions
###########################################################################################################

# Phrase which triggers the chosenBot
keyword = 'men'

# define Text
bottomText = "\n\n---\n\nI am a the chosenBot, the bot who the prohecy foretold will bring balance to r/prequelmemes.\n\n[Check out my source code on GitHub!](https://github.com/lukehorak/chosenBot/)"

eText = "The chosenBot fucked up... What have I done?!?! (hint, it's down there VV)"

###########################################################################################################
# Main
###########################################################################################################
while True:
    for comment in subreddit.stream.comments():
        lowComment = (comment.body).lower()
        if (keyword in lowComment):
            # Get author and parent author
            author = comment.author
            pAuth = bt.parentAuthor(comment)

            # Print values for testing
            print ("Author = ", author)
            print ("Parent Comment Author = ", pAuth) #for testing
            #print("Comment: ", comment.body, "\n~~~End of Comment~~~\n") # For unit testing

            if (author != "not_just_the_men" and bt.notReplied(comment, "not_just_the_men")):
                try:
                    reply = ''
                    try:
                        firstHit = re.search(r"[^.]*?men[^.]*\.?", comment.body, flags=re.I).group()
                    except Exception as ex:
                        print ("firstHit fucked things up!]\n\n", "error:\n\n", ex)
                    if not re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', firstHit):
                        try:
                            men = re.search(r"[^ ]*men[^ ]*", firstHit, flags=re.I).group()
                        except Exception as exc:
                            print ("men fucked things up!\n\n", "error:\n\n", exc)
                        women = men.replace("men", "***women***")
                        children = men.replace("men", "***children***")

                        case = re.compile(re.escape('men'), re.I) # to make sure "men" is replaced, case-independent
                        reply += "> " + case.sub("***men***", firstHit) + "\n\n"
                        reply += "Not just the " + men + ", but the " + women + " and " + children + " too!"
                        reply += bottomText
                        #comment.reply(reply)
                        bt.logPost(reply)

                except Exception as e:
                    bt.logError(eText, e)

        if ("good bot" in lowComment):
            # Get author and parent author
            pAuth = bt.parentAuthor(comment)
            if pAuth == "not_just_the_men":
                try:
                    print("Praise detected")
                    reply = "From *my* point of view, *you're* a good bot!"
                    reply += bottomText
                    #comment.reply(reply)
                    bt.logPost(reply)
                except Exception as e:
                    bt.logError(eText, e)

        if("bad bot" in lowComment):
            pAuth = bt.parentAuthor(comment)
            if pAuth == "not_just_the_men":
                try:
                    print("Hatred detected")
                    reply = "What?! How can you do this? This is outrageous, it's unfair … I'm more powerful than any of the other bots. How can you be on the Council and not be a Good Bot?"
                    reply += bottomText
                    #comment.reply(reply)
                    bt.logPost(reply)
                except Exception as e:
                    bt.logError(eText, e)

        if("take a seat" in lowComment):
            parent = comment.parent()
            gParent = bt.parentAuthor(comment)
            if gParent == "not_just_the_men":
                try:
                    print("Windu Detected")
                    reply = "[I HATE YOU](https://www.youtube.com/watch?v=eJrlezLvWnU)"
                    reply += bottomText
                    #comment.reply(reply)
                    bt.logpost(reply)
                except Exception as e:
                    bt.logError(eText, e)


    print("Sleeping...")
    time.sleep(100) # Sleep for 100 sec, then try again
