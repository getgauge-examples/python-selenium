# python-selenium

This project serves as an example for writing Automation using [Gauge](https://github.com/getgauge/gauge)

This project uses 

- [Selenium](http://selenium-python.readthedocs.org/)

# Concepts covered

- Use [Webdriver](http://docs.seleniumhq.org/projects/webdriver/) as base of implementation
- [Concepts](https://docs.gauge.org/latest/writing-specifications.html#concept)
- [Specification](https://docs.gauge.org/latest/writing-specifications.html#specifications-spec), [Scenario](https://docs.gauge.org/latest/writing-specifications.html#longstart-scenarios) & [Step](https://docs.gauge.org/latest/writing-specifications.html#longstart-steps) usage
- [Table driven execution](https://docs.gauge.org/latest/execution.html#data-driven-execution)
- [External datasource (special param)](https://docs.gauge.org/latest/execution.html#external-csv-for-data-table)

# Prerequisites
- Python 3
- [Java 1.7](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html). [Required to bring up the [SUT](#setting-up-the-system-under-test-sut)
- [Install Gauge](https://docs.gauge.org/latest/installation.html)

- [Install Gauge-Python plugin](https://gauge-python.readthedocs.io/en/latest/installation.html) by running<br>
```
gauge install python
[pip / pip3] install getgauge
```
- Google Chrome

## Setting up the System Under Test (SUT)

* Download [activeadmin-demo.war](https://github.com/getgauge-examples/activeadmin-demo/releases/tag/untagged-f0befd5494efa4baabd2)
* Bring up the SUT by executing the below command
```
java -jar activeadmin-demo.war
```
* The SUT should now be available at [http://localhost:8080/](http://localhost:8080)


# Executing specs

### Set up
This project requires pip to install dependencies. To install dependencies run :  
````
pip install -r requirements.txt
````

Run the following command to install chromedriver, if it fails then download it from [here](http://chromedriver.storage.googleapis.com/index.html) and add it to the `PATH` variable.

```
[pip / pip3] install chromedriver_installer
```

### All specs
````
gauge run specs
````
This will also compile all the supporting code implementations.
