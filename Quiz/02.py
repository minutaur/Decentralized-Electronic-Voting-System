from flask import Flask, jsonify, request

app = Flask(__name__)

chain = []
cnt = 0


@app.route("/",methods = ['POST', 'GET'])  # 3
def hello():
    return '''<!DOCTYPE HTML><html>
      <body>
        <h1>1.블록 체인 조회</h1><br>
        <h1>2.투표 생성</h1><br>
        <h1>3.투표</h1><br>
      </body>
    </html>'''


def result():
    if request.method == 'POST':
        request.form
        return '''
      <!doctype html>
        <html>
           <body>

              <table border = 1>
                 {% for key, value in result.items() %}

                    <tr>
                       <th> {{ key }} </th>
                       <td> {{ value }} </td>
                    </tr>
                 {% end-for %}
              </table>

           </body>
        </html>
'''

if __name__ == '__main__':
    app.run()



@app.route('/list', methods=['GET'])
def vote_list():
    return jsonify(chain)


@app.route('/open', methods=['POST'])
def vote_open():
    global cnt
    try:
        data = request.get_json()
        block = {
            'type': 'open',
            'data': {
                'id': str(cnt),
                'question': data['question'],
                'options': data['options']

            }
        }

        cnt += 1
        chain.append(block)
        return jsonify({'status': 'success'})

    except:
        return jsonify({'status': 'failed'})


@app.route('/vote', methods=['POST'])
def vote():
    try:
        data = request.get_json()
        block = {
            'type': 'vote',
            'data': {
                'id': data['id'],
                'vote': data['vote']

            }
        }
        chain.append(block)
        return jsonify({'status': 'success'})

    except:
        return jsonify({'status': 'failed'})


app.run()
