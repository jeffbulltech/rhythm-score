from rhythm_score import db, Activity, app

def clear_database():
    with app.app_context():
        db.session.query(Activity).delete()
        db.session.commit()

clear_database()