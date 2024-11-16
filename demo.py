from flask import Flask
from flask import render_template, send_from_directory, request

from difflib import SequenceMatcher
def similar(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

app = Flask(__name__)

@app.route('/')
def page1():
    return send_from_directory('static', "index.html")

schools = ["UCLA", "USC", "CPP"]

@app.route('/school')
def hello():
    school_from = request.args.get('from')
    if school_from in schools:
        return render_template('school.html', school_from=school_from)
    else:
        nearest = max(schools, key=lambda r: similar( r.upper(), school_from.upper() ))
        return render_template('school_error.html', school_from=school_from, DYM=nearest)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25565)
