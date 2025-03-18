# PlasmaPS 

This is a final year project by myself. This is web application on medical side that helps connect donors and recipients.

To try this website locally, follow my instructions:

1. $git clone https://github.com/SIWNUS/PlasmaPS

2. $sudo apt install mysql

3. $mysql -u root -p

4. Create a mysql database 'webapp' 

5. exit mysql

6. Now do : $pip install -r requirements.txt

7. Then, follow the below instructions to make it work or you will get an error called, "No module called 'MySQLdb' found"

8. $pip install mysqlclient or $pip3 install mysqlclient

9. now based on your OS, follow the corresponding instruction.
   Ubuntu: sudo apt install python3-dev default-libmysqlclient-dev build-essential
   CentOS: sudo yum install python3-dev default-libmysqlclient-dev build-essential
   Fedora: sudo dnf install python3-dev default-libmysqlclient-dev build-essential

9. Now try to import the module in python. It will work.

10. Now just do "$python main.py" and it will run.


# Documentation

# Project Overview
A solo-developed web application designed to facilitate plasma donation by connecting donors with recipients. The project aimed to simplify and streamline the communication and logistics involved in plasma donation.

# Technologies Used

Backend: Python, Flask

Frontend: HTML, CSS, JavaScript, Bootstrap, Jinja2 templates

Database: MySQL with Flask-SQLAlchemy for ORM


# Key Features

User-Centric Design: Developed an accessible and easy-to-navigate interface using responsive design principles.

Database Integration: Implemented a robust MySQL database schema that efficiently manages donor and recipient information.

ORM Functionality: Utilized Flask-SQLAlchemy to abstract and simplify database interactions, improving code maintainability and scalability.


# Challenges & Solutions

Connecting Stakeholders: Built a system to reliably match donors with recipients, ensuring that communication is smooth and data is securely handled.

Scalability: Optimized the application to manage structured data efficiently and support analytical queries as the user base grows.


# Live Demo

http://suswin.pythonanywhere.com/
