import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

daysWeek = {
    'Понедельник': '1',
    'Вторник': '2',
    'Среда': '3',
    'Четверг': '4',
    'Пятница': '5',
    'Суббота': '6'
}

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

@app.route('/update', methods=['POST'])
def update():
    numclas = request.form['numclas']
    lesson = request.form['lesson']
    dayWeek = request.form['dayWeek']
    numles = request.form['numles']
    if numclas == '11А': update_class11A(lesson, dayWeek, numles)
    elif numclas == '11Б': update_class11B(lesson, dayWeek, numles)
    elif numclas == '11В': update_class11C(lesson, dayWeek, numles)
    return 'lesson updated'

def update_class11A(lesson, dayWeek, numles):
    con = sqlite3.connect('LessonsList.db')
    cur = con.cursor()
    if numles == 'Первый': cur.execute('UPDATE class11A SET LessonOne = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Второй': cur.execute('UPDATE class11A SET LessonTwo = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Третий': cur.execute('UPDATE class11A SET LessonThree = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Четвертый': cur.execute('UPDATE class11A SET LessonFour = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Пятый': cur.execute('UPDATE class11A SET LessonFive = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Шестой': cur.execute('UPDATE class11A SET LessonSix = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Седьмой': cur.execute('UPDATE class11A SET LessonSeven = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Восьмой': cur.execute('UPDATE class11A SET LessonEight = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    else:
        print("ERROR")
    con.commit()
    con.close()


def update_class11B(lesson, dayWeek, numles):
    con = sqlite3.connect('LessonsList.db')
    cur = con.cursor()
    if numles == 'Первый': cur.execute('UPDATE class11B SET LessonOne = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Второй': cur.execute('UPDATE class11B SET LessonTwo = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Третий': cur.execute('UPDATE class11B SET LessonThree = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Четвертый': cur.execute('UPDATE class11B SET LessonFour = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Пятый': cur.execute('UPDATE class11B SET LessonFive = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Шестой': cur.execute('UPDATE class11B SET LessonSix = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Седьмой': cur.execute('UPDATE class11B SET LessonSeven = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Восьмой': cur.execute('UPDATE class11B SET LessonEight = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    else:
        print("ERROR")
    con.commit()
    con.close()


def update_class11C(lesson, dayWeek, numles):
    con = sqlite3.connect('LessonsList.db')
    cur = con.cursor()
    if numles == 'Первый': cur.execute('UPDATE class11C SET LessonOne = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Второй': cur.execute('UPDATE class11C SET LessonTwo = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Третий': cur.execute('UPDATE class11C SET LessonThree = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Четвертый': cur.execute('UPDATE class11C SET LessonFour = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Пятый': cur.execute('UPDATE class11C SET LessonFive = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Шестой': cur.execute('UPDATE class11C SET LessonSix = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Седьмой': cur.execute('UPDATE class11C SET LessonSeven = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    elif numles == 'Восьмой': cur.execute('UPDATE class11C SET LessonEight = ? WHERE ROWID = ?', (lesson, daysWeek[dayWeek]))
    else:
        print("ERROR")
    con.commit()
    con.close()

@app.route("/")
def index():
    return render_template("Lessons_list.html", **{"Class11A": get_class11A(), "Class11B": get_class11B(), "Class11C": get_class11C()})

if __name__ == '__main__':
    app.run(debug=True)