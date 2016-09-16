#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Describe model of user.

Model of user, that gives posibility of using CRUD queries for user.

"""

from ORM import Driver


class UserModel(Driver):
    """Give posibility of using CRUD queries for user.

    UserModel extends Driver methods.

    Instance variables: table_name.

    Public methods: connect_to_db, insert_user,
    select_user, update_user, delete_user.

    """

    def __init__(self):
        """Initialize variable and object."""
        self.table_name = "Test"
        self.DB = Driver()

    def insert_user(self, columns, vals):
        """Insert records into user table."""
        print "Inserting"
        self.DB.insert(self.table_name, columns, vals)

    def select_user(self, columns):
        """Read user records."""
        print "Reading"
        print self.DB.select(self.table_name, columns)

    def update_user(self, changes, condition):
        """Update user records."""
        print "Updating"
        self.DB.update(self.table_name, changes, condition)

    def delete_user(self, condition):
        """Delete user."""
        print "Deleting"
        self.DB.delete(self.table_name, condition)

if __name__ == '__main__':

    User = UserModel()

    User.insert_user(('fullName', 'email', 'password', 'avatar',
                     'isActive', 'role_id'), ('Oleg', 'naumleg@urk.net',
                     'Hero', 'Uleshka', 1, 2))

    User.insert_user(('fullName', 'email', 'password', 'avatar',
                     'isActive', 'role_id'), ('Denis', 'dendendeneg@urk.net',
                     'Heron', 'Hellhbd', 1, 2))

    User.select_user(('email', 'password'))

    User.update_user('avatar = "Duda"', 'fullName = "Oleg"')

    # User.delete_user('password = "hahaha"')
