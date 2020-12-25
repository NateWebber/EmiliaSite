import praw, random

reddit = praw.Reddit(
    client_id="ppRz0Ov67mXSHA",
    client_secret="rkyzWdN5Oq65rX7HD3D-wUWm8G4",
    user_agent="Emilia Site Script by u/Nuz_"
)
#list of valid subreddits for birbs
subreddits = ['birbs', 'partyparrot', 'birdpics']
def fetch_birb():
    random_sub = random.choice(subreddits)
    print("CHOSEN SUBREDDIT: " + random_sub)
    post = reddit.subreddit(random_sub).random()
    print("CHOSEN POST URL: " + post.url)
    while not "i.redd" in post.url:
        print("PREVIOUS POST WAS NOT ACCEPTABLE, TRYING AGAIN....")
        post = reddit.subreddit(random_sub).random()
        print("CHOSEN POST URL: " + post.url)
    print("FOUND ACCEPTABLE IMAGE AT: " + post.url)

fetch_birb()