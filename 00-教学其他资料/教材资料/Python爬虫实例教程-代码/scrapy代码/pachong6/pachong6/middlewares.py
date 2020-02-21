# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import scrapy


class Pachong6DownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        chrome_options = Options()
        chrome_options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        driver = webdriver.Chrome(executable_path = r'D:\sp\chromedriver.exe',options = chrome_options)
        time.sleep(1)
        driver.get(request.url)
        time.sleep(1.5)
        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        time.sleep(1.5)
        content = driver.page_source.encode('utf-8')
        driver.quit()
        return scrapy.http.HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
        
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
#        chrome_options = Options()
#        chrome_options.add_argument('--ignore-certificate-errors')
#        chrome_options.add_argument('--headless')
#        chrome_options.add_argument('--disable-gpu')
#        chrome_options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
#        driver = webdriver.Chrome(executable_path = r'D:\sp\chromedriver.exe',options = chrome_options)
