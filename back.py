import sqlite3


def connection():
    conn = sqlite3.connect('trail.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS data(
		Id INTEGER PRIMARY KEY,
		Lname text,
		Sname text,
		Mname text,
		Bday text,
		Sex text,
		Age INTEGER,
		Loc text,
		Contact text
		)""")
    conn.commit()
    conn.close()


def insert(Lname, Sname, Mname, Bday, Sex, Age, Loc, Contact):
    conn = sqlite3.connect('trail.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES ( NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
                (Lname, Sname, Mname, Bday, Sex, Age, Loc, Contact))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('trail.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    datas = cur.fetchall()
    conn.commit()
    conn.close()
    return datas


print(view())

# def delete(id):
# 	conn = sqlite3.connect('trail.db')
# 	cur = conn.cursor()
# 	cur.execute("DELETE FROM data WHERE id = ?", (id,))
# 	conn.commit()
# 	conn.close()

# def search(date = '', earnings = '', exercise = '', study = '', diet = '', python = ''):
# 	conn = sqlite3.connect('trail.db')
# 	cur = conn.cursor()
# 	cur.execute("""SELECT * FROM data WHERE
# 				date = ? OR
# 				earnings = ? OR
# 				exercise = ? OR
# 				study = ? OR
# 				diet = ? OR
# 				python = ?""",
# 				(date, earnings, exercise, study, diet, python))
# 	datas = cur.fetchall()
# 	conn.commit()
# 	conn.close()
# 	return datas

connection()
