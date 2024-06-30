# Word API

Word API is a Flask-based web application that provides two endpoints for working with words based on a software testing exercise.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/fabiozr/word-api.git
cd word-api
```
2. Create a virtual environment and activate it:
    
```bash
python -m venv venv
source venv/bin/activate  
```

3. Install the required dependencies:
    
```bash
pip install -r requirements.txt
```

## Usage
To run the development server, execute the following command:

```bash
python run.py
```

The server will start running on `http://localhost:5000`.

## API Endpoints
1. `/vowel_count`
    - Method: `POST`
    - Description: Count the number of vowels in each word provided.
    - Request Body:
        ```json
        {
          "words": ["batman", "robin", "coringa"]
        }
        ```
    - Response:
        ```json
        {
          "batman": 2,
          "robin": 2,
          "coringa": 3
        }
        ```

2. `/sort`
    - Method: `POST`
    - Description: Sort the provided list of words in alphabetical order.
    - Request Body:
        ```json
        {
          "words": ["batman", "robin", "coringa"],
          "order": "asc"
        }
        ```
    - Response:
        ```json
        [
          "batman",
          "coringa",
          "robin"
        ]
        ```

## Testing
To run the test suite, execute the following command:

```bash
python -m unittest discover tests
```

To check the test coverage, run the following command:

```bash
coverage run -m unittest discover tests
coverage report
```