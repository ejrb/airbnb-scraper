# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def split_path_and_querystring(url):
    qidx = url.index("?")
    return url[:qidx], url[qidx:]


class RoomSpider(scrapy.Spider):
    name = "room"
    allowed_domains = ["www.airbnb.co.uk"]

    def start_requests(self):
        urls = [
            "https://www.airbnb.co.uk/rooms/19278160?s=51",
            "https://www.airbnb.co.uk/rooms/1583556?s=51",
            "https://www.airbnb.co.uk/rooms/1963643?s=51",
        ]
        for url in urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse_room,
                wait_time=30,
                wait_until=(
                    EC.visibility_of_element_located(
                        (By.XPATH, '//div[contains(text(), "bedroom")]')
                    )
                    and EC.visibility_of_element_located(
                        (By.XPATH, '//div[contains(text(), "bathroom")]')
                    )
                ),
            )

    def parse(self, response):
        # scrapy complains if parse() isn't defined
        pass

    def parse_room(self, response):
        bedroom_result = response.css("div::text").re(r"([0-9]+) bedrooms?")
        bathroom_result = response.css("div::text").re(r"([0-9]+) bathrooms?")
        result = {
            "name": response.css("div#summary")
            .css("div[itemprop=name] > span > h1 > span::text")
            .get(),
            "num_bedrooms": bedroom_result[0] if bedroom_result else 0,
            "num_bathrooms": bathroom_result[0] if bathroom_result else 0,
        }

        base_url, querystring = split_path_and_querystring(response.url)
        yield SeleniumRequest(
            url=base_url + "/amenities" + querystring,
            callback=self.parse_amenities,
            wait_time=40,
            wait_until=EC.visibility_of_element_located(
                (By.XPATH, '//div[@aria-label="Amenities"][@role="dialog"]')
            ),
            priority=1,
            meta={"result": result,},
        )

    def parse_amenities(self, response):
        yield {
            **response.meta["result"],
            "amenities": response.css('div[role="dialog"]')
            .css("section > div > div > div::text")
            .getall(),
        }
