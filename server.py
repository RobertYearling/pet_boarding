from flaskapp import app
from flaskapp.controllers import controllers_users, controllers_pets

if __name__=="__main__":
    app.run(debug=True)