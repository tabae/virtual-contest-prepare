# virtual-contest-prepare

AtCoder Problems のバーチャルコンテストのサンプルテストケースを一括ダウンロードする．

## 使い方

```
$ gentemp virtual_constest
$ cd virtual contest
$ python3 virtual-contest-prepare.py [バーチャルコンテストのURL]
```

([gentemp](https://github.com/tabae/gentemp)コマンドで生成される) 以下のような構造のディレクトリに各問題のサンプルケースを[online-judge-tools](https://github.com/online-judge-tools/oj)を使ってダウンロードします．
```
virtual_constest/
├── a
│   └── main.cpp
├── b
│   └── main.cpp
...
└── h
    └── main.cpp
```

## 要件
- [online-judge-tools](ttps://github.com/online-judge-tools/oj)を使用しています．
- BeautifulSoup, Selenium, ChromeDriverを使用しています．
    - 参考：https://www.handsonplus.com/programming/python-scraping/
