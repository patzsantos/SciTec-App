# SciTec App
Welcome to the SciTec App, a secure software developed by Bulwark Systems to check and monitor spacecraft cabin environment parameters inside the International Space Station (ISS). 

## Development 
The program was built using Django 5.0.6 web framework in Python 3.11.9 in the PyCharm 2023.2.6 version. 

## Security Features

Three of the Open Web Application Security Project (OWASP)'s top ten web application security risks (OWASP, 2021), were referenced to the security attacks SciTec were designed to fight against:  

| OWASP Top 10:2021 Web Application Security Risks   | Attack |
| ------------------ | ------------- |
| AO3:2021- Injection | API Injection  |
| A07: 2021- Identification and Authentication | Brute Force Attacks |
| A09:2021- Security Logging and Monitoring Failures| Denial of Service |

SciTec, through the use of Django web framework's built-in security features, is designed to fight off these attacks using the following: 

### Authorisation and Authentication

ScitTec App  values the 'Rights of the data subject', in accordance with General Data Protection Regulation (GDPR) Chapter 3 (GDPR, N.D.). Therefore, the application can only be accessed by authorised ISS software security engineers, who will act as the software admin, astronauts, and scientists. 

**1) Superadmin**- Can create, read, update, and delete account users, groups, and ISS cabin environment health checks.  

**2) Astronauts and Scientists**- Can create, read, update, and delete environment health checks They can view the groups and users, but cannot create, update, and delete them.

**3) Trainees**- They can only view the ISS environment health checks.

### Encryption

Passwords of all users will be secured using the 


## Purpose 
This is the individual coding output of the team [design document]() developed by Team Bulwark for the Secure Software Development (Computer Science) course of The Unviversity of Essex Online. 

## References: 

General Data Protection Regulation (N.D.) Chapter 3 (Art 12-23) Archives. Available from: https://gdpr.eu/tag/chapter-3/ [Accessed 26 May 2024]. 

Open Web Application Security Project (2021). OWASP Top 10:2021. Available from: https://owasp.org/Top10/ [Accessed 26 May 2024]. 


