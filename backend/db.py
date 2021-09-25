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


class NotFoundError(Exception):
    pass


class NotAuthorizedError(Exception):
    pass


class InternalServerError(Exception):
    pass


def some_function(id: int=666):
    return {"Message": f"This is a test/placeholder function id: {id}"}


def login():
    return some_function()


def register():
    pass
