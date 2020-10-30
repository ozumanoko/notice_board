from flask import Flask, redirect, url_for, session
from flask import render_template, request
import os, json, datetime
import bbs_login
import bbs_data

app = Flask(__name__)
app.secret_key = 'GYJBFRTYJafGTYUf'

@app.route('/')
def index():
    #ログイン確認
    if not bbs_login.is_login():
        return redirect('/login')
    #ログ一覧を表示
    return render_template('index.html',
                            user=bbs_login.get_user(),
                            data=bbs_data.load_data())
#ログイン画面を表示
@app.route('/login')
def login():
    return render_template('login.html')

#ログイン処理
@app.route('/try_login', methods=['POST'])
def try_login():
    user = request.form.get('user', '')
    pw = request.form.get('pw', '')
    if bbs_login.try_login(user, pw):
        return redirect('/')

    return show_msg('ログインに失敗しました。')

#ログアウト処理
@app.route('/logout')
def logout():
    bbs_login.try_logout()
    return show_msg('ログアウトしました。')

#書き込み処理
@app.route('/write', methods=['POST'])
def write():
    #ログインが必要
    if not bbs_login.is_login():
        return redirect('/login')
    #フォームテキストを取得
    ta = request.form.get('ta', '')
    if ta == '': return show_msg('書き込みが空でした')
    #データに追記保存
    bbs_data.save_data_append(user=bbs_login.get_user(),
                              text=ta)
    return redirect('/')

#テンプレートを利用してメッセージを出力
def show_msg(msg):
    return render_template('msg.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
