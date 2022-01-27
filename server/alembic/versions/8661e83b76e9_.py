"""empty message

Revision ID: 8661e83b76e9
Revises: f8584b069665
Create Date: 2022-01-27 14:28:49.923648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8661e83b76e9'
down_revision = 'f8584b069665'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_portfolio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('price_history_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['price_history_id'], ['price_history.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_portfolio_id'), 'user_portfolio', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_portfolio_id'), table_name='user_portfolio')
    op.drop_table('user_portfolio')
    # ### end Alembic commands ###
