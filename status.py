statuses = [
    'started', 'paused', 'in progress', 'completed'
]

class Task_status():
    def __init__(self, id):
        self.status_id = id
    
    def __repr__(self):
        return statuses[self.status_id]
