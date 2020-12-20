import os
import jwt
import datetime
import uuid
class config:
    SECRETE_KEY=os.environ.get('SECRETE_KEY') or'you-will-never-guess'
    API_KEY=os.environ.get('API_KEY')or'6961d7333843f1a7c280ffda57c5f3'
#def uuid4():
    """Generate a random api_key."""
    #return UUID(bytes=os.urandom(16)), version==4

#print(uuid.uuid4().hex[2:])
