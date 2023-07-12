from playwright.sync_api import sync_playwright
import json

my_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

try:
    # Starting playwright
    p = sync_playwright().start()
    # Launching Browser
    browser = p.chromium.launch(headless = False)
    page = browser.new_page(user_agent = my_user_agent)
    # Logging into url
    page.goto('https://www.dota2.com/hero/abaddon')
    
    # Parse data function
    def parse_data():
        # Wait for a tag to load
        page.wait_for_selector('a.heropage_BottomSectionHero_1mdsq')
        # Defining variables
        var_hero_name = page.query_selector('div.heropage_HeroName_2IcIu').inner_text()
        var_hero_attrib = page.query_selector('div.heropage_PrimaryStat_3HGWJ').inner_text()
        var_attack_type = page.query_selector('div.heropage_Value_3ce-D').inner_text()
        var_skill1 = page.query_selector_all('div.heropage_TooltipTitle_oRzqV')[0].inner_text()
        var_skill2 = page.query_selector_all('div.heropage_TooltipTitle_oRzqV')[1].inner_text()
        var_skill3 = page.query_selector_all('div.heropage_TooltipTitle_oRzqV')[2].inner_text()
        var_skill4 = page.query_selector_all('div.heropage_TooltipTitle_oRzqV')[3].inner_text()

        def get_skill5():
           try:
            return page.query_selector_all('div.heropage_TooltipTitle_oRzqV')[4].inner_text()
           except:
              pass
    
        var_skill5 = 'None' if get_skill5() ==  page.query_selector_all('div.heropage_TooltipTitle_oRzqV')[0].inner_text() else get_skill5()
        
        #writing to json function
        def write_json(data, filename = 'results.json'):
           with open(filename, 'w') as f:
              json.dump(data, f, indent = 4)

        with open('results.json') as json_file:
           data = json.load(json_file)
           temp = data['heroes']
           y = {
                'name': var_hero_name,
                'primary_attrib': var_hero_attrib,
                'attack_type': var_attack_type,
                'skill_1': var_skill1,
                'skill_2': var_skill2,
                'skill_3': var_skill3,
                'skill_4': var_skill4,
                'skill_5': var_skill5
           }
           temp.append(y)
        # run wtite json function
        write_json(data)

        # Search for next page button
        next = page.query_selector_all('a.heropage_BottomSectionHero_1mdsq  div.heropage_Name_2xP5N')[1]
        print(next.inner_text())
        
        # Looping condition
        if str(next.inner_text()) == 'ABADDON':
            browser.close()
        else:
            next.click() 
            parse_data()
    
    #run parse data function
    parse_data()

finally:
    # closing everthing
    browser.close()
    print('Browser closed')
    p.stop()

