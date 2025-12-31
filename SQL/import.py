import sqlite3

#conn is the variable representing the connection with gamesinfo.db
conn = sqlite3.connect("presidentsinfo.db")

#maingames is the cursor that allows us to request edits to the .db file
presidents = conn.cursor()

#list of tuples of incumbent Presidents/VP, their election year, approval rating, EC count, POTUS/VP
#all approval rating data collected from https://www.presidency.ucsb.edu/statistics/data/presidential-job-approval-all-data
# TRUE = POTUS, FALSE = VP (too lazy to write out POTUS lol)
presidential_outcomes = [
	('Harry Truman', 1948, 40, 303, 1, 'WON'),
	('Dwight D. Eisenhower', 1956, 68, 457, 1, 'WON'),
	('Richard Nixon', 1960, 58, 219, 0, 'LOST'),
	('Lyndon B. Johnson', 1964, 74, 486, 1, 'WON'),
	('Hubert Humphrey', 1968, 42, 191, 0, 'LOST'),
	('Richard Nixon', 1972, 56, 520, 1, 'WON'),
	('Gerald Ford', 1976, 45, 240, 1, 'LOST'),
	('Jimmy Carter', 1980, 37, 49, 1, 'LOST'),
	('Ronald Reagan', 1984, 58, 525, 1, 'WON'),
	('George H.W Bush', 1988, 51, 426, 0, 'WON'),
	('George H.W Bush', 1992, 34, 168, 1, 'LOST'),
	('Bill Clinton', 1996, 54, 379, 1, 'WON'),
	('Al Gore', 2000, 57, 266, 0, 'LOST'),
	('George W. Bush', 2004, 48, 286, 1, 'WON'),
	('Barack Obama', 2012, 51, 332, 1, 'WON'),
	('Donald Trump', 2020, 45, 232, 1, 'LOST'),
	('Kamala Harris', 2024, 41, 226, 0, 'LOST'),
]
#Creating presidents Table
presidents.execute("""
CREATE TABLE IF NOT EXISTS presidents(
    name TEXT,
    election_year INTEGER,
    approval INTEGER,
    electoral_votes INTEGER,
    is_president INTEGER,
    won_election TEXT
)
""")

presidents.execute("DELETE FROM presidents;")

presidents.executemany("""
INSERT INTO presidents (name, election_year, approval, electoral_votes, is_president, won_election)
VALUES (?, ?, ?, ?, ?, ?)
""", presidential_outcomes)

u45_or_below = """
SELECT name, approval, electoral_votes, won_election
FROM presidents
WHERE approval <= 45 
ORDER BY won_election
"""
presidents.execute(u45_or_below)
below_45_results = presidents.fetchall()

vp_results = """
SELECT name, approval, electoral_votes, won_election
FROM presidents
WHERE is_president = 0  
ORDER BY won_election
"""
presidents.execute(vp_results)
vp_ec_results = presidents.fetchall()

over50 = """
SELECT name, approval, electoral_votes, won_election
FROM presidents
WHERE approval >= 50
ORDER BY won_election
"""
presidents.execute(over50)
over_50 = presidents.fetchall()

potus_results = """
SELECT name, approval, electoral_votes, won_election
FROM presidents
WHERE is_president = 1  
ORDER BY won_election
"""
presidents.execute(potus_results)
potus_ec_results = presidents.fetchall()

def print_section(title, query):
    print(title)
    presidents.execute(query)
    for name, approval, electoral_vote, outcome in presidents.fetchall():
        print(f"{name} | {approval}% approval | {electoral_vote} EC | {outcome}")
    print()

print_section("INCUMBENT VICE PRESIDENT RESULTS SINCE 1948", vp_results)
print_section("INCUMBENT PRESIDENT RESULTS SINCE 1948", potus_results)
print_section("INCUMBENT RESULTS WITH AN APPROVAL RATING BELOW 45%", u45_or_below)
print_section("INCUMBENT RESULTS WITH AN APPROVAL RATING OVER 50%", over50)
#makes the saves to the .db file and closes the connection
conn.commit()
conn.close()



