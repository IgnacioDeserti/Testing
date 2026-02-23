def test_example_title(driver):
    driver.get("https://example.com/")
    assert "Example Domain" in driver.title


def test_example_h1(driver):
    driver.get("https://example.com/")
    h1 = driver.find_element("css selector", "h1").text
    assert h1.strip() == "Example Domain"