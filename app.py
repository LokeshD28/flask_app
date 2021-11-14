from flask import Flask, request

app = Flask(_name_)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return '''
            <form method="post">
                <input type="text" name="expression" />
                <input type="submit" value="Calculate" />
            </form>
        '''
    elif request.method == 'POST':
        expression = request.form.get('expression')
        result = eval(expression)
        return 'result: %s' % result

if _name_ == '_main_':
    app.run(debug=True)
