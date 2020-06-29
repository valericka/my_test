from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
import time

driver = webdriver.Chrome()

#1.Перейти по ссылке на главную страницу сайта Netpeak.
driver.get('https://netpeak.ua/')

#2.Перейдите на страницу "Работа в Netpeak", нажав на кнопку "Карьера"
btn = driver.find_element_by_link_text('Карьера')
btn.click()

driver.implicitly_wait(3)
#time.sleep(5)

#3.Перейти на страницу заполнения анкеты, нажав кнопку - "Я хочу работать в Netpeak"
btn_1 = driver.find_element_by_link_text('Я хочу работать в Netpeak')
btn_1.click()

#4. Загрузить файл с недопустимым форматом в блоке "Резюме", например png, и проверить что на странице появилось сообщение, о том что формат изображения неверный.
time.sleep(2)
upload = driver.find_element_by_name('up_file')
upload.send_keys('W:\Z\PyProj\W\g.png')
time.sleep(2)
er = driver.find_element_by_xpath('//*[@id="up_file_name"]/label')
assert "Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf)." in driver.page_source

#5.Заполнить случайными данными блок "3. Личные данные"
name = driver.find_element_by_id("inputName")
name.send_keys('Валерий')
lastname = driver.find_element_by_id('inputLastname')
lastname.send_keys('Городничий')
email = driver.find_element_by_id('inputEmail')
email.send_keys('blabla@email.com')

#6.Нажать на кнопку отправить резюме
send_btn = driver.find_element_by_id('submit')
send_btn.click()

#7.Проверить что сообщение на текущей странице  - "Все поля являются обязательными для заполнения" - подсветилось красным цветом
RED = Color.from_string('red')
red_text = Color.from_string(driver.find_element(By.XPATH,'/html/body/div[2]/div/p').value_of_css_property('color'))
assert red_text == RED

#8. Нажать на логотип для перехода на главную страницу и убедиться что открылась нужная страница.
logo = driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div[1]/div[1]/a')
logo.click()
time.sleep(3)
url = driver.current_url
print(url)
assert "https://netpeak.ua/" == url


driver.close()
