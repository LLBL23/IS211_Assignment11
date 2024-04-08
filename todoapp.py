from flask import Flask, request, redirect, render_template
import re
app = Flask(__name__)  # creates a new website in the app variable

headings = ["Task", "Email", "Priority"]
to_do_items = []

email_Regex = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[a-z]{2,3}$')   # email Regex confirming email input is valid


@app.route('/', methods=['GET'])  # first controller to view to do items
def hello_world():
    return render_template('table.html', headings=headings, to_do_items=to_do_items)



@app.route('/submit', methods=['POST'])  # second controller to submit a new item
def add_items():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    if re.match(email_Regex, email):  # confirm a valid email has been entered
        if priority == "select an option...":  # confirm a priority level has been selected
            return redirect('/')
    else:
        return redirect('/')

    to_do_items.append(
        (
            task,
            email,
            priority
        )
    )
    return redirect('/')


@app.route('/clear', methods=['POST'])  # third controller to clear list
def clear_list():
    to_do_items.clear()  # empty to_do_list
    return redirect('/')


if __name__ == '__main__':
    app.run()
