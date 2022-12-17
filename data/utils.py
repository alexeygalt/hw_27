import csv
import json

csv_file_ads = 'ad.csv'
json_file_ads = '../ads/fixtures/ads.json'
ads_model = 'ads.ad'

csv_file_categories = 'category.csv'
json_file_categories = '../ads/fixtures/categories.json'
categories_model = 'ads.category'

csv_file_locations = 'location.csv'
json_file_locations = '../ads/fixtures/locations.json'
locations_model = 'ads.location'

csv_file_users = 'user.csv'
json_file_users = '../ads/fixtures/users.json'
users_model = 'users.user'


def replace_values(value):
    """Convert digits and bool values into required types"""
    if value.isdigit():
        return int(value)
    if value == 'TRUE' or value == 'FALSE':
        return bool(value)

    return value


def converter_to_json(csv_path: str, json_path: str, model):
    """Convert csv to json"""
    with open(csv_path, encoding='utf-8') as file:
        csv_rows = csv.DictReader(file, delimiter=',', quotechar='"')
        result = []
        for row in csv_rows:
            result.append({
                'model': model,
                'pk': int(row['id'] if row.get('id') else int(row['Id'])),
                'fields': {key: replace_values(value) for key, value in row.items() if key != 'Id' and key != 'id'}
            })

    with open(json_path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(result, indent=4, ensure_ascii=False))

    return f'Data from csv ({csv_path}) converted to json ({json_path})'


if __name__ == '__main__':
    print(converter_to_json(csv_file_categories, json_file_categories, categories_model))
    print(converter_to_json(csv_file_ads, json_file_ads, ads_model))
    print(converter_to_json(csv_file_locations, json_file_locations, locations_model))
    print(converter_to_json(csv_file_users, json_file_users, users_model))


# python3 manage.py loadall python3 manage.py loaddata file.json