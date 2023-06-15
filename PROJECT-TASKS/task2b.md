## Function 2: Display Tasks Functionality - Walkthrough

1. Locate the `tasks()` function in `app.py`.
2. Inside the function, write the code to read the tasks from the text file. You can use file handling techniques to read the lines from the file and store them in a list. Here's an example code snippet:

   ```python
   with open('tasks.txt', 'r') as file:
       tasks = file.read().splitlines()
   ```

   This code opens the `tasks.txt` file in read mode and uses the `read()` method to retrieve its content as a single string. Then, the `splitlines()` method is used to split the string into a list of tasks, with each task as a separate item.

3. Pass the list of tasks to the template that renders the home page. You can do this by adding the tasks as a parameter when rendering the template. Here's an example code snippet:

   ```python
   return render_template('index.html', tasks=tasks)
   ```

   This code passes the `tasks` list as the `tasks` variable to the `index.html` template.

4. Modify the template (`index.html`) to display the tasks dynamically. You can use Jinja templating syntax to iterate over the task list and display each task in an appropriate format. Here's an example code snippet:

   ```html
   {% for task in tasks %}
   <p>{{ task }}</p>
   {% endfor %}
   ```

   This code uses the `{% for %}` loop to iterate over each task in the `tasks` list and displays it as a paragraph (`<p>`) element.

5. Test the functionality by running the application and verifying that the tasks stored in the `tasks.txt` file are displayed on the home page.

---
