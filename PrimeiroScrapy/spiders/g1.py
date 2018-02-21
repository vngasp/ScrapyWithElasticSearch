# -*- coding: utf-8 -*-
import scrapy

# Classe que contem as propriedades que iremos extrair
from PrimeiroScrapy.items import PrimeiroscrapyItem

# Classe do Scrapy que vamos utilizar
from scrapy.contrib.spiders             import CrawlSpider, Rule
from scrapy.linkextractors              import LinkExtractor
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
            Rule(LinkExtractor(allow=[]), callback=('parse_item'),follow=True),
        )

    # Este método será o resonsável por analisar o código html e coletar as informações
    def parse_item(self, response):
        
        # Após acessar a pagina precisamos navegar entre as tags html até encontra no tão precisos dado
        # Podemos fazer isso de várias formas utlizando algumas bibliotecas disponíveis como;
        # BeautifulSoup
        # lxml
        # O Scrapy tem seu proprio mecanismo de extração de dados, o HtmlXPathSelector(). Ele permite "selecionar"
        # parte do HTML utilizando Xpath
        # Xpath é uma linguagem para selecionar Nós em XML, que pode ser usada com HTML, não é lindo isso.
        # Dito isso, vamos criar um objeto da classe HtmlXPathSelector()
        hrx = HtmlXPathSelector()


        # Lembra da classe que implementamos dentro do arquivo items.py, então, é aqui que vamos utlizar ela.
        # Vamos instanciamos um objeto item da classe PrimeiroscrapyItem()
        item = PrimeiroscrapyItem()

        # Legal, até aqui tudo tranquilo. Agora chegou a hora de coletar o dados efetivamente.
        # item['url'] = Precisamos saber qual a url que estamos coletando os dados, para fazer isso utilizamos um metodo da
        # classe HtmlXPathSelector() chamado "url" que já coleta essa informação pra gente
        # item['conteudo'] = Queremos também o conteudo inteiro da página. Isso é simple, basta usar o metodo xpath
        # e navegar até o item ou usar uma marcação pronta "//body" que irá coletar todo conteudo dentro dentro das tags
        # <body> </body> do site. Lindo, não é?
        # item['categoria'] = Deixei esse por último pois é o mais emocionante. Aqui vamos conhecer mais uma ferramenta do Scrapy
        # chamada "shell". 
        #-------------- Shell
        # O shell do Scrapy permite você analisar a sua extração de dados sem precisar rodar todo seu código, isso 
        # facilita muito,  pois, você pode testar seus Xpath de forma rápida é só implementar no seu codigo depois que tiver
        # estiver funcionando.
        # Para executar o Shell é muito simple, veja o código abaixo.
        # ------- Código
        # scrapy shell <link da pagina>

        url         = hrx.url
        conteudo    = hrx.xpath('//body').extract_first()
        categoria   = hrx.xpath('//div[@class = "header-title-content"]').extract_first()

        yield{
            'url': url,
            'categoria': categoria,
            'conteudo': conteudo
        }