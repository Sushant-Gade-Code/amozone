from PageObjects.loginPage import LoginPage
from Utilities.Readproperties import ReadConfig

class Test_loginPage_001:
    baseUrl = ReadConfig.getUrl()
    userEmail = ReadConfig.getuserEmail()
    passWord = ReadConfig.getpassWord()

    def test_HomePageTitle(self,setup):
        self.driver=setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        act_title=self.driver.title
        exp_title='Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
        if act_title==exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Report\\"+"test_HomePageTitle.png")
            self.driver.close()
            assert False


    def test_loginPage(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.getdropsing()
        self.lp.getbtnSign()
        self.lp.setEmailuser(self.userEmail)
        self.lp.getBtnEmail()
        self.lp.setPassword(self.passWord)
        self.lp.getBtnPassword()
        act_Title=self.driver.title
        print(act_Title)
        exp_Title='Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
        if act_Title==exp_Title:
            assert True
        else:
            self.driver.save_screenshot(".\\Report\\"+"test_loginPage.png")
            assert False





