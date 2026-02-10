def login(login_page):
    def wrapper(user,password):
        if user == "admin" and password == "12345":
            print("Login Succesfull")
            login_page(user, password)
        else:
            print("Login fail")

    return wrapper
@login
def login_page(user,password):
    print("Login Succesfull")

login_page("admin", "1234")