# -*- coding: utf-8 -*-
import scrapy

# Classe que contem as propriedades que iremos extrair
from PrimeiroScrapy.items from PrimeiroscrapyItem

# Classe do Scrapy que vamos utilizar
from scrapy.contrib.spiders             import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector                    import HtmlXPathSelector


class G1Spider(scrapy.Spider):

    # Para cada spider dentro do projeto é definido um nome único.  
    name = 'g1'

    # Aqui definimos a url que nosso spider irá iniciar.
    start_urls = ['http://www.g1.com.br/']

    # O método callback "parse" é responsável por acessar(request) as url's  
    def parse(self, response):
        pass

    # Este método será o resonsável por analisar o código html e coletar as informações
    def parse_item(self, response):
        pass