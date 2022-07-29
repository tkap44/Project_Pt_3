import pymysql
import requests

conn = pymysql.connect(host='remotemysql.com', port=3306, user='eCiPNxZhD1', password='LsyRZQfzqo', db='eCiPNxZhD1')
cursor = conn.cursor()

user_id = 2
user_id = str(user_id)

res = requests.post('http://127.0.0.1:5001/users/'+user_id, json={"name": "test"})
if res.ok:    # res.ok checks if the server response is okay, only then will the next thing happen. error 500 is not okay!!!
    print("POST request response:", res.json())
    res2 = requests.get('http://127.0.0.1:5001/users/'+user_id)
    if res2.ok:
        data = res2.json()
        print("GET request response:", data)
        name = data.get('user_name')
        if name == 'test':
            cursor.execute("SELECT * FROM eCiPNxZhD1.users WHERE id = %s", user_id)
            data = cursor.fetchall()
            print(data)

else:
    print(res.json())


res = requests.delete('http://127.0.0.1:5001/users/'+user_id)
if res.ok:
    print(res.json())
else:
    print(res.json())
