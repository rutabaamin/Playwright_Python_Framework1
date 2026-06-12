#import allure
import time
from pages.leavePage import LeavePage



#@allure.feature("Leave Module")
#@allure.story("Assign Leave")
def test_assign_leave(logged_in_page):

    leave = LeavePage(logged_in_page)

    leave.open_assign_leave()

    leave.assign_leave(
        employee="Zeeshan ASGHAR ALI",
        leave_type="CAN - FMLA",
        from_date="2026-10-06",
        to_date="2026-10-06",
        partial_days="Full Day",
        comment="Automation leave test"
    )

    assert leave.is_success()
    time.sleep(2)