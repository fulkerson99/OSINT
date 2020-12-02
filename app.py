from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import json
import os
import requests
import random
import string
import sys
import time




app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template("main.html")

@app.route('/instagram_intelligence_report' , methods=['GET','POST'])
def instagram_intelligence_report():
    iguser = request.form['iguser']
    if iguser:

        username = iguser
        useragents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

        # scrape profile

        # Get the html data with the requests module
        r = requests.get(f'http://instagram.com/{username}', headers={'User-Agent': random.choice(useragents)})

        soup = BeautifulSoup(r.text, 'html.parser')

        # Find the tags that hold the data we want to parse
        general_data = soup.find_all('meta', attrs={'property': 'og:description'})
        more_data = soup.find_all('script', attrs={'type': 'text/javascript'})
        description = soup.find('script', attrs={'type': 'application/ld+json'})
        # Try to parse the content -- if it fails then the program exits
        try:
            text = general_data[0].get('content').split()
            description = json.loads(description.get_text())
            profile_meta = json.loads(more_data[3].get_text()[21:].strip(';'))
            # Works!
        except:
            # ADD TEMPLATE HERE
            print("fail")
        
        profile_name = profile_meta['entry_data']['ProfilePage'][0]['graphql']['user']['username']
        profile_url = description['mainEntityofPage']['@id']
        profile_follower = text[0]
        profile_following = text[2]
        profile_posts = text[4]
        profile_bio = str(profile_meta['entry_data']['ProfilePage'][0]['graphql']['user']['biography'])
        profile_pic_url= str(profile_meta['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd'])
        profile_is_business_account = str(profile_meta['entry_data']['ProfilePage'][0]['graphql']['user']['is_business_account'])
        profile_connected_to_fb = str(profile_meta['entry_data']['ProfilePage'][0]['graphql']['user']['connected_fb_page'])
        profile_externalurl = str(profile_meta['entry_data']['ProfilePage'][0]['graphql']['user']['external_url'])
        profile_joined_recently = str(profile_meta['entry_data']['ProfilePage'][0]['graphql']['user'][
                                                        'is_joined_recently'])
        profile_business_category_name = str(
                                 profile_meta['entry_data']['ProfilePage'][0]['graphql']['user'][
                                     'business_category_name'])
        profile_is_private = str(profile_meta['entry_data']['ProfilePage'][0]['graphql']['user']['is_private'])
        profile_is_verified=str(profile_meta['entry_data']['ProfilePage'][0]['graphql']['user']['is_verified'])        
        

        return render_template("instagram_intelligence.html", iguser=iguser, username=username, profile_name=profile_name, profile_url=profile_url, profile_follower=profile_follower, profile_following=profile_following, profile_posts=profile_posts, profile_bio=profile_bio, profile_pic_url=profile_pic_url, profile_is_business_account=profile_is_business_account, profile_connected_to_fb=profile_connected_to_fb,profile_externalurl=profile_externalurl, profile_joined_recently=profile_joined_recently,  profile_business_category_name= profile_business_category_name, profile_is_private=profile_is_private,   profile_is_verified=profile_is_verified)

    else:
        return 'No user entered!'

if __name__ == '__main__':
    app.run()