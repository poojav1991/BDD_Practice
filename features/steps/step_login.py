import requests
#from steps import context
from behave import *
from requests import session

from payload_data import *
#from utilities import config

from utilities.apiResourses import *
from login_detail import *

from utilities.config import *
from behave import given
#from utilities import config, apiResourses


@given('The login Details which needs to be logged in to App')
def step_impl_1(context):
    config = getconfig()
    context.url_login = config['API']['baseurl'] + API_resourses.login
    context.headers_login = {"Accept": "application/json"}
    context.query = "select * from app_users where mobile = 9909020991"
@when('We execute login PostAPI method')
def step_impl(context):
    context.response_login = requests.post(context.url_login, json=querypayload(context.query),
                                   headers=context.headers_login, )


@then('Login successfully')
def step_impl_token(context):
    #print(context.response_login.json())
    context.responsejson = context.response_login.json()
    context.session = {}
    #context['token'] = context.responsejson['data'][0]['token']
    token = context.responsejson['data'][0]['token']
    #print(context.token)
    #context['token'] = context.responsejson['data'][0]['token']
    #print(API_resourses.token)
    print(context.responsejson['data'][0]['token'])
    context.token =context.responsejson['data'][0]['token']
    print("Sesssion token of login ")
    print(context.session['token'])

    # @fixture
    # def token_session(context):
    #     context.session = session()
    #     context.token = None
    #     yield context.session
    #     context.session.close()
    # #return context.responsejson['data'][0]['token']
