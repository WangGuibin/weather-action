from bs4 import BeautifulSoup

soup = BeautifulSoup(open('result.html'),"html.parser")
titleArr = soup.select('.u')
#标题
headerTitle = titleArr[0].get_text()
formatText = headerTitle + '\n'

#新闻
newsStr = ""
newsElement = soup.select('.news-wrap > .line')
for div in newsElement:
	news = div.get_text() + '\n'
	newsStr += news
formatText += newsStr + '\n'

#历史上的今天
historyTitle = soup.select('.u')[1].get_text()
formatText += historyTitle + '\n'
historyArr = soup.select('.history-wrap > .line a')
index = 0
history = ''

for a in soup.select('.history-wrap > .line a'):
	index += 1
	history += str(index) + '. ' + a.get_text() + '\n'

formatText += history + '\n'

#时间进度条
progress = '时间进度条: ' + soup.select('.progress-bar')[0].get_text()
progress_text = soup.select('.line')[-1].get_text()
formatText += progress + '\n'
formatText += progress_text + '\n'
filename = 'result.txt'
with open (filename,'w') as file:
    file.write(formatText)   






