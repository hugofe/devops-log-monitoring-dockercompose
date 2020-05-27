from flask import Flask, render_template, request
from log import get_log
from mysql.connector import errorcode
import mysql.connector
import db as db
from flask_script import Manager, Server


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def create():
    my_logger = get_log()

    if request.method == 'GET':
        return render_template('form/createcomments.html')

    if request.method == 'POST':
        _nome = request.form['nome']
        _email = request.form['email']
        _comentario = request.form['comentario']

        try:
            cursor, cnx_mysql = db.get_db()

            query = "INSERT INTO devopstestedb.form(nome,email,comentario) \
                    VALUES('{}','{}','{}')".format(_nome,_email,_comentario)


            cursor.execute(query)
            cnx_mysql.commit() 

            cursor, cnx_mysql = db.get_db()
            
            query = "SELECT * FROM devopstestedb.form"
            cursor.execute(query)

            return render_template('form/getcomments.html', cursor=cursor)


        except cnx_mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                my_logger.error("Something is wrong with your user name or password")

            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                my_logger.error("Database does not exist ")
            else:
                my_logger.error(err.msg)
        finally:
            cnx_mysql.close()

@app.route('/getcomments', methods=['GET'])
def index():
    my_logger = get_log()
    # return "teste"
    try:
        cursor, cnx_mysql = db.get_db()
        query = "SELECT * FROM devopstestedb.form"
        cursor.execute(query)
        return render_template('form/getcomments.html', cursor=cursor)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            my_logger.error("Something is wrong with your user name or password")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            my_logger.error("Database does not exist ")
        else:
            my_logger.error(err.msg)
    finally:
        cnx_mysql.close()



if __name__ == "__main__":
    app.run(host='0.0.0.0')