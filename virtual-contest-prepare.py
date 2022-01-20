from bs4 import BeautifulSoup
import os

src_dir = '/path/to/saved_html_file'
src_file = 'AtCoder Problems.html'
out_dir = '/path/to/contest_directory'

fname = src_dir + '/' + src_file
with open(fname) as f:
    html = f.read()
soup = BeautifulSoup(html, "html.parser")

problems = []
for ele in soup.find_all('a'):
    url = ele.get('href')
    if(url != None and url.startswith('https://atcoder.jp/contests/')):
        problems.append(url)

os.chdir(out_dir)
for i in range(7):
    os.chdir(chr(ord('a')+i))
    os.system('touch test')
    os.system('rm -rf test')
    os.system('oj d ' + problems[i])
    os.chdir('..')