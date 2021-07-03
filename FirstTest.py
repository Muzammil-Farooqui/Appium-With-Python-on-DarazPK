from appium import webdriver

desired_cap = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "app": "C://Users//Farooqui//Downloads//APKs//AirMirror.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)