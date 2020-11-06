import requests
import random
password_length = 16
password_length2 = 32
possible_characters = "abcDefGhijKlmnopqrstuvVxyZ1234567890"

random_character_list = [random.choice(possible_characters) for i in range(password_length)]
random_character_list2 = [random.choice(possible_characters) for i in range(password_length2)]
random_password = "".join(random_character_list)
random_password2 = "".join(random_character_list2)

print(random_password)
print(random_password2)

service = input("Service: ")
pass_choice = input("1 or 2: ")

#Example of a channel link: https://discord.com/api/v8/channels/723456789011124521/messages (Tutorial on github)

if pass_choice == "1":
	requests.post('Channel Link', headers={
				    'Authorization': 'Your Discord Token (Your user account, not a bot/webhook)'
				}, json={
					"content": "",
				    "embed":
				    {
				        "title": "Password Manager",
				        "color": 2909402,
				        "fields": [
				        {
				            "name": "Service",
				            "value": service,
				            "inline": True
				            },
				            {
				            "name": "Password",
				            "value": random_password,
				            "inline": True
				        }],
				        "thumbnail":
				        {
				            "url": "https://static.thenounproject.com/png/9362-200.png"
				        }
				    }
				})

elif pass_choice == "2":
	requests.post('Channel Link', headers={
				    'Authorization': 'Your Discord Token (Your user account, not a bot/webhook)'
				}, json={
					"content": "",
				    "embed":
				    {
				        "title": "Password Manager",
				        "color": 2909402,
				        "fields": [
				        {
				            "name": "Service",
				            "value": service,
				            "inline": True
				            },
				            {
				            "name": "Password",
				            "value": random_password2,
				            "inline": True
				        }],
				        "thumbnail":
				        {
				            "url": "https://static.thenounproject.com/png/9362-200.png"
				        }
				    }
				})