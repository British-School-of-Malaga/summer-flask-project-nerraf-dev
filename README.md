# Todo List Application Project

## Introduction

Welcome to the Todo List Application project! In this project, you will have the opportunity to create a simple yet functional todo list application using Python and Flask. The project is designed to help you practice your web development skills, gain hands-on experience with Flask, and understand the basics of building web applications.

Throughout this project, you will start with a basic implementation where tasks are stored in a text file. You will gradually enhance the application by adding features such as displaying tasks on the home page, including date and time stamps, marking tasks as complete, and enabling task deletion. Additionally, you will have the chance to apply CSS and HTML formatting to make your application visually appealing.

This project will not only strengthen your understanding of web development concepts but also provide a solid foundation for future projects involving databases and advanced functionalities. The skills and knowledge you gain from this project will serve as a valuable building block in your programming journey.

## Project Goals

By the end of this project, you will have accomplished the following:

1. Developed a functioning todo list application using Python and Flask.
2. Implemented text file storage to persist tasks.
3. Displayed tasks on the home page for easy access.
4. Added date and time stamps to track task creation.
5. Enabled marking tasks as complete for task management.
6. Implemented the ability to delete tasks from the list.
7. Applied CSS and HTML formatting to enhance the visual appearance of the application.

## Prerequisites

To make the most out of this project, it is recommended that you have a basic understanding of the following:

- Python programming language
- HTML and CSS fundamentals
- Flask web framework

If you are unfamiliar with any of these topics, don't worry! This project will provide step-by-step instructions, code examples, and resources to help you along the way.

## Getting Started

To get started with this project, you will need to set up your development environment. 

Option 1:
We will be using the online coding platform **replit.com** for this project, which provides a user-friendly interface and allows easy collaboration. Follow the instructions provided in the next section to set up your environment and start coding!

Option 2: Use VS Code <<TO DO!>>


** Read this page carefully! **

The following will explain the skeleton code you have been provided, so read it carefully! Then go to the `tasks` folder

### 1. Skeleton Setup

The skeleton code sets up the basic structure of the Flask application. It includes necessary imports, creates a Flask app instance, and defines different routes using decorators. The @app.route() decorator maps a URL to a specific function that handles the request. The app.run(debug=True) line starts the Flask development server, allowing us to test our application.

#### The Bones

The skeleton code sets up the basic structure of the Flask application. It includes necessary **imports**, **creates a Flask app instance**, and **defines different routes** using _decorators_. The `@app.route()` decorator maps a URL to a specific function that handles the request. The `app.run(debug=True)` line starts the Flask development server, allowing us to test our application.

The initial route is defined using `@app.route('/')`. It maps the root URL ("/") to the home() function. In this function, we use the `render_template()` function to render the HTML template called `index.html`. This template will be displayed as the home page of our application.

```python
@app.route('/')
def home():
    return render_template('index.html')
```

The `/add_task` route is used to handle task submission. It expects a `POST` request, which is triggered when the user submits the task form. The `add_task()` function retrieves the task from the form using `request.form['task']`. We will add the code to store the task in the text file later. Finally, we use `redirect('/task_added')` to **redirect** the user to the task added confirmation page.

```python
@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    # Code to add the task to the text file goes here
    return redirect('/task_added')
```

The `/task_added` route maps to the `task_added()` function. This function renders the HTML template called `task_added.html`. When a task is successfully added, the user will be redirected to this page to see the confirmation message.

```python
@app.route('/task_added')
def task_added():
    return render_template('task_added.html')
```

The `/tasks` route maps to the `tasks()` function. This function will be responsible for retrieving the tasks from the text file and passing them to the HTML template called `tasks.html`. The template will be used to display the list of tasks on a separate page.

```python
@app.route('/tasks')
def tasks():
    # Code to read tasks from the text file and pass them to the template goes here
    return render_template('tasks.html')
```

In order to start working on the project, you need to set up the basic skeleton for our Flask application. Please refer to the separate skeleton file provided to you. Follow the instructions in that file to set up the skeleton of your Flask application. Once you have completed the setup, return to this document to continue with the next steps.

### 2. Create the HTML Templates

Create the HTML templates for the different pages in the folder named **templates**. 

Inside the templates folder, create two HTML files: `index.html` and `task_added.html`. These templates will define the structure and content of the home page and the task added confirmation page, respectively.

In the `index.html` template, add the necessary HTML structure and any placeholders you want for displaying tasks and input fields.

```html
<!-- index.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Todo List</title>
  </head>
  <body>
    <h1>Todo List</h1>
    <!-- Add your HTML content here -->
  </body>
</html>
```

In the `task_added.html` template, add the necessary HTML structure and content for displaying the task added confirmation.

```html
<!-- task_added.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Task Added</title>
  </head>
  <body>
    <h1>Task Added</h1>
    <!-- Add your HTML content here -->
  </body>
</html>
```

Now that we have the skeleton in place, let's start working on the first functionality: adding tasks to the todo list. ...

Head on over to the next project in the unit to begin the coding!

---