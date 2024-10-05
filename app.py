from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def find_records():
    return render_template('index.html', show_result=False, developer_name='Enes')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
