# User Management REST API
A Flask-based RESTful API application that enables users to perform CRUD operations (Create, Read, Update, Delete) on user data using in-memory storage. Built as part of a backend development task to demonstrate core API development skills.

## Features
- User Creation: Add new users using JSON-based POST requests.
- User Retrieval: Fetch individual users or get all users via GET requests.
- User Update: Modify existing user records with PUT requests.
- User Deletion: Remove users with a DELETE request.
- JSON Format: All data exchanged in clean, structured JSON format.
- Test-Friendly: Fully testable with Postman or Curl.

## Implementation Overview
- Framework: Uses Flask to define RESTful routes.
- Data Handling: Stores users in a Python dictionary as in-memory storage.
- API Endpoints: Supports standard HTTP methods on /users and /users/<id>
- Error Handling: Returns appropriate status codes like 200, 201, and 404.
- Modular Structure: Encapsulated logic with Flask’s routing decorators.
- Debug Mode: Runs with debug=True for quick iteration during development.


## Execution


## Getting started
1. Clone this repository to your local machine.

   ```https://github.com/RohitBhavsar27/Elevate-Labs-Internship.git```

   ```cd Task 4 - June 27```


2. Create a virtual environment and install Flask.

    ```
    python -m venv venv  
    source venv/bin/activate  # For Windows: venv\Scripts\activate  
    pip install flask
    ```

3. Run the Flask app.
   Make sure you have Python installed (version 3.6+ recommended).

   ```python app.py```

4. Use Postman or Curl to interact with the API.

## Acknowledgments
This project was built as part of the Elevate Labs internship tasks under the Ministry of MSME, Govt. of India. It helped reinforce fundamental concepts of REST, Flask, and HTTP methods while building real-world backend functionality.

## License
This project is released under the MIT License. Feel free to use and learn!

