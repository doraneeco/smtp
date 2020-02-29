import schedule
import time
import glob
import os

def job():
    # datas配下のファイル一覧を取得
    datas = glob.glob("./datas/*")
    # dataを処理
    for data in datas:
        with open(data, encoding="utf-8") as f:
            s = f.read()
            print(s)
            f.close() 
            os.remove(data)

 
def job_listen():
    # jobを登録
    schedule.every(1).seconds.do(job)
    while True:
          schedule.run_pending()
          time.sleep(1)

job_listen()
