import pymysql

class MariaDB:
    def __init__(self):
        try:
            if self.readConfig():
                self.conn = pymysql.connect(
                    host= self.host,
                    user= self.user,
                    password= self.password,
                    database= self.database,
                    port=3306
                )
                self.cursor = self.conn.cursor()
            else:
                self.readConfig()
                self.conn = pymysql.connect(
                    host= self.host,
                    user= self.user,
                    password= self.password,
                    database= self.database,
                    port=3306
                )
                self.cursor = self.conn.cursor()

        except:
            self.writeConfig("195.231.112.144", "host", "host", "ShotMarket")
            self.__init__()


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

    #funziona che controlla se il file esiste
    def checkFileExists(self):
        try:
            open("config.txt", "r")
            return True
        except:
            return False

    #funzione per scrivere dati collegamento al database su file config.txt
    def writeConfig(self, host, user, password, database):
        file = open("config.txt", "w")
        file.write(host + "\n")
        file.write(user + "\n")
        file.write(password + "\n")
        file.write(database + "\n")
        file.close()


    #funzione per leggere i dati dal file config.txt
    def readConfig(self):
        if not self.checkFileExists():
            self.writeConfig("195.231.112.144", "host", "host", "ShotMarket")
        file = open("config.txt", "r")
        self.host = file.readline().strip()
        self.user = file.readline().strip()
        self.password = file.readline().strip()
        self.database = file.readline().strip()
        file.close()
        return True

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