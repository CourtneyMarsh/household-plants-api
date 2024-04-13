fake_database_plants = {
    "SnakePlant": {
        "Watering": {
            "Frequency": "Once every two weeks",
            "TapWater": False,
            "Temperature": "Lukewarm"
        }

    }
}

fake_database_user_plants = {

}


def get_all_plant_details(plant_name):
    return fake_database_plants[plant_name]


def get_feature_details(plant_name, feature):
    return fake_database_plants[plant_name][feature]


def get_plant_detail(plant_name, feature, detail):
    return fake_database_plants[plant_name][feature][detail]


def create_plant_entry(nickname, last_watered, plant_name):
    if not fake_database_plants.get(plant_name):
        return 500

    obj = {
        "LastWatered": last_watered,
        "PlantType": fake_database_plants[plant_name]
    }
    fake_database_user_plants[nickname] = obj
    return fake_database_user_plants[nickname]
