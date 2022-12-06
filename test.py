import unittest

from config import *


class TestCase(unittest.TestCase):
    with app.app_context():
        u1 = User(username='john', password = 'ekanshgupta1!')
        u2 = User(username='susan', password = 'ekanshgupta1!')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        u = u1.follow(u2)
        db.session.add(u)
        db.session.commit()
        assert u1.followed.count() == 9

if __name__ == '__main__':
    unittest.main()
        
