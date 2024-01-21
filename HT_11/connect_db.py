import sqlite3
import os


current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)


class ConnectDB:
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
        for note in notes_data:
            self.cursor.execute("SELECT * FROM atm_notes WHERE denomination = ?", (note[0],))
            if self.cursor.fetchone() is None:
                self.cursor.execute('INSERT OR IGNORE INTO atm_notes (denomination, quantity) VALUES (?, ?)', note)
                self.conn.commit()
    
    def initialize_admin(self):
        self.cursor.execute("SELECT * FROM users WHERE username = ?", ('admin',))
        if self.cursor.fetchone() is None:
            self.cursor.execute("INSERT OR IGNORE INTO users (username, password, is_cashier) VALUES (?, ?, ?)",
                                ('admin', 'admin', 1))
            self.conn.commit()

    def current_notes(self):
        self.cursor.execute("SELECT denomination,quantity FROM atm_notes")
        return self.cursor.fetchall()

    def check_user(self,user_data):
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (user_data[0], user_data[-1]))
        user = self.cursor.fetchone()
        if user is not None:
            return True
        else:
            return False
    
    def register_user(self,user_data,balance):
        try:
            if len(user_data) == 2:
                self.cursor.execute("INSERT INTO users (username, password, balance) VALUES (?, ?, ?)",
                                    (user_data[0], user_data[-1], balance))
                self.conn.commit()
                return "Все чудово ви зареєстровані"
            else:
                return "Немає паролю"
        except sqlite3.IntegrityError as e:
            return f"Виникла помилка {e}"
    
    def current_balance(self,user):
        self.cursor.execute("SELECT balance FROM users WHERE username=? ", (user[0],))
        return (self.cursor.fetchone())[0]
    
    def update_balance_withdraw(self, user, withdraw):
        new_balance = self.current_balance(user) - withdraw
        self.cursor.execute('UPDATE users SET balance = ? WHERE username = ?', (new_balance, user[0]))
        self.conn.commit()
    
    def update_balance_deposit(self,user,deposit):
        new_balance = self.current_balance(user) + deposit
        self.cursor.execute('UPDATE users SET balance = ? WHERE username = ?', (new_balance, user[0]))
        self.conn.commit()

    def check_user_login(self,user_data):
        self.cursor.execute("SELECT * FROM users WHERE username=? ", (user_data,))
        user = self.cursor.fetchone()
        if user is not None:
            return True
        else:
            return False
    
    def update_notes(self,notes,make:bool):
        if make:
            for note in notes:
                self.cursor.execute("SELECT quantity FROM atm_notes WHERE denomination=? ", (note[0],))
                quantity = (self.cursor.fetchone())[0]
                new_quantity = quantity + int(note[-1])
                self.cursor.execute('UPDATE atm_notes SET quantity = ? WHERE denomination = ?', (new_quantity, note[0]))
                self.conn.commit()
        else:
            check_note = []
            for note in notes:
                self.cursor.execute("SELECT quantity FROM atm_notes WHERE denomination=? ", (note[0],))
                quantity = (self.cursor.fetchone())[0]
                if quantity >= int(note[-1]):
                    check_note.append(False)
                else:
                    check_note.append(True)
            if True in check_note:
                return "Коштів недостатньо"
       
            for note in notes:
                self.cursor.execute("SELECT quantity FROM atm_notes WHERE denomination=? ", (note[0],))
                quantity = (self.cursor.fetchone())[0]
                new_quantity = quantity - int(note[-1])
                self.cursor.execute('UPDATE atm_notes SET quantity = ? WHERE denomination = ?', (new_quantity, note[0]))
                self.conn.commit()



connectdb = ConnectDB()