import sqlite3

def get_events():
	res = []
	con = sqlite3.connect("instance\Events.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM Events")
	rows = cur.fetchall()
	for i in rows:
		res.append(list(i))
	con.commit()
	con.close()
	return res

def get_workers():
	res = []
	con = sqlite3.connect("instance\Workers.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM Workers")
	rows = cur.fetchall()
	for i in rows:
		res.append(list(i))
	con.commit()
	con.close()
	return res

def get_colors():
	res = []
	con = sqlite3.connect("user_field\instance\Colors.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM Colors")
	rows = cur.fetchall()
	for i in rows:
		res.append(list(i))
	con.commit()
	con.close()
	return res

def update_colors(text, BG, BGLOW, lines):
	con = sqlite3.connect('user_field\instance\Colors.db')
	cur = con.cursor()
	cur.execute('UPDATE colors SET text = ?, BG = ?, BGLOW = ?, lines = ? WHERE ROWID = ?', (text, BG, BGLOW, lines, 1))
	con.commit()
	con.close()