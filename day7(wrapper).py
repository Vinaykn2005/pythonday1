def admin(dashboard):
    def wrapper(user):
        if user == "admin":
            dashboard(user)
        else:
            print("Access denied")

    return wrapper
@admin
def dashboard(user):
    print("Login Succesfull")

dashboard("admin")