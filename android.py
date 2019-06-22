from appium import webdriver
import time

desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "4200833ad39663f7",
    "app": "C:/Users/A/Desktop/app-universal-debug.apk",
    "appPackage": "ru.pauri.app",
    "appActivity": "ru.pauri.app.presentation.feature.splash.view.SplashActivity"
}
# adb shell "dumpsys window windows | grep -E 'mCurrentFocus'"


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


def tap(x, y, z):
    time.sleep(3)
    driver.tap([(x, y)], z)


def intro_test():
    time.sleep(4)
    if driver.find_element_by_xpath('''/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v4.view.ViewPager[2]/android.view.View/android.widget.TextView[1]
    '''):
        print("Первый слайд найден")
        driver.find_element_by_id("ru.pauri.app:id/tvNext").click()
        print("Первый слайд пропущен")
        time.sleep(3)
    else:
        print("Первого слайда нет")

    if driver.find_element_by_xpath('''/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v4.view.ViewPager[2]/android.view.View/android.widget.TextView[1]
    '''):
        print("Второй слайд найден")
        driver.find_element_by_id("ru.pauri.app:id/tvNext").click()
        print("Второй слайд пропущен")
        time.sleep(3)
    else:
        print("Второго слайда нет")

    if driver.find_element_by_xpath('''/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v4.view.ViewPager[2]/android.view.View/android.widget.TextView[1]
    '''):
        print("Третий слайд найден")
        driver.find_element_by_id("ru.pauri.app:id/tvNext").click()
        print("Третий слайд пропущен")
        time.sleep(3)
    else:
        print("Третьего слайда нет")


def menu_button_test():
    if driver.find_element_by_xpath(xpath_button_url[1]).click():
        print("Центральная кнопка")
        time.sleep(2)
    else:
        print("Ошибка центральной нопки")

    if driver.find_element_by_xpath(xpath_button_url[2]).click():
        print("Правая кнопка")
        time.sleep(2)
    else:
        print("Ошибка Правая нопки")

    if driver.find_element_by_xpath(xpath_button_url[0]).click():
        print("ЛЕвая кнопка")
        time.sleep(2)
    else:
        print("Ошибка ЛЕвая нопки")


xpath_button_url = [
    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
    '.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.HorizontalScrollView/android.widget'
    '.LinearLayout/android.support.v7.app.ActionBar.Tab[1]',
    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
    '.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.HorizontalScrollView/android.widget'
    '.LinearLayout/android.support.v7.app.ActionBar.Tab[2]',
    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
    '.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.HorizontalScrollView/android.widget'
    '.LinearLayout/android.support.v7.app.ActionBar.Tab[3]']

intro_test()

menu_button_test()




# def menu_button_test():
#     if driver.find_element_by_id("ru.pauri.app:id/imageContent"):
#         print("Картиночка найдена")
#         driver.find_element_by_id("").click()


# time.sleep(5)
# if driver.find_element_by_id("ru.pauri.app:id/imageContent"):
#     print("Картиночка найдена")
#     driver.find_element_by_id("ru.pauri.app:id/imageContent").click()
# else:
#     print("Ошибка")

# a = 0
# while a < 10:
#     if driver.find_element_by_link_text("Выберете тему") = True:
#     tap(340, 755, 200)
#     tap(123, 755, 200)
#     a = a + 1
#     print("Тап номер:", a)

# time.sleep(3)
# driver.tap([(420, 745)], 200)
# time.sleep(3)
# driver.tap([(420, 745)], 200)
# time.sleep(3)
# driver.tap([(420, 745)], 200)

# driver.find_element_by_id(11).click()
# driver.find_element_by_id(17).click()

# driver.tap(415, 738).perform()
# driver.tap(417, 735).perform()
# driver.tap(234, 724).perform()
# driver.tap(354, 569).perform()

print("Конец")
