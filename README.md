# PythonFaceFinder

## 概要

-   後さんが作成してくださった顔認証プログラムのサンプル

## 機能

1. カメラを起動し撮影した画像内の `人の顔` を検出する
    - PC 上で動作

## 利用技術

| ID  | 技術名      | 説明                 | 備考                                                            |
| :-- | :---------- | :------------------- | :-------------------------------------------------------------- |
| 1   | python      | -                    |                                                                 |
| 2   | cv2(OpenCV) | 顔判定用のライブラリ | [Qita 上の説明+関連情報リンク集](https://qiita.com/tags/opencv) |

## 補足

1. PR に後さんが作詞途中の WEB 版のサンプルもあります
1. 後さんに教えてもらって知りましたが[リンク先](https://www.eranger.co.jp/blog/news/face-detection-recognition-by-opencv)にあるようにカスタムの顔認識も容易に行えそうです
1. WEB 版の完成のためのアイデア
    1. [JS(クライアント)+Python(Flask)](https://qiita.com/taka_katsu411/items/9ca5baa04671c8aedde7)
        - `WebRTC スマホ python` などでググればたくさん出てくると思います
    1. WebAssembly を Python で作成しフロントは JS(React)などもおもしろそうです
        - [こちら](https://qiita.com/maruzmaruz/items/887ab9fc172db2a45c87)は技術探求のみで実用面では、まだまだこれからだと思います
        - WebAssembly については、こちらの[記事](https://www.creationline.com/tech-blog/others/python/58019)がわかりやすかもです
