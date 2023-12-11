from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to the database
db = mysql.connector.connect(
    host="developeriq-db.cg9nkdufkidw.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="i42aws2023",
    database="developeriq_productivity"
)

cursor = db.cursor()

@app.route('/')
def hello_word():
    return "<p>Good Morning User!</p>"


@app.route('/submit/<int:employee_id>/<int:project_code>', methods=['POST'])
def submit_metrics(employee_id, project_code):
    # data = request.get_json()
    # employee_id = data['employee_id']
    # project_code = data['project_code']

    query = f"SELECT commit_count, issues_resolved, merge_frequency, mttr, build_success_rate FROM productivity_metrics WHERE user_id = {employee_id} AND repo_id = {project_code};"

    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        keys = ['commit_count', 'issues_resolved', 'merge_frequency', 'mttr', 'build_success_rate']
        metrics_dict = dict(zip(keys, result))
        return jsonify([metrics_dict])
    else:
        return jsonify({'error': 'Metrics not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
