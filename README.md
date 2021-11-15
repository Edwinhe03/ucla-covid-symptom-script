# UCLA COVID-19 Symptom Survey Script
The script will fill out the UCLA Daily Symptom Survey automatically, assuming you are healthy and have no symptoms of COVID-19.

Prerequisites:
- Have Google Chrome installed (currently works on Chrome version 96; update instructions below)
- On a Command Line, check that Python 3 is installed by running:
  - python3 --version
- If not, you can install Python 3 from https://www.python.org/downloads/
- Check that pip is available by running:
  - python3 -m pip --version
- If not, you can install pip by running:
  - python3 -m ensure-up --default-pip
- Install Selenium WebDriver by running:
  - python3 -m pip install selenium

To use:
- Download the project
- On a Command Line, navigate to the project directory
- Run the following line of code to start the script:
  - python3 symptom_form.py
- Enter your UCLA Logon username and password as prompted
- Have the DUO Mobile app ready to authenticate the logon

NOTES:
- For Windows users, replace any instance of "python3" with "py".
- On first use, Mac users may see the message: "'chromedriver' cannot be opened because the developer cannot be verified."
  - Go to System Preferences > Security & Privacy > General, and click "Allow Anyway"
  - Run the program again, and click "Open" when prompted
- There are no checks for errors or exceptions, so you must enter you credentials correctly
- Your credentials will not be saved
- You must be connected to the internet or mobile data to complete the form
- If Google Chrome updates to a new version, go to https://chromedriver.chromium.org/downloads and download the latest release of ChromeDriver
  - In the ./driver directory, replace only "chromedriver" (Mac) or "chromedriver.exe" (Windows) with the new unzipped executable 
