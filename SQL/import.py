import sqlite3

#conn is the variable representing the connection with gamesinfo.db
conn = sqlite3.connect("presidentsinfo.db")

#maingames is the cursor that allows us to request edits to the .db file
presidents = conn.cursor()

#list of incumbent Presidents/VP, their election year, approval rating, EC count, POTUS/VP
#all approval rating data collected from https://www.presidency.ucsb.edu/statistics/data/presidential-job-approval-all-data
# TRUE = POTUS, FALSE = VP
presidential_outcomes = [
	('Harry Truman', 1948, 40, 303, 1)
	('Dwight D. Eisenhower', 1956, 68, 457, 1)
	('Richard Nixon', 1960, 58, 219, 0)
	('Lyndon B. Johnson', 1964, 74, 486, 1)
	('Richard Nixon', 1972, 56, 520, 1)
	('Gerald Ford', 1976, 45, 240, 1)
	('Jimmy Carter', 1980, 37, 49, 1)
	('Ronald Reagan', 1984, 58, 525, 1)
	('George H.W Bush', 1988, 51, 426, 0)
	('George H.W Bush', 1992, 34, 168, 1)
	('Bill Clinton', 1996, 54, 379, 1)
	('Al Gore', 2000, 57, 266, 0)
	('George W. Bush', 2004, 48, 286, 1)
	('Barack Obama', 2012, 51, 332, 1)
	('Donald Trump', 2020, 45, 232, 1)
	('Kamala Harris', 2024, 41, 226, 0)
]
#Creating presidents Table
presidents.execute("""CREATE TABLE presidents(
		INSERT INTO games (president_name, election_year, approval_rating, ec_count)

	)""")
#REAL refers to floating_point numbers (i.e 5.12345)
#TEXT refers to numeric text (i.e 'Batman')
#INTEGER of course, refers to integers (i.e 5)



#makes the saves to the .db file and closes the connection
conn.commit()
conn.close()