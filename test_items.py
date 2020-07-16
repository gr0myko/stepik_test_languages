link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_all_lang(browser):
    browser.get(link)
    add_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert add_button, "Button not found"