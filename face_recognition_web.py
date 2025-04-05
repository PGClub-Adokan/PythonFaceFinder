# プログラムの実行方法
# https://www.python.org/
# からpythonをダウンロードしインストールする
#
# cv2を使う為の準備
# コマンドプロンプトで下記のコマンドを実行
# pip install opencv-contrib-python
#
# Flaskを使う為の準備
# コマンドプロンプトで下記のコマンドを実行
# pip install flask
#
# コマンドプロンプトでapp.pyを置いたフォルダに移動し、下記コマンドを実行
# python app.py
# 表示されたURLにブラウザでアクセスする
import time

import cv2
from flask import Flask, Response

app = Flask(__name__)


# カスケード分類器を読み込む
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def generate_frames():
    # 無限ループ
    while True:
        # カメラのデバイスIDを0から4で繰り返し
        for camera_number in range(0, 5):
            # カメラの画像取得コマンド
            cap = cv2.VideoCapture(camera_number, cv2.CAP_DSHOW)
            success, frame = cap.read()

            # 画像取得に成功した？
            if success is True:
                # 現在の時刻を取得
                start = time.time()

                # 無限ループ
                while True:
                    # 経過時間を計算
                    elasped_time = time.time() - start

                    # カメラの画像取得コマンド
                    success, frame = cap.read()

                    # 5秒経過してたらwhileを抜ける
                    if elasped_time > 5.0:
                        break

                    # 処理を軽くするためにグレー化
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    # 顔を検出する
                    faces = face_cascade.detectMultiScale(
                        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
                    )

                    # 検出した顔の周りに矩形を描画する
                    for x, y, w, h in faces:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                    # 画像を表示
                    _, buffer = cv2.imencode(".jpg", frame)
                    frame = buffer.tobytes()
                    yield (
                        b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
                    )


@app.route("/")
def video_feed():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
