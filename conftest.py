import os
import time
from pathlib import Path

import pytest

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker, clear_mappers

from orm import metadata, start_mappers


def get_postgres_uri():
    host = 'localhost'
    port = 5432
    password = os.environ.get('POSTGRES_PASSWORD', 'tserewara')
    user, db_name = 'postgres', 'blog'
    return f'postgresql://{user}:{password}@{host}:{port}/{db_name}'


@pytest.fixture
def session_factory(in_memory_db):
    start_mappers()
    yield sessionmaker(bind=in_memory_db)
    clear_mappers()


@pytest.fixture
def session(session_factory):
    yield session_factory()


def wait_for_postgres_to_come_up(engine):
    deadline = time.time() + 10
    while time.time() < deadline:
        try:
            return engine.connect()
        except OperationalError:
            time.sleep(0.5)
    pytest.fail('Postgres never came up')


@pytest.fixture(scope='session')
def postgres_db():
    engine = create_engine(get_postgres_uri())
    wait_for_postgres_to_come_up(engine)
    metadata.create_all(engine)
    return engine


@pytest.fixture
def postgres_session(postgres_db):
    start_mappers()
    session = sessionmaker(bind=postgres_db)()
    session.execute(
        'DELETE FROM credential'
    )
    yield session

    clear_mappers()
