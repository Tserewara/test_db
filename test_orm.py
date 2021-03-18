from main import Credential


def test_can_save_credential(postgres_session):

    credential = Credential('Tserewara', 'password')

    postgres_session.add(credential)
    postgres_session.commit()

    assert postgres_session.query(Credential).first() == credential


def test_can_verify_credential_retrieved_from_db(postgres_session):

    credential = Credential('Tserewara', 'password1')

    postgres_session.add(credential)
    postgres_session.commit()

    assert postgres_session.query(Credential).first()
