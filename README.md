# Packing App

This is a simple packing application built using Flask and Python. Users can create bags for their trips, add items to these bags, and mark items as packed. Users can also delete items and bags. The application features an attractive and easy-to-use UI.

## Features

- Create, view, and delete bags
- Add, view, and delete items within bags
- Mark items as packed/unpacked
- View a total packed count for each bag

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/packing-app.git
    cd packing-app
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

## Usage

1. **Run the application**:
    ```bash
    python app.py
    ```

2. **Open your browser and navigate to**:
    ```
    http://127.0.0.1:5000
    ```

## Project Structure

packing_app/
├── app.py
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── create_bag.html
│ ├── create_item.html
│ ├── view_bag.html
├── static/
│ ├── css/
│ │ └── styles.css
│ ├── js/
│ │ └── scripts.js
├── models.py
└── forms.py


- **app.py**: Main application file with route definitions.
- **templates/**: Folder containing HTML templates.
- **static/**: Folder containing static files like CSS and JavaScript.
- **models.py**: Contains SQLAlchemy models for the Bag and Item.
- **forms.py**: Contains WTForms forms for creating bags and items.

## Dependencies

- Flask
- Flask-SQLAlchemy
- Flask-WTF
- WTForms

You can install these dependencies using the `requirements.txt` file provided.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/)


