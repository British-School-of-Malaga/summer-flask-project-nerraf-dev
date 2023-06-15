from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Initial route to display the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle task submission
@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    # Code to add the task to the text file goes here
    return redirect('/task_added')

# Route to display the task added confirmation page
@app.route('/task_added')
def task_added():
    return render_template('task_added.html')

# Route to display the list of tasks
@app.route('/tasks')
def tasks():
    # Code to read tasks from the text file and pass them to the template goes here
    return render_template('tasks.html')

if __name__ == '__main__':
    app.run(debug=True)
