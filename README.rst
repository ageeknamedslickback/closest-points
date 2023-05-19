Closest Points
==============

Django application with an API that receives a set of points on a grid as semicolon separated values. 
And then it finds the points that are closest to each other. Store the received set of points and the 
closest points on a DB.

How To Run The Project
======================

This assumes that you are running on any `*nix` environment and have `Python 3.10+` and `git` installed
in your local machine.

1. Clone the repository

.. code-block:: bash

    $ git clone git@github.com:ageeknamedslickback/closest-points.git
    $ cd closest-points

2. Create and activate a virtual environment to run your code

.. code-block:: bash

    $ python3 -m venv <name of your venv>
    $ source <name of your venv>/bin/activate

3. Install dependancies

.. code-block:: bash

    $ pip3 install -r requirements.txt

4. Create an `env.sh` file and add the following

.. code-block:: bash

    export SECRET_KEY="<your secret key>"
    export DEBUG="true"

5. Remeber to source your environment variables

.. code-block:: bash

    $ source env.sh


6. Run `migrations` (code uses SQLite thus no further configs) and the server

.. code-block:: bash

    $ python3 manage.py migrate
    $ python3 manage.py runserver

    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    May 18, 2023 - 21:47:51
    Django version 4.2.1, using settings 'config.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

How To Test The Project
=======================

.. code-block:: bash

    $ tox -r

Calculate Closest Points API
============================

Create
------

.. list-table:: Create

    * - Path
      - Method
      - Description
    
    * - `/api/v1/closest-points`
      - `POST`
      - Calculates and store a set of points and the closest points in the set

Payload
*******

.. code-block:: json

    {
        "points_set": "2,2;-1,30;20,11;4,5"
    }

Response (Status: `201`)
*******

.. code-block:: json

    {
        "points_set": "2,2;-1,30;20,11;4,5",
        "closest_points": "2,2;4,5"
    }

List
----

.. list-table:: List

    * - Path
      - Method
      - Description
    
    * - `/api/v1/closest-points`
      - `GET`
      - Gets all the stored point sets and their closes points

Response (Status: `200`)
*******

.. code-block:: json

    [
        {
            "points_set": "2,2;-1,30;20,11;4,5",
            "closest_points": "2,2;4,5"
        }
    ]

Admin
=====

You have the ability to see the data in the database using Django's Admin interface.

1. Create a super user

.. code-block:: bash

    $ python3 manage.py createsuperuser

    Username (leave blank to use 'dumbledore'): stewie
    Email address: stewie@email.com
    Password: 
    Password (again):
    Superuser created successfully.

2. Visit the admin page `/admin` and login using the above created credentials