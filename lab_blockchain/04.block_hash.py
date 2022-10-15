import hashlib


def get_block_hash(block):
    data = dict()
    data['type'] = block['transaction']['type']
    data['data'] = sorted(block['transaction']['data'].copy().items())
    data = sorted(data.items())
    return hashlib.sha256(str(data).encode()).hexdigest()


chain = []

block1 = {
    'transaction': {
        'type': 'open',
        'data': {
            'id': '투표 ID',
            'question': '투표 질문',
            'options': ['투표 항목1', '투표 항목2', '투표 항목3']
        }
    }
}
block1['hash'] = get_block_hash(block1)

chain.append(block1)

block2 = {
    'transaction': {
        'type': 'vote',
        'data': {
            'id': '투표 ID',
            'vote': '투표 항목'
        }
    }
}
block2['hash'] = get_block_hash(block2)

chain.append(block2)

print(chain)