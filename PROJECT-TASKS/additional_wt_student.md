# Walkthrough: Adding Additional Features to the Todo List Application

In this walkthrough, we will be adding three additional features to our existing todo list application: marking tasks as complete, deleting tasks, and adding date and time stamps. These features will enhance the functionality of our application and provide users with more control over their tasks.

**Reminder: Check Code Placement**

When implementing the additional features, it is crucial to place the code snippets in the correct locations within the files. Carefully follow the instructions and double-check the placement of your code additions to ensure they are inserted in the right place. Incorrect placement may result in errors or unexpected behavior.

Take the time to review the existing code and identify the appropriate locations to add your code. Pay attention to the specific functions and template sections where the new features should be integrated. Refer to the provided code examples and compare them with your own code to ensure consistency.

Remember to test your application after making each change to ensure that the feature functions as expected. If you encounter any issues, carefully review your code and verify the placement of your additions.

**Step 1: Mark Task Complete**

1. Update the `index.html` template:
   - Open the `templates/index.html` file.
   - Add the following code snippet inside the `<li>` element, just before the task description:
     ```html
     <input type="checkbox" name="task_complete">
     ```
   - This will create a checkbox next to each task.

2. Update the `add_task()` function in the `app.py` file:
   - Open the `app.py` file.
   - In the `add_task()` function, add the following code snippet after retrieving the task description:
     ```python
     completed = True if 'task_complete' in request.form else False
     ```
   - This code checks if the checkbox for marking the task as complete was selected or not.

**Step 2: Delete Task**

1. Update the `index.html` template:
   - Open the `templates/index.html` file.
   - Add the following code snippet inside the `<li>` element, after the task description:
     ```html
     <button name="delete_task">Delete</button>
     ```
   - This will add a delete button next to each task.

2. Update the `add_task()` function in the `app.py` file:
   - Open the `app.py` file.
   - In the `add_task()` function, add the following code snippet after retrieving the task description:
     ```python
     if 'delete_task' in request.form:
         delete_task(task)
     ```
   - This code checks if the delete button for the task was clicked and calls a separate function `delete_task()` to handle the deletion logic.

**Step 3: Date and Time Stamps**

1. Update the `add_task()` function in the `app.py` file:
   - Open the `app.py` file.
   - Import the `datetime` module by adding the following line at the top of the file:
     ```python
     from datetime import datetime
     ```
   - In the `add_task()` function, add the following code snippet after retrieving the task description:
     ```python
     timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
     ```
   - This code retrieves the current date and time and formats it as a timestamp.

   - Modify the code that writes the task to the text file by adding the timestamp. For example:
     ```python
     with open('tasks.txt', 'a') as file:
         file.write(f"{task},{completed},{timestamp}\n")
     ```

**Step 4: Guide Students in Implementing the Features**

1. Provide the updated `app.py` code and the modified `index.html` template to the students.

2. Explain the changes made for each feature, highlighting the code snippets and their placement in the files.

3. Guide the students through the code changes required in the `add_task()` function, explaining the logic behind each change and how it contributes to the feature.

4. Encourage students to test their application after implementing each feature to ensure proper functionality.

**Conclusion**

Congratulations! You have successfully added additional features to your todo list application. Users can now mark tasks as complete, delete tasks, and view the date and time stamps for each task.