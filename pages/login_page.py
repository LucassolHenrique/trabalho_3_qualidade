class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://local-eats-unisenac.vercel.app/static/index.html"
        self.email_input = page.locator("#loginEmail")
        self.password_input = page.locator("#loginPassword")
        self.login_button = page.locator("button[type='submit'] >> text='Entrar'")

    def navigate(self):
        self.page.goto(self.url)

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
