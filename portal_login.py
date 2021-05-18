import sys, os
try:
    from selenium import webdriver
except:
    print("selenium package is required, using pip to install selenium...")
    os.system("python3 -m pip install selenium")
    from selenium import webdriver

try:
    import chromedriver_binary
except:
    print("chromedriver_binary package is required, using pip to install chromedriver_binary...")
    os.system("python3 -m pip install chromedriver_binary")
    import chromedriver_binary

driver = webdriver.Chrome()
try: 
	driver.get("http://wlanauth.noc.titech.ac.jp")
except:
	sys.exit(0)

username = driver.find_element_by_name("username")
username.clear()

password = driver.find_element_by_name("password")
password.clear()

username.send_keys("your_user_name")
password.send_keys("your_password")

loginbutton = driver.find_element_by_class_name("button")
loginbutton.click()

print("Logged In.")

try:
    driver.quit()
    driver.close()
except:
    pass
