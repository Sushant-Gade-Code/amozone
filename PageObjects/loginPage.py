from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class LoginPage:
    btn_mosuAction_By_XPATH='//span[@class="nav-line-2 "]//span'
    btn_sign_in_By_Link_text="Sign in"
    inpt_Email_by_Xpath='//input[@id="ap_email"]'
    btn_Email_by_ID ='continue'
    inpt_passW_by_ID='ap_password'
    btn_passW_by_ID='signInSubmit'


    def __init__(self,setup):
        self.driver=setup

    def getdropsing(self):
        ele=self.driver.find_element(By.XPATH,self.btn_mosuAction_By_XPATH)
        self.act=ActionChains(self.driver)
        self.act.move_to_element(ele).perform()

    def getbtnSign(self):
        ele1 = self.driver.find_element(By.LINK_TEXT,self.btn_sign_in_By_Link_text)
        self.act.move_to_element(ele1).double_click(ele1).perform()
        # ele1=self.driver.find_element(By.ID,self.btn_sign_in_By_ID)
        # self.act.move_to_element(ele1).double_click(ele1).perform()

    def setEmailuser(self,email):
        self.driver.find_element(By.XPATH,self.inpt_Email_by_Xpath).clear()
        self.driver.find_element(By.XPATH,self.inpt_Email_by_Xpath).send_keys(email)

    def getBtnEmail(self):
        self.driver.find_element(By.ID,self.btn_Email_by_ID).click()

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.inpt_passW_by_ID).clear()
        self.driver.find_element(By.ID,self.inpt_passW_by_ID).send_keys(password)

    def getBtnPassword(self):
        self.driver.find_element(By.ID,self.btn_passW_by_ID).click()













