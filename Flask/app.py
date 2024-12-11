import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_class11A():
    res = []
    con = sqlite3.connect('LessonsList.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM class11A')
    rows = cur.fetchall()
    for i in range(len(rows)):
        res.append(list(rows[i]))
    con.commit()
    con.close()
    return res

def get_class11B():
    res = []
    con = sqlite3.connect('LessonsList.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM class11B')
    rows = cur.fetchall()
    for i in range(len(rows)):
        res.append(list(rows[i]))
    con.commit()
    con.close()
    return res

def get_class11C():
    res = []
    con = sqlite3.connect('LessonsList.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM class11C')
    rows = cur.fetchall()
    for i in range(len(rows)):
        res.append(list(rows[i]))
    con.commit()
    con.close()
    return res

@app.route("/")
def index():
    return render_template("Lessons_list.html", **{"Class11A": get_class11A(), "Class11B": get_class11B(), "Class11C": get_class11C()})

if __name__ == '__main__':
    app.run(debug=True)