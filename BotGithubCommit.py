import requests
import time
access_token = "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"
url = f"https://api.github.com/repos/WBBR05/GitBot/commits"
headers = {
    "Authorization": f"token {access_token}"
}
print(url)
print(headers)
memory=""
while True:
    response = requests.get(url, headers=headers)
    #print(response)
    if response.status_code == 200:
        commits = response.json()
        com2 = commits[0]
        #print(com2)
        if memory == "":
            memory = com2
            print("Initalization")
        elif memory != com2:
            print("New commit!!")
            memory = com2
            requests.post(
                'https://api.telegram.org/bot6490343462:AAGLtHVEHDhdXV4QCs_IhgZqAa0qNP76BOY/sendMessage?chat_id=-4069828355&text=New commit on Github ')

        else:
            print("Nothing changed")
    
    else:
        print(f"Error connect with Github: {response.status_code}")
    time.sleep(5)
