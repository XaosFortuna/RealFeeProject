import os

#PATHES
cwd = os.path.dirname(os.path.realpath(__file__)) + '\\'


#DATABASE CONFIGURATIONS
DBName = 'CurrencyDB.db'
TableName = 'Currencies'



#DELIMITERS
DelimitersList = {
			'HaratDollar' : '\xD9\x87\xD8\xB1\xD8\xA7\xD8\xAA', 
			'IstanbulDollar': '\xD8\xA7\xD8\xB3\xD8\xAA\xD8\xA7\xD9\x86\xD8\xA8\xD9\x88\xD9\x84',
			'SoleimaniehDollar' : '\xD8\xB3\xD9\x84\xDB\x8C\xD9\x85\xD8\xA7\xD9\x86\xDB\x8C\xD9\x87',
			'NaghdiDollar' : '\xD9\x86\xD9\x82\xD8\xAF\xDB\x8C',
			'KaghaziDollar' : '\xDA\xA9\xD8\xA7\xD8\xBA\xD8\xB0\xDB\x8C'
			}