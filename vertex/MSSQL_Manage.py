import pyodbc
import time

class MSSQLManage(object):

    pyodbc.pooling = False
    _instance = None

    #def db_connect(cls):
    def __new__(cls):
        """db_config = {
            'server': '10.35.10.97',
            'database': 'VertexUserTouhidul',
            'uid': 'sa',
            'pwd': 'SteSysAdmin10#'
        }
        connect_string = 'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={uid};PWD={pwd}'.format(**db_config)
        """
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            db_config = {'DRIVER': '{ODBC Driver 17 for SQL Server}',
                         'SERVER': '10.35.10.97',
                         'UID': 'sa',
                         'PWD': 'SteSysAdmin10#',
                         'Autocommit': True }
            try:
                print('connecting to the database...')
                connection = MSSQLManage._instance.connection = pyodbc.connect(**db_config)
                cursor = MSSQLManage._instance.cursor = connection.cursor()
                cursor.execute('SELECT @@version;')
                db_version = cursor.fetchone()

            except Exception as error:
                print('Error: database connection not successful.')
                #print('Error: database connection not successful. {}'.format(error))
                MSSQLManage._instance = None
            else:
                print('Database connection successful with {}'.format(db_version[0]))
        return cls._instance

    def __init__(self):
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor

    def query(self, sql_query):
        try:
            result = self.cursor.execute(sql_query)
        except pyodbc.ProgrammingError as e:
            print("No results, " + str(e))
            results = None
        except Exception as error:
            print('Executing query "{}", error: {}'.format(sql_query, error))
            return None
        else:
            return result
        """
        finally:
            if self.cursor != None:
                self.cursor.close()
            elif self.connection != None:
                self.connection.close()
        """

    def backup_database(self, databaseName, backupFileName):
        """ please enter first param the databaseName = MSSQL existing Database Name, which you need to create backup file.
            and enter 2nd param the backupFileName as backup file name will be created at location 'C:\\test\\AUTO_DB_BACKUPS\\*.bak',
        :databaseName: 'str'
        :backupFileName: 'str'
        :author: VertexUserTouhidul"""

        if ".bak" in backupFileName.lower():
            backupFileName = backupFileName.split(".")[0]
        else:
            backupFileName = backupFileName
        sql_databases = "SELECT name FROM sys.databases WHERE name NOT IN('master','model','msdb','tempdb')"
        databases = self.query(sql_databases).fetchall()
        if database_name in str(databases):
            #it will replace the backup file, if you want to append the bak file then use option: WITH NOINIT
            sql_backup_stmt = "SET NOCOUNT ON; BACKUP DATABASE {0} TO  DISK = N'C:\\Test\\AUTO_DB_BACKUPS\\{1}.bak' WITH NOFORMAT, INIT, SKIP, NOREWIND, NOUNLOAD;".format(databaseName, backupFileName)
            try:
                self.query(sql_backup_stmt)
            #except pyodbc.ProgrammingError as e:
            #    print("No results, " + str(e))
            #    results = None
            except Exception as e:
                print("Exception:" + str(e))
            else:
                print("Database: {} BACKUP successfully.".format(databaseName))
        else:
            print("Database: {} doesn't exist. Backup can't perform.".format(databaseName))

    def restore_database(self, restore_db_name, backup_file_name):
        if ".bak" in backup_file_name.lower():
            backup_file = backup_file_name.split(".")[0]
        else:
            backup_file = backup_file_name
        sql_restore_stmt ="RESTORE DATABASE {0} FROM DISK = N'C:\\Test\\AUTO_DB_BACKUPS\\{1}.bak' WITH REPLACE, NOUNLOAD, STATS = 20".format(restore_db_name, backup_file)
        print("restore database processing....")
        try:
            #self.delete_database(backup_db_name)
            self.query(sql_restore_stmt)
            time.sleep(30)
            print("Database: {} RESTORE successfully.".format(restore_db_name))
        except Exception as e:
            print("Exception:" + str(e))

    def delete_database(self, databaseName):
        """ Delete Database if exists.
        :type database_name: 'str'"""
        sql_drop_db = "DROP DATABASE IF EXISTS {}".format(databaseName)
        sql_drop_database = """IF EXISTS (SELECT name from sys.databases WHERE (name = '{0}'))
                                BEGIN
                                    ALTER DATABASE {0} SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
                                    DROP DATABASE {0};
                                END;""".format(databaseName)
        #print("drop database stmt: " +sql_drop_database)
        try:
            self.query(sql_drop_db)
            self.query(sql_drop_database)
            time.sleep(5)
        except Exception as e:
            print("Exception:" + str(e))
        else:
            print("Database: {} DELETED successfully.".format(databaseName))

    def find_company(self):
        self.query("USE VertexUserTouhidul")
        sql = "SELECT CmpID, Code, Name FROM [dbo].Company"
        #sql ="SELECT CmpID, Code, Name FROM [VertexUserTouhidul].[dbo].Company"
        rows = self.query(sql).fetchall()
        print("=====Fetching Company data=====")
        for row in rows:
            print(row)
            #print(row.CmpID, row.Code, row.Name)
        print("===============================")

        """
    def show_tables(self):
        self.query("USE VertexUserTouhidul;")
        all_tables = self.cursor.tables()
        print(type(all_tables))
        for row in all_tables:
            print(row.table_name)
        """

    def find_driver(self):
        for driver in pyodbc.drivers():
            print(driver)
            print("pyodbc version:" + pyodbc.version)

    def find_hostname(self):
        hostname = "SELECT @@SERVERNAME AS 'Server Name';"
        result = self.query(hostname).fetchone()
        if result:
            print("hostname:" + str(result))

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        print("Connection closed.")


db = MSSQLManage()
db.find_driver()
db.find_hostname()
db.backup_database("VertexUserTouhidul")
#=================================
db.restore_database("VertexUserTouhidul","test.bak")
#db.find_company()
#db.delete_database("VertexUserTouhidul")
#=================================
#db.show_tables()
#db.db_connect()
# 'DATABASE': 'VertexUserTouhidul',
