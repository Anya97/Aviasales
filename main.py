from flask import Flask
import csv_reder
from database_service import get_fligths_by_id

app = Flask(__name__)


@app.route('/flights/<id>')
def get_flights_by_id(id):
    return get_fligths_by_id(int(id)).to_dict()


if __name__ == '__main__':
    csv_reder.read_data_from_file()
    app.run(port=8080)
