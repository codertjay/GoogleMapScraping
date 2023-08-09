import time

from scraper import get_all_place

import csv
import json


def create_item_task(csv_file_path):
    """
    This function updates items based on data from a CSV file.

    :param csv_file_path: Path to the CSV file.
    :return: List of updated places.
    """
    all_places = []

    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skip the header row (first row)
        next(csv_reader)
        all_categories = []
        all_places = []
        for row in csv_reader:
            all_categories.append(row[0])
            all_places.append(row[1])
        # loop through all the categories each categories will go through for all places
        for category in all_categories:
            for place in all_places:
                try:

                    all_places.append(get_all_place(category, place))
                    with open("all_places.json", 'w') as json_file:
                        json.dump(all_places, json_file, indent=4)
                except Exception as e:
                    print("Error:", e)
                    # In case of an error, write the data to a JSON file
                    error_data = {
                        "query": query,
                        "category": category,
                        "error": str(e)
                    }
                    with open("error_data.json", 'a') as json_file:
                        json.dump(error_data, json_file, indent=4)
                        json_file.write('\n')  # Add a new line after each entry
    return all_places


def convert_searched_dictionary_to_csv():
    """
    this is used to load from and search from the csv
    :return:
    """
    # always replace this with the csv
    all_places = create_item_task(csv_file_path="csv_file.csv")

    # Get the field names from the keys of the first JSON object
    fieldnames = all_places[0].keys()
    # write into the csv file
    current_time = str(time.time()).replace(".", "")
    file_name = f"scraped_data_{current_time}.csv"
    print("The file name is :", file_name)
    print("Converting scraped data to csv ")
    print("🤭===================================🤭===================================🤭")
    print("🤭===================================🤭===================================🤭")
    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the CSV header
        csv_writer.writeheader()

        # Write each JSON object as a row in the CSV file
        for json_obj in all_places:
            csv_writer.writerow(json_obj)


# run the search query
convert_searched_dictionary_to_csv()
