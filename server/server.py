from bottle import route, run, template, get, post, request, static_file
import urllib
import json
import extractor

@route('/<filename>')
def return_resouce(filename):
    return static_file(filename, root='../')

@route('/<f1>/<f2>')
def return_resource_resource(f1, f2):
    return static_file(f1 + "/" + f2, root="../")

@route('/<f1>/<f2>/<f3>')
def return_resource_resource(f1, f2, f3):
    return static_file(f1 + "/" + f2 + "/" + f3, root="../")

@route('/extractor', method="POST")
def return_extractor():
    url = request.forms.get('url')
    return extractor.get_sentence_dates(url)

@route('/', method='GET')
def commit():
    return static_file("timeline.html", root='../')

run(host='localhost', port=8080)
