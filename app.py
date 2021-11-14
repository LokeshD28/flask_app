#!/usr/bin/env python
from flask import Flask, request

# create app
app = Flask(_name_)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # show html form
        return '''
            <form method="post">
                <input type="text" name="expression" />
                <input type="submit" value="Calculate" />
            </form>
        '''
    elif request.method == 'POST':
        # calculate result
        expression = request.form.get('expression')
        result = eval(expression)
        return 'result: %s' % result

# run app
if _name_ == '_main_':
    app.run(debug=True)
