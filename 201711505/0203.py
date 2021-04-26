# urlToStr2.py 수업진행

from urlToStr2 import urlToStr
data = urlToStr('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
print(data)


from bs4 import BeautifulSoup
bs=BeautifulSoup(data, 'html.parser')


meta=bs.meta
print(meta)

div=bs.div
print(div)

a=bs.a
print(a)

p=bs.p
print(p)
print(type(p))


p1=bs.find('p')
print(p1)
print(type(p1))


ps=bs.find_all('p')
print(ps)
print(type(ps))


for p in ps:
    print(p)
    print('-'*30)


for p in ps:
    print(p.text)
    print('-'*30)



p1 = bs.select_one('p')
#print(p1.text)
print(p1)
print('-'*30)


tit3=bs.select_one('.tit3')
print(tit3)
print('-'*20)


tit3s=bs.select('.tit3')
print(tit3s)
print('-'*20)

print(type(tit3s))
# print(tit3s.text) 오류나는 것 확인
for tit3 in tit3s :
    print(type(tit3.text))
    print(tit3.text)
    print('*'*30)

for tit3 in tit3s :
    print(tit3.text.replace('\n',''))
print('-'*20)

##### 변동순위 뽑기1
rang=bs.select_one('td.range.ac')
print(type(rang))
rangs=bs.select('td.range.ac')
print(type(rangs))
#print(rnag.text) list 이기 때문에 불가능
for rang in rangs :
    print(type(rang.text))
    print(rang.text)
    print('*'*30)

for rang in rangs:
    print(rang.text.replace('\n',''))
print('-'*20)



##### 변동순위&제목 뽑기
tit3s=bs.select('tbody > tr')
for tit3 in tit3s:
    print(tit3.select_one('.tit3'))
    print(tit3.select_one('.range.ac'))
    print('-'*20)

for tit3 in tit3s:
    tit3_tags = tit3.find_all('td') # td가 4개 나오는 것에서 우리가 추출할 정보가 들어있음.
    print(tit3_tags)
    print('-'*30)

for tit3 in tit3s:
    tit3_tags = tit3.find_all('td') # 페이지 화면 내 공백선 부분이 td 값이 1로 나오는 것을 알 수 있음.
    print(len(tit3_tags))
    print('-'*30)

for tit3 in tit3s:
    tit3_tags = tit3.find_all('td') # 페이지 화면 내 공백선 부분이 td 값이 1로 나오는 것을 알 수 있음.
    if (len(tit3_tags) ==4 ) :
        print(tit3_tags[1].text.replace('\n','')+ " : "+ tit3_tags[3].text.replace('\n',''))
        print('-'*30)


for tit3 in tit3s:
    tit3_tags = tit3.find_all('td')
    if ( len(tit3_tags)==4 ):
        print(tit3_tags[0].find('img'))
        print(tit3_tags[1].find('a'))
        print(tit3_tags[2].find('img'))
        print(tit3_tags[3].text)
    print('-'*30)

 
# for tit3 in tit3s:
#     tit3_tags = tit3.find_all('td')
#     if ( len(tit3_tags)==4 ):
#         print(tit3_tags[0].find('img').get('alt'))  # 이미지가 없는 번호 32, 49가 없기 때문에 오류 발생
#         print(tit3_tags[1].find('a').text)
#         print(tit3_tags[2].find('img')['src'])
#         print(tit3_tags[3].text)
#     print('-'*30)
#  Toggle Line Comment Ctrl+/
#  Toggle Block Comment Shift+Alt+A
        
for tit3 in tit3s:
    tit3_tags = tit3.find_all('td')
    if ( len(tit3_tags)==4 ):
        if tit3_tags[0].find('img'):
            print(tit3_tags[0].find('img')['alt'])
        print(tit3_tags[1].find('a').text)
        print(tit3_tags[2].find('img')['src'])
        print(tit3_tags[3].text)
    print('-'*30)


























