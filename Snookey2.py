import sys
import praw
import pytz
import time
import datetime
import requests
import webbrowser
from pytz import timezone

print("Welcome to Snookey2 v2.0 made by u/Spikeedoo and modified by u/IOnlyPlayAsDrif!\n")
print("Contact me or Spikeedoo for help! My Discord is Drift#5339.\n")
print("Remember to follow the Reddit TOS and Broadcasting Guidelines here: https://www.redditinc.com/policies/broadcasting-content-policy\n")
print("The app icon is the official logo to RPAN so credit to Reddit for the logo.\n")
print("If you find any bugs or errors in Snookey2, please contact me at u/IOnlyPlayAsDrif or on Discord at Drift#5339!\n")

# 'Reddit for Android' Client ID
client_id = "ohXpoqrZYub1kg"
response_type = "token"
scope = "*"
callback = "http://localhost:65010/callback"
state = "SNOOKEY"
request_url = "https://www.reddit.com/api/v1/authorize?client_id=%s&response_type=%s&redirect_uri=%s&scope=%s&state=%s" % (client_id, response_type, callback, scope, state)

#Open browser to get access token
webbrowser.open(request_url, new=0)

#Get user input
print("The access code can be found after you click Accept and in the URL after it's done loading after the part that says access_token, but DON'T include the = or &.\n")
while True:
  try:
    user_token = input("Please enter your access token:\nType tutorial for a video tutorial on how to use Snookey!\nType reopen in the field to reopen the webpage if you closed it/didn't load up.\n")
    options = user_token.lower()
    if options == "tutorial":
      print("")
      webbrowser.open("https://www.youtube.com/watch?v=Oi54fiFOoCI&t=2s", new=0)
      continue
    elif options == "reopen":
      print("")
      webbrowser.open(request_url, new=0)
      continue
    elif len(user_token) < 40:
      print("")
      ays = input("This access token is in a different format, or you copy and pasted it wrong.\nAre you sure this is correct? Type yes or no to answer:\n")
      if ays.lower() == "yes":
        print("")
        break
      if ays.lower() == "no":
        print("")
        continue
      else:
        print("")
        print("Invalid response inputted. Please try again.")
        print("")
        continue
    elif user_token[0:12].isdigit() == False:
      print("")
      ays = input("This access token is in a different format, or you copy and pasted it wrong.\nAre you sure this is correct? Type yes or no to answer:\n")
      if ays.lower() == "yes":
        break
      if ays.lower() == "no":
        print("")
        continue
      else:
        print("")
        print("Invalid response inputted. Please try again.")
        print("")
        continue
  except:
    print("Unexpected error occured, closing program in 10 seconds...")
    time.sleep(10)
    sys.exit()
  else:
    break
  
full_token = "Bearer " + user_token

while True:
  try:
    print("")
    subreddit = input("Subreddit you want to broadcast to:\nType list in the field to get a list of the subreddits you can stream to!\n")
    subset = subreddit.lower()
    
    if subset == "list":
      print("")
      print("Here's the list of subreddits for you:")
      date_format='%H'
      date = datetime.datetime.now(tz=pytz.utc)
      date = date.astimezone(timezone('US/Pacific'))
      
      if datetime.datetime.utcnow().strftime("%A") == "Thursday":
        if date.strftime(date_format) < 17:
          print("PAN - The OG subreddit for all livestreams on Wednesday's from Midnight to 5PM PST!")
        else:
          pass
      else:
        pass
      url = "https://pastebin.com/raw/rgsZYPkC"
      r = requests.get(url)
      content = r.text
      Dict = eval(content)
      for key,val in Dict.items():
        print("")
        print(key + " - " + val)
      print("The list and database get updated whenever they add new subreddits and I have the time to add them.")
      continue
    
    elif subset == "thegamerlounge":
      while True:
        try:
          print("")
          assure = input("This program is not meant to be used to just do random gaming streams, please use this program for things that are worth the limited spots.\nDO NOT do a boring regular gaming stream.\nIf you're going to do a gaming stream, make sure it has something interesting and fun to it.\nIf you want to do just a normal gaming stream and there's already a bunch of other people doing a normal gaming stream on RPAN, please wait until they're done so RPAN isn't flooded with gaming streams.\n\nType yes if you read the whole thing and understand.\n")
          assset = assure.lower()
          if assset == "yes":
            break
          
        except:
          print("Please type yes or no into the prompt.")
          continue
        else:
          if assset == "no":
            sys.exit()
          print("Please type yes or no into the prompt.")
          continue
  except:
    sys.exit()

  url = "https://pastebin.com/raw/6D92xhca"
  r = requests.get(url)
  content = r.text
  
  if subset not in str([content]):
    print("")
    subnotfound = input("The subreddit you just typed in couldn't be found in this script's database.\nType yes to move on with " + subreddit + " or type no if you made a mistake.\n")
    snf = subnotfound.lower()
    if snf == "yes":
      print("")
      break
    if snf == "no":
      print("")
      continue
    else:
      print("")
      print("Invalid response. Please try again.")
      continue
  
  else:
    if subset == "pan":
      if datetime.datetime.utcnow().strftime("%A") == "Thursday":
        break
        if datetime.datetime.utcnow().hour < 17:
          break
        else:
          print("")
          print("RPAN is available on Wednesdays from Midnight-5PM PST (times might change).\nPlease pick another subreddit to stream to.")
          continue
      else:
        print("")
        print("RPAN is available on Wednesdays from Midnight-5PM PST (times might change).\nPlease pick another subreddit to stream to.")
        continue
    break
  
title = input("Stream title:\n")

broadcast_endpoint = "https://strapi.reddit.com/r/%s/broadcasts?title=%s" % (subreddit, title)

payload = {}
headers = {
  'User-Agent': 'Project SnooKey/0.1',
  'Authorization': full_token
}

# Request broadcast slot
while True:
  token_req = requests.request("POST", url=broadcast_endpoint, headers=headers, data=payload)

  if token_req.status_code == 200:
    # Success!  Stream prepped
    response = token_req.json()
    print("")
    print("Server Link: rtmp://ingest.redd.it/inbound/")
    print("Your Stream Key: " + response["data"]["streamer_key"])
    print("DON'T share your Stream Key with anyone.")
    print("You can put these into your OBS Settings by going to the Stream section of the settings and switching Service to Custom...")
    print("YOU ARE LIVE: " + response["data"]["post"]["outboundLink"]["url"])
    print("This program will close in 1 minute.")
    time.sleep(60)
    sys.exit()
  else:
    # Failed
    print("")
    print("Stream failed to connect! Trying again in 2 seconds...")
    try:
      print("Error message: " + token_req.json()["status"])
      time.sleep(2)
    except:
      print("Error message: Invalid subreddit/access code/broadcast title.\nPlease restart the program and try again.\nThis program will automatically close in 10 seconds.")
      time.sleep(10)
      sys.exit()

# Fix to prevent windows .exe from closing on completion
#print("")
#aainput("Press enter to exit...")
