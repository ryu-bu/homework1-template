from flask import Flask, render_template, request, jsonify
from main import calc_score


api_json = []
app = Flask(__name__)

@app.route('/api/inputs', methods=['GET'])
def get_api():
    return jasonify(api_json)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-score', methods=['GET', 'POST'])
def generate_score():
    args = request.args
    inp = args['input']
    output = args['output']
    ucf = args['ucf']
    verilog = args['verilog']
    print(verilog, inp, output, ucf)
    score = calc_score(verilog, inp, output, ucf) 

    return render_template('score.html', score=score)



if __name__ == '__main__':
    
    app.run()