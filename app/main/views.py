from flask import render_template,redirect,request,url_for,abort
from . import main
from flask_login import login_required
from .forms import BlogForm
from ..models import Blog


# View
@main.route('/')
def index():
    '''
    view root page fxn that returns the index page and its data
    '''
    title = 'Welcome to this awesome blog'
    return render_template('index.html', title=title)


@main.route('/blog',methods = ['GET','POST'])
@login_required
def blog():

    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data

        new_blog = Blog(title=title,post=post)
        new_blog.save_blog()

        return redirect(url_for('.index'))

    # blog = Blog.get_blog_order()
    return render_template('blog.html', BlogForm=form)