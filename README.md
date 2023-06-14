# The Olympics Dashboard

This project is a Python-based web dashboard that provides insights and visualizations about Olympic data. It utilizes the Dash framework, along with Bootstrap components, to create an interactive user interface.

## Installation

To run this project, please follow the steps below:

1. Clone the repository to your local machine.

```
git clone <repository_url>
```

2. Install the required dependencies by running the following command in your terminal:

```
pip install -r requirements.txt
```

## Usage

1. Ensure that you have the dataset file `athlete_events.csv` located in the `data` directory. If the file is not present, make sure to acquire it and place it in the correct location.

2. Open the terminal and navigate to the project directory.

3. Execute the following command to run the dashboard:

```
python app.py
```

4. Once the server is running, open your web browser and visit the URL displayed in the terminal.

## Project Structure

- `app.py`: The main script that initializes the Dash application and defines the layout using the `create_layout` function from the `layout` module.
- `layout.py`: Contains the layout definition for the dashboard, including HTML and Dash components.
- `data/util.py`: Module responsible for loading and processing the Olympic data from the `athlete_events.csv` file.
- `data/athlete_events.csv`: The dataset file containing the Olympic data. Make sure it is present in this location.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://opensource.org/licenses/MIT)

## Acknowledgments

This project is developed based on the Dash framework and Bootstrap components. We would like to express our gratitude to the developers of these tools and the community for their valuable contributions.
