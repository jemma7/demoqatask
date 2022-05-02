
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

PATH = 'chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("https://demoqa.com/text-box")
sleep(3)
driver.maximize_window()

#print(driver.title)

expected_page_title = "ToolsQA"
#assert driver.title == expected_page_title

if expected_page_title == driver.title:
    print(f"{expected_page_title} is successfully opened.")
else:
    print(f"{expected_page_title} is not opened.")


driver.find_element_by_id("userName").send_keys("Tom Brown")
driver.find_element_by_id("userEmail").send_keys("brown@tttmail.com")
driver.find_element_by_id("currentAddress").send_keys("Madrid")
driver.find_element_by_id("permanentAddress").send_keys("London")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element_by_id("submit").click()


sleep(5)

#output = driver.find_element_by_xpath('//*[@id="output"]')
#output=driver.find_element_by_id("output")
def compare(self):
    self.name=driver.find_element_by_id("name").getText()
    self.email=driver.find_element_by_id("email").getText()
    self.current_address=driver.find_element_by_id("currentAddress").getText()
    self.permanent_address=driver.find_element_by_id("permanentAddress").getText()
    self.submited_data = "Name:Tom Brown,Email:brown@tttmail.com,Current Address :Madrid,Permananet Address :London"
    self.driver.assertEqual("Tom Brown","brown@tttmail.com","Madrid","London","Name:Tom Brown,Email:brown@tttmail.com,Current Address :Madrid,Permananet Address :London")

compare()
print("done")

# output = driver.find_element_by_id("output")
# submitedText = output.text
# receivedText = "Name:Tom\nEmail:brown@tttmail.com\nCurrent Address :Madrid\nPermananet Address :London"

# if receivedText == submitedText:
#     print('the data submited successfully')
# else:
#     print('the data is not submited')


sleep(5)
driver.close()
driver.quit()
