from repositories import plants_repository


def get_all_plant_details(plant_name):
    return plants_repository.get_all_plant_details(plant_name)


def get_feature_details(plant_name, feature):
    return plants_repository.get_feature_details(plant_name, feature)


def get_plant_detail(plant_name, feature, detail):
    return plants_repository.get_plant_detail(plant_name, feature, detail)


def create_plant_entry(nickname, last_watered, plant_name):
    return plants_repository.create_plant_entry(nickname, last_watered, plant_name)