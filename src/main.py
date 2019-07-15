from flask import Flask, jsonify
# TODO: 手元の環境ではCDが../srcのため from src import bus_scrにしないと動かない
from . import bus_scr

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>This page is unofficial TUT school bus timetable api.</h1>'


@app.route('/timetable/hm/')
def hm_timetable():
    scr = bus_scr.get_timetable("hm")
    return jsonify(scr)


@app.route('/timetable/h/')
def h_timetable():
    scr = bus_scr.get_timetable("h")
    return jsonify(scr)


@app.route('/timetable/gk/')
def gs_timetable():
    scr = bus_scr.get_timetable("gk")
    return jsonify(scr)


if __name__ == '__main__':
    import sys
    import pprint

    pprint.pprint(sys.path)

    app.run(debug=False, host='0.0.0.0', port=80)
