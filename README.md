# Light project
Project for terminals and their accessories

## About the project
The project aims to enhance my skills and capabilities using Python and the Django framework. Therefore, it can contain unnecessary functionalities or libraries, but they are used for the tests.

## How to install
* Install the needed packages following the requirements.txt file
   * Create your env and activate with the following command `source env/bin/acticate` 
   * Run `pip install -r requirements.txt`
* Create the database tables
   * Run `python manage.py migrate` 
* Add a superuser for the admin panel
   * Run `python manage.py cretesuperuser`
* Install the JS resources using Webpack
   * Run `npm install && npm run dev` (`npm run prod` for production environment)
* Build the project server
   * Run `python manage.py runserver`

## What contains
* Admin panel for users, user groups, terminals (with accessories)
* Public part for listing the terminals with their accessors (if exist)
* API terminal endpoints

## Implementation
* Using Webpack for the resources - Bootstrap 5, CSS, etc
* Separate the Terminals and Accessor in different directories - `apps/terminals/` and `apps/accessories`
* API implementation for the terminals using Django REST framework (DRF)
  * `/api/terminals` and `/api/terminals/ID` API endpoints are available
* Using an abstract model `CommonModel` with `created_at` and `updated_at` parameters. Like this the terminal model (and the future ones) will be extended with these fields.
* The Terminal model is related to the Accessories and added to the admin panel
* Used Paginator for the template pagination
* 404 Page not found is available
