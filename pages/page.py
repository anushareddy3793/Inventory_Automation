from selenium.webdriver.common.by import By

class BasePage:
    TITLEBAR = (By.ID, "android:id/action_bar_title")

class InventoryPage:
    '''
         Provides Locaters for the Inventory Home Page
    '''
    PRODUCTLOOKUP = (By.XPATH, "//android.widget.FrameLayout//android.widget.RadioGroup[1]/android.widget.TextView[1]")
    CREATEPICKLIST = (By.XPATH, "//android.widget.FrameLayout//android.widget.RadioGroup[2]/android.widget.TextView[1]")
    REPLENISHMENTTASKS = (By.XPATH, "//android.widget.FrameLayout//android.widget.RadioGroup[3]/android.widget.TextView[1]")
    ABOUT = (By.XPATH,"// android.widget.TextView[@content-desc = 'About']")

class ProudctLookUpPage:
    '''
        Provides Locaters for the Proudct Look Up Page
    '''
    EDITTEXT = (By.CLASS_NAME, "android.widget.EditText")
    GOBTN = (By.CLASS_NAME, "android.widget.Button")

class ProductInventoryPage:
    ItemsNotFOund = (By.XPATH, "//android.widget.FrameLayout//android.widget.RadioGroup[1]/android.widget.TextView[1]")
    RADIOGROUPLIST = (By.XPATH, "//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView//android.widget.RadioGroup")