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
        self.enter_text(self.EMPLOYEE_INPUT, name)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

    # dropdown handling
    def select_leave_type(self, value):
        dropdown = self.page.locator("div.oxd-select-text-input").first
        dropdown.click()

        self.page.get_by_text(value, exact=True).click()

    def set_date(self, locator, value):
        self.enter_text(locator, "")
        self.enter_text(locator, value)
        self.page.keyboard.press("Tab")

    def open_assign_leave(self):
        self.click_element(self.LEAVE_MENU)
        self.click_element(self.ASSIGN_LEAVE)

    def assign_leave(self, employee, leave_type, from_date, to_date, comment):
        self.select_employee(employee)
        self.select_leave_type(leave_type)

        self.set_date(self.FROM_DATE, from_date)
        self.set_date(self.TO_DATE, to_date)

        self.enter_text(self.COMMENT, comment)
        self.click_element(self.ASSIGN_BTN)

    def is_success(self):
        return self.page.locator(self.SUCCESS_TOAST).is_visible()