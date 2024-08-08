from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) # Initialize Flask

# Initialize task ID counter
task_id_counter = 2

# Placeholder for tasks with unique IDs
todos = [{"id": 0, "task_description": "Buy groceries", "done": False},
         {"id": 1, "task_description": "Read a book", "done": False},
         {"id": 2, "task_description": "Study Flask", "done": False}]

@app.route('/', methods=['GET', 'POST'])
def index():
    global task_id_counter
    if request.method == 'POST':
        task_content = request.form['new_todo']
        if task_content:
            task_id_counter += 1  # Increment ID for each new task
            todos.append({"id": task_id_counter, "task_description": task_content, "done": False})
        return redirect(url_for('index'))
    return render_template('index.html', todos=todos)

if __name__ == '__main__': # Define port, host, and debugging while running
    app.run(host='0.0.0.0', port=8080, debug=True)













# from flask import Flask, render_template, request, redirect, url_for 

# app = Flask(__name__) # Initialize Flask

# # Initialize task ID counter
# task_id_counter = 2

# # Placeholder for tasks with unique IDs
# todos = [{"id": 0, "task_description": "Buy groceries", "done": False},
#          {"id": 1, "task_description": "Read a book", "done": False},
#          {"id": 2, "task_description": "Study Flask", "done": False}]

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     global task_id_counter
#     if request.method == 'POST':
#         task_content = request.form['new_todo']
#         if task_content:
#             task_id_counter += 1  # Increment ID for each new task
#             todos.append({"id": task_id_counter, "task_description": task_content, "done": False})
#         return redirect(url_for('index'))
#     return render_template('index.html', todos=todos)


# app.run(host='0.0.0.0', port=8080, debug=True)
















# from flask import Flask, render_template, request, redirect, url_for 

# app = Flask(__name__) # Initialize Flask

# #Initialize task ID counter
# task_id_counter = 2

# # dummy data <- need to modify
# def get_sample_todos():
#     return [{"id":0,"task_description":"Buy groceries", "done":False},{"id":1, "task_description":"Read a book", "done":False},{"id":2, "task_description":"Study Flask", "done":False}]

# @app.route('/', methods=('GET', 'POST')) # Define route
# def index():  # Define what it would present or do
#     global task_id_counter
#     todos = get_sample_todos()
    
#     task_content=''

#     if request.method == "POST":
#         task_content == request.form['new_todo']
#         if task_content:
#             task_id_counter += 1 # Increment by 1
#             todos.append({"id":task_id_counter, "task_description":task_content, "done":False})
#         return redirect(url_for('index')) #url for - aalamin kung anong  
#     return render_template('index.html', todos=todos)
        

# if __name__ == '__main__': # Define port, host, and debugging while running
#     app.run(debug=True)



# from flask import Flask, render_template, request #import flask

# app = Flask(__name__) # initialize

# # dummy data <-- need to modify
# def get_sample_todos():
#     return [{"id":0,"task_description":"Buy groceries", "done":False},{"id":1, "task_description":"Read a book", "done":False},{"id":2, "task_description":"Study Flask", "done":False}]

# # get kumuha, post gumamit
# #decorator. route is from Flask. / url

# @app.route('/', methods=('GET', 'POST')) # define route , san mapupunta si url
# def index(): # define what it would present or do
#     global task_id_counter

#     if request.method == "POST":
#         task_content == request.form ['new todo']
#         if task_content: 
#             task_id_counter += 1 #increment by 1
#             task.append({})


#     todos = get_sample_todos() # yung todos dito, matatawag sa kabila
#     return render_template ('index.html', todos=todos)

# if __name__=='__main__': # define port, host, and debugging while running
#     app.run(debug=True) # for dummy only


























# from flask import Flask, render_template

# app = Flask(__name__) # Initialize Flask

# # dummy data
# def get_sample_todos():
#     return ["Buy groceries", "Read a book", "Study Flask"]

# @app.route('/', methods=('GET', 'POST')) # Define route
# def index():  # Define what it would present or do
#     todos = get_sample_todos()
#     return render_template('index.html', todos=todos) # Defining html to render

# if __name__ == '__main__': # Define port, host, and debugging while running
#     app.run(debug=True)
