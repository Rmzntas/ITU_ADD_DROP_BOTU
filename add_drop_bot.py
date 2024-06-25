import time, os

try:
    import webdriver_manager
except:
    os.system("pip install webdriver-manager")

try:
    import selenium
except:
    os.system("pip install selenium")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager

CRNS = ["30149", "30159"] #Almak istediğiniz CRN'leri yazın.


##### itü mail ve şifresi #####
mail = "abc@itu.edu.tr"
password = "abcdef"


service = Service(EdgeChromiumDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(service=service, options=options)
driver.implicitly_wait(10) # max bekleme süresi


##### kepler ders kayıt sayfasına gidiş
driver.get("https://kepler-beta.itu.edu.tr")

driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$tbUserName").send_keys(mail)
driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$tbPassword").send_keys(password)

login_btn = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btnLogin").click()

#driver.find_element(By.CLASS_NAME, "stretched-link").click()    ## eğer yatay geçiş yapmadıysanız bu satırı silin.

driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[1]/div[2]/div[1]/ul/li[5]/a").click()
time.sleep(0.4)
driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[1]/div[2]/div[4]/ul/li/div/ul/li[2]/a").click()


counter = 1
stack = 1

while True:

    if counter < 3001 :

        for i, crn in enumerate(CRNS):
            driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[2]/div/div/div[3]/div/form/div[1]/div/div[{}]/div/input".format(i+1)).send_keys(crn)

        print("Attempt: {} -- {}".format(stack,counter))

        driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[2]/div/div/div[3]/div/form/button").click()
        driver.find_element(By.XPATH, "//*[@id='modals-container']/div/div[2]/div/div[3]/button[2]").click()
        counter += 1
        time.sleep(0.9)

    else:
        driver.quit()
        driver = webdriver.Edge(service=service, options=options)
        driver.get("https://kepler-beta.itu.edu.tr")
        driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$tbUserName").send_keys(mail)
        driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$tbPassword").send_keys(password)
        login_btn = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btnLogin").click()
        #driver.find_element(By.CLASS_NAME, "stretched-link").click()    ## eğer yatay geçiş yapmadıysanız bu satırı silin.
        driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[1]/div[2]/div[1]/ul/li[5]/a").click()
        time.sleep(0.4)
        driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[1]/div[2]/div[4]/ul/li/div/ul/li[2]/a").click()
        time.sleep(0.1)
        counter = 1
        stack += 1




