# CSS-Project--Option-1-IMDb
## Movie Analysis Project

This project is a simple analysis of movie data using Python. It reads data from a movie dataset and performs basic analysis.
## Files in this Project

- **CSS_project_IMDb.py**: The main Python script that loads the dataset, performs data analysis, and visualizes the results.
- **movie_dataset.csv**: A CSV file containing information about various movies, including details like title, genre, release year, rating, and more.

## Requirements

To run the code, you need the following Python libraries:
- `pandas`

You can install it using:
```bash
pip install pandas
```

## Usage

1. Ensure that both `CSS_project_IMDb.py` and `movie_dataset.csv` are in the same directory.
2. Run the Python script:
   ```bash
   python CSS_project_IMDb.py
   ```

The script will load the dataset, perform analysis based on the data.

## Features

The script performs the following tasks:
- **Data Loading**: Reads the movie dataset from the CSV file.
- **Data Cleaning**: Handles missing values and data formatting if needed.
- **Data Analysis**: Performs various analyses, like finding top-rated movies, average ratings by genre, etc.
  
## The Outputs

After running the script, you can expect to see:
- The highest rated movies in the dataset
- The average revenue of all movies in the dataset.
- The average revenue of movies released from 2015 to 2017
- The total of movies directed by Christopher Nolan
- The most common actor in the dataset
- The total of unique genre in the dataset
- Etc
