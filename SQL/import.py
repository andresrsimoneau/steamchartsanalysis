import sqlite3

#conn is the variable representing the connection with gamesinfo.db
conn = sqlite3.connect("gamesinfo.db")

#maingames is the cursor that allows us to edit the .db file
games = conn.cursor()

#Creating Games Table
games.execute("""CREATE TABLE games(
		game_name TEXT,
		year_released INTEGER,
		sales_in_millions REAL,
	)""")




conn.commit()
conn.close()