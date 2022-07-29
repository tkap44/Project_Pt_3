from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/tkaplan/Code/Python/Automation/chromedriver")

driver.get("http://127.0.0.1:5001/users/2")

try:
    user = driver.find_element('id', 'user')
    user = user.text
    print("Web element exists!")
    print(user)

except:
    print("No user by that ID")

driver.close()

