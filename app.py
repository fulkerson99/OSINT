from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template("main.html")

@app.route('/instagram_intelligence_report' , methods=['GET','POST'])
def instagram_intelligence_report():
    return render_template("instagram_intelligence.html")



if __name__ == '__main__':
    app.run()