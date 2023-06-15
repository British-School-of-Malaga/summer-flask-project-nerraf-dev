To modify the program to display tasks on the home page and show a message when there are no tasks, you can follow these steps:

1. Open the `app.py` file in your code editor.

2. Locate the `home()` function.

3. Modify the function to read the tasks from the text file and pass them to the `index.html` template. Here's an example code snippet:

   ```python
   @app.route('/')
   def home():
       with open('tasks.txt', 'r') as file:
           tasks = file.read().splitlines()

       if not tasks:
           tasks = ['Nothing to do!']

       return render_template('index.html', tasks=tasks)
   ```

   This code reads the tasks from the `tasks.txt` file and stores them in the `tasks` list. If the list is empty, a single task with the message "Nothing to do!" is added. The `tasks` list is then passed as a variable to the `index.html` template.

4. Open the `index.html` template.

5. Modify the template to display the tasks dynamically and show the "Nothing to do!" message if there are no tasks. Here's an example code snippet:

   ```html
   <!-- index.html -->

   <!DOCTYPE html>
   <html>
     <head>
       <title>Todo List</title>
     </head>
     <body>
       <h1>Todo List</h1>
       {% if tasks %}
         <ul>
           {% for task in tasks %}
           <li>{{ task }}</li>
           {% endfor %}
         </ul>
       {% else %}
         <p>Nothing to do!</p>
       {% endif %}
     </body>
   </html>
   ```

   This code uses the `{% if %}` statement to check if there are tasks in the `tasks` list. If there are tasks, they are displayed as list items (`<li>`). If there are no tasks, the message "Nothing to do!" is displayed as a paragraph (`<p>`).

With these changes, when a user visits the home page, the tasks will be displayed dynamically. If there are no tasks, the message "Nothing to do!" will be shown. Students can implement these modifications as an extension task to enhance the functionality of the application.

Remember to test the modified program by running the application and verifying that the tasks are displayed correctly on the home page, including the "Nothing to do!" message when there are no tasks.