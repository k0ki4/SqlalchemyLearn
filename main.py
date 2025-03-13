from flask import Flask
from data import db_session
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


if __name__ == '__main__':
    main()