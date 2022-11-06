import sqlite3

conn = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
conn.execute("CREATE TABLE IF NOT EXISTS accounts("
             "_id INTEGER NOT NULL PRIMARY KEY, "
             "name TEXT NOT NULL, "
             "balance REAL NOT NULL)")

accounts = [
    ("Samir Halilović", 10050),
    ("Hasida Halilović", 8025),
    ("Haris Halilović", 6075),
]

if __name__ == "__main__":
    cursor = conn.cursor()
    for name, balance in cursor.execute("SELECT name, balance FROM accounts WHERE balance > 5000 ORDER BY name"):
        print(name, balance, sep=": ")

