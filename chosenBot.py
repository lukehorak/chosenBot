# chosenBot.py

import praw
import re
import botTools as bt

# Reddit API login, creds via praw.ini
reddit = praw.Reddit("chosenBot", user_agent="The chosenBot by Lukas Horak v1.0")

# active Subs - switch out which one is commented-out for easy testing purposes
#subreddit = reddit.subreddit("testingground4bots")
subreddit = reddit.subreddit('prequelmemes')

# Phrase which triggers the chosenBot
keyword = 'men'

# define Text
bottomText = "\n\n---\n\nI am a the chosenBot, the bot who the prohecy foretold will bring balance to r/prequelmemes.\n\n"
bottomText += "[Check out my source code on GitHub!](https://github.com/lukehorak/chosenBot/)"

eText = "The chosenBot fucked up... What have I done?!?! (hint, it's down there VV)"

# Where the magic happens
for comment in subreddit.stream.comments():
    if (keyword in (comment.body).lower()):
        # Get author and parent author
        author = comment.author
        pAuth = bt.parentAuthor(comment)

        # Print values for testing
        print ("Author = ", author)
        print ("Parent Comment Author = ", pAuth) #for testing
        #print("Comment: ", comment.body, "\n~~~End of Comment~~~\n") # For unit testing

        if (author != "not_just_the_men"):
            try:
                reply = ''
                try:
                    firstHit = re.search(r"[^.]*?men[^.]*\.?", comment.body, flags=re.I).group()
                except Exception as ex:
                    print ("firstHit fucked things up!]\n\n", "error:\n\n", ex)
                try:
                    men = re.search(r"[^ ]*men[^ ]*", firstHit, flags=re.I).group()
                except Exception as exc:
                    print ("men fucked things up!\n\n", "error:\n\n", exc)
                # Avoid matching URLs
                if not re.match(r"(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?", men):
                    women = men.replace("men", "***women***")
                    children = men.replace("men", "***children***")

                    case = re.compile(re.escape('men'), re.I) # to make sure "men" is replaced, case-independenr
                    reply += "> " + case.sub("***men***", firstHit) + "\n\n"
                    reply += "Not just the " + men + ", but the " + women + " and " + children + " too!"
                    reply += bottomText
                    #comment.reply(reply)
                    bt.logPost(reply)

            except Exception as e:
                bt.logError(eText, e)

    if ("good bot" in (comment.body).lower()):
        # Get author and parent author
        pAuth = bt.parentAuthor(comment)
        if pAuth == "not_just_the_men":
            try:
                print("Praise detected")
                reply = "From *my* point of view, *you're* a good bot"
                reply += bottomText
                #comment.reply(reply)
                bt.logPost(reply)
            except Exception as e:
                bt.logError(eText, e)

    if("bad bot" in (comment.body).lower()):
        pAuth = bt.parentAuthor(comment)
        if pAuth == "not_just_the_men":
            try:
                print("Hatred detected")
                reply = "[I HATE YOU](https://www.youtube.com/watch?v=eJrlezLvWnU)"
                reply += bottomText
                #comment.reply(reply)
                bt.logPost(reply)
            except Exception as e:
                bt.logError(eText, e)
