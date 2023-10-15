
from flask import Flask, render_template, request

from parser import get_riggles
from db import server

app = Flask(__name__)
server = server()


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    if request.method=='GET':
        server.create_table()
        return render_template('/main.html')

    if request.method=='POST':

        try:
            numbers = int(request.form['number'])
            for_insert = get_riggles(n=numbers)
            server.add_riggle(for_insert)

            with server.create_connection() as conn:
                curs = conn.cursor()
                curs.execute('SELECT id FROM riggles;')
                out_data = curs.fetchall()
                ind = numbers*(-1)
                out_data = out_data[ind:]
                out_data = ' '.join([str(i[0]) for i in out_data])

            return render_template('/out.html', data=out_data)


        except ValueError:
            error = 'You inserted wrong value'
            return render_template('/error.html', error=error)

if __name__=='__main__':
    app.run(host='0.0.0.0')