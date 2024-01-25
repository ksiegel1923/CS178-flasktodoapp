from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# This is the line I added while debugging my project
app.app_context().push()

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Here is an example of me using the variable candidate concept
# I am setting my variable db (which is short for database) to the database attached to this app
db = SQLAlchemy(app) 


class Todo(db.Model):
    # Here are three examples of me using the variable candidate concept
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# Here I am using the candiate concept of a route to indicate what will happen if I go to the "/" URL
@app.route("/")
def home():
    todo_list = Todo.query.all()
    # Here I am using the candidate concept of rendering so that when I load my page, the "base.html" code will load for the user to see
    return render_template("base.html", todo_list=todo_list)

# Here is another example of the route candidate concept
@app.route("/add", methods=["POST"])
def add():
    # Here is another example of me using the variable candidate concept
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    # Here is an example of me using the redirect candidate concept to lead back to my home function
    return redirect(url_for("home"))

# Here is another example of the route candidate concept and the variable routes concept
# My update route will depend on the id of the todo that I want to update 
# (this variable will also be passed into my update function)
@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    # Here is another example of the redirect candidate concept
    return redirect(url_for("home"))

# Here is another example of the route candidate concept and the variable routes concept
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    # Here is another example of the redirect candidate concept
    return redirect(url_for("home"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
