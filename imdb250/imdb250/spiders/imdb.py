import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'

    start_urls = ['https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']

    def parse(self, response):
        for movies in response.css('.lister-item-header'):
            yield{
                'movie':movies.css('.lister-item-header a::text').get(),
                  'year':movies.css('.text-muted.unbold ::text').get(),
                  'rating':movies.css('.ratings-imdb-rating strong ::text').get()
            }
        pass
