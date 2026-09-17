from flask import Flask, request, render_template, redirect
from model.todo_db import TodoDB

app = Flask(__name__)
todo_db = TodoDB()
cache_list = []

@app.route("/")
def home():
    global cache_list
    tasks = todo_db.get()
    print(tasks)
    cache_list = tasks
    print(cache_list)
    return render_template("task.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    todo_db.add(title)
    return redirect('/')

@app.route('/complete/<int:index>')
def complete_task(index):
    print(f'index : {index}')
    todo_index = cache_list[index][0]
    todo_db.completed(todo_index)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_task(index):
    todo_index = cache_list[index][0]
    todo_db.remove(todo_index)
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
