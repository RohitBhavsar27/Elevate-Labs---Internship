# Portfolio Website - Flask App
A responsive personal portfolio website built using **Python Flask**, featuring personal information, full education history, dynamically rendered project showcase, professional skills, and a working contact form, developed using Flask, Bootstrap, and Jinja2 templating.

## Live Demo

Your portfolio website is live at:

🔗 **[https://portfolio-rohit-bhavsar.onrender.com](https://portfolio-rohit-bhavsar.onrender.com)**

To view the full list of projects directly:

🔗 **[https://portfolio-rohit-bhavsar.onrender.com/projects](https://portfolio-rohit-bhavsar.onrender.com/projects)**


## Features
- **Homepage with Introduction**: Profile photo, name, and short self-description
- **About Section**: Background and career goals
- **Education**: Includes Bachelor (BE), HSC, and SSC with CGPA/percentages
- **Projects**: Dedicated `/projects` route with dynamically rendered project cards
- **Skills Section**: Tech stack, tools, and core concepts
- **Contact Form**: Handles form submissions using POST
- **Download Resume**: Single-click resume download as PDF
- **Responsive Design**: Clean, mobile-friendly layout with Bootstrap 5

## Implementation Overview
- **Framework**: Python Flask used to build web routes and render templates.
- **Templating**: Jinja2 syntax for reusable HTML templates (`base.html`, `index.html`).
- **Forms**: Built-in HTML form with `POST` method and custom input fields.
- **Styling**: Bootstrap 5 for mobile-friendly layout, Font Awesome icons for polish.
- **Static Files**: All CSS, JS, images, and PDF resume served through Flask's `static` folder.
- **Routing**:
  - `/`: Homepage rendering `index.html`
  - `/projects`: Dynamic Projects Page
  - `/sendemail/`: Placeholder route for form submission


## Folder Structure
```
portfolio/
├── app.py
├── data/
│ │ └── projects.json
├── static/
│ ├── css/
│ │ └── styles.css
│ ├── images/
│ │ ├── profile.jpg
│ │ ├── sharesphere.png
│ │ ├── ebook.png
│ │ ├── textutils.png
│ │ ├── topictrek.png
│ │ └── quizly.png
│ └── Rohit_Bhavsar_Resume.pdf
├── templates/
│ ├── base.html
│ ├── index.html
│ └── projects.html
└── README.md
```

## Screenshots

![Screenshot 2025-07-01 142823](https://github.com/user-attachments/assets/dbc98533-967b-4d65-8a20-472311946995)

![Screenshot 2025-07-01 142518](https://github.com/user-attachments/assets/2f9761a1-0002-4e1d-a0b3-4ca663d93b4a)

![Screenshot 2025-07-02 122046](https://github.com/user-attachments/assets/5e0b11e7-dec2-4f8e-88c6-6ba94023edf1)

![Screenshot 2025-07-02 121510](https://github.com/user-attachments/assets/1d3b9020-5bda-428c-960c-3f2f9561dedd)

![Screenshot 2025-07-02 121638](https://github.com/user-attachments/assets/150710f9-281f-42ff-b62f-833943468773)


## Getting started
1. Clone this repository to your local machine.

   ```
    https://github.com/RohitBhavsar27/Elevate-Labs-Internship.git
   ```
   ```
    cd 'Task 6 - July 1/portfolio'
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

4. Visit: http://127.0.0.1:5000 in your browser

## Acknowledgments
This portfolio website was created as part of the Elevate Labs Internship under the Ministry of MSME, Govt. of India. It helped solidify concepts in Flask routing, templating, form handling, and static file management.

## License
This project is released under the MIT License. Feel free to use and learn!

