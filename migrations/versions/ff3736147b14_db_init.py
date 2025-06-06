"""db init

Revision ID: ff3736147b14
Revises: d620fcdca9b6
Create Date: 2025-05-12 15:30:30.169338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff3736147b14'
down_revision = 'd620fcdca9b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('i18n',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('en_text', sa.String(length=15), nullable=True),
    sa.Column('target', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resource_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=15), nullable=True),
    sa.Column('description', sa.String(length=15), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['resource_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resource_cost',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=15), nullable=True),
    sa.Column('description', sa.String(length=15), nullable=True),
    sa.Column('time_cost', sa.Boolean(), nullable=True),
    sa.Column('unit_time_reference', sa.Integer(), nullable=True),
    sa.Column('unit_cost', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resource_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=15), nullable=True),
    sa.Column('type', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profil_management',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creation_right', sa.Boolean(), nullable=True),
    sa.Column('update_right', sa.Boolean(), nullable=True),
    sa.Column('read_right', sa.Boolean(), nullable=True),
    sa.Column('delete_right', sa.Boolean(), nullable=True),
    sa.Column('managed_profil_id', sa.Integer(), nullable=True),
    sa.Column('master_profil_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['managed_profil_id'], ['profil.id'], ),
    sa.ForeignKeyConstraint(['master_profil_id'], ['profil.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profil_resource_management',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creation_right', sa.Boolean(), nullable=True),
    sa.Column('update_right', sa.Boolean(), nullable=True),
    sa.Column('read_right', sa.Boolean(), nullable=True),
    sa.Column('delete_right', sa.Boolean(), nullable=True),
    sa.Column('profil_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['profil_id'], ['profil.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resource',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=15), nullable=True),
    sa.Column('qty_available', sa.Integer(), nullable=True),
    sa.Column('resources_unit_cost', sa.Float(), nullable=True),
    sa.Column('photo', sa.String(length=15), nullable=True),
    sa.Column('warning_nb', sa.Integer(), nullable=True),
    sa.Column('resource_type_id', sa.Integer(), nullable=True),
    sa.Column('resource_category_id', sa.Integer(), nullable=True),
    sa.Column('resource_cost_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['resource_category_id'], ['resource_category.id'], ),
    sa.ForeignKeyConstraint(['resource_cost_id'], ['resource_cost.id'], ),
    sa.ForeignKeyConstraint(['resource_type_id'], ['resource_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=15), nullable=True),
    sa.Column('password', sa.String(length=15), nullable=True),
    sa.Column('date_creation', sa.DateTime(), nullable=True),
    sa.Column('date_expiration', sa.DateTime(), nullable=True),
    sa.Column('profil_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['profil_id'], ['profil.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('loan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('free', sa.Boolean(), nullable=True),
    sa.Column('retire', sa.Boolean(), nullable=True),
    sa.Column('rendu', sa.Boolean(), nullable=True),
    sa.Column('note', sa.String(length=15), nullable=True),
    sa.Column('resource_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['resource_id'], ['resource.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shop_cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('last_update_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shop_cart_detail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('last_update_date', sa.DateTime(), nullable=True),
    sa.Column('shop_cart_id', sa.Integer(), nullable=True),
    sa.Column('resource_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['resource_id'], ['resource.id'], ),
    sa.ForeignKeyConstraint(['shop_cart_id'], ['shop_cart.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shop_cart_detail')
    op.drop_table('shop_cart')
    op.drop_table('loan')
    op.drop_table('user')
    op.drop_table('resource')
    op.drop_table('profil_resource_management')
    op.drop_table('profil_management')
    op.drop_table('resource_type')
    op.drop_table('resource_cost')
    op.drop_table('resource_category')
    op.drop_table('i18n')
    # ### end Alembic commands ###
