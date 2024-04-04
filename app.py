from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_media_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            media_content = []

            # Find all image elements
            for img in soup.find_all('img'):
                src = img.get('src')
                if src:
                    media_content.append({'type': 'image', 'src': src})

            # Find all video elements
            for video in soup.find_all('video'):
                for source in video.find_all('source'):
                    src = source.get('src')
                    if src:
                        media_content.append({'type': 'video', 'src': src})

            return media_content
        else:
            return None
    except Exception as e:
        print('Error scraping media content:', str(e))
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_media', methods=['POST'])
def fetch_media():
    website_url = request.form['website_url']
    media_content = scrape_media_content(website_url)
    if media_content:
        return render_template('success.html', media_content=media_content)
    else:
        return 'Failed to fetch media content from the specified URL.'

if __name__ == '__main__':
    app.run(debug=True)
