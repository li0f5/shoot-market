import mysql.connector

class MariaDB:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def execute(self, query, params=None):
        if params is None:
            params = ()
        self.cursor.execute(query, params)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

''''
come richiamarlo in altri programmi

# crea una istanza di MariaDB
db = MariaDB(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# esegue una query
db.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

# Commit al database
db.commit()

# chiude la connessione con il database
db.close()

'''