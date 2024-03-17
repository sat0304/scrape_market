# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
# import undetected_chromedriver as uc
# import pickle
#
#
# def set_driver():
#
#     driver = uc.Chrome()
#     driver.delete_all_cookies()
#     driver.get("https://www.ozon.ru/category/telefony-i-smart-chasy-15501/?sorting=rating")
#     pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
#     driver.maximize_window()
#     cookies = pickle.load(open("cookies.pkl", "rb"))
#     for cookie in cookies:
#         driver.add_cookie(cookie)
#
#
# driver = set_driver()