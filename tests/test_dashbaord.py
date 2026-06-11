import time

from pages.dashboardPage import DashboardPage

def test_dashboardPageWidgets(logged_in_page):

    dashboard = DashboardPage(logged_in_page)

    widgets = [
        "Time at Work",
        "My Actions",
        "Quick Launch"
    ]

    for widget in widgets:
        assert dashboard.is_widget_visible(widget)

    time.sleep(2)

def test_dashboard(logged_in_page):

    dashboard = DashboardPage(logged_in_page)

    dashboard.navigate_to_pim()
    time.sleep(2)