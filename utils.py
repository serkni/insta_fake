import json

POSTS = 'data/posts.json'
COMMENTS = 'data/comments.json'
BOOKMARKS = 'data/bookmarks.json'

def get_post_all():
    with open(POSTS, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts

def get_posts_by_user(user_name):
    with open(POSTS, 'r', encoding='utf-8') as file:
        posts = json.load(file)
        try:
            post_user = []
            for post in posts:
                if post['poster_name'] == user_name:
                    post_user.append(post)

        except ValueError:
            print('Такого пользователя нет')
    return post_user

def get_comments_by_post_id(post_id):
    with open(COMMENTS, 'r', encoding='utf-8') as file:
        comments = json.load(file)
        try:
            comments_user = []
            for comment in comments:
                if comment['post_id'] == post_id:
                    comments_user.append({'comment': comment['comment'],'commenter_name': comment['commenter_name'] })

        except ValueError:
            print('Такого поста нет')
    return comments_user

def search_for_posts(query):
    with open(POSTS, 'r', encoding='utf-8') as file:
        posts = json.load(file)
        posts_query = []
        for post in posts:
            if query in post['content']:
                posts_query.append(post)

    return posts_query

def search_for_posts_tag(tagname):
    with open(POSTS, 'r', encoding='utf-8') as file:
        posts = json.load(file)
        posts_query = []
        for post in posts:
            if ('#' + tagname) in post['content']:
                posts_query.append(post)

    return posts_query


def get_post_by_pk(pk):
    with open(POSTS, 'r', encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
            if post['pk'] == pk:
                return post


def get_post_by_json():
    with open(BOOKMARKS, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts