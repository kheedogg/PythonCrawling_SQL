

from urlToStr2 import urlToStr
data = urlToStr('https://movie.daum.net/boxoffice/yearly')
#print(data)


from bs4 import BeautifulSoup
bs=BeautifulSoup(data, 'html.parser')



""" year=bs.select_one('a.date_calender')
print(type(year))
print(year)
 """

#mArticle > ul > li:nth-child(1) > div.wrap_movie > div > a
lis=bs.select('#mArticle ul li')
print(lis) # li 들 쉼표(,)로 구분되어 출력


n=0
for li in lis:
    taga=li.select_one('.desc_boxthumb > .tit_join > a')
    if taga:
        n=n+1
        print(n, '위',taga.text)
    print('-'*30)

    if n==10: break



















