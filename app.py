from flask import Flask, render_template #import flask

app = Flask(__name__) # initialize

# dummy data
def get_sample_todos():
    return ["Buy groceries", "Read a book", "Study Flask"]

# get kumuha, post gumamit
#decorator. route is from FLask. / url

@app.route('/', methods=('GET', 'POST')) # define route , san mapupunta si url
def index(): # define what it would present or do
    todos = get_sample_todos() # yung todos dito, matatawag sa kabila
    return render_template ('index.html', todos=todos)

if __name__=='__main__': # define port, host, and debugging while running
    app.run(debug=True) # for dummy only




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
