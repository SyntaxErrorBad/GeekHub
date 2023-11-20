# -*- coding: utf-8 -*-
import sqlite3
import os


current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)

# conn = sqlite3.connect(os.path.join(parent_directory,'bank_atm.db'))
# cursor = conn.cursor()


class DBConnect:
    def __init__(self) -> None:
        self.conn = sqlite3.connect(os.path.join(parent_directory, 'bank_atm.db'))
        self.cursor = self.conn.cursor()
        self.create_db()
        self.initialize_atm()
        self.initialize_admin()

    def create_db(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                balance INTEGER,
                is_cashier INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()
    
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS atm_notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                denomination INTEGER,
                quantity INTEGER
            )
        ''')
        self.conn.commit()

    def initialize_atm(self):
        notes_data = [
            (10, 100),
            (20, 100),
            (50, 100),
            (100, 100),
            (200, 100),
            (500, 100),
            (1000, 100)
        ]
        # self.cursor.executemany('INSERT OR IGNORE INTO atm_notes (denomination, quantity) VALUES (?, ?)', notes_data)
        # self.conn.commit()
        for note in notes_data:
            self.cursor.execute("SELECT * FROM atm_notes WHERE denomination = ?", (note[0],))
            if self.cursor.fetchone() is None:
                self.cursor.execute('INSERT OR IGNORE INTO atm_notes (denomination, quantity) VALUES (?, ?)', note)

    def take_notes(self):
        self.cursor.execute("SELECT denomination,quantity FROM atm_notes")
        return self.cursor.fetchall()

    def update_notes(self, notes, action):
        if action == "зняти":
            for note in notes:
                self.cursor.execute("SELECT quantity FROM atm_notes WHERE denomination=? ", (note[0],))
                quantity = (self.cursor.fetchone())[0]
                new_quantity = quantity - int(note[-1])
                self.cursor.execute('UPDATE atm_notes SET quantity = ? WHERE denomination = ?', (new_quantity, note[0]))
                self.conn.commit()
        else:
            for note in notes:
                self.cursor.execute("SELECT quantity FROM atm_notes WHERE denomination=? ", (note[0],))
                quantity = (self.cursor.fetchone())[0]
                new_quantity = quantity + int(note[-1])
                self.cursor.execute('UPDATE atm_notes SET quantity = ? WHERE denomination = ?', (new_quantity, note[0]))
                self.conn.commit()

    def initialize_admin(self):
        self.cursor.execute("SELECT * FROM users WHERE username = ?", ('admin',))
        if self.cursor.fetchone() is None:
            self.cursor.execute("INSERT OR IGNORE INTO users (username, password, is_cashier) VALUES (?, ?, ?)",
                                ('admin', 'admin', 1))
            self.conn.commit()

    def add_user(self, username, password, balance):
        try:
            self.cursor.execute("INSERT INTO users (username, password, balance) VALUES (?, ?, ?)",
                                (username, password, balance))
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Ошибка {e}")

    def check_balance(self, username):
        self.cursor.execute("SELECT balance FROM users WHERE username=? ", (username,))
        return (self.cursor.fetchone())[0]

    def update_balance(self, user, withdraw, action, note):
        if action == "зняти":
            new_balance = self.check_balance(user) - withdraw
            self.cursor.execute('UPDATE users SET balance = ? WHERE username = ?', (new_balance, user))
            self.conn.commit()
            self.update_notes(note, action)
        else:
            new_balance = self.check_balance(user) + withdraw
            self.cursor.execute('UPDATE users SET balance = ? WHERE username = ?', (new_balance, user))
            self.conn.commit()
            self.update_notes(note, action)

    def login_valid_user(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = self.cursor.fetchone()
        if user is not None:
            return True, user[1], user[-1]
        else:
            return False, None, None


connectDB = DBConnect()
