from flaskapp import app
from flaskapp.controllers import controllers_users, controllers_pets

if __name__=="__main__":
    app.run(debug=True)


# from server import app as application
# if __name__ == "__main__":
#     application.run()

# [Unit]
# Description=Gunicorn instance
# After=network.target
# [Service]
# User=ubuntu
# Group=www-data
# WorkingDirectory=/home/ubuntu/pet_boarding
# Environment="PATH=/home/ubuntu/pet_boarding/venv/bin"
# ExecStart=/home/ubuntu/pet_boarding/venv/bin/gunicorn --workers 3 --bind unix:pet_boarding.sock -m 007 wsgi:application
# [Install]
# WantedBy=multi-user.target