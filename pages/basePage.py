class BasePage:

    def __init__(self, page):
        self.page = page

    def click_element(self, locator):
        self.page.locator(locator).click()

    def enter_text(self, locator, text):
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def select_dropdown(self, locator, value):
        self.page.locator(locator).click()
        self.page.get_by_text(value).click()
