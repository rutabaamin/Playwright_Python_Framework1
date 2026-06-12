from pages.basePage import BasePage

class LeavePage(BasePage):

    LEAVE_MENU = "//span[text()='Leave']"
    ASSIGN_LEAVE = "//a[text()='Assign Leave']"

    EMPLOYEE_INPUT = "//input[@placeholder='Type for hints...']"
    LEAVE_DROPDOWN = "//label[text()='Leave Type']/../following-sibling::div//div[contains(@class,'oxd-select-text')]"
    FROM_DATE = "//label[text()='From Date']/../following-sibling::div//input"
    TO_DATE = "//label[text()='To Date']/../following-sibling::div//input"
    COMMENT = "//textarea"
    ASSIGN_BTN = "//button[normalize-space()='Assign']"

    SUCCESS_TOAST = ".oxd-toast-content"

    # dynamic employee selection
    def select_employee(self, name):
        self.page.fill(self.EMPLOYEE_INPUT, name)

        self.page.wait_for_timeout(1000)

        self.page.locator("//div[@role='listbox']//span").first.click()

    # dropdown handling
    def select_leave_type(self, value):
        dropdown = self.page.locator("div.oxd-select-text-input").first
        dropdown.click()

        self.page.get_by_text(value, exact=True).click()

    def set_date(self, locator, value):
        self.enter_text(locator, "")
        self.enter_text(locator, value)
        self.page.keyboard.press("Tab")

    def select_partial_days(self, value):

        # 1. open dropdown
        self.page.locator("div.oxd-select-text-input").nth(1).click()

        # 2. reuse generic method
        self.select_from_dropdown(
            options_locator="div[role='listbox'] span",
            value=value
        )

    def select_from_dropdown(self, options_locator, value):

        options = self.page.locator(options_locator)

        for i in range(options.count()):
            text = options.nth(i).inner_text().strip()

            if text == value:
                options.nth(i).click()
                return True

        return False

    def open_assign_leave(self):
        self.click_element(self.LEAVE_MENU)
        self.click_element(self.ASSIGN_LEAVE)

    def assign_leave(
            self,
            employee,
            leave_type,
            from_date,
            to_date,
            partial_days,
            comment):
        self.select_employee(employee)

        self.select_leave_type(leave_type)

        self.set_date(self.FROM_DATE, from_date)
        self.set_date(self.TO_DATE, to_date)

        self.select_partial_days(partial_days)

        self.enter_text(self.COMMENT, comment)

        self.click_element(self.ASSIGN_BTN)
        # confirmation popup
        ok_btn = self.page.get_by_role("button", name="Ok")

        if ok_btn.count() > 0:
            ok_btn.click()

        # wait for success toast
        self.page.locator(".oxd-toast-content").wait_for(timeout=10000)


    def is_success(self):
        return self.page.locator(self.SUCCESS_TOAST).is_visible()