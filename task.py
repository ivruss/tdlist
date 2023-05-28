from status import Task_status, statuses

class Task:
    def __init__(self, id, task, note, status_id, deadline):
        self.id = id
        self.task = task
        self.note = note
        self.status = Task_status(status_id)
        self.deadline = deadline
    
    def get_dict(self):
        return {
            'id': self.id,
            'task': self.task,
            'note': self.note,
            'status': statuses[self.status.status_id],
            'deadline': self.deadline
        }
        
    def __repr__(self):
        return f'id:{self.id}, task:{self.task}, note:{self.note}, status:{statuses[self.status.status_id]}, deadline:{self.deadline}'