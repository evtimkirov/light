# Light project
Project for terminals and their accessories.

## About the project
The project aims to enhance my skills and capabilities using Python and the Django framework. Therefore, it may contain unnecessary functionalities or libraries, but they are used for testing purposes.

## How to install
### Run the following commands
* `python -m venv env` // Create a virtual environment
* `source env/bin/activate` _(for Ubuntu)_ // Activate the virtual environment
* `pip install -r requirements.txt` // Install the needed dependencies
* `python manage.py migrate` // Apply database migrations
* `python manage.py createsuperuser` // Create an admin user
* `npm install && npm run dev` (`npm run prod` for production) // Install frontend dependencies and build assets
* `python manage.py runserver` // Run the project server

## What contains
* Admin panel for users, user groups, terminals (with accessories)
* Public part for listing terminals with their accessories (if any)
* API endpoints for terminals

## Implementation
* Using Webpack for the resources - Bootstrap 5, CSS, etc
* Separate the Terminals and Accessor in different directories - `apps/terminals/` and `apps/accessories`
* API implementation for the terminals using Django REST framework (DRF)
  * `/api/terminals` and `/api/terminals/ID` API endpoints are available
* Using an abstract model `CommonModel` with `created_at` and `updated_at` parameters. Like this the terminal model (and the future ones) will be extended with these fields.
* The Terminal model is related to the Accessories and added to the admin panel
* Used Paginator for the template pagination
* 404 Page not found is available
