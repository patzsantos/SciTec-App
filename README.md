# SciTec App

Welcome to the **SciTec App**, a secure software developed by Bulwark Systems. This application is designed for the use of scientists and astronauts in charge of checking and monitoring the spacecraft cabin environment inside the International Space Station (ISS). This data can be simultaneously relayed to the different space stations on Earth who have authorised access to the SciTec app. 

## Purpose 

This is the individual coding output of the team [design document](https://github.com/patzsantos/scitecapp/blob/main/Design%20Document/SSDCS_PCOM7E%20March%202024%20Bulwark%20Systems%20%C2%A9%20SciTec%20App%20for%20the%20International%20Space%20Station%20(ISS).docx) developed by Team Bulwark for the Secure Software Development (Computer Science) postgraduate certificate course of The Unviversity of Essex Online.

Scrum solo, a method wherein only a sole developer implements all the tasks during code development (Moyo & Mnkandla. 2020), was implemented in the creation of this application. Therefore, it is important to take note that some changes from the initial design proposal were applied to this version of SciTec. 

## Development 

The program was developed using the **Django 5.0.6** web framework in **Python 3.11.9**. It was written and run in the **PyCharm 2023.2.6** version IDE. 

Django is the chosen framework since it follows the Model-View-Controller (MVC) structure discussed by Pillai (2017), though not exactly the same. Django does not use the MVC terminology, since their framework is more commonly known as MTV, for **Model-Template-View**. However, it applies the same logic since Django (N.D.a) discusses that the view shows the page from the URL, the templates present data, and the controller serves as the program dispatching to request the view. 

## Security Features

| OWASP Top 10:2021 Web Application Security Risks   | Attack |
| ------------------ | ------------- |
| AO3:2021- Injection | API Injection  |
| A07: 2021- Identification and Authentication | Brute Force Attacks |
| A09:2021- Security Logging and Monitoring Failures| Denial of Service |

Three of the Open Web Application Security Project (OWASP) top ten web application security risks from 2021(Open Web Application Security Project, 2021), were identifited to classify the security attacks and their mitigations that SciTec is designed to defend against. With the help of OWASP, these following security features are implemented in the SciTec app: 

**Authorisation and Authentication**

ScitTec App  values the _'Rights of the data subject'_, in accordance with General Data Protection Regulation (GDPR) Chapter 3 (General Data Protection Regulation, N.D.). To protect the personal data of users, as well as API injections, the application can only be accessed by authorised ISS software system administrators known as the superuser, astronauts, scientists, and trainees. 

Authentication is done through login of only those with authorised usernames and passwords. The privileges of different user groups are granted based on their account type, as seen in the table below: 


| User   | Authorisation |
| ------------------ | ------------- |
| Superusers | They can create, read, update, and delete (CRUD) account users, groups, and ISS cabin environment health checks. They are the only users with access to the Easy Audit Application, which is used for event monitoring. They are also the only ones who can manage the user database. |
| Astronauts and Scientists | They can perform CRUD on ISS cabin environment health checks. They can view the groups and users, but cannot create, update, and delete them. |
| Trainees| They can only view the ISS cabin environment health checks. |

**Encryption**

The ISS environment database stored in the **db.sqlite** file uses ```django-encrypted-model-fields``` that is sourced from Python cryptograph library (Python Package Index, 2022), to encrypt data. When checking the sqlite3 database in the project, the parameter is not displayed in plain text form to protect the data from API injections. 

**Event Monitoring** 

CRUD, login, and request events are stored and can be monitored using ```django-easy-edit``` from soynatan (2024). This event monitoring tool is called **Easy Audit Application**. This security feature can alert the superuser of any suspicious activities during login and processing of records in SciTec that can lead to Denial of Service attacks on the SciTec app.

_Note: This security feature was added last, and therefore cannot be seen in the interface of the software in the demo .gifs in [CRUD demonstrations](https://github.com/patzsantos/scitecapp/edit/main/README.md#crud-demonstrations). Rest assured, the Easy Audit Application is included in the final version of the application, as seen from the screenshot below._
![Event Monitoring in the final version of the application](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/event%20monitoring.png)

**Hashing Passwords**

All levels of user privileges do not have access to the plain text form of the passwords, including their own. This is because Django hashes passwords through SHA-256 using the PBKDF2 algorithm (Django, N.D.b). This secure hashing of passwords prevents the exposure of sensitive data that can eventually lead to unauthorised access of the Scitec app due to Brute Force Attacks. 

## How to Run Scitec

1) Download the Bulwark Systems package that contains the Python file and requirements. There are two main project folders, namely **cabin** and **scitec**. Make sure that your IDE can run Python 3.11. 
2) Install requirements
   ```pip install -r requirements.txt```.
4) Run your virtual environment
```- virtualenv --version```
``` virtualenv my_env```.
4) Once installed, open your terminal and run
```python3 manage.py runserver```.
5) Enter the development server at:  http://127.0.0.1:8000/.
6) Use these credentials to login:

| Username   | Password |
| ------------------ | ------------- |
| superuser | admin2024 |
|  austronaut.trial| user1234 |
| trainee.trial| user1234 |

