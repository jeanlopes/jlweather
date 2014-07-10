#!/usr/bin/python

URL = 'https://www.google.com/search?q=()+temperature'
FORECAST_EL = '#wob_dc'
TEMPERATURE_EL = '#wob_tm'

headers = {'scheme':'https',
		   'version':'HTTP/1.1',
		   'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		   'accept-encoding':'gzip,deflate,sdch',
		   'accept-language':'pt-BR,pt;q=0.8,en-US;q=0.6,en;q=0.4',
		   'cache-control':'max-age=0',
		   'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
