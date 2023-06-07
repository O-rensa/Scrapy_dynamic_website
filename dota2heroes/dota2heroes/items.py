# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Dota2HeroesItem(scrapy.Item):
    # define the fields for your item here like:
    Hero_name = scrapy.Field()
    Category = scrapy.Field()
    Skill_1 = scrapy.Field()
    Skill_2 = scrapy.Field()
    Skill_3 = scrapy.Field()
    Skill_4 = scrapy.Field()
    Skill_5 = scrapy.Field()
