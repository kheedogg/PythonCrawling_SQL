# urlToStr2.py 수업진행

from urlToStr2 import urlToStr
#print(data)
from bs4 import BeautifulSoup
from tqdm import tqdm
import pymysql



datars = []


def naverCraw(page, cnt) :
    data = urlToStr('https://movie.naver.com/movie/point/af/list.nhn?&page='+str(page))
    bs=BeautifulSoup(data, 'html.parser')
    tit3s=bs.select('tbody > tr')
    for tit3 in tit3s:
        cnt=cnt+1
        datars1=[]
        mvname = tit3.find('a').text
        star = int( tit3.find('em').text)
        writer = tit3.select_one('.author').text
        cdate = tit3.find_all("td")[2].text[8:]
        #cdate = tit3.find_all('td')[2].text.split("****")[1]   # 20line과 동일 code
        story = tit3.find_all('td')[1].text.split('\n')[5]
        #story = tit3.find_all('td')[1].find_all('a')[1]['href'].split(',')[2]
        datars1.append(mvname)
        datars1.append(star)
        datars1.append(writer)
        datars1.append(cdate)
        datars1.append(story)
        #print(cnt, '.', mvname,'★', star, writer, cdate, ':', story)
        datars1 = tuple(datars1)
        datars.append(datars1)
        #print(datars1)
        #print('-'*30)
    return datars

def InsertData(totalData) :
    conn = pymysql.connect(host='localhost', user='root', password='root1234',
                        db='testdb', charset='utf8')
    curs = conn.cursor()
    sql = """
            insert into moviestar (mvname, star, writename, writedate, content) 
            values (%s, %s, %s, %s, %s)
        """
    curs.executemany(sql, totalData)
    conn.commit()   # insert하고나면 반드시 commit 필요
    conn.close()


def View(review, avg) :
    conn = pymysql.connect(host='localhost', user='root', password='root1234',
                        db='testdb', charset='utf8')
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT mvname, COUNT(*) AS cnt, AVG(star) AS avge "
    sql = sql + "FROM moviestar "
    sql = sql + "GROUP BY mvname "        
    sql = sql + "HAVING cnt >" + str(review) + " AND avge >=" + str(avg) + ' '     
    sql = sql + "ORDER BY COUNT(*) DESC"
    #print(sql)
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)



# ##### 1page 내 추출

# data = urlToStr('https://movie.naver.com/movie/point/af/list.nhn?&page=1')
# bs=BeautifulSoup(data, 'html.parser')
# tit3s=bs.select('tbody > tr')
# for tit3 in tit3s:
#     mvname = tit3.find('a').text
#     star = int( tit3.find('em').text)
#     writer = tit3.select_one('.author').text
#     cdate = tit3.find_all("td")[2].text[8:]
#     #cdate = tit3.find_all('td')[2].text.split("****")[1]   # 20line과 동일 code
#     #story = tit3.find_all('td')[1].text.split('\n')[5]
#     story = tit3.find_all('td')[1].find_all('a')[1]['href'].split(",")[2].replace("'",'')
#     print(mvname, star, writer, cdate,':', story)
#     print('-'*30)


if __name__=='__main__' :
    totalData=[]
    cnt=0
    pbar = tqdm(total=10)
    for n in range(1,11):
        #print('-'*50)
        datars = naverCraw(n, cnt)
        totalData += datars
        cnt+=10
        pbar.update(1)
    #print(totalData)    # list 안에 한페이지를 담은 tuple들 존재확인

    # InsertData(tuple(totalData))
    review = int(input('최소 조회수를 입력하세요.'))
    avg = float(input('최소 평점을 입력하세요.'))

    View(review, avg)
    print()
    print('Finish')
















