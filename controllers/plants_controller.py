from services import plants_service
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/get-all-plant-details/<plant_name>")
def get_all_plant_details(plant_name):
    data = plants_service.get_all_plant_details(plant_name)
    return jsonify(data)


@app.route("/get-feature-details/<plant_name>/<feature>")
def get_feature_details(plant_name, feature):
    data = plants_service.get_feature_details(plant_name, feature)
    return jsonify(data)


@app.route("/get-plant-detail/<plant_name>/<feature>/<detail>")
def get_plant_detail(plant_name, feature, detail):
    data = plants_service.get_plant_detail(plant_name, feature, detail)
    return jsonify(data)


@app.route("/create-plant-entry", methods=["POST"])
def create_plant_entry():
    data = request.get_json()
    return jsonify(plants_service.create_plant_entry(data["Nickname"], data["LastWatered"], data["PlantName"]))


if __name__ == "__main__":
    app.run(debug=True)


