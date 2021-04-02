from flask import Flask, render_template, request, jsonify
from main import calc_score
from optimization import optimize

app = Flask(__name__)

@app.route('/')
def index():
    """This is the home page of the app. It renders index.html

    Returns:
        index.html
    """
    return render_template('index.html')

@app.route('/about')
def about():
    """This is the about page. It renders about.html

    Returns:
        about.html
    """
    return render_template('about.html')

@app.route('/generate-score', methods=['GET', 'POST'])
def generate_score():
    """This is /generate-score page. It renders score.html.

    Query string format:
    /generate-score?verilog=[verilog_file]&input=[input_file]&output=[output_file]&ucf=[ucf_file]

    Returns:
        score.html
    """
    args = request.args
    inp = args['input']
    output = args['output']
    ucf = args['ucf']
    verilog = args['verilog']
    print(verilog, inp, output, ucf)

    # run optimizaiton and create a modifled file under "modified" directory
    data = optimize(inp)

    # calculate score

    score = calc_score(verilog, inp, output, ucf) 
    modified_file = f'{inp}.input.json'

    return render_template('score.html', score=score, file=modified_file, data=data)


if __name__ == '__main__':
    
    app.run()