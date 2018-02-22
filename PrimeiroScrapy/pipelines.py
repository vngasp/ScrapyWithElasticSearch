# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PrimeiroscrapyPipeline(object):
    def process_item(self, item, spider):
        
        # Após um item ser coletado pelo spider e enviado o Item Pipeline que fica dentro do arquivo pipelines.py. É nessa parte do projeto 
        # que fazemos a limpeza dos dados, validações, checar duplicidade e armazenar os dados no banco de dados.   

        return item
