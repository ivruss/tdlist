# import os
# print(os.getcwd())
from task import Task

tasks = []

id = 0

def task_creation(task, note, status, deadline):
    global id
    new_task = Task(id, task, note, status, deadline)
    tasks.append(new_task)
    id+=1
    return '204'


def task_update(task_id, params):
    item = next((x for x in tasks if x.id == task_id), None)
    if not item:
        return {'message': 'Task with given id is not found'}, 400
    for key in params.keys():
        for value in list(params.values()):
            exec(f'item.{key} = "{value}"')
    return item


def task_delete(task_id):
    task = list(filter(lambda x: x.id == task_id, tasks))[0]
    tasks.pop(tasks.index(task))
    return '204'
    
    
def get_task(task_id):
    task = list(filter(lambda x: x.id == task_id, tasks))[0]
    return task

task_creation(1,1,1,1)
task_creation(2,2,2,2)




    
