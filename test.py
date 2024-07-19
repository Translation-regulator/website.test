from flask import Flask
app=Flask(__name__) # 建立 Application 物件

# 建立網站首頁的回應方式
@app.route("/")
def index():
    return "馨寶貝" # 回傳網站內容

# 啟動網站伺服器
app.run()

""""
執行時 uvicorn main:app --reload --port "自己想要的阜號"

https://www.google.com/search?q=test

通訊協定：https
主機名稱：www.google.com
埠號：https 預設443，我們測試用網址為8000
路徑：/search
要求字串：q=test


"""

"""
from flask import Flask
app=Flask(__name__) #__name__代表目前執行的模組

@app.route("/") #函式的裝飾 (Decorator): 已函式為基礎，提供附加的功能
def home():
    return "123"

@app.route("/test") #代表我們要處理的網站路徑
def test():
    return "This is Test"

if __name__=="__main__": #如果以主程式執行
    app.run() #立刻啟動伺服器

"""