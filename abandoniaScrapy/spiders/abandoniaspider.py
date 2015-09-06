import logging

import scrapy

from abandoniaScrapy.items import GameItem


class AbandoniaSpider(scrapy.Spider):
    """Abandonia.com all games crawler"""

    name = "abandonia"
    allowed_domains = ["abandonia.com"]
    start_urls = ["http://www.abandonia.com/en/game/all"]

    def parse(self, response):
        for gamelist in response.xpath("//div[@class='gamelist']"):
            game_image_path = gamelist.xpath(".//div[@class='gamelistimage']/*/img/@src")

            # Information block
            gameinfo = gamelist.xpath(".//div[@class='gamelistinformation']")
            title = gameinfo.xpath(".//div[contains(@class, 'title')]/a")
            game_link = title.xpath("./@href")
            game_name = title.xpath("./text()")
            game_rating = gameinfo.xpath(".//div[contains(text(), 'Your rating')]"
                                             "/following-sibling::*/text()")
            game_year = gameinfo.xpath(".//div[contains(text(), 'Year of release')]"
                                            "/following-sibling::*/a/text()")
            # /Information block

            game_tags = gamelist.xpath(".//div[@class='gamelisttags']/a/text()")

            item = GameItem()
            item['titleimage_path'] = [response.urljoin(href) for href in game_image_path.extract()]
            item['name'] = game_name.extract()
            item['year'] = game_year.extract()
            item['tags'] = game_tags.extract()
            item['rating'] = game_rating.extract()
            item['gamepage_link'] = game_link.extract()

            if gameinfo.xpath(".//div/img[contains(@src, 'downloadable')]"):
                # Go to game download page
                for href in game_link.extract():
                    url = response.urljoin(href)
                    nextrequest = scrapy.Request(url, callback=self.parse_download_screenshots)
                    nextrequest.meta['gameitem'] = item
                    yield nextrequest
            else:
                yield item

        # Go to Next page, repeat again
        nextpage = response.xpath("//div[@id='pager']"
                                  "/a[contains(@class,'pager-next')]/@href")
        if nextpage:
            nextpagelink = nextpage.extract()
            if nextpagelink:
                href = nextpagelink[0]          # There is two same pagers, but we need only one
                url = response.urljoin(href)
                yield scrapy.Request(url, callback=self.parse)

    def parse_download_screenshots(self, response):
        game_download = response.xpath("//div[@class='game_downloadpicture']/a/@href")
        screenshots = response.xpath("//div[@class='screenshotimage']/img/@src")

        preitem = response.meta['gameitem']
        preitem['download_link'] = game_download.extract()

        screenshots_path = [response.urljoin(href) for href in screenshots.extract()]
        preitem['screenshots_path'] = screenshots_path
        yield preitem