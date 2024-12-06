import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Users')

cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')

for i in range(1, 11):
    agei = i*10
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"Users{i}", f"example{i}gmail.com",f"{agei}", "1000"))

cursor.execute("UPDATE Users SET balance = 500 WHERE MOD(ID, 2) = 0")

cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
results = cursor.fetchall()

for username, email, age, balance in results:
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

if total_users !=0:
    average_balance = all_balances / total_users
else: average_balance = 0

print(average_balance)

connection.commit()
connection.close()
