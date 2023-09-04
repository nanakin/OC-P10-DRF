# OC-P10-DRF

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/nanakin/OC-P10-DRF.git DRF-project
   ```
2. Move to the project directory:   
   ```sh
   cd DRF-project
   ```
3. Install dependencies in a new virtual environment:
   ```sh
   poetry install
   ```
   and use it:
   ```sh
   poetry shell
   ```
4. Migrate the database
   ```sh
   python3 manage.py migrate
   ```
5. Launch the server:
   ```sh
   python3 manage.py runserver
   ```
6. Open http://127.0.0.1:8000/ on your web browser.
