# This contains our frontend; since it is a bit messy to use the @app.route
# decorator style when using application factories, all of our routes are
# inside blueprints. This is the front-facing blueprint.
#
# You can find out more about blueprints at
# http://flask.pocoo.org/docs/blueprints/
import os
from flask import jsonify
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from markupsafe import escape

#from .forms import SignupForm
from nav import nav

import pymysql

frontend = Blueprint('frontend', __name__)

# We're adding a navbar as well through flask-navbar. In our example, the
# navbar has an usual amount of Link-Elements, more commonly you will have a
# lot more View instances.
nav.register_element('frontend_top', Navbar(
    View('Flask-Bootstrap', '.index'),
    View('Home', '.index'),
    #View('Forms Example', '.example_form'),
    #View('Debug-Info', 'debug.debug_root'),
    Subgroup(
        'Docs',
        Link('Flask-Bootstrap', 'http://pythonhosted.org/Flask-Bootstrap'),
        Link('Flask-AppConfig', 'https://github.com/mbr/flask-appconfig'),
        Link('Flask-Debug', 'https://github.com/mbr/flask-debug'),
        Separator(),
        Text('Bootstrap'),
        Link('Getting started', 'http://getbootstrap.com/getting-started/'),
        Link('CSS', 'http://getbootstrap.com/css/'),
        Link('Components', 'http://getbootstrap.com/components/'),
        Link('Javascript', 'http://getbootstrap.com/javascript/'),
        Link('Customize', 'http://getbootstrap.com/customize/'), ),
    Text('Using Flask-Bootstrap {}'.format(FLASK_BOOTSTRAP_VERSION)), ))


# Our index-page just shows a quick explanation. Check out the template
# "templates/index.html" documentation for more details.
@frontend.route('/')
def index():
    files = ['static/page7-1145px-ספר_השרשים-segmentations/%s'%f for f in os.listdir('static/page7-1145px-ספר_השרשים-segmentations/')]
    files = book_list()
    return render_template('index.html', files=files)

# TODO: move to DB API file
def book_list():
    """Get list of books from database"""
    con = pymysql.Connection(read_default_file='~/replica.my.cnf', host='tools.db.svc.eqiad.wmflabs', database='s53588__pageslices', charset='utf8')
    result = []
    with con.cursor() as cursor:
        cursor.execute('select distinct(book) from pageSlices')
        result = cursor.fetchone()
    return result

# TODO: move to DB API file
def num_pages_in_book(bookname):
    """Get list of pages of a book from database"""
    con = pymysql.Connection(read_default_file='~/replica.my.cnf', host='tools.db.svc.eqiad.wmflabs', database='s53588__pageslices', charset='utf8')
    result = []
    with con.cursor() as cursor:
        cursor.execute('select distinct(page) from pageSlices where book=%s', bookname)
        result = [r[0] for r in cursor.fetchall()]
    return result


@frontend.route('/book/<bookname>', defaults={'page': None})
@frontend.route('/book/<bookname>/<page>')
def book(bookname, page):
    # TODO: replace the URLs with real data from DB
    if page is None:
        return jsonify({'book': bookname, 
            'pdf': 'https://commons.wikimedia.org/wiki/File:%D7%A1%D7%A4%D7%A8_%D7%94%D7%A9%D7%A8%D7%A9%D7%99%D7%9D.pdf',
            'wikisource': 'https://he.wikisource.org/wiki/%s'%bookname,
            'pages': num_pages_in_book(bookname),
            'warning': 'THIS IS EXPERIMENTAL DATA'
           })
    else:
        files = []
        for i, f in enumerate(os.listdir('static/page7-1145px-ספר_השרשים-segmentations/')):
            files.append({'url':  '/section/%s/%s/%i'% (bookname, page, i) })
        return jsonify({'book': bookname,
            'pdf': 'https://commons.wikimedia.org/wiki/File:%D7%A1%D7%A4%D7%A8_%D7%94%D7%A9%D7%A8%D7%A9%D7%99%D7%9D.pdf',
            'wikisource': 'https://he.wikisource.org/wiki/%s/%s' %(bookname, page),
            'sections': [],
            'warning': 'THIS IS EXPERIMENTAL DATA'
           })



@frontend.route('/section/<bookname>/<page>/<section>')
def section(bookname, page, section):
    # TODO: use DB
    files = ['static/page7-1145px-ספר_השרשים-segmentations/%s'%f for f in os.listdir('static/page7-1145px-ספר_השרשים-segmentations/')]
    return send_file(files[0], mimetype='image/jpg')
