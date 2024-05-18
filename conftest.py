@pytest.fixture()
def setting_browser():
    browser.config.window_height = 700
    browser.config.window_width = 1000
    yield
    browser.quit()