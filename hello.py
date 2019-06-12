#hello.py

#최초 실행 = shift+alt+f10
#반복 실행 = shift+f10

#문자열은 통상 싱글쿼트로 표기
print('hello world')

a = 1
b = 1

#들여쓰기 레벨로 하나의 블록 구분
#블록 시작 = :(콜론 기호)
#빈 블록 = pass
if a == 1:
    print('park')
    print('jin')
    print('young')

    #int i = 1; i<10; i++와 동일
    for i in range(1,10):
        print('',i)

print('end')

def add(m,n):
    return m+n

def mymax(m,n):
    if m > n:
        return m
    else:
        return n

print(add(a,b))
print(mymax(a,b))
