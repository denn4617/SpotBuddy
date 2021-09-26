"""
This doc contains:

Functions which are called from the website
and acts as a layer between api and database.
also, Errors which can be raised if the exception
needs to be handled on the api layer

ps. the class some_function(id) is a function to return test data, used for validation.

Needs to be added:
 - class for easy access to db
 - all the features

"""
import psycopg2
from config import config

class NotFoundError(Exception):
    pass


class NotAuthorizedError(Exception):
    pass


class InternalServerError(Exception):
    pass

class DBHandler():
    connection = None
    def connect(self):
        try:
            params = config()
            self.connection = psycopg2.connect(**params)
            self.cursor = self.connection.cursor()
        
        except (Exception) as error:
            print(error)
            self.disconnect()

#         finally:
#             if (self.connection):
#                 self.cursor.close()
#                 self.connection.close()
#                 print("PostgreConnection Closed")
# 
    def disconnect(self):
        if(self.connection):
            self.cursor.close()
            self.connection.close()

    def test_connect(self):
        if (self.connection):
            print("Connection Works")
        else:
            print("Connection Not open, ya idiot")

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM user_table")
        return self.cursor.fetchall()
    
    def get_user_by_id(self,id):
        self.cursor.execute("SELECT * FROM user_table WHERE user_id = %s", (id,))
        return self.cursor.fetchone()

def some_function(id: int=666):
    return {"Message": f"This is a test/placeholder function id: {id}"}


def login():
    return some_function()


def register():
    pass


hander = DBHandler()
hander.connect()
print(hander.get_user_by_id(1))
hander.disconnect()
