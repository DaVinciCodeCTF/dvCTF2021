from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        try:
            if '칠팔육육' in request.values.get('code'):
                return 'dvCTF{It_1s_0p3n_7866}'
            else:
                return render_template('index.html')
        except:
            return render_template('index.html')
