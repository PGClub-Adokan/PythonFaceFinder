# PythonFaceFinder

## 概要

- 社内の方が作成してくださった顔認証プログラムのサンプル

## 機能

1. カメラを起動し撮影した画像内の `人の顔` を検出する
    - PC上で動作

## 利用技術

| ID  | 技術名      | 説明                 | 備考                                                            |
| :-- | :---------- | :------------------- | :-------------------------------------------------------------- |
| 1   | python      | -                    |                                                                 |
| 2   | cv2(OpenCV) | 顔判定用のライブラリ | [Qita 上の説明+関連情報リンク集](https://qiita.com/tags/opencv) |

## 補足

1. PRに作成途中(こちらも社内の方が作成くださった)のWEB版のサンプルもあります
1. 作成者さんに教えてもらって知りましたが[リンク先](https://www.eranger.co.jp/blog/news/face-detection-recognition-by-opencv)にあるようにカスタムの顔認識も容易に行えそうです
1. WEB 版の完成のためのアイデア
    1. [JS(クライアント)+Python(Flask)](https://qiita.com/taka_katsu411/items/9ca5baa04671c8aedde7)
        - `WebRTC スマホ python` などでググればたくさん出てくると思います
    1. Node から Python を利用
        - [exec(ライブラリなし)を利用](https://sikou.blog/Node-js-javascript-typescript-python-111b034e829f8078ab5ed484781777c8)
        - [Pytho-shell を利用](https://qiita.com/Ayumu_walker/items/fae0e368d635c6b70fea)
    1. WebAssembly を Python で作成しフロントは JS(React)などもおもしろそうです
        - [こちら](https://qiita.com/maruzmaruz/items/887ab9fc172db2a45c87)は技術探求のみで実用面では、まだまだこれからだと思います
        - WebAssembly については、こちらの[記事](https://www.creationline.com/tech-blog/others/python/58019)がわかりやすかもです
