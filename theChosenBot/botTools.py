###########################################################################################################
# botTools.py
###########################################################################################################

import datetime

# TODO - finish logger
###########################################################################################################
# Main Tools
###########################################################################################################

def parentAuthor(comment):
    parent = comment.parent()
    return parent.author

def logPost(reply):
    print("posted\n\n") # For logging purposes
    print("Reply:\n", reply, "\n~~~End of Reply~~~\n")

def logError(eText, e):
    print(eText, "\n\n", e)

def notReplied(comment, user):
    for reply in comment.replies:
        if reply.author == user:
            return False
    return True

###########################################################################################################
# Logger
###########################################################################################################

def makeLog():
    timestamp = str(datetime.datetime.now())
    # Do stuff with timestamp
    return timestamp
