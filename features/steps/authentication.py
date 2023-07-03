from lib2to3.pgen2 import token

import requests
# from steps import context
from behave import *
from pyexpat import features

import requests
from requests import session
from requests.auth import HTTPBasicAuth

# from requests import session

from features.steps import step_login
from features.steps.step_login import *
from payload_data import *
# from utilities import config

from utilities.apiResourses import *
from login_detail import *

from utilities.config import *
from behave import given, when, then
print(step_login.session())
print("$$$$$$$$$$$")
@given('We have API get profile')
def step_impl(context):
    config = getconfig()
    print(context.token)
    #context.session.headers["Authorization"] = f"Bearer {context.token}"
    context.authtoken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZmI0ZDdmODMxNTM1YjIxMWUzMWIyNGEyNjVkZDI2NDRmNDE3YmU3ZDUwODk4ZGU1YTg3NzYyOGNmYjEyNTc5ZmYwNWYxNTdlODQxODI1MGEiLCJpYXQiOjE2ODczNDUyMTAuOTEzMzQ2LCJuYmYiOjE2ODczNDUyMTAuOTEzMzUxLCJleHAiOjE3MTg5Njc2MTAuOTA2Mjc3LCJzdWIiOiI0NzEiLCJzY29wZXMiOltdfQ.AmtvYlpwtEB24svE-I7kFB6hdy8Z64nEEzsgpozWiMcx7klBvnKcIMEHt3Oxrw1iOEYWWZJuwaBfRSMaA3SP8R4wiU9VN5LdbEHsuWuVmJiUjY7Zem2cqd0sND1WFanGY_8FNeZ5h4Ue9hn97Sk7coL1ox_2SpUsfAiZCyPZV4IFyDwbTJvvs1rIHr6hcEwLpUb-BrIn0lpiwLcOOFda4mDFprTqTNOZjQeYNS6svFRXbyfydccilneownbB21wyoNeBdvG9li1MjAqhPDxliJ79m1yjQ-UFxegYxE5H2GaLtQM14XPPbANIA5uwxh3V_ykRWHep4Irkbed4fJoUsf3v4AsIU8YrKIjLUMu8BzioAMN66jgWN0He5IxtHDkj2R1gyRWksXM0ytgex9W4KzGteRayP1cVa9Y_cqmYXiFKuz17ygSKEuVetVuZnS6ZTQ2oG87dSY_TysrBCc3jPZDivxdS9ISxU1b7JkCAhz09xfxMW93vTvhkVXlJFrO5fMh_f8D3lWYJKtgc1mKfIDdSS4ViW52B2LOi22zeeEaeWZJhu9JVoC_6DQgJqg42ZeHe7XFwOeCL9sOnHPdRiPY7Ycuso6T-sOLcqw0X9X0SfPspUaXH1f9xS_souRvu2NUJ6gxxw7ouy7TJB81eItfXjUCPvzLiimG0vMRvQDI"
    context.headers_getprofile = {
        'Authorization': f'Bearer {context.authtoken}',
        'Content-Type': 'application/json'  # Adjust the content type as needed
    }
    context.session_token = requests.session()
    context.session_token.headers = context.headers_getprofile
    context.url_getprofile = config['API']['baseurl'] + API_resourses.get_profile
    # context.query = "select * from app_users where mobile = 9909020991"


@when('We hit get profile API with Auth')
def step_impl(context):
    context.response = context.session_token.get(context.url_getprofile,
                                                 headers=context.headers_getprofile)


@then('Status code of response should be 201')
def step_impl(context):
    print("=====Get Profile=====")
    #print(context.response.json())
    response= context.response.json()
    print(response['data'])
    print(context.response.status_code)
