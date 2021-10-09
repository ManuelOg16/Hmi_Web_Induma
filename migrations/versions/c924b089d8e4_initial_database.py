"""Initial database

Revision ID: c924b089d8e4
Revises: 38bca5a9d107
Create Date: 2021-10-09 10:56:38.518272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c924b089d8e4'
down_revision = '38bca5a9d107'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hmi_troqueladora_73', sa.Column('referencia_1', sa.Boolean(), nullable=False))
    op.drop_column('hmi_troqueladora_73', 'produccion_estimada')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hmi_troqueladora_73', sa.Column('produccion_estimada', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('hmi_troqueladora_73', 'referencia_1')
    # ### end Alembic commands ###
