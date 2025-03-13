import datetime
from xmlrpc.client import DateTime

from flask import Flask
from data import db_session
from data.jobs import Jobs
from data.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'k0ki4_176'


def main():
    db_session.global_init("db/blogs.db")
    add_capitan()
    # app.run()

def add_capitan():
    user = User()

    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.speciality = "research engineer"
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    user.hashed_password = 'capitan'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

def first_job():
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.start_date = datetime.datetime.now()
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()