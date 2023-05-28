from flask import Flask, jsonify, request # Импортируем класс Flask для создания объекта-приложения
from task_controller import tasks, task_creation, task_delete, task_update, get_task

app = Flask(__name__)

client = app.test_client()

@app.route('/task', methods=['GET'])
def get_list():
    tasks_json = list(map(lambda x: x.get_dict(), tasks))
    return jsonify(tasks_json)


@app.route('/task', methods=['POST'])
def append_to_list():
    with app.app_context():
        new_task = request.json
        tasks.append(new_task)
        return jsonify(tasks)


@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    with app.app_context():
        params = request.json
        task_update(task_id, params)
        return '204'


@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    with app.app_context():
        try:
            task_delete(task_id)
            return '', 204
        except Exception:
            return {'message': 'Task with given id is not found'}, 404
    
    
if __name__ == "__main__":
    app.run(debug=True)
    # print(get_list())