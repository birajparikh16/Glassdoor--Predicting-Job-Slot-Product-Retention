from app import app

from flask import Flask, request, render_template

@app.errorhandler(404)
def not_found_error(e):
    return render_template('404.html', ), 404