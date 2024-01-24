from bs4 import BeautifulSoup #pip install bs4
import request

resp = requests.get(url)



category=['P','E','L']

print(resp)
print(type(resp))
print(list(resp))

soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)
title_tags = soup.select('.sh_text_headline')
print(title_tags)
print(len(title_tags))
print(type(title_tags[0]))
titles=[]
for title_tag in title_tags:
    re.compile('[^가-힝|a-z|A-Z|').sub(' ', title_tage.text)


re_title = re.compile('[^가-힣')
headers = {'User-Agent":'mozilla}

for i in range(6):
    url:
    resp= requests.get(url,header=headers)
    soup=BeautifulSoup(resp.textm,'html.parser')
    title_tags = soup.select('.sh_text')
    titles=[]
    for title_tag in title_tags :
        titles.append()
    df_section_titles = pd.DataFrame(titles,)