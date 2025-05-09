from flask import Flask, render_template, request, redirect, url_for, flash
from flask import get_flashed_messages

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

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
        flash("Registration successful!", "success")
    else:
        flash("Voter already registered.", "error")
    return redirect(url_for('index'))

@app.route('/vote', methods=['POST'])
def vote():
    voter_id = request.form['voter_id']
    candidate = request.form['candidate']
    if voter_id in voters and not voters[voter_id]['has_voted']:
        if candidate in votes:
            votes[candidate] += 1
            voters[voter_id]['has_voted'] = True
            flash("Vote cast successfully!", "success")
        else:
            flash("Invalid candidate selected.", "error")
    else:
        flash("Invalid vote or duplicate voting attempt.", "error")
    return redirect(url_for('index'))

@app.route('/results')
def results():
    return render_template('admin.html', votes=votes)
