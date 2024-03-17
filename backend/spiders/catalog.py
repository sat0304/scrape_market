import csv
import json
import logging
import pandas as pd
import pickle
import re
import time
from json import JSONDecoder
import undetected_chromedriver as uc
import matplotlib.pyplot as plt

import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.common.exceptions import TimeoutException
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class CatalogSpider(scrapy.Spider):
    def __init__(self):
        self.driver = uc.Chrome()

    products_os = []
    settings = get_project_settings()
    name = "catalog"
    allowed_domains = ['ozon.ru', 'www.ozon.ru']
    start_urls = [ 'www.ozon.ru']
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='log.txt',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )

    def parse(self, response, **kwargs):
        smartphone = {"os_name": "1", "os_version": "2"}
        with open('ozon.csv', 'a', encoding='utf-8') as filecsv:
            csv.DictWriter(filecsv, fieldnames=["os_name", "os_version"]).writerow(smartphone)
        self.driver.quit()

    def parse_pages(self, response, **kwargs):
        url = 'https://www.ozon.ru/'
        yield SeleniumRequest(
            url=url,
            callback=self.parse,
        )

    def make_product_url_list(self):
        self.driver.get('https://www.ozon.ru/')
        time.sleep(3)
        for page in range(1, 101):
            if page == 1:
                url = f'https://www.ozon.ru/category/telefony-i-smart-chasy-15501/?sorting=rating'
            else:
                url = f'https://www.ozon.ru/category/telefony-i-smart-chasy-15501/?page={page}&sorting=rating'
            self.driver.get(url)
            time.sleep(10)
            block = self.driver.find_element(By.CLASS_NAME, 'widget-search-result-container')
            href_list = block.find_elements(By.TAG_NAME, 'a')
            filename = 'smartphone_url.txt'
            with open(filename, 'a') as f:
                for href in href_list:
                    stringify_href = str(href.get_attribute('href'))
                    if '-smartfon-' in stringify_href:
                        f.write(stringify_href)
                        f.write('\n')
                        time.sleep(2)

    def make_smartphone_description(self):
        result_file = open('os_list.csv', 'a', encoding='utf-8')
        with open('smartphone_url.txt', 'r', encoding='utf-8') as f:
            line = f.readline()
            line_counter = 100
            while line and line_counter:
                self.driver.get(line)
                time.sleep(10)
                line_counter -= 1
                try:
                    os_value = WebDriverWait(self.driver, 20).until(
                        ec.visibility_of_any_elements_located(
                            (
                                By.XPATH,
                                "//dl[./dt/span[contains(text(),'Операци')]]/dd/a"
                            )))[0]
                    stringify_os_value = str(os_value.get_attribute("innerHTML"))
                    result_file.write(stringify_os_value)
                    result_file.write(',')
                except TimeoutException:
                    os_value = WebDriverWait(self.driver, 20).until(
                        ec.visibility_of_any_elements_located(
                            (
                                By.XPATH,
                                "//dl[./dt/span[contains(text(),'Операци')]]//a"
                            )))[0]
                    stringify_os_value = str(os_value.get_attribute("innerHTML"))
                    result_file.write(stringify_os_value)
                    result_file.write(',')
                if stringify_os_value == 'iOS':
                    try:
                        os_ver_value = WebDriverWait(self.driver, 20).until(
                            ec.visibility_of_any_elements_located(
                                (
                                    By.XPATH,
                                    "//dl[./dt/span[contains(text(),'Версия iOS')]]//a"
                                )))[0]
                        stringify_os_ver_value = str(os_ver_value.get_attribute("innerHTML"))
                        result_file.write(stringify_os_ver_value)
                    except TimeoutException:
                        os_ver_value = WebDriverWait(self.driver, 20).until(
                            ec.visibility_of_any_elements_located(
                                (
                                    By.XPATH,
                                    "//dl[./dt/span[contains(text(),'Версия iOS')]]/dd"
                                )))[0]
                        stringify_os_ver_value = str(os_ver_value.get_attribute("innerHTML"))
                        result_file.write(stringify_os_ver_value)
                    finally:
                        result_file.write('\n')
                else:
                    try:
                        os_ver_value = WebDriverWait(self.driver, 20).until(
                            ec.visibility_of_any_elements_located(
                                (
                                    By.XPATH,
                                    "//dl[./dt/span[contains(text(),'Версия Android')]]/dd"
                                )))[0]
                        stringify_os_ver_value = str(os_ver_value.get_attribute("innerHTML"))
                        result_file.write(stringify_os_ver_value)
                    except TimeoutException:
                        result_file.write('Android MUIU 14')
                    finally:
                        result_file.write('\n')
                line = f.readline()

    def get_stat_result(self):
        titles = ['os_name', 'os_version']
        os_list = pd.read_csv("os_list.csv",
                              names=titles, header=None)
        os_groups = os_list.groupby(['os_version']).agg(
            count_os=pd.NamedAgg(column="os_version", aggfunc="count")
        )
        os_groups = os_groups.sort_values(by=['count_os'], ascending=False)
        with open('stat_result.csv', 'a') as f:
            os_groups.to_csv(f)
        image_stat = os_groups.plot(kind='bar')
        fig = image_stat.get_figure()
        fig.savefig('image_stat.pdf')

    def start_requests(self):
        self.make_smartphone_description()
        self.make_product_url_list()
        self.driver.quit()
        self.get_stat_result()
        url = 'https://www.ozon.ru/'
        yield SeleniumRequest(
            url=url,
            callback=self.parse_pages,
        )
