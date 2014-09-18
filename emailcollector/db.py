# -*- coding: utf-8 -*-
from sqlite3 import dbapi2 as sqlite3
from flask import _app_ctx_stack
from emailcollector import app


def get_db():
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
        top.sqlite_db.row_factory = sqlite3.Row
    return top.sqlite_db
#enddef


@app.teardown_appcontext
def close_database(exception):
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()
#enddef


#def init_db():
#    db = get_db()
#    with app.open_resource('sql/schema.sql', mode='r') as f:
#        db.cursor().executescript(f.read())
#    db.commit()
##enddef


#@app.cli.command('initdb')
#def initdb_command():
#    init_db()
#    print("DB initialized.")
##enddef


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    return (rv[0] if rv else None) if one else rv
#enddef





