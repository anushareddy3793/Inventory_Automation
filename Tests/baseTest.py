import unittest, sys, os, time
from appium import webdriver
from utilities.db_utils import dbutils
from pages.page import *

class baseTest(unittest.TestCase):
    def setUp(self):
        '''
        Launch The Application
        :return:
        '''
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'android-bed46ea8e786aee2'
        desired_caps['udid'] = '162445225D0021'
        desired_caps['appPackage'] = 'com.zebra.smartlens.inventory'
        desired_caps['appActivity'] = 'md53e444a8805cd24d2b0d21bfdb8c5f21f.MainActivity'
        desired_caps['autoGrantPermissions'] = 'true'
        desired_caps['autoAcceptAlerts'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)
        print "Application launched"
        print("------------------------------")
        self.dbutilsObj = dbutils()
        self.dbutilsObj.createConnection()


    def tearDown(self):
        '''
        close the Application
        :return:
        '''
        print("------------------------------")
        self.driver.quit()
        print("Application closed.")
        self.dbutilsObj.closeConnection()

    def handlePermisionsPopUp(self):
        try:
            allow_Btn = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
            if (allow_Btn.is_displayed()):
                allow_Btn.click()
        except(Exception):
            print "Permisions popUP not displayed"

    #####################################################################
    #
    #####################################################################

    def findElement(self, locator):
        '''
        finds the element using the locator
        :param locator:
        :return: WebElement
        '''
        return self.driver.find_element(*locator)

    def findElements(self, locator):
        '''
        finds the elements using the locator
        :param locator:
        :return: list of WebElement
        '''
        return self.driver.find_elements(*locator)

    def sample(self):
        print "sample code to test the configuration"
        # print '#######'
        # print self.dbutils1.executeQuery('SELECT version()')
        # print '#######'
        self.driver.find_element(*InventoryPage.PRODUCTLOOKUP).click()
        self.driver.find_element(*ProudctLookUpPage.EDITTEXT).send_keys("00047193046897")
        self.driver.find_element(*ProudctLookUpPage.GOBTN).click()
        time.sleep(5)
        itms = self.driver.find_elements(By.XPATH, "//*[@id='android:id/content']//android.widget.RadioGroup")
        print 'page items: '
        print len(itms)

