# -*- coding: utf-8 -*-
import scrapy

# Classe que contem as propriedades que iremos extrair
from PrimeiroScrapy.items import PrimeiroscrapyItem

# Classe do Scrapy que vamos utilizar
from scrapy.contrib.spiders             import CrawlSpider, Rule
from scrapy.linkextractors              import LinkExtractor
from scrapy.selector                    import HtmlXPathSelector


class G1Spider(CrawlSpider):

    # Para cada spider dentro do projeto é definido um nome único.  
    name = 'g1'

    # Aqui podemos definir que nosso spider só acesse páginas do dominio parametrizado
    # Isso é necessário em nosso projeto, pois o objetivo do nosso spider e acessar todos os link encontrados nas
    # paginas analisadas, mas pode ser que contenham link de outros dominios, então defimos aqui quais os dominios
    # que o spider poderá analisar.
    allowed_domains = [
        'g1.globo.com'
    ]

    # Aqui definimos a url que nosso spider irá iniciar.
    start_urls = [        
        'http://g1.globo.com/',
    ]
        
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
        hrx = HtmlXPathSelector(response)

        # Lembra da classe que implementamos dentro do arquivo items.py, então, é aqui que vamos utlizar ela.
        # Vamos instanciamos um objeto item da classe PrimeiroscrapyItem()
        item = PrimeiroscrapyItem()

        # Legal, até aqui tudo tranquilo. Agora chegou a hora de coletar o dados efetivamente.
        # item['url'] = Precisamos saber qual a url que estamos coletando os dados, para fazer isso utilizamos o metodo "url" do response
        # item['categoria'] = Aqui nós temos um problema. Queremos coletar a categoria principal do site Ex:. Economia, Tecnologia, etc..
        # Mas dentro do HTML não temos um pouco fixo que podemos coletar essa informação, então a solução mais plausivel foi quebrar a string da url
        # e pegar o texto após a barra "g1.globo.com.br/" que sempre será a categoria principal do conteudo.
        # item['conteudo'] = Deixei esse por último pois é o mais emocionante. Queremos também o conteudo inteiro da página. Isso é simple, basta usar o metodo xpath
        # e navegar até o item ou usar uma marcação que contenhã no HTML, no caso do G1 temos a tag "//article". Como só queremos os textos utilizamos a função 
        # normalize-space() que irá retirar todas as tags HTML, deixando somente os textos. Lindo, não é?
        # Você deve estar se perguntando. Mas como ele sabe que existe a tag //article no G1? Inspesionando o código HTML do site, simples assim!
        # Ok, então eu tenho que excutar o meu crawler e ficar testando o xpath até conseguir coletar o dados corretamente? 
        # Não! Nós podemos usar o shell do Scrapy. 
        #-------------- Shell
        # O shell do Scrapy permite você analisar a sua extração de dados sem precisar rodar todo seu código, isso 
        # facilita muito,  pois, você pode testar seus Xpath de forma rápida é só implementar no seu codigo depois que tiver
        # estiver funcionando.
        # Para executar o Shell é muito simple, veja o código abaixo.
        # ------- Código
        # scrapy shell <link da pagina>

        item['url']         = response.url
        item['categoria']   = response.url.split("/")[3]
        item['conteudo']    = hrx.xpath('normalize-space(//article)').extract_first()


        yield item 