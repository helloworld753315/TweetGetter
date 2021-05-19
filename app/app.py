#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template,request
import sys
sys.path.append("/opt/anaconda3/lib/python3.7/site-packages")
import tweepy

#Flaskオブジェクトの生成
app = Flask(__name__)

@app.route("/index")
def index():
    name = request.args.get("name")
    return render_template("index.html",name=name)


#以下を追加
@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    # 取得した各種キーを格納---------------------------------------------
    consumer_key ="3UKy3NqODhieKg9ozFlnctCai"
    consumer_secret ="054pUmoHqm8n2GbfEtiZ4LCQsO4xgGbO416a2REVmb9DTM5W8n"
    access_token="946015076267343872-4rM8Tj6uXMLPwBKHO0raW3P8hQj2xl2"
    access_token_secret ="JLIZkoaHQ4gOXTB42Jcc1KcvAqvXvXgLfsXEzIKqWzllR"
    
    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    #-------------------------------------------------------------------
    
    #ツイートを投稿
    account_li = name.split() #取得したいユーザーのユーザーIDを代入
    '''
    account_li = [
        "@SATOMU97258957",
        "@Ryusei57606646",
        "@ryoka_okiu_aka",
        "@OKIU_VR"
    ]
    '''

    return render_template("index.html", name=name,account_li = account_li)


#おまじない
if __name__ == "__main__":
    app.run(debug=True)