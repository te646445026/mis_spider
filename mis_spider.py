from selenium import webdriver
import time

username = 'jmgjb'
password = 'abc12345'
url = 'http://10.0.2.2:8080'#内网
#url = 'http://mis.gdsei.org.cn/' #外网

browser = webdriver.Ie()

browser.get(url)

time.sleep(5)

#找到用户框，输入账号
inputName = browser.find_element_by_css_selector('input#j_username')
inputName.send_keys(username)

#找到密码框，输入密码
inputPassword = browser.find_element_by_css_selector('input#j_password')
inputPassword.send_keys(password)

#找到登录按钮，点击
button  = browser.find_element_by_css_selector('a#loginButton')
button.click()

time.sleep(5)
