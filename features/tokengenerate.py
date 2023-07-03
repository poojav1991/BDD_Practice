from behave import fixture, use_fixture
from requests.sessions import Session
@fixture
def token_session(context):
    context.session = Session()
    context.token = None
    yield context.session
    context.session.close()
