# kidConnect
## Introduction
Welcome to this reporting system. Report your lost child via the website and track down any notifications through the notifications button linked to the child profile..

## Features
**1. User-Friendly Interface**

    Simple, easy-to-navigate design suitable for children and adults with minimal tech knowledge.
    Clear icons and labels for different categories of reports.

**2. Anonymity and Privacy**

    Option to report anonymously to ensure safety for the user.
    Encryption for all communications to protect the privacy of the user and the reported information.

**3. Multiple Report Categories**

    Categories to choose from (e.g., physical abuse, emotional abuse, neglect, bullying, unsafe environments).
    Option for the user to provide detailed information about the incident.

**4. Incident Report Form**

    A structured form to collect the relevant information, such as:
        Who is involved
        Date, time, and location of the incident
        Type of abuse/incident
        Any witnesses
        Detailed description of the situation
    Ability to upload photos or videos as evidence (if necessary).

**5. Language Support**

    Multiple language options to ensure accessibility for diverse populations.
    Kid-friendly language to guide younger users through the process.

**6. Location and Context Awareness**

    Option to include GPS location or school/work address (if relevant) for the report.
    If reporting in emergency situations, a feature to alert local authorities.

**7. Live Chat or Helpline Integration**

    Access to live chat with a counselor or trusted adult.
    Integration with a helpline number (e.g., national child abuse hotline) for immediate assistance.

**8. Educational Resources**

    Section with educational materials for children and parents on what constitutes abuse, safety tips, and what to do if they are in danger.
    Videos, quizzes, or FAQs to help children better understand the reporting process.

**9. Automatic Follow-Up Reminders**

    Notification system to remind users to check in or follow up with authorities, counselors, or support groups.
    Option for users to receive updates on the progress of their report, if applicable.

# Overview
We host this application here: [kidConnect](https://comingsoon.com). Visit and check this out.

**NOTE:**  For testing the website locally then;
Create a superuser ```python manage.py createsuperuser``` and login to management

http://localhost:8000/management

# Installation
1. For linux:
```bash
sudo apt install python3 git -y
```
In windows: ``Install git and python's latest version from their official sites``

2. Clone the repository using the following command:
```bash
git clone https://github.com/IamSila/alx-webstack_portfolio_project-kidConnect.git
```
3. Navigate to the project directory using the following command:
```bash
cd alx-webstack_portfolio_project-kidConnect
```
4. Install the required packages using pip:
```bash
pip install -r requirements.txt
```

## Usage
1. Start the django development server using the following command:
```bash
python manage.py runserver
```
2. Open your web browser and navigate to http://127.0.0.1:8000.
3. Sign up for an account on the platform.
4. Create your own questions and quizzes or answer existing ones.
5. Track your progress and see how your knowledge expands over time.

## Technologies Used
- Django: A high-level Python web framework that provides a clean and efficient way to build web applications.
- HTML/CSS: The standard markup language and stylesheet language used for creating the website's user interface.
- JavaScript: A programming language that enables interactive and dynamic features on the website.
- SQLite: A powerful open-source relational database management system used for efficient data storage and retrieval.
- Git: A version control system used for tracking changes in the project's source code.

## Contributing
Contributions are welcome!
If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.
Make sure to follow the project's code of conduct.

## Authors
- [Sila](https://github.com/IamSila "Sila Mulingi")
- [Sylvia-254](https://github.com/Sylvia-254 "Sylvia Cheptoo")

## ToDo
- make the UI/UX more pleasing.
- Make the notifications more account specific.

## License
This project is licensed under the [MIT License](LICENSE "License File").
