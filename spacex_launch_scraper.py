"""
SpaceX Launch Analysis Pipeline

Inputs: 
    - Data Source: SpaceX Public API endpoint (https://api.spacexdata.com/v4/launches)

Processes:
    - Data Acquisition: Fetch JSON launch data using the requests library and verify response status codes.
    - Database Storage: Define a Peewee Model and save launch records into a SQLite database, 
                        utilizing an existence check on the unique flight number to prevent duplicate entries.
    - Data Query & Analysis: Load the database records into a Pandas DataFrame, perform a groupby 
                             aggregation to calculate total launches and success rates per rocket type.
    - Visualization: Generate a Matplotlib bar chart visually comparing rocket metrics.

Outputs:
    - A SQLite database file containing the stored launch records.
    - An analysis summary printed to the console (including total record count and aggregated statistics).
    - A saved Matplotlib chart image (e.g., rocket_success_chart.png).
"""