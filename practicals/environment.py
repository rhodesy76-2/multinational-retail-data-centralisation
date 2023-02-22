# import os
# for key in os.environ:
#    print(os.environ[key])

import os

# Set environment variables
os.environ['API_USER'] = 'username'
os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')

print(USER)
print(PASSWORD)