Please refer to the [Authorisation and Authentication](https://github.com/patzsantos/scitecapp/edit/main/README.md#authorisation-and-authentication) for the allowed permissions of each user you want to login as. 

## CRUD Demonstrations

**Superuser:**

_1) Create:_ Superusers can add users, group, cabin environment, and range. They are the only users who can control and assign the authorisations of groups. They are also the only ones who can manage the user database. 

![Create](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/create.gif)

_2) Read:_ Superusers can view users, groups, and spacecraft cabin environment data. As mentioned in the [Security Features- Event Monitoring](https://github.com/patzsantos/scitecapp/edit/main/README.md#security-features) section, only the superusers can view the event monitoring application called 'Easy Audit'.
   
![Read](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/read.gif)

_3) Update:_ Superusers can update users, groups, and spacecraft cabin environment data. 

![Update](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/update.user.gif)

_4) Delete:_ Superusers can delete users, groups, and spacecraft cabin environment data. 
   
![Delete](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/delete.gif)


**Astronauts and scientists:**

Astronauts and scientists can only view users and groups. However, they can perform CRUD on spacecraft cabin environment health checks so that they can log and monitor the parameters and data onboard the ISS. 

![CRUD ISS cabin environment, and view users and groups](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/astronaut.gif)

**Trainees:**

Trainees are the users with the least permission. They can only view the data from the ISS cabin health checks. 

![View ISS cabin environment only](https://github.com/patzsantos/scitecapp/blob/main/demo.screenshots/trainee.gif)

## Testing

Unit tests were done using **Django test cases**, which according to Python Software Foundation (N.D.), tests definite answers to inserted code in individual units. Test cases were written and run for **cabin project _urls and models_,** and **scitec project _views_**. Tests were revised accordingly when they failed. 

Upon deployment of the software, all tests have passed. Proofs of successfully ran cabin and scitec tests can be found in the [Testing Documentation](https://github.com/patzsantos/scitecapp/tree/main/Testing%20Documentation) folder, but are attached here as well: 

Cabin folder test case results: 
![cabin test](https://github.com/patzsantos/scitecapp/blob/main/Testing%20Documentation/django%20cabin%20test.png)

Scitec folder test case results: 
![scitec test](https://github.com/patzsantos/scitecapp/blob/main/Testing%20Documentation/django%20scitec%20test.png)

Linters were also ran to improve code. The three linters used were **pylama, flake8,** and **pylint**. After the initial testing, remediations were performed to further improve the code quality. Pylama and flake8 were more focused on coding style and structure. Both pylama and flake8 tests were cleared. Pylint was more time-consuming. Unfortunately, due to time constraints, the developer was unable to significantly raise the code rating of the cabin project. 

Screenshots of initial linter testing, and the remediations performed afterwards, can be found in the 
[Testing Documentation](https://github.com/patzsantos/scitecapp/tree/main/Testing%20Documentation) folder. 

## Future Improvements to the Code

- Encrypt usernames in the database - This strengthens authorisation and authentication as this extra security layer would prevent exposure of usernames, and is in line with GDPR Chapter 3, 'Rights of the data subject' (GDPR, N.D.)
- Use multi factor authentication during login- Based on the team design, this is an extra layer of security that will prevent Brute Force Attacks, as it implements various levels of authentication.
- Implement locking out of users after a maximum of 3 failed login attempts- Another mitigation based on the team design that is designed to fight off Brute Force Attacks once suspicious user login or activity is detected during event monitoring. 
- Write more unittests to ensure that the code logic is working correctly
- Aim for higher linter code rating
- Run other linter tests, such as mccabe, to assess code complexity. 

## Disclaimer

Though presented as a secure application, SciTec is a postgraduate requirement, not an actual program. When using any part of the code, please use it with caution. 

## References: 

Django (N.D.a) FAQ: General | Django documentation. Available from: https://docs.djangoproject.com/en/5.0/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names [Accessed 27 May 2024]. 

Django (N.D.b) Password management in Django | Django Documentation | Django. Available from: https://docs.djangoproject.com/en/5.0/topics/auth/passwords/ [Accessed 27 May 2024]. 

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

Moyo, S. & Mnkandla, E. (2020) A Novel Lightweight Solo Software Development Methodology With Optimum Security Practices. _IEEE Access_ 8: 33735-33747. DOI: http://dx.doi.org/10.1109/ACCESS.2020.2971000. [Accessed 27 May 2024].

OpenAI. 2024. ChatGPT (May 2024 version). Available at: https://www.openai.com/chatgpt [Accessed 25 May 2024).

Pillai, A.B. (2017) Software Architecture with Python: Design and architect highly scalable, robust, clean, and high performance applications in Python. 1st ed. Birmingham, UK: Packt Publishing. Available from: https://learning.oreilly.com/library/view/software-architecture-with/9781786468529/?sso_link=yes&sso_link_from=university-of-essex [Accessed 27 May 2024].

Ridgway, A. (2021) Django Testing for Beginners. Available from:
https://alicecampkin.medium.com/django-testing-for-beginners-146bd285a178
[Accessed 25 May 2024].

soynatan (2024) GitHub - soynatan/django-easy-audit: Yet another Django audit log app, hopefully the simplest one. Available from: https://github.com/soynatan/django-easy-audit [Accessed 27 May 2024]. 







