from flask import Flask, render_template, request
import mysql.connector


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/sources')
def sources():
    return render_template('sources.html')

@app.route('/about')
def about():
    return render_template('about.html') #, posts=posts



@app.route('/diary')
def diary():
    db = mysql.connector.connect(
    host="miranda.mysql.pythonanywhere-services.com",
    user="miranda",
    passwd="molinase",
    database= "miranda$default")
    cur= db.cursor()
    cur.execute("SELECT * FROM molini limit 700 offset 10")
    data = cur.fetchall()
    cur.close()

    def search(query):
        a= [] #if query.lower() in x]
        for square in data:
            for round in square:
                if query.lower() in round.lower():
                  a.append(square)
        return a

    q = request.args.get("q", "")
    result=search(q)

    return render_template('diary.html', q=q, result=result, data=data)















