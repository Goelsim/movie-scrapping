import scrapy

class Movie(scrapy.Spider):
    name = "movie"
    allowed_domains = ['rottentomatoes.com']
    start_urls = [
        'https://www.rottentomatoes.com/top/bestofrt/',
    ]

    def parse(self, response):
        movie = response.css('.table>tr>td')
        rank = movie.css('.bold::text').extract()
        rating = movie.css('span>span.tMeterScore::text').extract()
        title = movie.css('a::text').extract()
        for i in range(len(title)):
            yield {
                'rank': rank[i],
                'rating': rating[i],
                'title': title[i].strip(),
            }

