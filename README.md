[![Build Status](https://travis-ci.org/lenileiro/flask-postgresql.svg?branch=develop)](https://travis-ci.org/lenileiro/flask-postgresql)
[![Coverage Status](https://coveralls.io/repos/github/lenileiro/flask-postgresql/badge.svg?branch=develop)](https://coveralls.io/github/lenileiro/flask-postgresql?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a2ba7d88ba0b45189d58fd361e33cea6)](https://www.codacy.com/app/lenileiro/flask-postgresql?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lenileiro/flask-postgresql&amp;utm_campaign=Badge_Grade)

[![Maintainability](https://api.codeclimate.com/v1/badges/f77c1865eb3d2b732e4f/maintainability)](https://codeclimate.com/github/lenileiro/flask-postgresql/maintainability)

# database
simple python database rapper

### Setup and Installation

1 Clone repo from github

        ```bash
            git clone https://github.com/lenileiro/database.git

            cd database

            git checkout develop branch
        ```

2 Create a virtual environment

        ```bash
            virtualenv venv

        ```
3 Activate the virtual environment

    
        ```bash
            source venv/bin/activate

        ```

4 Install project dependencies

         ```bash
            pip install -r requirements.txt

        ```


### Running Tests

        ```bash
            coverage run --source=app -m pytest && coverage report

        ```

### author

[Anthony Leiro](https://github.com/lenileiro)