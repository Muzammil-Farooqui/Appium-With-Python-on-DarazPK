import base64
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

#------------------------------------------------------------ Server Configuration -------------------------------------------------------------------------
desired_cap = {
    "platformName": "Android",
    "deviceName": "Android",
    "app": "C://Users//Farooqui//Downloads//APKs//Daraz - Online Shopping App.apk",
    "appPackage": "com.daraz.android",
    "appWaitActivity": "com.lazada.intro.IntroActivity"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)


def verticalScrollScreen(pressX, pressY, moveX, moveY):
    touch = TouchAction(driver)
    touch.press(x=pressX, y= pressY).move_to(x= moveX, y= moveY).release().perform()

def horizontalScrollScreen(pressX, pressY, moveX, moveY):
    touch = TouchAction(driver)
    touch.press(x=pressX, y=pressY).move_to(x=moveX, y=moveY).release().perform()
    touch.press(x=510, y=420).move_to(x=245, y=395).release().perform()

def startRecording():
    driver.start_recording_screen()

def stopRecording():
    videoRawdata = driver.stop_recording_screen()
    videoName = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")

    filePath = os.path.join("E:/XordWork/Appium/VideoRecordings/", videoName + ".mp4")

    with open(filePath,"wb") as vd:
        vd.write(base64.b64decode(videoRawdata))

def takeScreenShot():
    ts = time.strftime("%Y_%m_%d_%H%M%S")
    activityName = driver.current_activity
    fileName = activityName + ts
    driver.save_screenshot("E:/XordWork/Appium/Screenshots/" + fileName + ".png")

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
        resetPassword("test1@testmail.com")

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
    for i in range(1, 3):
        horizontalScrollScreen(674, 433, 29, 427)

    # Scroll Down
    verticalScrollScreen(320, 920, 310, 560)
    verticalScrollScreen(320, 920, 310, 560)

    driver.find_element_by_id("com.daraz.android:id/main_action_container").click()     # click on add to cart to open cart modal

    try:
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.view.ViewGroup/android.widget.ImageView").click()
        time.sleep(2)
        # try to change capacity
        try:
            driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.view.ViewGroup/android.widget.TextView[2]").click()
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

    time.sleep(1)
    driver.find_element_by_id("com.daraz.android:id/main_action_container").click()
    time.sleep(1)

    if (driver.find_element_by_id("com.daraz.android:id/ll_welcome_login").is_displayed() == True):
        driver.find_element_by_id("com.daraz.android:id/tv_signin").click()  # click on login with password
        signIn("test@testmail.com", "Trees123")  # call signin function


    # ######## Specification Tab ##########
    # # check specificaion tab exist or not
    # if(driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.view.ViewGroup/android.widget.ImageView").is_displayed() == True):
    #     # click on variation to open variation modal
    #     try:
    #         driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.view.ViewGroup/android.widget.ImageView").click()
    #         time.sleep(2)
    #         # try to change capacity
    #         try:
    #             driver.find_element_by_xpath(
    #                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.view.ViewGroup/android.widget.TextView[2]").click()
    #         except:
    #             pass
    #
    #         # increase quantity
    #         for i in range(1, 4):
    #             driver.find_element_by_id("com.daraz.android:id/add").click()
    #         time.sleep(1)
    #
    #         # decrease quantity
    #         for i in range(1, 2):
    #             driver.find_element_by_id("com.daraz.android:id/remove").click()
    #         time.sleep(1)
    #
    #         # close modal
    #         driver.find_element_by_id("com.daraz.android:id/button_close").click()
    #     except:
    #         pass

        # click on add to cart show modal
        # driver.find_element_by_id("com.daraz.android:id/main_action_container").click()
        # time.sleep(2)

    #clickon add to cart
    # driver.find_element_by_id("com.daraz.android:id/main_action").click()
    # time.sleep(2)
    #
    # if (driver.find_element_by_id("com.daraz.android:id/ll_welcome_login").is_displayed() == True):
    #     driver.find_element_by_id("com.daraz.android:id/tv_signin").click()  # click on login with password
    #     signIn("test@testmail.com", "Trees123")  # call signin function
    # # click on sign in
    # driver.find_element_by_id("com.daraz.android:id/tv_signin").click()
    #
    # # call Sign in function
    # signIn("test@testmail.com", "Trees123")


############################################################## Main ################################################################3
if __name__ == '__main__':
    time.sleep(2)    # wait

    startRecording()    # Screen Recording Started

    #start screen sliders
    for i in range(1, 3):
        horizontalScrollScreen(650, 700, 100, 700)

    driver.find_element_by_id("com.daraz.android:id/intro_skip_btn").click()    # click on skip button
    time.sleep(3)   # wait for page loading
    verticalScrollScreen(350, 300, 350, 1000)   # Refresh screen
    time.sleep(3) # wait for page loading
    for i in range(1, 3):   # scroll down main screen
        verticalScrollScreen(350, 1000, 350, 300)
        time.sleep(2)

    # click on messages tab
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.FrameLayout[2]/android.widget.LinearLayout").click()
    time.sleep(1)
    driver.back()

    # click on cart tab
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.FrameLayout[3]").click()
    time.sleep(1)
    driver.back()

    #click on account tab
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.FrameLayout[4]").click()
    time.sleep(1)

    #click on setting button
    driver.find_element_by_id("com.daraz.android:id/tv_settings").click()
    time.sleep(1)
    takeScreenShot()    # call screenshot function

    #click on messages
    driver.find_element_by_id("com.daraz.android:id/setting_notification_container").click()
    time.sleep(1)

    #click on check box
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[4]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.CheckBox").click()
    time.sleep(1)
    driver.back()

    #click on back button
    time.sleep(1)
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton").click()
    time.sleep(1)

    # Click on country tab
    driver.find_element_by_id("com.daraz.android:id/changeCountryHeader").click()
    time.sleep(1)

    #click on first country
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView").click()
    time.sleep(1)
    driver.find_element_by_id("android:id/button2").click()     # click on cancel button of alert
    time.sleep(1)
    driver.back()
    time.sleep(1)
    driver.back()
    time.sleep(1)
    # driver.find_element_by_id("com.daraz.android:id/txt_login_signup").click()    # click on login/signup button
    # if (driver.find_element_by_id("com.daraz.android:id/ll_welcome_login").is_displayed() == True):
    #     driver.find_element_by_id("com.daraz.android:id/tv_signin").click()  # click on login with password
    #     signIn("test@testmail.com", "Trees123")  # call signin function
    # time.sleep(1)

    #click on homme tab
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.FrameLayout[1]").click()
    time.sleep(2)

    verticalScrollScreen(350, 1000, 350, 300)
    time.sleep(2)
    verticalScrollScreen(350, 1000, 350, 300)
    time.sleep(2)

    searchProducts("iphone")        # call search product function

    # click on Daraz mall tab
    # driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[2]/android.widget.FrameLayout/android.widget.LinearLayout").click()

    # scroll down main screen
    time.sleep(1)
    verticalScrollScreen(350, 1109, 350, 455)
    time.sleep(2)
    # click on product
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.LinearLayout").click()
    time.sleep(2)

    # Call products Details function
    productsDetails()


    stopRecording()