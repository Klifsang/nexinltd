"""empty message

Revision ID: e56b946d475e
Revises: 
Create Date: 2024-04-22 06:52:14.412620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e56b946d475e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('user_name', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.Column('phone_number', sa.String(length=15), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('availability', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('tickets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('OPEN', 'CLOSED', 'IN_PROGRESS', name='ticketstatus'), nullable=True),
    sa.Column('priority', sa.Enum('URGENT', 'HIGH', 'MEDIUM', 'LOW', name='prioritylevel'), nullable=True),
    sa.Column('deadline', sa.DateTime(), nullable=False),
    sa.Column('assign_to', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('comments', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['assign_to'], ['admin.id'], name=op.f('fk_tickets_assign_to_admin')),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], name=op.f('fk_tickets_client_id_clients')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('ticket_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ticket_id'], ['tickets.id'], name=op.f('fk_tasks_ticket_id_tickets')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    op.drop_table('tickets')
    op.drop_table('clients')
    op.drop_table('admin')
    # ### end Alembic commands ###