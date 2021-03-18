from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper

from main import Credential

metadata = MetaData()

credential_orm = Table('credential', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('username', String, index=True, nullable=False),
                       Column('password', String, nullable=False),
                       )


def start_mappers():
    mapper(Credential, credential_orm)
