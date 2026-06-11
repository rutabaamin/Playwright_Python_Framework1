from pages.basePage import BasePage


class DashboardPage(BasePage):

    pim_menu = "//span[normalize-space()='PIM']"

    def navigate_to_pim(self):
        self.page.locator(self.pim_menu).click()


    def is_widget_visible(self, widget_name):
        locator = self.page.locator("div.orangehrm-dashboard-widget") \
            .filter(has_text=widget_name) \
            .first

        return locator.is_visible()