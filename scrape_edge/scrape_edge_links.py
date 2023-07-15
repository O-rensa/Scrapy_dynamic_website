from playwright.sync_api import sync_playwright
import csv
from links import search_links

my_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

try:
    # start playwright
    p = sync_playwright().start()
    #start browser
    browser = p.chromium.launch(headless = False)
    context = browser.new_context(user_agent = my_user_agent)
    page = context.new_page()

    pages = search_links

    # go to url
    for i in pages:
        page.goto(i)
        page.wait_for_selector('td.alignR')
        
        name = page.query_selector('div.compInfo p').inner_text()

        financial_data = page.query_selector_all('td.alignR')
        my_list = [name]

        for i in range(0,74):
            my_list.append("'"+financial_data[i].inner_text()+"'")

        my_list.append(page.url)

        data_to_append = [my_list]

        with open('Financial_reports.csv', 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerows(data_to_append)


        print(name)
        page.wait_for_timeout(1000)
finally:
    browser.close()
    p.stop()