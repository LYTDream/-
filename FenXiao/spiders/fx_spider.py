import scrapy


class FxSpiderSpider(scrapy.Spider):
    name = 'fx_spider'
    allowed_domains = ['fenxiao.xiaoe-tech.com']
    start_urls = ['https://fenxiao.xiaoe-tech.com/pc/get_classify_list?page=1&order=1&classify_id=28&page_size=20']

    def parse(self, response):
        status_code = response.status
        if status_code != 200:
            pass
        # response.text = response.body.decode(response.encoding)
        data = response.text
        # print(response.body.decode('utf-8'))
        # data = data.decode('utf-8')
        # print(data)
        # if data['msg'] != 'ok':
        #     pass
        import json
        data = json.loads(data)
        i = []
        for d in data['data']['list']:
            print(d['name'], d['study_num'], d['price'])
            print('-' * 50)
            i = d
        print(i)

