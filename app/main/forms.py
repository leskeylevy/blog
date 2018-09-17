from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required


class BlogForm(FlaskForm):
    title = StringField('Blog title', validators=[Required()])
    post = TextAreaField('Blog Post', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('comment',validators=[Required()])
    submit = SubmitField('Submit')
