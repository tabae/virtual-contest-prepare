from bs4 import BeautifulSoup
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

if(len(sys.argv) < 2 or sys.argv[1] == '--help' or sys.argv[1] == '-h'):
    print('Usage: python3 ' + sys.argv[0] + ' [URL of virtual contest page]')
    sys.exit(0)        
    
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(sys.argv[1])
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

problems = []
for ele in soup.find_all('a'):
    url = ele.get('href')
    if(url != None and url.startswith('https://atcoder.jp/contests/')):
        problems.append(url)

problems = list(dict.fromkeys(problems))

if(not problems):
    print('Error: failed to download problems from AtCoder Problems')
    sys.exit(0)

for i in range(len(problems)):
    os.chdir(chr(ord('a')+i))
    os.system('touch test')
    os.system('rm -rf test')
    os.system('oj d ' + problems[i])
    os.chdir('..')
