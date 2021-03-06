# -*- coding: utf-8 -*-
""" TODO criar cabecalho bonitinho com licenca """
from httplib2 import Http
from urllib2 import quote
from lib.cssselect.xpath import HTMLTranslator
from lxml.html import fromstring
import jlweather_consts
import os
import pdb

class WeatherClient:        
    """ 
    Cliente que acessa um endereço remoto e obtém a temperatura a partir de um local guardado na cache

    """

    def __check_place(self, new_place=None):
        """ __check_place(new_place) 

            :new_place -> o novo lugar ex.: 'Porto Alegre+RS'
        """
        path = os.getenv('HOME') + '/.jlweather/'
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + 'places.cache', 'a+') as cache_file:
            current_place = cache_file.readline()
            if new_place and new_place != current_place:
                cache_file.seek(0)
                cache_file.write(new_place)
                current_place = new_place

        return current_place

    def set_place(self, city, uf):
        """ 
        set_place(city, uf)

        :city -> cidade ex.: Porto Alegre
        :uf -> estado ex.: RS

        """
        self.__check_place(city.strip() +'+'+ uf.strip())

    def get_place(self):
        ''' retorna a localidade atual '''
        return self.__check_place()


    def reload_weather_info(self):
        """ 
        Método responsável por obter informações sobre a temperatura a partir do endereço weather_consts.URL

        uso do cssselect (fromstring)
        http://pythonhosted.org//cssselect/#quickstart
        """
        
        place = self.__check_place()
        place = quote(place)
        url = jlweather_consts.URL.replace('()', place)
        response = Http().request(url, headers=jlweather_consts.headers)
        html_result = response[1]

        trans = HTMLTranslator()
        expr_forecast = trans.css_to_xpath(jlweather_consts.FORECAST_EL)
        expr_temp = trans.css_to_xpath(jlweather_consts.TEMPERATURE_EL)

        google_document = fromstring(html_result)
        forecast = google_document.xpath(expr_forecast)[0].text
        temperature = google_document.xpath(expr_temp)[0].text
        return forecast, temperature
