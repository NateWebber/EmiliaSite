from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import praw, random
app = Flask(__name__)
application = app
bootstrap = Bootstrap(app)

#reddit reader setup
reddit = praw.Reddit(
    client_id="ppRz0Ov67mXSHA",
    client_secret="rkyzWdN5Oq65rX7HD3D-wUWm8G4",
    user_agent="E Site Script by u/Nuz_"
)

#list of valid subreddits for birbs
subreddits = ['birbs', 'partyparrot', 'birdpics', 'illegallysmolbirbs', 'divorcedbirds']

def fetch_birb():
    random_sub = random.choice(subreddits)
    post = reddit.subreddit(random_sub).random()
    while not "i.redd" in post.url:
        post = reddit.subreddit(random_sub).random()
    return post



@app.route('/')
def index():
    random_post = fetch_birb()
    return render_template(
        'index.html', birb = random_post.url, post_url = random_post.permalink, post_title = random_post.title, post_author = random_post.author.name, post_subreddit = random_post.subreddit.display_name
        )