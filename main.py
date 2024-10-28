import json

from logger import *
import re
from flask import request, render_template, Flask
from utils import get_post_all, get_comments_by_post_id, get_post_by_pk, search_for_posts, get_posts_by_user, \
    search_for_posts_tag, get_post_by_json
from werkzeug.utils import redirect

app = Flask(__name__)

BOOKMARKS = 'data/bookmarks.json'




@app.route('/', methods=['GET'])
def main():
    posts = get_post_all()
    posts_json = get_post_by_json()
    return render_template('index.html', posts=posts, len_posts=len(posts_json))

@app.route('/posts/<int:pk>', methods=['GET'])
def post(pk):
    post = get_post_by_pk(pk)

    comments = get_comments_by_post_id(pk)
    print(comments)
    return render_template('post.html', post=post, comments=comments)

@app.route('/search/')
def search():
    search_by = request.args['s']
    posts = search_for_posts(search_by)

    return render_template('search.html', posts=posts, search_by=search_by)

@app.route('/users/<username>', methods=['GET'])
def users(username):
    posts = get_posts_by_user(username)

    return render_template('user-feed.html', posts=posts)


@app.route('/api/posts', methods=['GET'])
def get_posts():
    logger.info('Started processing GET /api/posts request')
    logger.info('Finished processing GET /api/posts request')

    posts = get_post_all()
    return posts


@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    logger.info('Started processing GET /api/posts request')
    logger.info('Finished processing GET /api/posts request')

    post = get_post_by_pk(post_id)
    return post

@app.template_filter()
def replace_hashtags(text):
    return re.sub(r'#(\w+)', r'<a href="/tag/\1">#\1</a>', text)


@app.route('/tag/<tagname>', methods=['GET'])
def tag(tagname):
    posts = search_for_posts_tag(tagname)
    return render_template('tag.html', posts=posts, tagname=tagname)

@app.route('/bookmarks/add/<int:post_id>')
def add_bookmarks(post_id):
    post = get_post_by_pk(post_id)
    with open(BOOKMARKS, 'r', encoding='utf-8') as file:
        posts_json = json.load(file)
    posts_json.append(post)
    with open(BOOKMARKS, 'w', encoding='utf-8') as file:
        json.dump(posts_json, file, ensure_ascii=False, indent=4)
    return redirect('/', code = 302)




@app.route('/bookmarks/remove/<int:post_id>')
def del_bookmarks(post_id):
    with open(BOOKMARKS, 'r', encoding='utf-8') as file:
        posts_json = json.load(file)
    for i in range(len(posts_json)):
        if posts_json[i]['pk'] == post_id:
            del posts_json[i]
            break
    with open(BOOKMARKS, 'w', encoding='utf-8') as file:
        json.dump(posts_json, file, ensure_ascii=False, indent=4)


    return redirect('/', code = 302)



@app.route('/bookmarks')
def bookmarks():
    posts = get_post_by_json()
    return render_template('bookmarks.html', posts=posts)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def not_server_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)