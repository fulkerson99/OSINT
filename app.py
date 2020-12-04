from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import json


import stweet as st
from igramscraper.instagram import Instagram
import twint



app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template("main.html")

@app.route('/instagram_intelligence_report' , methods=['GET','POST'])
def instagram_intelligence_report():
    iguser = request.form['iguser']
    instagram = Instagram()

    instagram.with_credentials('testingOSINT', 'osintpass123')
    instagram.login()

    account = instagram.get_account(iguser)

    username = account.username
    profile_name = account.full_name
    profile_bio = account.biography
    profile_pic_url = account.get_profile_picture_url()
    profile_externalurl = account.external_url
    profile_posts = account.media_count
    profile_follower = account.followed_by_count
    profile_following = account.follows_count
    profile_is_private = account.is_private
    profile_is_verified = account.is_verified
    
    return render_template("instagram_intelligence.html", iguser=iguser, username=username, profile_name=profile_name, profile_follower=profile_follower, profile_following=profile_following, profile_posts=profile_posts, profile_bio=profile_bio, profile_pic_url=profile_pic_url, profile_externalurl=profile_externalurl,  profile_is_private=profile_is_private, profile_is_verified=profile_is_verified)
      

@app.route('/twitter_report' , methods=['GET','POST'])
def twitter_report():
    username = request.form['twitteruser']
    if username:
        # Configure
        search_tweets_task = st.SearchTweetsTask(all_words='#covid19' ,tweets_count=20)
        tweets_collector = st.CollectorTweetOutput()
        st.TweetSearchRunner(search_tweets_task=search_tweets_task,tweet_outputs=[tweets_collector, st.CsvTweetOutput('output_file.csv')]).run()

        tweets = tweets_collector.get_scrapped_tweets()
        
        return render_template("tweets.html", tweets=tweets, username=username)


    else:
        return render_template("error.html")


if __name__ == '__main__':
    app.run()