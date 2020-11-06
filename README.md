# Discord-Password-Manager
A password generator and manager, sends to a discord webhook. 

How to grab the links/tokens?
- Login to the discord account on chrome that you wish to send alerts with, it HAS to be a user account (not a bot/webhook).
- Press F12, go to network and send a message to the channel you wish to store passwords in.
- The response "messages" should pop up in networking, click it and copy the "Request URL" at the top. Put this as the link to send passwords to.
- Scroll down to "Request Headers" and copy the "Authorization" token, and place that in the .py file where it says "Your Discord Token".

Run the file, using python insertFileNameHere.py
