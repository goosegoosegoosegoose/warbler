import os
from unittest import TestCase
from models import db, User, Message

os.environ['DATABASE_URL'] = "postgresql:///warbler_test"

from app import app, CURR_USER_KEY

db.drop_all()
db.create_all()

class WarblerTestCase(TestCase):
    def 