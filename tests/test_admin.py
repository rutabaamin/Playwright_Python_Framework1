import time

from pages.adminPage import AdminPage

def test_admin_page_loaded(logged_in_page):

    admin = AdminPage(logged_in_page)
    admin.open_admin_page()

    assert admin.verify_page_loaded() == True
    time.sleep(2)

def test_search_system_user(logged_in_page):

    admin = AdminPage(logged_in_page)
    admin.open_admin_page()

    admin.search_user("Admin")

    assert admin.verify_page_loaded() == True
    time.sleep(2)

def test_add_button_visible(logged_in_page):

    admin = AdminPage(logged_in_page)
    admin.open_admin_page()

    assert admin.is_add_button_visible() == True
    time.sleep(2)

def test_reset_filters(logged_in_page):

    admin = AdminPage(logged_in_page)
    admin.open_admin_page()

    admin.search_user("Admin")
    admin.reset_filters()

    assert admin.verify_page_loaded() == True
    time.sleep(2)