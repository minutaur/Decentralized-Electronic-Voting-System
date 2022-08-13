chain = []
#투표함
block1 = {
    'type': 'open',
    'data': {
        'id': '투표ID',
        'question': '투표질문',
        'options': ['투표항목1', '투표항목2', '투표항목3']
    }
}
chain.append(block1)

#투표확인
block2 = {
    'type': 'vote',
    'data': {
        'id': '투표ID',
        'vote': '투표항목1',
    }
}
chain.append(block2)

print(chain)