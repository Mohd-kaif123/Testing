from driver_helper import get_driver
import time

driver = get_driver()
driver.get("https://www.pw.live/")
time.sleep(5)

print("Title:", driver.title)
assert "Physics wallah" in driver.title  # small 'w' — exactly jaisa title hai
print("✅ Title Tested Successfully!")

driver.quit()