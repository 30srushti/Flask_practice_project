from flask import Flask, render_template,request, redirect
app = Flask(__name__)

users=[]

@app.route('/')
def home():
    return render_template('index.html',users=users)

@app.route('/add',methods=['POST'])
def add_user():
    name=request.form['name']
    users.append(name)
    return redirect('/')

@app.route('/update/<int:index>',methods=['POST']) 
def update_user(index):
    if index<len(users):
        users[index]=request.form['new_name']
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_user(index):
    if index<len(users):
        users.pop(index)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)