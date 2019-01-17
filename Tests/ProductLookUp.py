
from Tests.baseTest import baseTest
from pages.page import *
import time, unittest


class ProductLookupValidation(baseTest):
    def test_productLookup(self):
        invalidinputs = ['12', '123', '12345', '123456']
        for input in invalidinputs:
            self.findElement(InventoryPage.PRODUCTLOOKUP).click()
            self.findElement(ProudctLookUpPage.EDITTEXT).send_keys(input)
            self.findElement(ProudctLookUpPage.GOBTN).click()
            time.sleep(5)
            textElemnt = self.findElements(ProductInventoryPage.ItemsNotFOund)
            self.assertEqual(len(textElemnt), 1)
            self.assertEqual(textElemnt[0].text, 'Item not found in store.', 'The message is not properly show when an invalid product code: ' + input + ' is used')
            self.findElement(BasePage.TITLEBAR).click()
            time.sleep(5)

        validInputs = ['00490150386725', '00047193045722']
        for input in validInputs:
            self.findElement(InventoryPage.PRODUCTLOOKUP).click()
            self.findElement(ProudctLookUpPage.EDITTEXT).send_keys(input)
            self.findElement(ProudctLookUpPage.GOBTN).click()
            time.sleep(5)
            RadioGroup = self.findElements(ProductInventoryPage.RADIOGROUPLIST)
            self.assertTrue(len(RadioGroup) >= 3, 'The actual length is :' + str(len(RadioGroup)))
            ItemsCount = 0
            for x in range(2, len(RadioGroup)):
                locationText = RadioGroup[x].find_elements(By.XPATH, "//android.widget.TextView")
                self.assertEqual(len(locationText), 2)
                print locationText[0].text + '\t\t' + locationText[1].text
                ItemsCount = ItemsCount + int(locationText[1].text)
            print 'The total items count for the product with id:' + input + ' is: ' + str(ItemsCount)

            query = 'SELECT * FROM "BAR"."ItemInventory" WHERE "Site"=\'X9774ed35-1af8-446b-a339-7ca8ef80cd20\' AND  "GTIN"=\'' + input + '\' AND ("EventType"<>\'MISSING\' AND "EventType"<>\'GHOST\' AND "EventType"<>\'DEPARTURE\');'
            result = self.dbutilsObj.executeQuery(query)
            print result
            print 'Sql query result: ' + str(len(result))
            self.assertTrue(len(result), ItemsCount)
            #print textElemnt[0].text
            self.findElement(BasePage.TITLEBAR).click()
            time.sleep(5)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ProductLookupValidation)
    unittest.TextTestRunner(verbosity=2).run(suite)
