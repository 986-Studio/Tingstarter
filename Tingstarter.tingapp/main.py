import os
import sys
import tingbot
from tingbot import *
import kickscraper
import kickscraper.comments

# setup code here
p = kickscraper.Project("tingbot")
project = {}
project["tingbox"] = p.url + "/comments";
com_auth, com_data = kickscraper.comments.getLatestCommentAndAuthorForProjects(project)

def loop():
    # drawing code here
    screen.fill(color='black')
    screen.line(start_xy=(0,30), end_xy=(320,30), width=1, color='green')
    screen.image(p.photo['thumb'], xy=(0,240), align='bottomleft')
    screen.text(p.title,  xy=(160,240), align='bottom', font_size=10)
    screen.text("Last comment", xy=(160,0), align='top', font_size=20)
    screen.text("From: " + com_auth["tingbox"], xy=(3,31), align='topleft', font_size=20)
    screen.text(com_data["tingbox"], font_size=15, align='center')
# run the app
tingbot.run(loop)
