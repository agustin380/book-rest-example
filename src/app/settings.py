import sys

# Database
if 'test' in sys.argv:
    DATABASE_URI = 'sqlite:///:memory:'
else:
    DATABASE_URI = 'sqlite:///../../test.db'

# Logging
LOG_FILE_LOCATION = 'app.log'
LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s '
