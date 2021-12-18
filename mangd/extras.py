from flask import redirect, session, url_for
from functools import wraps


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if session.get("user_id") is None:
            return redirect(url_for('users.login'))
        return view(**kwargs)
    return wrapped_view
    
def dynamic_filer(order):
    pass