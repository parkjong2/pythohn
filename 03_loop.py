'''
n = 0
while n < 5:
    print('대표님 열심히 일하겠습니다.')
    n = n + 1
'''

numbers = [1, 2, 3, 4, 5, 6]
#numbers에서 for문을 이용해 요소를 꺼내 각각의 요소에 2를 곱해주세여.
'''
for number in numbers:
    print(number*2, end =' ,')
'''
new_numbers = []
for number in numbers:
    new_numbers.append(number*2)
    print(new_numbers)
    