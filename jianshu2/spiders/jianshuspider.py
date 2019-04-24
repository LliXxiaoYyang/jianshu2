# -*- coding: utf-8 -*-



from scrapy.http import Request

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
from jianshu2.items import Jianshu2Item


class Jianshuspider(CrawlSpider):
    #urls = ['https://www.jianshu.com/c/V2CqjW?order_by=added_at&page={}'.format(str(i)) for i in range(2, 10)]
    name = 'jianshuspider'
    #allowed_domains = ['www.jianshu.com']
    start_urls = ['https://www.jianshu.com/c/V2CqjW?order_by=added_at&page=1']

    #def make_requests_from_url(self, url):
    #    """ This method is deprecated. """
    # #   return Request(url, dont_filter=True)

    #def start_requests(self):
    #    urls = ['https://www.jianshu.com/c/V2CqjW?order_by=added_at&page={}'.format(str(i)) for i in range(2, 10)]
    #    for url in urls:
    #        yield Request(url=url,callback=self.parse)

    def parse(self,response):
        item = Jianshu2Item()
        print(1234)
        selector = Selector(response)
        infos = selector.xpath('//ul[@class="note-list"]/li')
        for info in infos:
            try:
                user = info.xpath('div/div/a[1]/text()').extract()[0]
                title = info.xpath('div/a/text()').extract()[0]
                comment = info.xpath('div/div/a[2]/text()').extract()[1]
                like = info.xpath('div/div/span/text()').extract()[0]

                #print('halou',comment,like)

                item['user'] = user
                item['time'] = '00'
                item['title'] = title
                item['view'] = '01'
                item['comment']=comment
                item['like']=like
                item['gain']='10'

                yield item
            except IndexError:
                print('渣男')
        #urls = ['https://www.jianshu.com/c/V2CqjW?order_by=added_at&page={}'.format(str(i)) for i in range(2, 10)]
        url = 'https://www.jianshu.com/c/V2CqjW?order_by=added_at&page='
        for i in range(2,10):
            yield Request(url=url+str(i),callback=self.parse,dont_filter=True)
        # request = Request(urls[0], callback=self.parse)
        # print(request)
        # # for url in urls:
        #     yield Request(url,self.parse)


























    '''
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
    '''