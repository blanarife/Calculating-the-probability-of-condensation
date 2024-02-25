# Calculating-the-probability-of-condensation
The project uses data received from a dht22 sensor and uses a bayesian network to calculate the probability of condensation.

Programming languages used: Python, MicroPython.
Hardware: Raspberry Pi Pico W, DHT22, LCD1602.


The microcontroller sends data such as temperature and humidity to a Google Sheet where it gets saved.
The program on the PC uses bayesian networks to calculate probabilities of certain nodes from different bayesien models written as bif files.
At the same time it calculates an average of temperatures and humidities from the Google Sheet which is accessed using the Google Sheets API and updates the file "exemplu.bif".
If the chosen bayesian model is "exemplu.bif", it will use the values calculated.
The user may select certain nodes to have a fixed value. This will affect the probabilities of the nodes that follow this one.
Any existing node may be interrogated.
The file "creds.json" needs to contain the credentials to connect to Google Sheet.

Used libraries on Raspberry Pi Pico W:
lcd1602.py
DHT22.py
