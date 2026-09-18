from flask import Flask, request, render_template, redirect
from model.todo_db import TodoDB

app = Flask(__name__)
todo_db = TodoDB()

@app.route("/")
def home():
    tasks = todo_db.get()
    print(tasks)
    return render_template("task.html", tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    todo_db.add(title)
    return redirect("/")


@app.route('/complete/<int:todo_index>', methods=['PATCH'])
def complete_task(todo_index):
    print(f'index : {todo_index}')
    todo_db.completed(todo_index)
    return "", 200


@app.route('/delete/<int:todo_index>', methods=['DELETE'])
def delete_task(todo_index):
    todo_db.remove(todo_index)
    return "", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
