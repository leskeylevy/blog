from flask import render_template, redirect, request, url_for, abort
from . import main
from flask_login import login_required, current_user
from .forms import BlogForm, CommentForm
from ..models import Blog, Comment
from ..email import mail_message


# View
@main.route('/')
def index():
    '''
    view root page fxn that returns the index page and its data
    '''
    title = 'Welcome to this awesome blog'
    return render_template('index.html', title=title)


@main.route('/blog', methods=['GET', 'POST'])
@login_required
def blog():
    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data

        new_blog = Blog(title=title, post=post)
        new_blog.save_blog()

        return redirect(url_for('.viewblog'))

    # blog = Blog.get_blog_order()
    return render_template('blog.html', BlogForm=form)


@main.route('/viewblog', methods=['GET', 'POST'])
@login_required
def viewblog():
    title = 'Recently posted blogs'
    blog = Blog.query.order_by().all()
    return render_template('viewblog.html',title=title,blog=blog)


@main.route('/viewblog/comments/<int:id>', methods=['GET','POST'])
@login_required
def comment(id):
    form = CommentForm()
    blog = Blog.query.filter_by(id=id).first()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment=comment, user=current_user)

        new_comment.save_comment()

        return redirect(url_for('main.comment', id=blog.id))

    all_comments = Comment.query.filter_by().all()
    return render_template('comments.html', form=form, blog=blog, comments=all_comments)
