import sqlite3


def connection():
    conn = sqlite3.connect('trail.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS data(
		Id INTEGER PRIMARY KEY,
		Lname TEXT NOT NULL,
		Sname TEXT NOT NULL,
		Mname TEXT NOT NULL,
		Bday TEXT NOT NULL,
		Sex TEXT NOT NULL,
		Age INTEGER NOT NULL,
		Loc TEXT NOT NULL,
		Contact TEXT NOT NULL
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
    # print("print in db: ",datas)
    return datas


# print(view())

def delete(id):
	conn = sqlite3.connect('trail.db')
	cur = conn.cursor()
	cur.execute("DELETE FROM data WHERE id = ?", (id,))
	conn.commit()
	conn.close()

def search(Lname = '', Sname = '', Mname = '', Bday = '', Sex = '', Age = '', Loc = '', Contact = ''):
	conn = sqlite3.connect('trail.db')
	cur = conn.cursor()
	cur.execute("""SELECT * FROM data WHERE
				Lname = ? OR
				Sname = ? OR
				Mname = ? OR
				Bday = ? OR
				Sex = ? OR
				Age = ? OR
                Loc = ? OR
                Contact = ?""",
				(Lname, Sname, Mname, Bday, Sex, Age, Loc, Contact))
	datas = cur.fetchall()
	conn.commit()
	conn.close()
	return datas

connection()
