@pytest.fixture()
def setting_browser():
    yield
    browser.quit()