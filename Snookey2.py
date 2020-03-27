import sys
import time
import requests
import webbrowser

print("Welcome to Snookey2 v1.2 made by u/Spikeedoo and modified by u/IOnlyPlayAsDrif!\n")
print("Contact me or Spikeedoo for help! My Discord is Drift#5339.\n")
print("Remember to follow the Reddit TOS and Broadcasting Guidelines here: https://www.redditinc.com/policies/broadcasting-content-policy\n")
print("The app icon is the official logo to RPAN so credit to Reddit for the logo.\n")

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
    if options == "reopen":
      print("")
      webbrowser.open(request_url, new=0)
      continue
  except:
    print("Unexpected error occured, closing program in 10 seconds...")
    time.sleep(10)
    sys.exit()
  else:
    break
full_token = "Bearer " + user_token
subreddit = input("Subreddit you want to broadcast to:\n")
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
    except:
      print("Error message: Invalid subreddit/access code/broadcast title.\nPlease restart the program and try again.\nThis program will automatically close in 10 seconds.")
      time.sleep(10)
      sys.exit()
    time.sleep(2)

# Fix to prevent windows .exe from closing on completion
#print("")
#aainput("Press enter to exit...")
