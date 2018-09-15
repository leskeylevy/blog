"""created a blog table in the database

Revision ID: f67b9277f525
Revises: 62b8fda0b37c
Create Date: 2018-09-15 16:37:26.615098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f67b9277f525'
down_revision = '62b8fda0b37c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('post', sa.String(length=255), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blogs_post'), 'blogs', ['post'], unique=False)
    op.create_index(op.f('ix_blogs_title'), 'blogs', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_blogs_title'), table_name='blogs')
    op.drop_index(op.f('ix_blogs_post'), table_name='blogs')
    op.drop_table('blogs')
    # ### end Alembic commands ###