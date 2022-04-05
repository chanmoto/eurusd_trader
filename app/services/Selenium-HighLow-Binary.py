from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
import chromedriver_binary
from selenium.webdriver.common.by import By
    
BC_ADRESS = "Mail or Wallet"
PASSWORD = "PASSWORD"
 
def l(str):
    print("%s : %s"%(datetime.now().strftime("%Y/%m/%d %H:%M:%S"),str), flush=True)
 
def s(t = 5):
    import time
    time.sleep(t)
 
def x(str = ""):
    import traceback
    traceback.print_exc()
    if str != "":
        l(str)
 
def start():
    # ドライバー指定でChromeブラウザを開く 
    chrome_service = fs.Service(executable_path='./chromedriver') 
    b = webdriver.Chrome(service=chrome_service)
    b.get('https://app.highlow.com/quick-demo?source=header-quick-demo-cta')
    s()
    return b
 
def login():
    b.find_element_by_css_selector('.login_menu_button a').click()
    i = b.find_element_by_id('login_form_btc_address')
    i.send_keys(BC_ADRESS)
    i = b.find_element_by_id('login_form_password')
    i.send_keys(PASSWORD)
    b.find_element_by_id('login_button').click()
    s()
    
def purchase(driver, high_low_xxx, entry_price):
    if high_low_xxx == "high":
        b.find_element(by=By.XPATH,value = "//div[text()='High']").click()
        s(0.5)
        b.find_element(by=By.XPATH,value = "//div[text()='今すぐ購入']").click()
        s(0.5)
        b.find_element(by=By.XPATH,value = "//div[text()='High']").click()
        
    elif high_low_xxx == "low":
        b.find_element(by=By.XPATH,value = "//div[text()='Low']").click()
        s(0.5)
        b.find_element(by=By.XPATH,value = "//div[text()='今すぐ購入']").click()
        s(0.5)
        b.find_element(by=By.XPATH,value = "//div[text()='Low']").click()

@app.get("/order/")
async def order(signal : float ,db:Session = Depends(get_db)):
    
        if signal>4 and signal<100:
            s(0.5)
            purchase(b,"high",1000)
            s(0.5)
            
        elif signal>0.001 and signal<0.25:
            s(0.5)
            purchase(b,"low",1000)
            s(0.5)
    
        return {"ordered":str(signal)}