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

    def get_all_following(self,id):
        self.cursor.execute("""
        SELECT username, user_id 
        FROM user_table JOIN following_table
        ON user_table.user_id = following_table.followee_id
        WHERE follower_id = %s""", (id,))
        return self.cursor.fetchall()

    def get_all_spots_from_id(self,id):
        self.cursor.execute("SELECT * FROM spit WHERE user_id = %s", (id,))
        return self.cursor.fetchall()

    # TODO: Debate wether this should just be ID, or all
    def get_all_spots_by_tag(self, tag_name):
        self.cursor.execute("""
        SELECT spot.spot_id FROM spot
        JOIN spot_tags_relation
        ON spot.spot_id = spot_tags_relation.spot_id
        WHERE tag_name = %s
        """, (tag_name, ))
        return self.cursor.fetchall()

    def get_reviews_from_user(self, id):
        self.cursor.execute("SELECT * FROM review WHERE user_id = %s", (id,))
        return self.cursor.fetchall()

def some_function(id: int=666):
    return {"Message": f"This is a test/placeholder function id: {id}"}


def login():
    return some_function()


def register():
    pass


hander = DBHandler()
hander.connect()
print(hander.get_all_spots_by_tag("Urban"))
hander.disconnect()
