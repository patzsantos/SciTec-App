# SciTec App
Welcome to the SciTec App, a secure software developed by Bulwark Systems to check and monitor the spacecraft cabin environment inside the International Space Station (ISS).

## Purpose 
This is the individual coding output of the team [design document](https://github.com/patzsantos/scitecapp/blob/main/Design%20Document/SSDCS_PCOM7E%20March%202024%20Bulwark%20Systems%20%C2%A9%20SciTec%20App%20for%20the%20International%20Space%20Station%20(ISS).docx) developed by Team Bulwark for the Secure Software Development (Computer Science) course of The Unviversity of Essex Online.

## Development 
The program was built using Django 5.0.6 web framework in Python 3.11.9 in the PyCharm 2023.2.6 version. 

## Security Features

| OWASP Top 10:2021 Web Application Security Risks   | Attack |
| ------------------ | ------------- |
| AO3:2021- Injection | API Injection  |
| A07: 2021- Identification and Authentication | Brute Force Attacks |
| A09:2021- Security Logging and Monitoring Failures| Denial of Service |

Three of the Open Web Application Security Project (OWASP) top ten web application security risks (OWASP, 2021), were referenced to prevent security attacks SciTec is designed to fight against through the following mitigations: 

**Authorisation and Authentication**

ScitTec App  values the 'Rights of the data subject', in accordance with General Data Protection Regulation (GDPR) Chapter 3 (GDPR, N.D.). To protect the personal data of users and API injections, the application can only be accessed by authorised ISS software system administrators known as the superuser, astronauts, scientists, and trainees. Authentication is done through login using authorised usernames and passwords. Privileges of different user groups are granted based on their account type, as seen in the table below: 


| User   | Authorisation |
| ------------------ | ------------- |
| Superusers | Can create, read, update, and delete (CRUD) account users, groups, and ISS cabin environment health checks. They are the only users with access to the Easy Audit Application, which is used for event monitoring. |
| Astronauts and Scientists | Can perform CRUD on ISS cabin environment health checks. They can view the groups and users, but cannot create, update, and delete them. |
| Trainees| Can only view the ISS cabin environment health checks. |

**Encryption**

The ISS environment database stored in the db.sqlite file uses django-encrypted-model-fields to encrypt data sourced from python cryptograph library (Python Package Index, 2022). When checking the sqlite3 database in the project, the parameter is not displayed in plain form to protect the data from API injections. 

**Event Monitoring** 

CRUD, login, and request events are stored and can be monitored using ```django-easy-edit``` from soynatan (2024). This security feature can alert the superuser of any suspicious activities, such as Denial of Service, during login and processing of records in SciTec.

_Note: This security feature was added last, and is therefore not included in the demo .gifs in [CRUD demonstrations(https://github.com/patzsantos/scitecapp/edit/main/README.md#crud-demonstrations). Rest assured, they are in included in the final version of the application._
![Event Monitoring in the final version of the application](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/event%20monitoring.png)

**Hashing Passwords**

Django automatically hashes password using SHA-256 using the PBKDF2 algorithm (Django, N.D.) to prevent exposure of sensitive data that can lead to unauthorised access to Scitec due to Brute Force Attacks. All levels of user privileges do not have access to the string form of the passwords, including their own. 

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

**Superuser:**

1) Create: Superusers can add users, group, and cabin environment. They can control and assign the authorisations of groups as well.

![Create](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/create.gif)

2) Read: Superusers can view users, groups, and spacecraft cabin environment data. As mentioned in the [Security Features- Event Monitoring](https://github.com/patzsantos/scitecapp/edit/main/README.md#security-features) section, only the superusers can view the event monitoring application called 'Easy Audit'.
   
![Read](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/read.gif)

3) Update: Superusers can update users, groups, and spacecraft cabin environment data.

![Update](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/update.user.gif)

4) Delete: Superusers can delete users, groups, and spacecraft cabin environment data.
   
![Delete](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/delete.gif)


**Astronauts and scientists:**

Astronauts and scientists can only view users and groups. However, they can perform CRUD on spacecraft cabin environment health checks so that they can log and monitor the parameters and data. 

![CRUD ISS cabin environment, and view users and groups](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/astronaut.gif)

**Trainees:**

The users with the least permission. They can only view the data from the ISS cabin health checks. 

![View ISS cabin environment only](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/trainee.gif)

## Testing

Unit tests were done using Django's test cases, which according to Python Software Foundation (N.D.), tests definite answers to inserted code in individual units. Test cases were made for urls, models, and views. Tests were revised accordingly when they failed. At present, all tests have passed. They can be found in the test folders in the cabin and scitec projects. 

Linters were ran to improve code as well. The three linters used were pylama, flake8, and pylint. After initial testing, remediations were performed to improve the code. Screenshots of initial testing and the remediations done afterwards can be found in the **test screenshots** folder. 



## References: 

Django (N.D.) Password management in Django | Django Documentation | Django. Available from: https://docs.djangoproject.com/en/5.0/topics/auth/passwords/ [Accessed 27 May 2024]. 

General Data Protection Regulation. (N.D.) Chapter 3 (Art 12-23) Archives. Available from: https://gdpr.eu/tag/chapter-3/ [Accessed 26 May 2024]. 

Open Web Application Security Project. (2021). OWASP Top 10:2021. Available from: https://owasp.org/Top10/ [Accessed 26 May 2024]. 

Python Package Index. (2022) django-encrypted-model-fields. Available from: https://pypi.org/project/django-encrypted-model-fields/ [Accessed 27 May 2024].

Python Software Foundation. (N.D.) unittest- Unit testing framework- Python 3.12.3 documentation. Available from: https://docs.python.org/3/library/unittest.html [Accessed 27 May 2024]. 

## Code Credits 

The Scitec App Coding Project was made by following this video: 

Rooney, J.W. (2022) Django Rest Framework for Beginners - Simple CRUD API. Available from: https://www.youtube.com/watch?v=OJdFj5hPAKs&t=8s [Accessed 22 May 2024]. 

---- 
Circumeo (2023) Encrypting Data in a Django Application. Available from: https://circumeo.io/blog/entry/encrypting-data-in-a-django-application/ [Accessed 26 May 2024].

Gregory & sunwarr10r. (2019) How to change site title, site header and index title
in Django Admin?. Available from: https://stackoverflow.com/a/36251770 [Accessed 25 May 2024]

Kumar, M. & Parmentier, B. (2023) How do I change the text "Thanks for spending some quality time with the Web site today." in Django?. Available  https://stackoverflow.com/a/65907636 [Accessed 23 May 2024]

Lorenz, T. (2019) Proper Unit Tests for Your Django Views.
Available from: https://blog.bitlabstudio.com/proper-unit-tests-for-your-django-views-b4a1730a922e
[Accessed on 25 May 2024].

OpenAI. 2024. ChatGPT (May 2024 version). Available at: https://www.openai.com/chatgpt [Accessed 25 May 2024).

Ridgway, A. (2021) Django Testing for Beginners. Available from:
https://alicecampkin.medium.com/django-testing-for-beginners-146bd285a178
[Accessed 25 May 2024].

soynatan (2024) GitHub - soynatan/django-easy-audit: Yet another Django audit log app, hopefully the simplest one. Available from: https://github.com/soynatan/django-easy-audit [Accessed 27 May 2024]. 







