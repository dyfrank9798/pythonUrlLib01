# import os
#
# os.makedirs('./img/', exist_ok=True)

from selenium import webdriver

driver = webdriver.Chrome()
# driver.get("https://morvanzhou.github.io/")
# # driver.find_element_by_xpath(u"//img[@alt='强化学习 (Reinforcement Learning)']").click()
# # driver.find_element_by_link_text("About").click()
# # driver.find_element_by_link_text(u"赞助").click()
# # driver.find_element_by_link_text(u"教程 ▾").click()
# # driver.find_element_by_link_text(u"数据处理 ▾").click()
# # driver.find_element_by_link_text(u"网页爬虫").click()

# driver.get("http://localhost:8080/ysxt/login.jsp")
# driver.find_element_by_id("login").click()
# driver.find_element_by_id("loginName").click()
# driver.find_element_by_id("loginName").click()
# driver.find_element_by_id("loginName").clear()
# driver.find_element_by_id("loginName").send_keys("ys1001")
# driver.find_element_by_id("password").clear()
# driver.find_element_by_id("password").send_keys("111111")
# driver.find_element_by_id("randomCode").clear()
# driver.find_element_by_id("randomCode").send_keys("0000")
# driver.find_element_by_id("btn").click()
# # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
# driver.find_element_by_link_text(u"药事所").click()
# # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
# # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
# driver.find_element_by_xpath("(//div[@name='menu'])[10]").click()
# driver.find_element_by_link_text(u"短缺药检测医疗机构信息维护").click()


driver.get("http://localhost:8088/ysxtqx/login.jsp#")
driver.find_element_by_id("loginName").click()
driver.find_element_by_id("password").clear()
driver.find_element_by_id("loginName").send_keys("ys1001")
driver.find_element_by_id("password").send_keys("111111")
driver.find_element_by_id("captcha").clear()
driver.find_element_by_id("captcha").send_keys("1111")
driver.find_element_by_xpath("//div[@onclick='onLoginClick()']").click()
driver.find_element_by_id("a$text").clear()
driver.find_element_by_id("a$text").send_keys("scqy0426")
driver.find_element_by_id("b$text").clear()
driver.find_element_by_id("b$text").send_keys("111")
driver.find_element_by_link_text(u"药事所").click()
driver.find_element_by_xpath("//div[@id='mini-6$4']/div/div[2]").click()
driver.find_element_by_id("10103001$text").click()

html = driver.page_source       # get html
driver.get_screenshot_as_file("./img/sreenshot1.png")
driver.close()
print(html[:200])