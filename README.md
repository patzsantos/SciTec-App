# SciTec App
Welcome to the SciTec App, a secure software developed by Bulwark Systems to check and monitor spacecraft cabin environment parameters inside the International Space Station (ISS). 

## Purpose 
This is the individual coding output of the team [design document]() developed by Team Bulwark for the Secure Software Development (Computer Science) course of The Unviversity of Essex Online. 

## Development 
The program was built using Django 5.0.6 web framework in Python 3.11.9 in the PyCharm 2023.2.6 version. 

## Security Features

| OWASP Top 10:2021 Web Application Security Risks   | Attack |
| ------------------ | ------------- |
| AO3:2021- Injection | API Injection  |
| A07: 2021- Identification and Authentication | Brute Force Attacks |
| A09:2021- Security Logging and Monitoring Failures| Denial of Service |

Three of the Open Web Application Security Project (OWASP)'s top ten web application security risks (OWASP, 2021), were referenced to prevent security attacks SciTec is designed to fight against through the following mitigations: 

### Authorisation and Authentication

ScitTec App  values the 'Rights of the data subject', in accordance with General Data Protection Regulation (GDPR) Chapter 3 (GDPR, N.D.). Therefore, the application can only be accessed by authorised ISS software system administrators known as the superuser, astronauts, scientists, and trainees. Their access to SciTec is limited depending on their roles.  

| User   | Authorisation |
| ------------------ | ------------- |
| Superusers | Can create, read, update, and delete (CRUD) account users, groups, and ISS cabin environment health checks. |
| Astronauts and Scientists | Can perform CRUD on ISS cabin environment health checks. They can view the groups and users, but cannot create, update, and delete them. |
| Trainees| Can only view the ISS cabin environment health checks. |

### Encryption

The ISS environment database stored in the db.sqlite file uses django-encrypted-model-fields to encrypt data sourced from python cryptograph library (Python Package Index, 2022). 

### Hashing

Django automatically hashes password using SHA-256 using the PBKDF2 algorithm (Django, N.D.) 

## How to Run Scitec
1) Download the Bulwark Systems package that contains the python file and requirements. Make sure that your IDE can run Python 3.11. 
2) Install requirements ```pip install -r requirements.txt```
3) Once installed, open your terminal and run ```python3 manage.py runserver```.
4) Enter the development server at:  http://127.0.0.1:8000/.
5) Use these credentials to login:

| Username   | Password |
| ------------------ | ------------- |
| superuser | admin2024 |
|  austronaut.trial| user1234 |
| trainee.trial| user1234 |

Please refer to the [Authorisation and Authentication](https://github.com/patzsantos/scitecapp/edit/main/README.md#authorisation-and-authentication) for the allowed permission for each user you want to login as. 

## CRUD Demonstrations
### Superuser:
   
![Create](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/create.gif)
Superusers can add users, group, and cabin environment. They can control and assign the authorisations of groups as well. 

![Read](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/read.gif)
Superusers can view users, groups, and spacecraft cabin environment data. 

![Update](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/update.user.gif)
Superusers can update users, groups, and spacecraft cabin environment data. 

![Delete](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/delete.gif)
Superusers can delete users, groups, and spacecraft cabin environment data. 

### Astronauts and scientists:

![CRUD ISS cabin environment, and view users and groups](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/astronaut.gif)
They can only view users and groups. However, they can perform CRUD on spacecraft cabin environment health checks. 

### Trainees:

![View ISS cabin environment only](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/trainee.gif)
The users with the least permission. They can only view the data from the ISS cabin health checks. 

## Testing

Unit tests were done using Django's test cases, which according to Python Software Foundation (N.D.), tests definite answers to inserted code in individual units. Test cases were made for urls, models, and views. Tests were revised accordingly when they failed. At present, all tests have passed. 

Linters were ran to improve code as well. The three linters used were pylama, flake8, and pylint. After initial testing, remediations were performed to improve the code. Screenshots of initial testing and the remediations done afterwards can be found in the **test screenshots** folder. 


## References: 

Django (N.D.) Password management in Django | Django Documentation | Django. Available from: https://docs.djangoproject.com/en/5.0/topics/auth/passwords/ [Accessed 27 May 2024]. 

General Data Protection Regulation. (N.D.) Chapter 3 (Art 12-23) Archives. Available from: https://gdpr.eu/tag/chapter-3/ [Accessed 26 May 2024]. 

Open Web Application Security Project. (2021). OWASP Top 10:2021. Available from: https://owasp.org/Top10/ [Accessed 26 May 2024]. 

Python Package Index. (2022) django-encrypted-model-fields. Available from: https://pypi.org/project/django-encrypted-model-fields/ [Accessed 27 May 2024].

Python Software Foundation. (N.D.) unittest- Unit testing framework- Python 3.12.3 documentation. Available from: https://docs.python.org/3/library/unittest.html [Accessed 27 May 2024]. 

## Code Credits 




