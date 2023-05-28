from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:superuser1604@localhost/to_do_list_db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)


class User_task_ids(db.Model):
    __tablename__ = 'user_task_ids'
    bond_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    task_id = db.Column(db.Integer)
    
    def __repr__(self):
        return str(self.task_id)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique = True)
    
    def __repr__(self):
        return f'<User: {self.name}'


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    containment = db.Column(db.String(200))
    deadline = db.Column(db.String(20))
    
    def __repr__(self):
        return f"""
    **{self.id}**
    <{self.containment}> - содержание

    <{self.deadline}> - дата выполнения
    """


def user_log_in():
    username = str(input('Введите имя пользователя '))
    
    print("""
Примечание: если имя пользователя не существует, будет создана новая учётная запись
        """)
    
    if username == 'Admin':
        with app.app_context():
            print('User_list:', User.query.all())
            
            print('Task_list:', Task.query.all())
        
    else:
        with app.app_context():
            if (db.session.query(User).filter_by(name=username).all()):
                print(f'Пользователь {db.session.query(User).filter_by(name=username).first().name}, вход успешен')

                return db.session.query(User).filter_by(name=username).first().id
    
            else:
                with app.app_context():
                    user = User(name=username)
                    db.session.add(user)
                    db.session.commit()


def task_adding():
    task_containment = str(input('Введите содержание задачи '))
    task_deadline = str(input('Введите дату завершения задачи в формате ДД:ММ:ГГ '))
    
    with app.app_context():
        task = Task(containment = task_containment, deadline = task_deadline)
        db.session.add(task)
        db.session.commit()
        
    with app.app_context():
        return db.session.query(Task).filter_by(containment = task_containment, deadline = task_deadline).first().id
    

def task_changing(task_id, task_containment):
    with app.app_context():
        task = Task.query.filter_by(id = task_id).first()
        task.containment = task_containment
        db.session.commit()
     
    
def userid_to_taskid_bond_creation(local_task_id, local_user_id):
    with app.app_context():
        bond = User_task_ids(user_id = local_user_id, task_id = local_task_id)
        db.session.add(bond)
        db.session.commit()
        
        
def task_delete(task_id_input):
    with app.app_context():
        task = Task.query.filter_by(id = task_id_input).first()
        db.session.delete(task)
        db.session.commit()
    
     
def main():
    id = user_log_in()
    if id:
        usercommand = int(input('Введите 1 для чтения всех задач, 2 для их добавления, 3 для изменения, 4 для удаления '))
        if usercommand == 1:
            with app.app_context():
                for user_id_local in db.session.query(User_task_ids).filter_by(user_id=id).all():
                    print(db.session.query(Task).filter_by(id=int(str(user_id_local))).first())
        elif usercommand == 2:
            task_id = task_adding()
            userid_to_taskid_bond_creation(task_id, id)
        elif usercommand == 3:
            task_id = input('Введите номер задачи ')
            task_containment = input('Введите новое желаемое содержание ')
            task_changing(task_id, task_containment)
        elif usercommand == 4:
            task_id = input('Введите номер задачи ')
            task_delete(task_id)


if __name__ == '__main__':
    main()

    