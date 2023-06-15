# Additional Functions

Once you have implemented the main functions, you can explore additional functionality to enhance the application:

- **Mark Task Complete:** Implement a function that allows users to mark tasks as complete. This function should update the status of a task in the text file and reflect the change on the home page.
- **Delete Task:** Implement a function to delete tasks from the list. This function should remove the task from the text file and update the task list displayed on the home page.
- **Date and Time Stamps:** Enhance the application by adding date and time stamps to the tasks. Modify the add task function to include the current date and time when storing the task in the text file. Display the timestamp alongside each task on the home page.

Remember to test each function after implementation and make any necessary adjustments. Feel free to refer to the Flask documentation and other resources to help you with the implementation.

---

To implement the additional features of marking a task as complete, deleting a task, and adding date and time stamps, you can follow these steps:

**Mark Task Complete:**

1. In the `index.html` template, add a checkbox next to each task to allow users to mark tasks as complete. Modify the `<li>` element to include the checkbox:

   ```html
   <li>
     <input type="checkbox" name="task_complete">
     {{ task }}
   </li>
   ```

2. Update the `add_task()` function in the `app.py` file to handle the task completion. Modify the code as follows:

   ```python
   @app.route('/add_task', methods=['POST'])
   def add_task():
       task = request.form['task']
       completed = False  # Default value for task completion

       # Code to add the task and its completion status to the text file goes here

       return redirect('/task_added')
   ```

   In this code, a variable `completed` is added to store the completion status of the task. By default, it is set to `False`.

**Delete Task:**

1. In the `index.html` template, add a delete button next to each task to allow users to delete tasks. Modify the `<li>` element to include the button:

   ```html
   <li>
     <input type="checkbox" name="task_complete">
     {{ task }}
     <button name="delete_task">Delete</button>
   </li>
   ```

2. Update the `add_task()` function in the `app.py` file to handle task deletion. Modify the code as follows:

   ```python
   @app.route('/add_task', methods=['POST'])
   def add_task():
       task = request.form['task']
       completed = False  # Default value for task completion

       if 'delete_task' in request.form:
           # Code to delete the task from the text file goes here
           pass
       else:
           # Code to add the task and its completion status to the text file goes here
           pass

       return redirect('/task_added')
   ```

   In this code, a conditional statement checks if the "Delete" button was clicked. If it was, the code to delete the task from the text file can be added.

**Date and Time Stamps:**

1. Update the `add_task()` function in the `app.py` file to include date and time stamps for each task. Modify the code as follows:

   ```python
   from datetime import datetime

   @app.route('/add_task', methods=['POST'])
   def add_task():
       task = request.form['task']
       completed = False  # Default value for task completion
       timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current date and time

       # Code to add the task, its completion status, and timestamp to the text file goes here

       return redirect('/task_added')
   ```

   This code imports the `datetime` module and retrieves the current date and time using `datetime.now()`. The `strftime()` method is used to format the timestamp string according to the desired format.

With these changes, you have implemented the ability to mark tasks as complete, delete tasks, and include date and time stamps for each task. Students can implement these features by modifying the HTML template and updating the `add_task()` function accordingly.

Need help....

Here's a guide (not a solution...some steps) for students who need extra support in implementing the additional features of marking a task as complete, deleting a task, and adding date and time stamps:

**Guide: Implementing Additional Features**

1. **Mark Task Complete:**

   - In the `index.html` template, add a checkbox next to each task using the `<input>` element with the `type="checkbox"` attribute.
   - In the `add_task()` function in the `app.py` file, retrieve the value of the checkbox for each task using `request.form['task_complete']`.
   - Update the code inside the `add_task()` function to handle the task completion based on the checkbox values. You can use a conditional statement to determine whether the checkbox is selected or not.

2. **Delete Task:**

   - In the `index.html` template, add a delete button next to each task using the `<button>` element with an appropriate name attribute, such as `name="delete_task"`.
   - In the `add_task()` function in the `app.py` file, check if the delete button was clicked using `if 'delete_task' in request.form`.
   - Implement the code to delete the selected task from the text file inside the conditional statement.

3. **Date and Time Stamps:**

   - In the `add_task()` function in the `app.py` file, import the `datetime` module using `from datetime import datetime`.
   - Use the `datetime.now()` function to retrieve the current date and time.
   - Format the timestamp string using the `strftime()` method, specifying the desired format. For example, `%Y-%m-%d %H:%M:%S` represents the year, month, day, hour, minute, and second.
   - Modify the code inside the `add_task()` function to include the timestamp along with the task and completion status when writing them to the text file.

Refer to the provided code examples and make use of resources like the Python documentation or online tutorials for further guidance on specific aspects of these features. Test their code regularly and seek help from me or your peers whenever you encounter difficulties.