from appium import webdriver
import time

#------------------------------------------------------------ Server Configuration -------------------------------------------------------------------------
desired_cap = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "app": "C://Users//Farooqui//Downloads//APKs//AirMirror.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)


#--------------------------------------------------------------- Sign Function -----------------------------------------------------------------------------
def signIn(email, password):
    driver.implicitly_wait(30)
    # email input
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.EditText").send_keys(email)
    # password input
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.EditText").send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.EditText").click()
    # show password
    driver.find_element_by_id("com.sand.airmirror:id/hide").click()
    time.sleep(2)
    # hide password
    driver.find_element_by_id("com.sand.airmirror:id/hide").click()
    # click on login button
    driver.find_element_by_id("com.sand.airmirror:id/btnLogin").click()
    time.sleep(2)
    try:
        driver.find_element_by_id("com.sand.airmirror:id/tvOK").click()
    except:
        pass
    time.sleep(2)

def signUp(email, password, reEnterPassword, nickName):
    # input Email
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.EditText").send_keys(email)
    # input Password
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.EditText").send_keys(password)
    # input Password again
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.EditText").send_keys(reEnterPassword)
    # input Nickname
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.EditText").send_keys(nickName)
    time.sleep(2)
    # click on next button
    driver.find_element_by_id("com.sand.airmirror:id/btnRegister").click()
    time.sleep(2)


if __name__ == '__main__':
    time.sleep(2)
    driver.find_element_by_id("com.sand.airmirror:id/tvLogin").click()
    time.sleep(2)
    signIn("test@testmail.com", "Trees123")

    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView").click()
    signUp("abc@testmail.com", "Trees123", "Trees123", "Mr Tester")
    time.sleep(2)