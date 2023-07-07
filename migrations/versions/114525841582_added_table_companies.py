"""added table companies

Revision ID: 114525841582
Revises: 8926f36068a9
Create Date: 2023-07-06 11:31:59.920730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '114525841582'
down_revision = '8926f36068a9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_company_inn', 'companies', type_='unique')
    op.create_index(op.f('ix_companies_company_inn'), 'companies', ['company_inn'], unique=True)
    op.add_column('leasing_contracts', sa.Column('company_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'leasing_contracts', 'companies', ['company_id'], ['id'])
    op.drop_column('leasing_contracts', 'company_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('leasing_contracts', sa.Column('company_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'leasing_contracts', type_='foreignkey')
    op.drop_column('leasing_contracts', 'company_id')
    op.drop_index(op.f('ix_companies_company_inn'), table_name='companies')
    op.create_unique_constraint('unique_company_inn', 'companies', ['company_inn'])
    # ### end Alembic commands ###