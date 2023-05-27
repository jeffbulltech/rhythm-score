from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///activities.db'
db = SQLAlchemy(app)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

@app.route('/', methods=['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'POST':
        type = request.form.get('type')
        duration = int(request.form.get('duration'))
        new_activity = Activity(type=type, duration=duration)
        db.session.add(new_activity)
        db.session.commit()
    elif request.method == 'DELETE':
        db.session.query(Activity).delete()
        db.session.commit()

    activities = Activity.query.all()
    work_hours = sum(a.duration for a in activities if a.type == 'work')
    life_hours = sum(a.duration for a in activities if a.type == 'life')
    rhythm_score = (life_hours / (work_hours + life_hours)) * 100 if work_hours + life_hours > 0 else 0
    
    if work_hours > life_hours:
        rhythm_statement = "Your rhythm currently favors Work over Life."
    elif life_hours > work_hours:
        rhythm_statement = "Your rhythm currently favors Life over Work."
    else:
        rhythm_statement = "Your rhythm is in harmony."
    
    return render_template('index.html', activities=activities, rhythm_score=rhythm_score, rhythm_statement=rhythm_statement)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
