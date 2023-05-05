export FLASK_APP=run.py
flask db upgrade
python3 migrate_users.py
flask run -h 0.0.0.0 -p 25000
