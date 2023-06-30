from flask import Flask
from flask import render_template, request
import requests

# initializes flask app:
app = Flask(__name__)

current_user = {
    'name': 'Walter',
    'username': 'walt2020',
    'profile_pic': 'https://picsum.photos/id/237/200/300'
}

@app.route('/')
def exercise1():
    return '''
        <!DOCTYPE html>
        <html lang="en" >
        <head>
            <meta charset="UTF-8">
            <title>Demo</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css">
            <link rel="stylesheet" href="/static/style.css">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body>
            <h1>Hello {name}!</h1>
            <img src="{pic}" />
        </body>
        </html>
    '''.format(
        name=current_user.get('name'),
        pic=current_user.get('profile_pic')
    )

@app.route('/e2')
def exercise2():
    return render_template(
        'index.html',
        profile=current_user
    )

@app.route('/e2b')
def exercise2b():
    return render_template(
        'index.html',
        profile=current_user,
        message=request.args.get('message')
    )

@app.route('/e3')
def exercise3():
    search_term = request.args.get('term')
    url = 'https://www.apitutor.org/spotify/simple/v1/search?q={term}&type=track'.format(term=search_term)
    response = requests.get(url)
    tracks = response.json()
    return render_template(
        'tracks.html',
        profile=current_user,
        tracks=tracks
    )

'''
# You can also look at the Spotify documentation to find out 
# how to embed a playlist for an artist or an album.

<iframe 
    src="https://open.spotify.com/embed/artist/0yNLKJebCb8Aueb54LYya3?utm_source=generator" 
    width="100%" 
    height="380" 
    frameBorder="0" 
    allowfullscreen="" 
    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
></iframe>
'''


# enables flask app to run using "python3 app.py"
if __name__ == '__main__':
    app.run()
