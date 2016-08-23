import sys

if 'test' in sys.argv:
    DATABASE_URI = 'sqlite:///:memory:'
else:
    DATABASE_URI = 'sqlite:///../../test.db'
