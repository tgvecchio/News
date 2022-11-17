def run_news():
	ids = ('abc-news',
		   'al-jazeera-english',
		   'ars-technica',
		   'bbc-news',
		   'bloomberg',
		   'business-insider-uk',
		   'buzzfeed',
		   'cbc-news',
		   'cbs-news',
		   'cnn',
		   'engadget',
		   'entertainment-weekly',
		   'espn',
		   'financial-post',
		   'fortune',
		   'four-four-two',
		   'fox-news',
		   'google-news',
		   'google-news-uk',
		   'hacker-news',
		   'independent',
		   'mashable',
		   'medical-news-today',
		   'msnbc',
		   'national-geographic',
		   'nbc-news',
		   'news24',
		   'new-scientist',
		   'newsweek',
		   'new-york-magazine',
		   'next-big-future',
		   'politico',
		   'polygon',
		   'recode',
		   'reuters',
		   'rte',
		   'techcrunch',
		   'techradar',
		   'the-globe-and-mail',
		   'the-hill',
		   'the-huffington-post',
		   'the-irish-times',
		   'the-next-web',
		   'the-verge',
		   'the-wall-street-journal',
		   'the-washington-post',
		   'the-washington-times',
		   'time',
		   'usa-today',
		   'vice-news',
		   'wired')

	try:
		for i in random.sample(ids, 4):
			njson = api.get_top_headlines(sources=i)
			for i in njson['articles']:
				# if i['publishedAt'] == None:
				string1 = ('' + i['title'] + '   ')
				print(string1)
				print('//', i['description'], '//', i['content'], '//', '', i['url'])
				print()
	except TypeError:
		pass
