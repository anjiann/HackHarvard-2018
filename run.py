#run.py

from app import app

#we need to set the FLASK_APP env var to run.py, so that we can
#run our app using our run.py file

if __name__ == '__main__':
    app.run()