from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from dotenv import load_dotenv

load_dotenv()

def setting_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("do-not-track")
    chrome_options.add_argument("disable-infobars") 


    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-popup-blocking")  
    chrome_options.add_argument("--disable-extensions")  
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--ignore-certificate-errors")  
    driver = webdriver.Chrome(options = chrome_options)

    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.get("https://www.google.com")
    driver.maximize_window()
    time.sleep(2)

    return driver

class YoutubeBot:

    def __init__(self, headless=True):
        self.driver = setting_driver()
    
    def get_transcript(self, url):
        self.driver.get(url)
        time.sleep(4)
        self.driver.execute_script(f"window.scrollTo({500}, {100});")
        more_button = self.driver.find_elements(By.XPATH, "//tp-yt-paper-button[@id='expand']")[0]
        time.sleep(2)
        more_button.click()
        time.sleep(2)
        show_transcript_button = self.driver.find_elements(By.XPATH, "//button[@aria-label='Show transcript'][1]")[0]
        show_transcript_button.click()
        time.sleep(2)
        title_info = self.driver.find_elements(By.XPATH, "//h1//*[@title]")[-1].text
        transcripts = self.driver.find_elements(By.XPATH, "//div[starts-with(@class, 'segment style') and contains(@aria-label, 'minute')]")
        content = '\n'.join([subtitle.get_attribute('aria-label') for subtitle in transcripts])
        return title_info, content


    def quit(self):
        self.driver.quit()

