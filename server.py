from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def counter():
    if 'count' not in session:
        print('key does not exist')
        session['count'] = 1
    else:
        print("session exists!")
        session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def double_counter():
    session['count'] += 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)