from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# this is my todo list app for the flask unit
# Mr. Henderson said we need at least 3 routes

todos = []

@app.route('/')
def home():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todos.append(task)
    return redirect(url_for('home'))

@app.route('/delete/<int:index>')
def delete(index):
    # make sure the index is valid before deleting
    if index < len(todos):
        todos.pop(index)
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
