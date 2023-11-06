"""Created database

Revision ID: 0a3dd3dd6944
Revises: 
Create Date: 2023-11-06 11:10:17.417076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a3dd3dd6944'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('skills', sa.String(length=300), nullable=True),
    sa.Column('experience', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('employers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('company_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employer_id', sa.Integer(), nullable=True),
    sa.Column('business_industry', sa.String(), nullable=True),
    sa.Column('employee_size', sa.String(), nullable=True),
    sa.Column('base_currency', sa.String(), nullable=True),
    sa.Column('continent', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('primary_contact_email', sa.String(), nullable=True),
    sa.Column('primary_contact_phone', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['employer_id'], ['employers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('employer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employer_id'], ['employers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ratings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('employer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.ForeignKeyConstraint(['employer_id'], ['employers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee_applications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('nationality', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('mobile', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('work_duration', sa.String(), nullable=True),
    sa.Column('work_location', sa.String(), nullable=True),
    sa.Column('work_description', sa.Text(), nullable=True),
    sa.Column('school', sa.String(), nullable=True),
    sa.Column('major', sa.String(), nullable=True),
    sa.Column('year_completed', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee_applications')
    op.drop_table('ratings')
    op.drop_table('jobs')
    op.drop_table('company_profiles')
    op.drop_table('employers')
    op.drop_table('employees')
    # ### end Alembic commands ###
