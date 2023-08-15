from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


keyword = input('What Do you Want   ?')

browser = webdriver.Chrome()
browser.get('https://www.digikala.com/search/?q={}'.format(keyword))


img_src = []


imgs = WebDriverWait(browser, 100).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.w-100.radius-medium.d-inline-block.lazyloaded')))
for idx, img in enumerate(imgs):
    image_address = img.get_attribute('src')
    img_src.append(image_address)
    response = requests.get(image_address)
    print(response.content)
    with open('digi{}.png'.format(idx), 'wb') as file:
        file.write(response.content)
with open('Images Soureces.txt', 'w') as file:
    for i in img_src:
        file.write(f'{i}\n')
time.sleep(10)



titles = WebDriverWait(browser, 100).until(EC.visibility_of_all_elements_located((
    By.CSS_SELECTOR, '.ellipsis-2.text-body2-strong.color-700.styles_VerticalProductCard__productTitle__6zjjN')))
textes = ''

for idx, title in enumerate(titles):
    text = title.text
    textes += f'{idx}: {text}\n'



with open('Titles.txt', 'w' , encoding ="UTF-8") as file:
    file.write(textes)


links = WebDriverWait(browser, 100).until(EC.visibility_of_all_elements_located((
    By.CSS_SELECTOR, '.d-block.pointer.pos-relative.bg-000.overflow-hidden.grow-1.py-3.px-4.px-2-lg.h-full-md.styles_VerticalProductCard--hover__ud7aD')))

nlink =''
for idx, link in enumerate(links):
    text = link.get_attribute('href')
    nlink += f'{idx}: {text}\n'
with open('Links.txt', 'w', encoding="UTF-8") as file:
    file.write(nlink)



Prices = WebDriverWait(browser , 100).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR , '.d-flex.ai-center.jc-end.gap-1.color-700.color-400.text-h5.grow-1')))

Price = ''

for ind , price in enumerate(Prices):
    p = price.text
    Price += f'{p}\n'
with open('Prices.txt', 'w' , encoding='UTF-8' ) as f:
    f.write(Price)

