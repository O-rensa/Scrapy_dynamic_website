import scrapy
from dota2heroes.items import Dota2HeroesItem
from dota2heroes.spiders.herolist import myherolist

class HeroscraperSpider(scrapy.Spider):
    name = "heroscraper"
    def start_requests(self):
       links = myherolist
       for link in links:
        yield scrapy.Request(
           url = link,
           meta = {
               'pyppeteer': True
           }
       )

    def parse(self, response):
        items = Dota2HeroesItem()
        items['Hero_name'] = response.css('div.heropage_HeroName_2IcIu::text').get()
        items['Category'] = response.css('div.heropage_PrimaryStat_3HGWJ::text').get()
        items['Skill_1'] = response.css('div.heropage_TooltipTitle_oRzqV::text')[0].get()
        items['Skill_2'] = response.css('div.heropage_TooltipTitle_oRzqV::text')[1].get()
        items['Skill_3'] = response.css('div.heropage_TooltipTitle_oRzqV::text')[2].get()
        items['Skill_4'] = response.css('div.heropage_TooltipTitle_oRzqV::text')[3].get()

        def get_skill5():
           try:
            return response.css('div.heropage_TooltipTitle_oRzqV::text')[4].get()
           except:
              pass
        
        items['Skill_5'] = 'None' if get_skill5() == response.css('div.heropage_TooltipTitle_oRzqV::text')[0].get() else get_skill5()
        
        yield items