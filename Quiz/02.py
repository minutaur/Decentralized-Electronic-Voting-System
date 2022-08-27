import requests
import json

while True:
    print('1.블록 체인 조회')
    print('2.투표 생성')
    print('3.투표')
    print('4.종료')

    menu = input('=>')

    if menu == '1':
        res = requests.get('http://127.0.0.1:5000/list')
        print(res.text)


    elif menu == '2':
        headers = {'Content-Type': 'application/json'}

        question = input('질문:')
        option1 = input('선택지1')
        option2 = input('선택지2')
        option3 = input('선택지3')

        data = {
            'question': question,
            'options': [option1, option2, option3]
        }

        res = requests.post('http://127.0.0.1:5000/open', data=json.dumps(data), headers=headers)

        print(res.text)




    elif menu == '3':
        pass

    elif menu == '4':
        break
