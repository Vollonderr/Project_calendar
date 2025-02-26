import sqlite3

def get_events():
	res = []
	con = sqlite3.connect("Events.db")
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
	con = sqlite3.connect("Workers.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM Workers")
	rows = cur.fetchall()
	for i in rows:
		res.append(list(i))
	con.commit()
	con.close()
	return res