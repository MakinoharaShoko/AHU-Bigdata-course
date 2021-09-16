import scrapy

from ICE_spider_EXP1.items import UserItem

class UserSpider(scrapy.Spider):
    name = 'users'

    def start_requests(self):
        top10_url = 'https://segmentfault.com/users'
        yield scrapy.Request(url=top10_url, callback=self.parse_top10)

    def parse_top10(self,response):
        users = response.xpath("//div[@class='d-flex align-items-center']/a[2]")

        for user in users:
            user_item = UserItem()

            user_item['username'] = user.xpath('@href').get().split('/')[2]
            user_item['nickname'] = user.xpath('span/text()').get()

            # yield user_item

            profile_url = 'https://segmentfault.com/u/'+user_item['username']
            yield scrapy.Request(url=profile_url, callback=self.parse_profile, meta={'hero_item': user_item['username']})
    
    def parse_profile(self,response):
        user_itemAll = UserItem()
        item = response.meta.get('hero_item')
        user_itemAll['username'] = item
        user_itemAll['nickname'] = response.xpath('//*[@id="root"]/div[4]/div/div[1]/div[1]/div/div[2]/h3/text()').get()
        user_itemAll['like'] = response.xpath('//*[@id="root"]/div[4]/div/div[1]/div[1]/div/div[2]/div[1]/div[2]/strong/text()').get()
        user_itemAll['fans'] = response.xpath('//*[@id="root"]/div[4]/div/div[1]/div[1]/div/div[2]/div[1]/div[3]/strong/text()').get()
        user_itemAll['prestige'] = response.xpath('//*[@id="root"]/div[4]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/a/strong/text()').get()
        user_itemAll['location'] = response.xpath('//*[@id="root"]/div[4]/div/div[1]/div[1]/div/div[2]/div[3]/span/text()').get()

        yield user_itemAll