
#1. PyMySql 모듈을 import
import pymysql

#2. MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='root1234',
                        db='testdb', charset='utf8')
    # DB와 Python을 연결하는 특정 다리의 이름이 conn이 된다.


#3.Connection 으로부터 Cursor 생성 => Dictoionary Cursor 생성
curs = conn.cursor()
#curs = conn.cursor(pymysql.cursors.DictCursor)   # dictionary type으로 읽는 방법

 
#4.SQL문 실행
#sql = "select * from codes"

# sql = """select concat( substring(fullcd,1,2), '-',
#                         substring(fullcd,3,2), '-',
#                         substring(fullcd,5,3) ),
#                         kornm
#                         from codes
#                         """


#curs.execute(sql)
                        

# ###PYTHON에서 DB에 데이터 삽입 방법
# sql = "insert into codes values ('0105019', 'test1', '')"
# curs.execute(sql)
# conn.commit()

# ###PYTHON에서 DB 자료 수정 방법
# sql = "update codes set kornm = '금정구' where fullcd = '0105018'"
# curs.execute(sql)
# conn.commit()
 
# ###PYTHON에서 DB 자료 삭제 방법
# sql = "delete from codes where fullcd='0105019'"
# curs.execute(sql)
# conn.commit()


#5.데이타를 서버로부터 가져온 후, Fetch 된 데이타를 사용
rows = curs.fetchall()
print(rows)     # 전체 rows =>튜플 

print('-'*30)
#print(rows[0])

# for row in rows :
#     print(row['fullcd'],row['kornm'])  # dictionary type으로 읽은 경우 for문


# for row in rows :
#     for item in row :
#         print( item , end= ' ')
#     print()

# print('-'*30)
# for row in rows :
#     print( row[0][:2], row[0][2:5], row[0][5:], ' ', row[1], sep='' )
    
#6.Connection 닫기
conn.close()
    # DB와의 다리 연결을 끊어줘야 다른사람들도 이용가능하다.
































