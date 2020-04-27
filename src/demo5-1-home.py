import selenium
from selenium import webdriver
import  time
from urllib.request import urlopen
driver = webdriver.Chrome()     # 打开 Chrome 浏览器

# 将刚刚复制的帖在这
# driver.get("https://morvanzhou.github.io/")
# driver.find_element_by_xpath(u"//img[@alt='强化学习 (Reinforcement Learning)']").click()
# driver.find_element_by_link_text("About").click()
# driver.find_element_by_link_text(u"赞助").click()
# driver.find_element_by_link_text(u"教程 ▾").click()
# driver.find_element_by_link_text(u"数据处理 ▾").click()
# driver.find_element_by_link_text(u"网页爬虫").click()

driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").click()
# time.sleep(3)
driver.find_element_by_id("kw").click()
# time.sleep(3)
driver.find_element_by_id("kw").click()
# time.sleep(3)
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
time.sleep(3)
# driver.find_element_by_id("s_form_wrapper").click()
# time.sleep(3)
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("13123123123")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.find_element_by_id("kw").click()
time.sleep(3)
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.find_element_by_link_text(u"Python_百度百科").click()
time.sleep(3)
# ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
driver.find_element_by_link_text(u"Python简介及应用领域").click()
time.sleep(3)
html = urlopen("https://baike.baidu.com/item/%E6%95%99%E5%AD%A6").read().decode('utf-8')
# driver.find_element_by_link_text(u"教学").click()
# ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_2 | ]]

# 得到网页 html, 还能截图
html = driver.page_source       # get html
driver.get_screenshot_as_file("img/sreenshot1.png")
driver.close()
print(html[:200])