from flask import Flask, request, render_template
from secrets import token_bytes
from os import system, remove
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/print_my_homework', methods=['POST'])
def print_my_homework():
    if 'homework' in request.form:
        to_render = request.form['homework']
        token = token_bytes(4).hex()
        sanitized = []
        for line in to_render.split('\n'):
            if '```' in line:
                line = line.replace(' ', '')
                if '```{' in line:
                    sanitized.append('```')
                else:
                    sanitized.append(line)
            else:
                sanitized.append(line)
        with open(f"/app/rscripts/{token}.Rmd", "w") as tmpfile:
            tmpfile.write('\n'.join(sanitized))
        try:
            system(f"Rscript /app/rscripts/render.R /app/rscripts/{token}.Rmd")
            with open(f"/app/rscripts/{token}.html", "r") as tmpfile:
                contents = tmpfile.read()
            remove(f"/app/rscripts/{token}.html")
        except:
            contents = "Error while compiling the homework"

        remove(f"/app/rscripts/{token}.Rmd")

        return contents
    else:
        return render_template('index.html')
