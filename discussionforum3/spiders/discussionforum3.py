import scrapy


class DiscussionForum3Spider(scrapy.Spider):
    name = 'forum3'
    page_number = 2
    c =0
    start_urls = ['https://forums.hardwarezone.com.sg/eat-drink-man-woman-16/ceca-bui-chee-retrenched-wor-158th-report-so-kelian-edmwers-got-lobang-her-6358262.html']
    
    # custom_settings={ 'FEED_URI': "discussion-forum2%(time)s.csv",
                       # 'FEED_FORMAT': 'csv'}
                    
    
    def parse(self, response):
        all_div = response.xpath("//*[@class='post-wrapper']")
        author = response.css('#content-header::text').extract_first() 
        title = response.css('.header-gray::text').extract_first().strip()
        like = response.css('.vbseo-likes-count span::text').extract_first()
        link = response.url
       
        for div in all_div:
            sequence = div.css('.thead strong::text').extract()
            date = div.css('.thead:nth-child(1)::text')[2:-1].extract()
            user = div.css('.bigusername::text').extract()
            comment = div.css('.post_message::text').extract()
            if (DiscussionForum3Spider.c==0):
                DiscussionForum3Spider.c = DiscussionForum3Spider.c + 1
                yield {'author' : author,
                    'title' : title,
                    'like' : like,
                    'Link' : link,
                    'Sequence' : sequence,
                    'Date' : [dt.strip() for dt in date],
                    'User' : user,
                    'Comment' : [com.strip() for com in comment]
                    
                    }
            else:
                yield {                        
                       'Link' : link,
                       'Sequence' : sequence,
                       'Date' : [dt.strip() for dt in date],
                       'User' : user,
                       'Comment' : [com.strip() for com in comment]
                        }
                
                
        page = str(DiscussionForum3Spider.page_number)
        next_page = 'https://forums.hardwarezone.com.sg/eat-drink-man-woman-16/ceca-bui-chee-retrenched-wor-158th-report-so-kelian-edmwers-got-lobang-her-6358262' + '-' + page + '.html'
        if DiscussionForum3Spider.page_number < 12:
            DiscussionForum3Spider.page_number = DiscussionForum3Spider.page_number + 1
            yield response.follow(next_page, callback= self.parse)
            
