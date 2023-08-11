**GoogleMapScraping**

This repository contains a Python script (`main.py`) that allows you to scrape data from Google Maps using the provided
API and save it to a CSV file. Follow the instructions below to set up and run the code.

### Prerequisites

Before you begin, ensure you have the following:

1. Python 3.x installed on your machine.
2. Git installed on your machine for cloning the repository.
3. A Google Maps API key. If you don't have one, you can obtain it by following the instructions on
   the [Google Cloud Platform](https://cloud.google.com/maps-platform/) website.

### Setup

1. Clone the repository:

```bash
git clone https://github.com/codertjay/GoogleMapScraping.git
```

2. Navigate to the repository's directory:

```bash
cd GoogleMapScraping
```

3. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

4. Activate the virtual environment:

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```

5. Install required packages:

```bash
pip install -r requirements.txt
```

6. Create a copy of the `.env--sample` file and name it `.env`:

```bash
cp .env--sample .env
```

7. Open the `.env` file in a text editor and replace `YOUR_GOOGLE_MAPS_API_KEY` with your actual Google Maps API key.

8. Make sure you have a `csv_file.csv` in the root folder of the project. If not, create an empty `csv_file.csv` file.

### Running the Script

After completing the setup steps, you can now run the script to start scraping data from Google Maps.

```bash
python main.py
```

The script will start fetching data from Google Maps using the provided API key and save the results to
the `csv_file.csv` file in the root directory.

Note: make sure you have [csv_file.csv](csv_file.csv)
Remember that this script uses web scraping techniques, and Google's policies on web scraping and API usage may change.
Make sure you review and comply with Google's terms of use and API usage policies.

If you encounter any issues or have questions, feel free to open an issue on this repository.

---

Please note that this README assumes the structure and contents of the repository based on your provided URL. If there
have been any changes or updates to the repository since then, you may need to adapt the instructions accordingly.