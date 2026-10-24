


class LoginPage:
    def __init__(self, argument_url):
        self.url = argument_url
        self.username = "admin"  
        self.password = ("id", "password")
        self.login_button = ("id", "submit")

    def fill_username_input (self, username):
        print(f"Wpisuje: {username}")

    def fill_password_input (self, password):
        print(f"Wpisuje: {password}")

    def click_login_button (self):
        print("Klikam logowanie")

    def login(self):
        self.fill_username_input()
        self.fill_password_input()
        self.click_login_button()



page_1 = LoginPage("http://127.0.0.1:8000/api/login")
# pager_1.login()
print(page_1.url)
print(page_1.username)