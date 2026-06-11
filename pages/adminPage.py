from pages.basePage import BasePage

class AdminPage(BasePage):

    # Locators
    ADMIN_MENU = "a[href*='admin']"
    USERNAME_INPUT = "//label[text()='Username']/../following-sibling::div//input"
    SEARCH_BUTTON = "//button[@type='submit']"
    RESET_BUTTON = "//button[normalize-space()='Reset']"
    ADD_BUTTON = "//button[normalize-space()='Add']"
    SYSTEM_USER_HEADER = "//h5"

    def open_admin_page(self):
        self.page.click(self.ADMIN_MENU)

    def verify_page_loaded(self):
        return "admin/viewSystemUsers" in self.page.url

    def search_user(self, username):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.click(self.SEARCH_BUTTON)

    def reset_filters(self):
        self.page.click(self.RESET_BUTTON)

    def is_add_button_visible(self):
        return self.page.locator(self.ADD_BUTTON).is_visible()