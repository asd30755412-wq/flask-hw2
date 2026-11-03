import os
from flask import Flask, render_template

app = Flask(__name__)

# 建立三筆包含 title, category, content 三個欄位的範例資料
posts = [
    {
        "title": "質子交換膜燃料電池 (PEMFC) 流道精密加工分析",
        "category": "氫能與燃料電池",
        "content": "探討雙極板微流道之精密加工公差對氣體擴散效率與水管理之影響，透過優化流場設計提升燃料電池整體發電功率密度。"
    },
    {
        "title": "再生能源併網與儲能系統整合架構",
        "category": "綠能系統整合",
        "content": "分析太陽能與風力發電在不同負載條件下之功率波動，並結合綠氫儲能系統進行削峰填谷，提升微電網之穩定度。"
    },
    {
        "title": "五軸複合加工機於綠能渦輪葉片之應用",
        "category": "精密機械加工",
        "content": "利用高剛性五軸同動加工技術進行複雜曲面葉片切削，有效降低表面粗糙度並減少二次加工耗時，大幅提升能源轉換效率。"
    }
]

@app.route("/")
def home():
    # 將 posts 資料傳遞給 templates/index.html 呈現
    return render_template("index.html", posts=posts)

if __name__ == "__main__":
    # 相容本地端執行與雲端動態 PORT 環境變數
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
