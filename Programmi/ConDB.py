import mysql.connector

class MariaDB:
    def __init__(self, optional_host="195.231.112.144", optional_user="host", optional_password="host", optional_database="ShotMarket"):
        if optional_host is None or optional_user is None or optional_password is None or optional_database is None:
            self.host = "195.231.112.144"
            self.user = "host"
            self.password = "host"
            self.database = "ShotMarket"
        else:
            self.host = optional_host
            self.user = optional_user
            self.password = optional_password
            self.database = optional_database
        self.conn = mysql.connector.connect(
            host=optional_host,
            user=optional_user,
            password=optional_password,
            database=optional_database
        )
        self.cursor = self.conn.cursor()

    def execute(self, query, params=None):
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def getHost(self):
        return self.host

    def getUser(self):
        return self.user

    def getPassword(self):
        return self.password

    def getDatabase(self):
        return self.database

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