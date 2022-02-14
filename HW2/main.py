import sqlite3
from flask import Flask, request
from utils import get_email, show_table_view

app = Flask(__name__)


@app.route("/")
def welcome_user():
    return """
    <p>Click the links below to get more information:</p>
    <a href='/emails/create/'>emails_create</a><br>
    <a href='/emails/read/'>emails_read</a><br>
    <a href='/emails/update/'>emails_update</a><br>
    <a href='/emails/delete/'>emails_delete</a>
    """


@app.route('/emails/create/')
def emails_create():
    name = request.args.get('name')
    phone = request.args.get('phone')
    email = get_email()

    con = sqlite3.connect('emails.db')
    cur = con.cursor()

    # Create table
    if name and phone:
        sql = f'''INSERT INTO emails (name, phone, email) VALUES('{name}', '{phone}', '{email}');'''
    else:
        return "it's not enough values, you must add name and phone"

    cur.execute(sql)
    con.commit()
    con.close()
    return 'OK'


@app.route('/emails/read/')
def emails_read():
    id_ = request.args.get('id')

    con = sqlite3.connect('emails.db')
    cur = con.cursor()

    # Create table
    if id_:
        sql = f'''SELECT * FROM emails WHERE id={id_};'''
    else:
        sql = f'''SELECT * FROM emails ORDER BY name ASC;'''
    cur.execute(sql)
    results = cur.fetchall()
    con.close()
    table = show_table_view(results)
    return table


@app.route('/emails/update/')
def emails_update():
    id_ = request.args.get('id')
    email = request.args.get('email')
    phone = request.args.get('phone')
    name = request.args.get('name')

    con = sqlite3.connect('emails.db')
    cur = con.cursor()

    # Create table
    if id and email:
        sql = f'''UPDATE emails SET email='{email}' WHERE id={id_};'''
    elif id and phone:
        sql = f'''UPDATE emails SET phone='{phone}' WHERE id={id_};'''
    elif id and name:
        sql = f'''UPDATE emails SET name='{name}' WHERE id={id_};'''
    else:
        return "it's not enough values, you must add (id and new email) or (id and new phone)" \
               "or (id and new name)"

    cur.execute(sql)
    con.commit()
    con.close()
    return 'OK'


@app.route('/emails/delete/')
def emails_delete():
    id_ = request.args.get('id')
    con = sqlite3.connect('emails.db')
    cur = con.cursor()

    # Create table

    if id_:
        sql = f'''DELETE FROM emails WHERE id={id_};'''
    else:
        return 'add id to delete'
    cur.execute(sql)
    con.commit()
    con.close()
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)