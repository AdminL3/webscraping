from playwright.sync_api import sync_playwright, Playwright

url = "https://www.bhphotovideo.com/c/buy/macbook-pro/ci/29069"


def run(playwright: Playwright):
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()

    page.goto(url)
    page.screenshot(path="page.png")

    for i in range(15):
        links = page.locator(
            'a[data-selenium="miniProductPageProductNameLink"]').all()
        print(f"Found {len(links)} links")
        for i, link in enumerate(links):
            p = browser.new_page()
            p.goto(f"https://www.bhphotovideo.com{link.get_attribute('href')}")
            # p.screenshot(path=f"data/product_{i}.png")

            data = p.locator(
                "script[type='application/ld+json']").nth(1).text_content()

            print(data)
            with open(f"data/product_{i}.json", "w") as f:
                f.write(data)

            p.close()
        browser.close()


with sync_playwright() as p:
    run(p)
