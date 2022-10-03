# 9785-crypto-ml
Group 2022-S2-24 A repo for the code for the 9785 Capstone Project

## Flask Web Application
The Flask web application is or chosen method for deploying our developed models in a simple and accessible way.

### Starting the Flask App
To start the Flask app, be in the root directory of this repository, where `app.py` lives, and execute: 
```console
$ flask run
```
If port 5000 is already in use by a different service, the port can be manually overidden at runtime using the following, where 'xxxx' is your chosen port:
```console
$ flask run --port=xxxx
```
### Using the Flask App
NOTE: This Flask app will run on its default port of 5000, change it as directed above if needed.
1. Access the Flask app by entering "localhost:5000" into your web browser of choice.
2. Enter the datetime to send to the model:
   - Clicking on the dd/mm/yyyy section will open a date selector
   -  The time is entered manually in the format of HH:MM AM/PM

The flask app will then receive the result for the ML models and redirect the user to the predicted results page.

Hitting the 'RESET' button wil take the user back the main page, ready for another datetime to be sent to the ML models.