import pymysql
import requests
from selenium import webdriver

user_id = 1
user_id = str(user_id)


conn = pymysql.connect(host='remotemysql.com', port=3306, user='eCiPNxZhD1', password='LsyRZQfzqo', db='eCiPNxZhD1')
cursor = conn.cursor()


res = requests.post('http://127.0.0.1:5001/users/'+user_id, json={"name": "test"})


if res.ok:    # res.ok checks if the server response is okay, only then will the next thing happen. error 500 is not okay!!!
    print("POST request response:", res.json())
    res2 = requests.get('http://127.0.0.1:5001/users/'+user_id)
    if res2.ok:
        cursor.execute("SELECT * FROM eCiPNxZhD1.users WHERE id = %s", user_id)
        data = cursor.fetchall()
        print(data)
        driver = webdriver.Chrome(executable_path="/Users/tkaplan/Code/Python/Automation/chromedriver")
        driver.get("http://127.0.0.1:5001/users/" + user_id)

        try:
            user = driver.find_element('id', 'user')
            user = user.text
            print("Web element exists!")
            print(user)
            driver.close()

        except:
            print("No user by that ID")
            driver.close()

else:
    print(res.json())


res = requests.delete('http://127.0.0.1:5001/users/'+user_id)
if res.ok:
    print(res.json())
else:
    print(res.json())
