from selenium import webdriver

def open_browser():
    print("Chrome open ho raha hai...")
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    print("Page Title:", driver.title)
    
    # 5 seconds hold taaki aap dekh sakein
    import time
    time.sleep(5)
    
    driver.quit()

open_browser()