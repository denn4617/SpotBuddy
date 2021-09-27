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
from pprint import pprint
from psycopg2.extras import RealDictCursor
import json
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
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

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
        self.connect()
        self.cursor.execute("SELECT * FROM user_table")
        res = self.cursor.fetchall()
        self.disconnect()
        return res

    def get_user_by_id(self, id):
        self.connect()
        self.cursor.execute(
            "SELECT * FROM user_table WHERE user_id = %s", (id,))
        res = self.cursor.fetchone()
        self.disconnect()
        return res

    def get_all_following(self, id):
        self.connect()
        self.cursor.execute("""
            SELECT username, user_id 
            FROM user_table JOIN following_table
            ON user_table.user_id = following_table.followee_id
            WHERE follower_id = %s
        """, (id,))
        res = self.cursor.fetchall()
        return res

    def get_all_spots_from_id(self, id):
        self.connect()
        self.cursor.execute("SELECT * FROM spot WHERE user_id = %s", (id,))
        res = self.cursor.fetchall()
        self.disconnect()
        return res

    # TODO: Debate wether this should just be ID, or all
    def get_all_spots_by_tag(self, tag_name):
        self.connect()
        self.cursor.execute("""
            SELECT spot.spot_id FROM spot
            JOIN spot_tags_relation
            ON spot.spot_id = spot_tags_relation.spot_id
            WHERE tag_name = %s
        """, (tag_name, ))
        res = self.cursor.fetchall()
        self.disconnect()
        return res

    def get_reviews_from_user(self, id):
        self.connect()
        self.cursor.execute("SELECT * FROM review WHERE user_id = %s", (id,))
        res = self.cursor.fetchall()
        self.disconnect()
        return res

    def create_user(self, email, username, hashed_pw):
        self.connect()
        self.cursor.execute("""
            INSERT INTO user_table(
                date_created,
                email,
                username,
                hashed_pw
            ) VALUES (
                now(),
                %s,
                %s,
                %s
            );
        """, (email, username, hashed_pw,))
        self.connection.commit()
        self.disconnect()

    def create_spot(self, longitude, latitude, user_id, is_private=False):
        self.connect()
        self.cursor.execute("""
            INSERT INTO spot(longitude, latitude, user_id, is_private)
            VALUES (%s, %s, %s, %s)
        """, (longitude, latitude, user_id, is_private,))
        self.connection.commit()
        self.disconnect()

    def create_tag(self, tag_name):
        self.connect()
        self.cursor.execute("INSERT INTO tags(tag_name) VALUES (%s)", (tag_name,))
        self.connection.commit()
        self.disconnect()

    def create_review(self, score, user_id, spot_id):
        #TODO: Check score not in range
        self.connect()
        self.cursor.execute("INSERT INTO review(score, user_id, spot_id) VALUES (%s, %s, %s)", (score, user_id, spot_id,))
        self.connection.commit()
        self.disconnect()

    def create_follow(self, follower_id, followee_id):
        self.connect()
        self.cursor.execute("INSERT INTO following_table(follower_id, followee_id) VALUES (%s, %s)", (follower_id, followee_id,))
        self.connection.commit()
        self.disconnect()
    
    def add_tag_to_spot(self,spot_id, tag_name):
        self.connect()
        self.cursor.execute("INSERT INTO spot_tags_relation(spot_id, tag_name) VALUES (%s,%s)", (spot_id,tag_name,))
        self.connection.commit()
        self.disconnect()


def some_function(id: int = 666):
    return {"Message": f"This is a test/placeholder function id: {id}"}


def login():
    return some_function()


def register():
    pass


handler = DBHandler()
if __name__ == "__main__":
    pprint(handler.get_all_users())
    pprint(handler.get_user_by_id(1))
    pprint(handler.get_all_following(1))
    pprint(handler.get_all_spots_from_id(1))
    pprint(handler.get_all_spots_by_tag("Urban"))
    pprint(handler.get_reviews_from_user(1))
