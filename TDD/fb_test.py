import os, tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.binary_location = "/usr/bin/google-chrome-stable"

options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-zygote")
options.add_argument("--no-zygote")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--incognito")
options.add_argument("--no-first-run")
options.add_argument("--window-size=1920,1080")

# Block WSLg from intercepting
os.environ.pop("DISPLAY", None)
os.environ.pop("WAYLAND_DISPLAY", None)
os.environ["DBUS_SESSION_BUS_ADDRESS"] = "disabled:"

tmpdir = tempfile.mkdtemp()
options.add_argument(f"--user-data-dir={tmpdir}")

service = Service(executable_path="/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.example.com/")
print("✅ Title:", driver.title)
driver.quit()
print("✅ Driver quit cleanly.")