import os
from flask import Flask, render_template,request
app = Flask(__name__)

# 這裡明確指定 templates 資料夾的路徑
template_dir = os.path.abspath('./templates')
app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def index():
    # 使用 render_template 來讀取 templates/base.html
    return render_template("base.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/Holland")
def Holland():
    return render_template("Holland.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/MIS")
def MIS():
    return render_template("MIS.html")

if __name__ == "__main__":
    app.run(debug=True)
