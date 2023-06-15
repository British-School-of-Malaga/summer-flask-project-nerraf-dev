# Function 1: Add Task Functionality - Walkthrough

1. Open the `app.py` file in your Replit project.
2. Locate the `add_task()` function, which is currently empty.
3. Inside the function, retrieve the task data from the form submitted by the user. You can use the `request.form['task']` syntax to access the value of the 'task' field.
4. To store the task in a text file, you need to open the file in append mode and write the task to it. Here's an example code snippet you can use:

   ```python
   with open('tasks.txt', 'a') as file:
       file.write(task + '\n')
   ```

   This code opens the `tasks.txt` file in append mode and writes the task followed by a newline character (`\n`).

   **Comment your code!**

6. After storing the task, redirect the user to the **Task Added** confirmation page using the `redirect()` function. You can use the following code:

   ```python
   return redirect('/task_added')
   ```

   This code redirects the user to the `/task_added` route, which will display the confirmation page.

7. Test the functionality by running the application and submitting a task through the input form on the home page. Verify that the task is successfully stored in the `tasks.txt` file and that the user is redirected to the confirmation page.

---
