# coding: utf-8
from flask import Flask, request
#import schedule
import time

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    #time.time()
    f = open('./datas/' + str(time.time()) + '.txt', 'w', encoding="utf-8")
    f.write(request.form['body'] + '\n')
    f.close()
    return "true"

if __name__ == '__main__':
    app.run()

