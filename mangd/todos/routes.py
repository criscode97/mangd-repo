# flask imports
from flask import flash, redirect, render_template, request, session, url_for, Blueprint

# datetime for todos
from datetime import datetime

# import local modules:
from mangd.extras import login_required
from mangd.googlecalendar import service
from mangd import db
from mangd.database import todo

todos_app = Blueprint('todos', __name__)

# homepage/ todos route
@todos_app.route("/", methods=("GET", "POST"))
@login_required
def todos():
    if request.method == "POST":
        title = request.form["todo-item"]
        deadline = None
        google_id = None
        # order = request.form['todo-filter']
        # check that the user provided a todo title before adding it
        if not title:
            flash("Please provide a text describtion for your todo", "danger")
            return redirect(url_for("todos.todos"))

        # if the user provided a deadline, reformat deadline from html to a python datetime object
        if request.form["deadline"]:
            deadline = datetime.strptime(request.form["deadline"], "%Y-%m-%dT%H:%M")
            created_event = (
                service.events()
                .quickAdd(calendarId="primary", text=f"{title} at {deadline}")
                .execute()
            )
            # save google id for the event so that the user can update/delete event later
            google_id = created_event["id"]

        # assign a stat value of false to every todo to mark it as pending
        stat = False

        # save new todo to database and commit changes
        td = todo(title, stat, deadline, session["user_id"], google_id)
        db.session.add(td)
        db.session.commit()
        return redirect(url_for("todos.todos"))

    page = request.args.get("page", 1, type=int)
    my_todos = (
        todo.query.filter_by(user=session["user_id"])
        .order_by(todo.stat, todo.deadline)
        .paginate(page=page, per_page=10)
    )
    return render_template("todos.html", my_todos=my_todos, filter="all")


@todos_app.route("/filter_by/<_filter>")
def todo_filter(_filter):

    page = request.args.get("page", 1, type=int)
    if _filter == "completed":
        my_todos = (
            todo.query.filter_by(user=session["user_id"], stat=True)
            .order_by(todo.deadline)
            .paginate(page=page, per_page=10)
        )
    elif _filter == "pending":
        my_todos = (
            todo.query.filter_by(user=session["user_id"], stat=False)
            .order_by(todo.deadline)
            .paginate(page=page, per_page=10)
        )
    elif _filter == "has-due-date":
        my_todos = (
            todo.query.filter((todo.user==session["user_id"]) & (todo.deadline != None))
            .order_by(todo.deadline)
            .paginate(page=page, per_page=10)
        )
    
    return render_template("todos.html", my_todos=my_todos, filter=_filter)

# status update route
@todos_app.route("/status/<int:todo_id>")
@login_required
def stat(todo_id):
    # query for todo using the todo id
    td = todo.query.filter_by(id=todo_id).first()

    # if status is pending('false') change it to completed("True")
    if td.stat == True:
        td.stat = False
    else:
        td.stat = True

    # commit changes to the database
    db.session.commit()
    return redirect(url_for("todos.todos"))


# delete route for todos
@todos_app.route("/delete/<int:todo_id>")
@login_required
def delete(todo_id):

    # query for todo using todo id
    td = todo.query.filter_by(id=todo_id).first()

    # if todo was added to user calendar, delete from there as well
    if td.google_id:
        service.events().delete(calendarId="primary", eventId=td.google_id).execute()
    db.session.delete(td)
    db.session.commit()
    return redirect(url_for("todos.todos"))


