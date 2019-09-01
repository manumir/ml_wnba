#! /usr/bin/python3

import time
import os
import sys
start_time = time.time()

from selenium import webdriver
from bs4 import BeautifulSoup as bs4

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

year=str(sys.argv[1])

def get_stats():

    print('program starting')
    driver = webdriver.Chrome(executable_path='C:/Users/dude/Desktop/chromedriver.exe')
    print('driver is initalized')

    driver.get('https://stats.wnba.com/teams/boxscores-traditional/?Season='+year+'&SeasonType=Regular%20Season')

    file=open('data1.txt','w')
    path_2_num_pages=driver.find_element_by_class_name("stats-table-pagination__info")
    NUMBER_OF_PAGES=int(path_2_num_pages.text[-2:])
    print(NUMBER_OF_PAGES)
    i=0
    for i in range(NUMBER_OF_PAGES):
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.nba-stat-table__overflow")))

        html=bs4(driver.page_source,'html.parser')
        #features = html.table.thead.tr.text #don't need to scrape this multiple times
        stats= html.table.tbody.text 
        file.write(stats)

        path=driver.find_element_by_class_name("stats-table-pagination__next")
        path.click()

    file.close()
    driver.quit()

get_stats()
print("--- %s seconds ---" % (time.time() - start_time))


f=[]
file =open('data1.txt','r') #,encoding ='cp1252')
file1=file.readlines()

for x in file1:
  x=x.strip('\n')
  x=x.strip(' ')
  x=x + ','

  if x != ',':
    f.append(x)

file.close()
os.remove('data1.txt')

file=open('finaldata1.txt','w')
i=0
for x in f:
    file.write(x)
    i+=1
    if i==24:
      file.write('\n')
      i=0
file.close()

#try to do this without having to open the file again

filer=open('finaldata1.txt','r')
lines=filer.readlines()
filer.close()
os.remove('finaldata1.txt')

file=open('raw_'+year+'.csv','w')
for line in lines:
  file.write(line)
file.close()

