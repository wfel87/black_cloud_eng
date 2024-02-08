from flask import Flask, render_template
from flask import Flask, render_template

app = Flask(__name__, template_folder='/Users/Wes/Desktop/python projects/HTML/templates', static_folder='/Users/Wes/Desktop/python projects/HTML/static')

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/backup_data', methods=['POST'])
def backup_data():
    # Implement data backup logic here
    return "Data backup successful."

if __name__ == "__main__":
    app.run(debug=False)
