from app.helpers import *
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from flask import Flask, flash
from app.error import bp


## Should this go in init?

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors will need to make this a function?
for code in default_exceptions:
    bp.errorhandler(code)(errorhandler)