from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data in-memory (replace with a database for production)
tasks = [
    {'id': 1, 'title': 'Task 1', 'description': 'Description of Task 1', 'done': False},
    {'id': 2, 'title': 'Task 2', 'description': 'Description of Task 2', 'done': True}
]

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# GET a specific task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if task:
        return jsonify({'task': task[0]})
    else:
        return jsonify({'error': 'Task not found'}), 404

# POST a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.get_json()
    if not new_task:
        return jsonify({'error': 'Invalid request'}), 400
    new_task['id'] = len(tasks) + 1  # Assign a unique ID
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
