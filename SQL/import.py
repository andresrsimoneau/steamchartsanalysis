import sqlite3

#conn is the variable representing the connection with gamesinfo.db
conn = sqlite3.connect("presidentsinfo.db")

#maingames is the cursor that allows us to request edits to the .db file
presidents = conn.cursor()

#list of tuples of incumbent Presidents/VP, their election year, approval rating, EC count, POTUS/VP
#all approval rating data collected from https://www.presidency.ucsb.edu/statistics/data/presidential-job-approval-all-data
# TRUE = POTUS, FALSE = VP (too lazy to write out POTUS lol)
presidential_outcomes = [
	('POTUS Harry Truman 1948', 1948, 40, 303, 1, 'WON', 4.48),
	('POTUS Dwight D. Eisenhower 1956', 1956, 68, 457, 1, 'WON', 10.9),
	('VP Richard Nixon 1960', 1960, 58, 219, 0, 'LOST', -0.17),
	('POTUS Lyndon B. Johnson 1964', 1964, 74, 486, 1, 'WON', 22.6),
	('VP Hubert Humphrey 1968', 1968, 42, 191, 0, 'LOST', -0.7),
	('POTUS Richard Nixon 1972', 1972, 56, 520, 1, 'WON', 23.2),
	('POTUS Gerald Ford 1976', 1976, 45, 240, 1, 'LOST', -2.1),
	('POTUS Jimmy Carter 1980', 1980, 37, 49, 1, 'LOST', -9.7),
	('POTUS Ronald Reagan 1984', 1984, 58, 525, 1, 'WON', 18.2),
	('VP George H.W Bush 1988', 1988, 51, 426, 0, 'WON', 7.7),
	('POTUS George H.W Bush 1992', 1992, 34, 168, 1, 'LOST', -5.5),
	('POTUS Bill Clinton 1996', 1996, 54, 379, 1, 'WON', 8.5),
	('VP Al Gore 2000', 2000, 57, 266, 0, 'LOST', 0.5),
	('POTUS George W. Bush 2004', 2004, 48, 286, 1, 'WON', 2.4),
	('POTUS Barack Obama 2012', 2012, 51, 332, 1, 'WON', 3.9),
	('POTUS Donald Trump 2020', 2020, 45, 232, 1, 'LOST', -4.5),
	('VP Kamala Harris 2024', 2024, 41, 226, 0, 'LOST', -1.3),
]

#Creating presidents Table
presidents.execute("""
CREATE TABLE IF NOT EXISTS presidents(
    name TEXT,
    election_year INTEGER,
    approval INTEGER,
    electoral_votes INTEGER,
    is_president INTEGER,
    won_election TEXT,
    margin_of_victory FLOAT
)
""")

presidents.execute("DELETE FROM presidents;")

presidents.executemany("""
INSERT INTO presidents (name, election_year, approval, electoral_votes, is_president, won_election, margin_of_victory)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", presidential_outcomes)

u45_or_below = """
SELECT name, approval, electoral_votes, won_election, margin_of_victory
FROM presidents
WHERE approval <= 45 
ORDER BY margin_of_victory DESC
"""
presidents.execute(u45_or_below)
below_45_results = presidents.fetchall()

vp_results = """
SELECT name, approval, electoral_votes, won_election, margin_of_victory
FROM presidents
WHERE is_president = 0  
ORDER BY margin_of_victory DESC
"""
presidents.execute(vp_results)
vp_ec_results = presidents.fetchall()

over50 = """
SELECT name, approval, electoral_votes, won_election, margin_of_victory
FROM presidents
WHERE approval >= 50
ORDER BY margin_of_victory DESC
"""
presidents.execute(over50)
over_50 = presidents.fetchall()

potus_results = """
SELECT name, approval, electoral_votes, won_election, margin_of_victory
FROM presidents
WHERE is_president = 1  
ORDER BY margin_of_victory DESC
"""
presidents.execute(potus_results)
potus_ec_results = presidents.fetchall()

def print_section(title, query):
    print(title)
    presidents.execute(query)
    for name, approval, electoral_vote, outcome, margin in presidents.fetchall():
        print(f"{name} | {approval}% approval | {electoral_vote} EC | {outcome} | PV margin {margin} pp")
    print() #used for spacing

print_section("INCUMBENT VICE PRESIDENT RESULTS SINCE 1948", vp_results)
print_section("INCUMBENT PRESIDENT RESULTS SINCE 1948", potus_results)
print_section("INCUMBENT RESULTS WITH AN APPROVAL RATING OF 45% OR BELOW", u45_or_below)
print_section("INCUMBENT RESULTS WITH AN APPROVAL RATING OVER 50%", over50)
#makes the saves to the .db file and closes the connection
conn.commit()
conn.close()



