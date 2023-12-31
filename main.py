import os
import time

from scraper import get_all_place

import csv
import json


def create_new_csv(places_dict_list, file_name, project_name):
    """
    this is used to create a  csv using the file name and the current places dictionary
    """
    try:
        # Get the field names from the keys of the first JSON object
        fieldnames = places_dict_list[0].keys()
        # write into the csv file

        file_path = f"{project_name}/{file_name}"

        print("The file name is :", file_name)
        print("The file path is :", file_path)
        print("Converting scraped data to csv ")
        print("🤭===================================🤭===================================🤭")
        print("🤭===================================🤭===================================🤭")
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write the CSV header
            csv_writer.writeheader()

            # Write each JSON object as a row in the CSV file
            for json_obj in places_dict_list:
                csv_writer.writerow(json_obj)
    except Exception as a:
        print(a)
        pass


def create_item_task(csv_file_path, project_name):
    """
    This function updates items based on data from a CSV file.


    :param csv_file_path: Path to the CSV file.
    :return: List of updated places.


    """
    all_places_dict = []

    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:

        csv_reader = csv.reader(csv_file)

        # Skip the header row (first row)

        next(csv_reader)
        all_categories = []
        all_places = []
        for row in csv_reader:
            all_categories.append(row[0])
            all_places.append(row[1])
        # loop through all the categories each category will go through for all places
        for category in all_categories:
            # if the category is none continue
            if category == '' or category is None:
                continue
            for place in all_places:
                # if the place is none continue
                if place == '' or place is None:
                    continue
                try:
                    place_dict = get_all_place(category, place)
                    if place_dict:
                        all_places_dict += place_dict
                    with open("all_places.json", 'w') as json_file:
                        #  dump the json and also write the csv
                        json.dump(all_places_dict, json_file, indent=4)
                        file_name = f"{category}_{place}.csv".replace(" ", "_")
                        create_new_csv(place_dict, file_name, project_name)
                except Exception as e:
                    print("Error:", e)
                    # In case of an error, write the data to a JSON file
                    error_data = {
                        "place": place,
                        "category": category,
                        "error": str(e)
                    }
                    with open("error_data.json", 'a') as json_file:
                        json.dump(error_data, json_file, indent=4)
                        json_file.write('\n')  # Add a new line after each entry
    return all_places_dict


def convert_searched_dictionary_to_csv():
    """

    this is used to load from and search from the csv
    :return:
    """
    # write into the csv file
    current_time = str(time.time()).replace(".", "")

    project_name = f"project_name_{current_time}"
    # create a directory for the project
    if not os.path.exists(project_name):
        os.mkdir(project_name)
        print("🤭===================================🤭===================================🤭")
        print("The project Name: ", project_name)
        print("🤭===================================🤭===================================🤭")
    # always replace this with the csv
    all_places_dict = create_item_task(csv_file_path="csv_file.csv", project_name=project_name)
    file_name = "z_all_datas.csv"
    create_new_csv(all_places_dict, file_name, project_name)


# run the search query
convert_searched_dictionary_to_csv()
