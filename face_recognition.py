# プログラムの実行方法
# https://www.python.org/
# からpythonをダウンロードしインストールする
#
# cv2を使う為の準備
# コマンドプロンプトで下記のコマンドを実行
# pip install opencv-contrib-python
import time

import cv2

# カスケード分類器を読み込む
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


# 画像を表示させて実際に確かめるコード
def check_camera_connection_display():
    # カメラのデバイスIDを0から4で繰り返し
    for camera_number in range(0, 5):
        # カメラの画像取得コマンド
        cap = cv2.VideoCapture(camera_number, cv2.CAP_DSHOW)
        ret, frame = cap.read()

        # 画像取得に成功した？
        if ret is True:
            # 現在の時刻を取得
            start = time.time()

            # 無限ループ
            while True:
                # 経過時間を計算
                elasped_time = time.time() - start

                # キーボードの「q」を押されていたらwhileを抜ける
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

                # 5秒経過してたらwhileを抜ける
                if elasped_time > 5.0:
                    break

                # カメラの画像取得コマンド
                ret2, frame = cap.read()

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
                cv2.imshow(f"Camera Number: {camera_number}", frame)

            # ビデオファイル解放
            cap.release()

            # 全てのウインドウを閉じる
            cv2.destroyAllWindows()

            # 標準出力に結果を表示
            print("port number", camera_number, "Find!")

        else:
            # 標準出力に結果を表示
            print("port number", camera_number, "None")


if __name__ == "__main__":
    check_camera_connection_display()
