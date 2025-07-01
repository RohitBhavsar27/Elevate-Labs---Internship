# Portfolio Website - Flask App
A responsive personal portfolio website built using **Python Flask**, featuring personal information, education, project highlights, professional skills, and a working contact form. Developed as part of the Elevate Labs Internship to demonstrate real-world full-stack development using Flask templating and routing.


## Features
- **Homepage with Introduction**: Displays name, profile picture, and a short self-description.
- **About Section**: Shares background and career goals.
- **Education**: Lists academic qualifications and key academic projects.
- **Skills**: Highlights programming languages, frameworks, databases, and tools.
- **Projects**: Showcases real-world apps and mini-projects with technologies used.
- **Contact Form**: Allows visitors to send a message using a POST request.
- **Responsive Design**: Fully responsive using Bootstrap 5.
- **Download Resume**: One-click resume PDF download option.

## Implementation Overview
- **Framework**: Python Flask used to build web routes and render templates.
- **Templating**: Jinja2 syntax for reusable HTML templates (`base.html`, `index.html`).
- **Forms**: Built-in HTML form with `POST` method and custom input fields.
- **Styling**: Bootstrap 5 for mobile-friendly layout, Font Awesome icons for polish.
- **Static Files**: All CSS, JS, images, and PDF resume served through Flask's `static` folder.
- **Routing**:
  - `/`: Homepage rendering `index.html`
  - `/sendemail/`: Placeholder route for form submission


## Folder Structure
portfolio/
├── app.py
├── static/
│ ├── css/
│ │ └── styles.css
│ ├── images/
│ │ └── profile.jpg
│ └── Rohit_Bhavsar_Resume.pdf
├── templates/
│ ├── base.html
│ └── index.html
└── README.md

## Screenshots

## Getting started
1. Clone this repository to your local machine.

   ```
    https://github.com/RohitBhavsar27/Elevate-Labs-Internship.git
   ```
   ```
    cd Task 6 - July 1/portfolio
   ```

2. Create a virtual environment and install Flask.

    ```
    python -m venv venv  
    source venv/bin/activate  # For Windows: venv\Scripts\activate  
    pip install flask
    ```

3. Run the Flask app.
   Make sure you have Python installed (version 3.6+ recommended).

   ```
   python app.py
   ```

## Acknowledgments
This portfolio website was created as part of the Elevate Labs Internship under the Ministry of MSME, Govt. of India. It helped solidify concepts in Flask routing, templating, form handling, and static file management.

## License
This project is released under the MIT License. Feel free to use and learn!

