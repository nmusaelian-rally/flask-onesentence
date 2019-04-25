'''
uwsgi --ini wsgi.ini -w run
'''
import os
from app.appbase import app

########################################################################################################
########################################################################################################

if __name__ == '__main__':
    print("about to run the app...")
    app.run(port=os.environ['PORT'])