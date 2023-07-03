class API_resourses:

    login = "/v1/login"
    get_product = "/v1/product/get-products"
    get_profile = "/v1/get-profile"
    get_notification ="/v1/get-notification"
    post_profileUpdate= "/v1/profile-update"
    checkUser = "/v1/check-user-exists"

def authfun(token):
    token = token
    print(token)
    return token