import requests
from behave import *
from payload_data import *
#from utilities import config
from utilities.apiResourses import *
from login_detail import *
from utilities.config import *

@given('The User Details which needs to be check')
def step_checkUser(context):
    config = getconfig()
    context.url_checkuser = config['API']['baseurl'] + API_resourses.checkUser
    context.headers_checkuser = {"Accept": "application/json"}
    context.check_user =checkUser("9909020991")
@when('We execute user exist PostAPI method')
def step_impl(context):
    context.response_checkuser = requests.post(context.url_checkuser, json=context.check_user,
                                   headers=context.headers_checkuser, )
@then('User Checked successfully')
def step_impl(context):
    #print(context.response_checkuser.json())
    responsejson = context.response_checkuser.json()
    #context.token = responsejson['data'][0]['token']
    print(responsejson['data'])
    print("User Checked successfully")
@given('The User Details which {user_name} check')
def step_checkUser(context,user_name):
    config = getconfig()
    context.url_checkuser = config['API']['baseurl'] + API_resourses.checkUser
    context.headers_checkuser = {"Accept": "application/json"}
    context.check_user =checkUser(user_name)
