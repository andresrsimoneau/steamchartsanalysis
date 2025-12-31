import sqlite3

#conn is the variable representing the connection with gamesinfo.db
conn = sqlite3.connect("presidentsinfo.db")

#maingames is the cursor that allows us to request edits to the .db file
presidents = conn.cursor()

#list of tuples of incumbent Presidents/VP, their election year, approval rating, EC count, POTUS/VP
#all approval rating data collected from https://www.presidency.ucsb.edu/statistics/data/presidential-job-approval-all-data
# TRUE = POTUS, FALSE = VP (too lazy to write out POTUS lol)
presidential_outcomes = [
	('Harry Truman', 1948, 40, 303, 1),
	('Dwight D. Eisenhower', 1956, 68, 457, 1),
	('Richard Nixon', 1960, 58, 219, 0),
	('Lyndon B. Johnson', 1964, 74, 486, 1),
	('Richard Nixon', 1972, 56, 520, 1),
	('Gerald Ford', 1976, 45, 240, 1),
	('Jimmy Carter', 1980, 37, 49, 1),
	('Ronald Reagan', 1984, 58, 525, 1),
	('George H.W Bush', 1988, 51, 426, 0),
	('George H.W Bush', 1992, 34, 168, 1),
	('Bill Clinton', 1996, 54, 379, 1),
	('Al Gore', 2000, 57, 266, 0),
	('George W. Bush', 2004, 48, 286, 1),
	('Barack Obama', 2012, 51, 332, 1),
	('Donald Trump', 2020, 45, 232, 1),
	('Kamala Harris', 2024, 41, 226, 0),
]

#Creating presidents Table
presidents.execute("""
CREATE TABLE IF NOT EXISTS presidents(
    name TEXT,
    election_year INTEGER,
    approval INTEGER,
    electoral_votes INTEGER,
    is_president INTEGER
)
""")

presidents.executemany("""
INSERT INTO presidents (name, election_year, approval, electoral_votes, is_president)
VALUES (?, ?, ?, ?, ?)
""", presidential_outcomes)

u45_or_below = """
SELECT name, approval, electoral_votes
FROM presidents
WHERE approval <= 45
"""

presidents.execute(u45_or_below)
below_45_results = presidents.fetchall()


vp_results = """
SELECT name, approval, electoral_votes
FROM presidents
WHERE is_president = 0
"""
presidents.execute(vp_results)
vp_ec_results = presidents.fetchall()


#REAL refers to floating_point numbers (i.e 5.12345)
#TEXT refers to numeric text (i.e 'Batman')
#INTEGER of course, refers to integers (i.e 5)

#makes the saves to the .db file and closes the connection
conn.commit()




