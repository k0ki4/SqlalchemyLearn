import datetime

from flask import Flask
from data import db_session
from data.jobs import Jobs
from data.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'k0ki4_176'


def main():
    name_db = input()
    db_session.global_init(name_db)
    # add_capitan()
    # first_job()
    # get_users()
    # add_capitan_2()
    # query_3()
    app.run(debug=True)


def get_users():
    session = db_session.create_session()
    for i in session.query(User).filter(User.address == 'module_1'):
        print(i)
    session.commit()

def query_2():
    session = db_session.create_session()
    for us in session.query(User).filter(User.address == 'module_1',
                                        'engineer' not in User.speciality,
                                        'engineer' not in User.position):
        print(us.id)
    session.commit()

def query_3():
    session = db_session.create_session()
    for us in session.query(User).filter(User.age < 18):
        print(f"{us} " + f"{us.age} " + "years")
    session.commit()


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

def add_capitan_2():
    user = User()

    user.surname = "K0k"
    user.name = "Ridley"
    user.age = 17
    user.speciality = "research"
    user.address = 'module_1'
    user.email = 'scott_chief@marsian.ru'
    user.hashed_password = 'bot'
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
