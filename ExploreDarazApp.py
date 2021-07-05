from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

#------------------------------------------------------------ Server Configuration -------------------------------------------------------------------------
desired_cap = {
    "platformName": "Android",
    "deviceName": "Android",
    "app": "C://Users//Farooqui//Downloads//APKs//Daraz - Online Shopping App.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)


def verticalScrollScreen(pressX, pressY, moveX, moveY):
    touch = TouchAction(driver)
    touch.press(x=pressX, y= pressY).move_to(x= moveX, y= moveY).release().perform()

def horizontalScrollScreen(pressX, pressY, moveX, moveY):
    touch = TouchAction(driver)
    touch.press(x=pressX, y=pressY).move_to(x=moveX, y=moveY).release().perform()
    touch.press(x=510, y=420).move_to(x=245, y=395).release().perform()

def resetPassword(email):
    driver.find_element_by_id("com.daraz.android:id/iv_clear_text").click()
    driver.find_element_by_id("com.daraz.android:id/et_input_text").send_keys("test@testmail.com")
    driver.find_element_by_id("com.daraz.android:id/btn_next").click()

def signIn(email, password):
    time.sleep(2)
    # Enter email
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText").send_keys(email)
    #enter password
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText").click()
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText").send_keys(password)
    time.sleep(1)
    #show password
    driver.find_element_by_id("com.daraz.android:id/cb_input_type").click()
    time.sleep(1)
    # hide password
    driver.find_element_by_id("com.daraz.android:id/cb_input_type").click()
    time.sleep(1)
    #clik on login button
    driver.find_element_by_id("com.daraz.android:id/btn_next").click()
    time.sleep(2)

    if (driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout").is_displayed() == True):
        driver.find_element_by_id("com.daraz.android:id/tv_agree").click()
        resetPassword("est1@testmail.com")

def searchProducts(productName):
    time.sleep(1)
    driver.find_element_by_id("com.daraz.android:id/laz_homepage_search_view").click()
    time.sleep(1)
    driver.find_element_by_id("com.daraz.android:id/search_input_box").send_keys(productName)
    driver.find_element_by_id("com.daraz.android:id/search_button").click()
    time.sleep(5)

def productsDetails():

    # accept alert popup
    try:
        driver.find_element_by_id("com.daraz.android:id/got_it").click()
    except:
        pass

    # side products pictures
    try:
        for i in range(1, 4):
            horizontalScrollScreen(510, 420, 245, 395)
    except:
        pass
    verticalScrollScreen(320, 920, 310, 560)
    verticalScrollScreen(320, 920, 310, 560)

    # click on variation to open variation modal
    try:
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.view.ViewGroup/android.widget.ImageView").click()
        time.sleep(2)
        # try to change capacity
        try:
            driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.view.ViewGroup/android.widget.TextView[2]").click()
        except:
            pass

        # increase quantity
        for i in range(1, 4):
            driver.find_element_by_id("com.daraz.android:id/add").click()
        time.sleep(1)

        # decrease quantity
        for i in range(1, 2):
            driver.find_element_by_id("com.daraz.android:id/remove").click()
        time.sleep(1)

        # close modal
        driver.find_element_by_id("com.daraz.android:id/button_close").click()
    except:
        pass

    # click on add to cart show modal
    driver.find_element_by_id("com.daraz.android:id/main_action_container").click()
    time.sleep(2)

    #clickon add to cart
    driver.find_element_by_id("com.daraz.android:id/main_action").click()
    time.sleep(2)

    # click on sign in
    driver.find_element_by_id("com.daraz.android:id/tv_signin").click()

    signIn("test@testmail.com", "Trees123")


############################################################## Main ################################################################3
if __name__ == '__main__':
    time.sleep(2)
    # select country
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.TextView").click()
    time.sleep(2)
    driver.find_element_by_id("com.daraz.android:id/intro_skip_btn").click()
    time.sleep(5)
    # scroll down main sceen
    for i in range(1, 3):
        verticalScrollScreen(370, 950, 360, 410)

    # call search product function
    searchProducts("iphone")

    # scroll down main sceen
    verticalScrollScreen(354, 934, 361, 391)
    # click on product
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.LinearLayout").click()
    time.sleep(2)
    productsDetails()