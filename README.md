
### IMPORTANT:  
### This application is not a virus and will not gain access or harm your computer, Reddit account, or anything else. Snookey2 is completely open source so you can check the .py file for all the code and see that there's nothing harmful. None of this data is stored, because I don't even know how to do that. I wouldn't even do it anyways if I knew how cause that would be really evil and ruin my reputation forever... Anyways, thank you for understanding, and have fun streaming! 

Hi!

This application might bring up Windows SmartScreen and I have no way to avoid that, like the notice says above there's nothing bad in this program. I use this program myself and many other Redditors do without issues.

This application was made by u/Spikeedoo and was updated by u/IOnlyPlayAsDrif!

App icon was made by Reddit.

[Join the Unofficial RPAN Discord Server for Snookey2 Support/Reporting Bugs/Suggestions/and just talking to other streamers/viewers!](https://discord.gg/3GcApfT)

Thank you for downloading Snookey!

Added:
- Discord Rich Presence
- More text in general
- More descriptive and better looking text
- Auto closes when getting a stream spot is successful after 1 minute
- Retries every 2 seconds if requesting a stream spot fails with error message
- Made the icon of the app the RPAN logo!

(Check the Releases tab of this repo to see the full list of changes.)

[Original Snookey by u/Spikeedoo is here.](https://github.com/Spikeedoo/SnooKey)   

[Video Tutorial on how to download and use Snookey2 is here.](https://youtu.be/Oi54fiFOoCI)

The text and stuff below was originally made by u/Spikeedoo (with some modifications from me):

# SnooKey2
Some reddit users figured out a way to stream to RPAN (Reddit's livestreaming platform) from desktop streaming software 
(like OBS).  Project SnooKey is my attempt at making this possibilty more accessible to RPAN users.

## START HERE
### Method 1 (Windows only)
If you have a Windows machine, you can run SnooKey without installing python by simply going into the Releases tab and downloading the latest version, and running Snookey.

### Method 2 (All platforms)
For this to work you will need Python3 installed to your system.      
*IF YOUR TERMINAL THINKS 'PYTHON' IS NOT A COMMAND, PYTHON HAS MOST LIKELY NOT BEEN ADDED TO YOUR PATH*     
[Install Python for Windows](https://realpython.com/installing-python/#windows)   
[Install Python for Linux](https://realpython.com/installing-python/#linux)   
[Install Python for OS X](https://realpython.com/installing-python/#macos-mac-os-x)   
Make sure the dependent Python modules are installed for the script to work:
```
pip install requests pytz pypresence
```
## Installation
Just click on the Releases tab and download the latest version.

## Using SnooKey2
Once you have SnooKey downloaded, it is time to run the script.     
(**If you have a Windows computer (Method #1) simply run ```snookey2_v(version number).exe```**)
```
python snookey2.py
```
This will open a link in your browser allowing you to get an access code from Reddit    
**NOTE:** The Reddit app you are allowing access is not mine.  It is the client_id for the mobile, in this case android, Reddit app.    
One way you can confirm that I am not BS'ing you is by looking at [your apps](https://www.reddit.com/prefs/apps/) after allowing access.
A third party application would normally appear here in the 'authorized applications' section with the developer's username.  This Reddit-built
application does not follow the same rules.   

Copy the access token from the localhost callback url and reply to the prompt in your terminal:
```
Please enter your access token: <enter access token here>
```
Follow the next two prompts by passing the subreddit you want to broadcast to and your stream's title:
```
Subreddit you want to broadcast to: <i.e. distantsocializing>
Stream title: <i.e. RPAN and chill!>
```
If all goes well you will be given your streamer key and the rpan link people will visit your stream from.

## How to use your streamer key
Step 1: Open up your desktop streaming software (in my example, OBS)      
Step 2: Navigate to your stream settings (Settings > Stream in OBS)    
Step 3: Make sure your Service is set to 'Custom' and fill in the following settings:
- Server: rtmp://ingest.redd.it/inbound/
- Stream Key: (your stream key)

Now hit 'Apply' and 'OK'

Hit 'Start Streaming' and watch the magic happen!

Disclaimer: I am not liable for your stupidity.  Please be responsible and follow the [Rules](https://www.redditinc.com/policies/broadcasting-content-policy).  Cheers.  
