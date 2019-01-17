import psycopg2, os
from ConfigParser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # joining the current Directory path to the fileName
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

class dbutils:
    def __init__(self):
        pass

    def createConnection(self):
        """ Connect to the PostgreSQL database server """
        self.conn = None
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**params)
            print 'Sucessfully connected to database....'
        except (Exception, psycopg2.DatabaseError) as error:
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print "Error while connecting to the PostgreSQL database server"
            print(error)
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    def executeQuery(self, query):
        try:
            # create a cursor
            cur = self.conn.cursor()

            # execute a statement
            cur.execute(query)
            data = cur.fetchall()

            # close the communication with the PostgreS
            cur.close()
            return data
        except(Exception) as error:
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print "Error while executing query: '" + query +"'"
            print error
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    def closeConnection(self):
        if self.conn is not None:
            self.conn.close()
            print('Database connection closed.')