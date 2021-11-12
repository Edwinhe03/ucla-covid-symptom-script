# UCLA COVID-19 Symptom Survey Script
The script will fill out the UCLA Daily Symptom Survey automatically, assuming you are healthy and have no symptoms for COVID-19.

Prerequisites:
- Install Python 3
- Install Selenium using the following line on CLI:
  - pip install selenium
- Selenium Chromedriver (already included in ./driver folder)

To use:
- Download the project
- On a CLI, navigate to the project directory
- Run the following line of code to start the script:
  - python3 symptom_form.py
- Enter your UCLA Logon username and password as prompted
- Have the DUO Mobile app ready to authenticate the logon

NOTES:
- There are no checks for errors or exceptions, so you must enter you credentials correctly
- Your credentials will not be saved
- You must be connected to the internet or mobile data to complete the form
