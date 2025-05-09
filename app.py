from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

voters = {}
votes = {"Candidate A": 0, "Candidate B": 0, "Candidate C": 0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    voter_id = request.form['voter_id']
    name = request.form['name']
    if voter_id not in voters:
        voters[voter_id] = {'name': name, 'has_voted': False}
        return redirect(url_for('index'))
    return "Voter already registered", 400

@app.route('/vote', methods=['POST'])
def vote():
    voter_id = request.form['voter_id']
    candidate = request.form['candidate']
    if voter_id in voters and not voters[voter_id]['has_voted']:
        if candidate in votes:
            votes[candidate] += 1
            voters[voter_id]['has_voted'] = True
            return redirect(url_for('index'))
    return "Invalid vote or duplicate voting attempt", 400

@app.route('/results')
def results():
    return render_template('admin.html', votes=votes)

if __name__ == '__main__':
    app.run(debug=True)
