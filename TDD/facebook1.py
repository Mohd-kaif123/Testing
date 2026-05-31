from driver_helper import get_driver
from selenium.webdriver.common.by import By          # ← YEH RAKHNI THI

driver = get_driver()
driver.get("https://facebook.com/")

driver.maximize_window()

email= driver.find_element(By.NAME,"email")
#assert email.is_displayed()
#print("Email Field Required")
email.send_keys("test@gmail.com")

password= driver.find_element(By.NAME,"pass")
#assert password.is_displayed()
#print("Password Field Required")
password.send_keys("password@1123")

button= driver.find_element(By.XPATH,'//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div')
button.click()

input("Press Enter to close the browser...")
#driver.quit()