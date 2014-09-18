# -*- coding: utf-8 -*-
from emailcollector import app
from flask import request, render_template, Markup, redirect
from db import get_db, query_db
from datetime import datetime
from forms import EmailForm


@app.route('/')
def index():
    return render_template('index.html', form=EmailForm())
#enddef


@app.route('/collect', methods=['POST'])
def save_email():
    form = EmailForm(request.form)
    if form.validate():
        db = get_db()
        db.execute('''INSERT INTO emails (email, registered)
        VALUES (?, ?)''', (request.form.get('email'), datetime.utcnow().isoformat()))
        db.commit()

        return render_template('email.html', email=Markup.escape(form.email.data))
    else:
        return redirect("/")
#enddef


@app.route('/list', methods=['GET'])
def list_emails():
    result = query_db('''SELECT * FROM emails''')

    return render_template('email-list.html', emails=result)
#enddef


@app.route('/delete', methods=['GET'])
def delete():
    return render_template('delete.html')
#enddef

@app.route('/delete_emails', methods=['POST'])
def delete_emails():
    #db = get_db()
    #db.execute('''DELETE FROM emails''')
    #db.commit()

    return redirect("/")
#enddef

