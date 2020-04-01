import sys
import pytz
import time
import datetime
import requests
import webbrowser
from pytz import timezone
from pypresence import Presence
  
print("Connecting to Discord for Rich Presence...\n")

try:
  client_id = "694286426338099250"
  RPC = Presence(client_id)
  RPC.connect()
  RPC.update(state="Setting up RPAN stream...", large_image="icon", large_text="Made by u/IOnlyPlayAsDrif", start=int(time.time()))
except:
  print("Failed to connect to Discord, restart the program or try again later to get Rich Presence!")

print("Welcome to Snookey2 v2.3 made by u/Spikeedoo and modified by u/IOnlyPlayAsDrif!\n")
print("Now with NEW Discord Rich Presence!\n")
print("Remember to follow the Reddit TOS and Broadcasting Guidelines here: https://www.redditinc.com/policies/broadcasting-content-policy\n")
print("The app icon is the official logo to RPAN so credit to Reddit for the logo.\n")
print("Join the RPAN Discord Server if you need help with Snookey2, or just want to chat with other streamers/viewers!\nhttps://discord.gg/NDfcVkP\n")


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
    user_token = input("Please enter your access token:\nType tutorial for a video tutorial on how to use Snookey!\nType reopen in the field to reopen the webpage if you closed it/didn't load up.\nType discord in the prompt to join the Unoffical RPAN Server for chatting with other streamers and Snookey2 support/bug reports/suggestions!\n")
    options = user_token.lower()
    if options == "tutorial":
      print("")
      webbrowser.open("https://www.youtube.com/watch?v=Oi54fiFOoCI&t=2s", new=0)
      continue
    elif options == "reopen":
      print("")
      webbrowser.open(request_url, new=0)
      continue
    elif options == "discord":
        print("")
        webbrowser.open("https://discord.gg/NDfcVkP", new=0)
        continue
    elif len(user_token) < 40:
      if len(user_token) < 36:
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
      else:
        break
    elif user_token[0:8].isdigit() is False:
      if user_token[0:12].isdigit() is False:
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
      else:
        break
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
      
      if datetime.datetime.utcnow().strftime("%A") == "Wednesday":
        if date.strftime(date_format) < 17 and date.strftime(date_format) > 1:
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
      if datetime.datetime.utcnow().strftime("%A") == "Wedneday":
        break
        if date.strftime(date_format) < 17 and date.strftime(date_format) > 1:
          break
        else:
          print("")
          print("RPAN is available on Wednesdays from 1AM-5PM PST (times might change).\nPlease pick another subreddit to stream to.")
          continue
      else:
        print("")
        print("RPAN is available on Wednesdays from 1AM-5PM PST (times might change).\nPlease pick another subreddit to stream to.")
        continue
    break
  
title = input("Stream title:\n")

broadcast_endpoint = "https://strapi.reddit.com/r/%s/broadcasts?title=%s" % (subreddit, title)

payload = {}
headers = {
  'User-Agent': 'Project SnooKey/0.1',
  'Authorization': full_token
}

count = 0

# Request broadcast slot
while True:
  token_req = requests.request("POST", url=broadcast_endpoint, headers=headers, data=payload)

  if token_req.status_code == 200:
    # Success!  Stream prepped
    response = token_req.json()
    try:
      RPC.update(state="Streaming " + title + " on r/" + subset + "!", details=response["data"]["post"]["outboundLink"]["url"], large_image="icon", large_text="Made by u/IOnlyPlayAsDrif")
    except:
      print("Failed to connect to Discord, restart the program or try again later to get Rich Presence!")
    print("")
    print("Server Link: rtmp://ingest.redd.it/inbound/")
    print("Your Stream Key: " + response["data"]["streamer_key"])
    print("DON'T share your Stream Key with anyone.")
    print("You can put these into your OBS Settings by going to the Stream section of the settings and switching Service to Custom...")
    print("YOU ARE LIVE: " + response["data"]["post"]["outboundLink"]["url"])
    print("\nThis program will close in about an hour.\nIf you close this application, Snookey2 will disconnect from Discord.\nSo if you want to keep Discord Rich Presence, just minimize this window.\nThanks for understanding!\n")
    time.sleep(180)
    RPC.update(state="Streaming on r/" + subset + " on RPAN!", details=response["data"]["post"]["outboundLink"]["url"], large_image="icon", large_text="Made by u/IOnlyPlayAsDrif", start=int(time.time()))
    time.sleep(3600)
    sys.exit()

  
  else:
    # Failed
    if count == 0:
      try:
        RPC.update(state="Trying to stream on RPAN...", details="Attempting to stream to r/" + subset + "...", start=int(time.time()), large_image="icon", large_text="Made by u/IOnlyPlayAsDrif")
        count += 1
      except:
        print("Failed to connect to Discord, restart the program or try again later to get Rich Presence!")
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
