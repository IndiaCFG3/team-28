# JPMC CFG Team-28

> A team comprising of 6 members from diverse parts of India.

## Table of Contents


  - [Installation](#installation)
  - [Features](#features)
  - [Team](#team)
  - [More Details](#more-details)
  - [License](#license)


---


## Installation ##

- Get the code
```bash
git clone https://github.com/IndiaCFG3/team-28.git
cd team-28
```

- Install the required modules  
```
pip3 install -r requirements.txt
```

- Create tables and make migrations for django models
```
python manage.py makemigrations
python manage.py migrate
```

- Replace the `account_sid` and `auth_token` with your Twilio credentials as mentioned on the Twilio Dashboard  
  
- In a new terminal, run the Flask Development server
```
python whatsapp_receive.py
```
- Now, setup the ngrok server to listen to incoming Whatsapp and SMS messages.(in a new terminal)
```
./ngrok http 5000
```
- Paste the ngrok server url in the twilio whatsapp sandbox, and you are good to go.
- Start the Django application (development mode) [default port 8000]
```
python manage.py runserver
```
- Access the web app in browser: http://127.0.0.1:8000/


---

## Features ##
- Single Platform to consolidate the student’s progress, learning material, content, feedback, etc.
- Send Learning modules in bulk with a single click, and get responses/answers from the students.
- Aggregate the scores in the dashboard, and be able to grade it on the go.
- Analyze the progress of the class and recommend the next course material to be taken, and take feedback from the users.


---

## Team ##

- [Syed Farhan Ahmad](https://www.linkedin.com/in/syedfarhanahmad/)
- [Soumya Vemuri]() 
- [Aiesha Fathima]()
- [Archit Kuhar]()
- [Saurabh Kemekar](https://www.linkedin.com/in/saurabh-kemekar-a8589710b/)
- [Akshaj Sunil]()
- [Malvika Jindal]()


---


## License ##
- License to be added, if required by JPMC
