from .settings import settings
#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request
import sys
sys.path.append("/opt/anaconda3/lib/python3.7/site-packages")
import tweepy

#Flaskオブジェクトの生成
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


#以下を追加
@app.route("/",methods=["post"])
def post():
    name = request.form["name"]
    # 取得した各種キーを格納---------------------------------------------

    consumer_key = settings.CK
    consumer_secret = settings.CS
    access_token = settings.AT
    access_token_secret = settings.ATS

    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    #-------------------------------------------------------------------
    
    #ツイートを投稿
    #account_li = name.split() #取得したいユーザーのユーザーIDを代入

    account_li = name.split()

    return render_template("index.html", api = api, account_li = account_li)


#おまじない
if __name__ == "__main__":
    app.run(debug=True) 