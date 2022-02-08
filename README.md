# DecodingHash
ハッシュ関数を解読する


## 概要
本プログラムは簡単なハッシュ関数を解読するプログラムです。

## 平文の条件
小文字アルファベット＋数字による6文字で構成されていること。

sha1,sha224,sha256,sha512,md5

のいずれかによってハッシュ化されているものとする。

## 使用例
今回は"abc123"という平文をmd5によってハッシュ化したものを解読する。

![image](https://user-images.githubusercontent.com/82374688/152969454-ac17600f-b54d-42c6-9f67-0864bbbb1a69.png)

![image2](https://user-images.githubusercontent.com/82374688/152970218-1b96f5b1-92a8-4c00-8a61-3db50fa98325.png)

因みに時間は52秒かかりました。

## 反省点
例えば"z0z0ww"のような辞書の末端に載っている文字で構成された平文の場合、

かなり時間がかかる。並列処理やGPUによる解読を可能にする必要がある。

※ここでいう辞書

"abcdefghijklmnopqrstuvwxyz0123456789"

### きっかけ
hashlibという面白そうなライブラリを発見したため
