from flask import Flask, render_template, request, redirect
import re

mylist = []
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def list():
    return render_template('index.html', mylist=mylist)

@app.route('/additem', methods=['POST', 'GET'])
def additem():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    if(re.search(regex,email)):
        mylist.append([task, email, priority])
    else:
        print("Invalid Email")
    return redirect('/')

@app.route('/clear/')
def clear():
    del mylist[:]
    return render_template('index.html', mylist=mylist)

if __name__ == '__main__':
    app.run(debug=True)
