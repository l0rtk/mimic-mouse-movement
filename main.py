from humancursor import SystemCursor
from humancursor import WebCursor
from selenium import webdriver
import time

# use systemcursor for os stuff
# use webscursor for web stuff

driver = webdriver.Chrome()

cursor = SystemCursor()
web_cursor = WebCursor(driver)

driver.maximize_window()
driver.get("https://www.google.com")

time.sleep(2)


cursor.move_to([450, 600]) 
time.sleep(1)

cursor.move_to([950, 100])
time.sleep(1)




