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

    # Aqui podemos definir que nosso spider só acesse páginas do dominio parametrizado
    # Isso é necessário em nosso projeto, pois o objetivo do nosso spider e acessar todos os link encontrados nas
    # paginas analisadas, mas pode ser que contenham link de outros dominios, então defimos aqui quais os dominios
    # que o spider poderá analisar.
    allowed_domains = ['www.g1.com.br']

    # Aqui definimos a url que nosso spider irá iniciar.
    start_urls = ['http://www.g1.com.br/']

    # O método callback "parse" é responsável por acessar(request) as url's  
    def parse(self, response):
        
        # SgmlLinkExtractor() e um objeto que tem o proposito de achar link dentro das paginas acessadas
        # Dentro do SgmlLinkExtractor() podemos definir algumas regras para a extração dos itens atraves do objeto Rule()
        # Para o nosso caso estamos definindo a função de callback que será executada para cada link encontrado
        # e o parametro "follow" para ele busque outras urls dentro da pagina que esta sendo acessada.
        # Assim garantimos que nosso spider não vai deixa passar nada. 
        rules = (
            Rule(SgmlLinkExtractor(allow=[]), callback=('parse_item'),follow=True),
        )

    # Este método será o resonsável por analisar o código html e coletar as informações
    def parse_item(self, response):
        pass