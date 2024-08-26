from flask import Flask, request, render_template, jsonify # request to check request library, render_template to load html

# create simple flask application
app = Flask(__name__)


# basic rounting
@app.route('/', methods=['GET'])
def welcome():
    return 'Welcome Kanchan'

# variable rule
# @app.route('/success/<int:score>', methods=['GET'])
@app.route('/success/<score>', methods=['GET'])
def success(score):
    return f'<h3>Yay! You passed with {score}%'

# another route for failure
@app.route('/fail/<score>', methods=['GET'])
def fail(score):
    return f'<h3>Yay! You failed with {score}%'

# route to handle get and post
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        maths = int(request.form['math'])
        science = int(request.form['science'])
        history = int(request.form['history'])
        average_marks = (maths+science+history)/3

        return render_template('form.html', score=average_marks)

# create simple api
@app.route('/api', methods=['POST'])
def calculate():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    response = {
        'result':a_val+b_val,
    }
    return jsonify(response)


if __name__=='__main__':
    app.run(debug=True) # debug == True vayena vane changes garnasath re-load garna parcha

