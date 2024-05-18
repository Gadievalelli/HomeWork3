import pytest
from selene import browser, be, have



def test_google_search(setting_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('goodday').press_enter()
    browser.element('[id="search"]').should(have.text('GoodDay is a powerful work management platform that help teams powers: projects, processes and workflows in one digital space.'))

def test_google_searching_empty_result(setting_browser):
    browser.open("https://google.ru")
    browser.element('[name="q"]').should(be.blank).type('gooddayyyyyyyyyyyyyyyyyyyyyy').press_enter()
    browser.element('#botstuff').should(have.text('По запросу gooddayyyyyyyyyyyyyyyyyyyyyy ничего не найдено.'))
