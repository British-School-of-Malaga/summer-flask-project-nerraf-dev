# Step 2: Function Development

In this task, you will focus on implementing the different functions of the todo list application. Each function will add specific functionality to the application and contribute to its overall behavior. Remember to refer to the project goals and the skeleton code we discussed in Lesson 1.

## Function 1: Add Task Functionality

The first function you will work on is the **Add Task** functionality. This function will handle the submission of tasks and store them in a text file. Follow these steps to implement it:

1. Open the `main.py` file in your Replit project.
2. Locate the `add_task()` function, which is currently empty.
3. Inside the function, retrieve the task data from the form submitted by the user. You can use the `request.form['task']` syntax to access the value of the 'task' field.
4. Write the code to store the task in a text file. You can use file handling techniques to append the task to the file, ensuring each task is on a new line.
5. After storing the task, redirect the user to the **Task Added** confirmation page using the `redirect()` function.

The steps seem ok until step 4. What does step 4 mean? *Write the code*...

Remember in the goals it says you are to implement a text file storage method. For this functionm you have already been provided the code that retrieves the content of the input box from the html form you will create later.

```python
task = request.form['task']
```

The variable `task` will hold the string form the form. 
Your task is to write the value to a text file called `tasks.txt`.

### Your turn...

Try to complete this task based on your existing knowledge of file handling in python.

If you get stuck you can click [here](task2a.md) to follow the steps.

## Function 2: Display Tasks Functionality

The second function you will work on is the **Display Tasks** functionality. This function will retrieve the tasks from the text file and display them on the home page. Follow these steps to implement it:

1. Locate the `tasks()` function in `main.py`.
2. Inside the function, write the code to read the tasks from the text file. You can use file handling techniques to read the lines from the file and store them in a list.
3. Pass the list of tasks to the template that renders the home page.
4. Modify the template (index.html) to display the tasks dynamically. You can use Jinja templating syntax to iterate over the task list and display each task in an appropriate format.


If you get stuck you can click [here](task2b.md) to follow the steps.


