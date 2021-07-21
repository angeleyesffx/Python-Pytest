# Python-Pytest

https://blog.testproject.io/2019/05/16/python-testing-framework-pros-cons/

**Install Python/pytest framework**

**IMPORTANT ---->>>>  This automation needs Python 3.8 or above**

***Step 1:*** Download and Install the latest version of Python on the official site: https://www.python.org/downloads/
        
You can find Installation Guide to your system here:  https://realpython.com/installing-python/


***Step 2:*** Install or Update pip
        
You can find Installation Guide to your system here:  https://pypi.org/project/pip/


***Step 3:*** Install behave and all dependencies listed on requirements.txt inside your project
        Execute the command line:
        
* `pip install -r requirements.txt` 

**IMPORTANT ---->>>>  If you need to install the dependencies in separate execute the command line:**
                  
                  
> **Make sure that your pip installation is update!** 

        
* `pip install SomeDependencie` 

***Step 4:*** Install Selenium and the appropriate webdrivers
       
You can find an installation Guide here:  https://selenium-python.readthedocs.io/installation.html
Download links for your Driver:
        
        
| Browser | Link                                                                  |
| ------  | --------------------------------------------------------------------- |
| Chrome: | https://sites.google.com/a/chromium.org/chromedriver/downloads        |
| Edge:   | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ | 
| Firefox:| https://github.com/mozilla/geckodriver/releases                       | 
| Safari: | https://webkit.org/blog/6900/webdriver-support-in-safari-10/          | 
       
For Linux Ubuntu:

***Firefox:***

***Step 1: Download Geckodriver***
*   `wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz`

***Step 2: Extract the file***
*   `tar -xvzf geckodriver*`

***Step 3: Make it executable***
*   `sudo mv geckodriver /usr/bin/geckodriver`
*   `sudo chown root:root /usr/bin/geckodriver`
*   `sudo chmod +x /usr/bin/geckodriver`


**User Guide of Pytest Framework:**

You can find information about pytest framework here: https://pytest.org

You can find information more information about command line here: https://docs.python.org/3/using/cmdline.html

**IMPORTANT ---->>>>  The name of the files .py in the folder steps MUST to start with the word "test". Pytest only collect the tests inside the files with the name like "test_your_step.py"** 

For execute the default configuration on pytest.ini command line below:

*   `pytest -v` 

For execute the default configuration on pytest.ini and a specific WIP scenario, or a list of WIP scenarios use above scenario @wip and execute the command line:

*   `pytest -m wip -v` 

For ignore pytest.ini configuration use the command line below:
        *The [root_path] to this project is: tests/features/steps*

*   `pytest -v [root_path] -capture=no` 

**You must ignore the pytest.ini in order to change the environment or browser default configuration.**

For change the environment use --environment=SOME_ENVIRONMENT like command line below:
        *The default environment is defined in conftest.py*
        *The [root_path] to this project is: tests/features/steps*
      
*   `pytest -v --environment=homolog [root_path] -capture=no` 


For change the browser use --browser=SOME_BROWSER like command line below:
        *The default browser is defined in conftest.py*
        *The [root_path] to this project is: tests/features/steps*

*  `pytest -v --browser=headless-chrome [root_path] -capture=no` 

For execute a specific feature the command line is:
        
*  `pytest -v tests/features/steps/test_your_steps.py` 


For execute a specific WIP scenario, or a list of WIP scenarios use above scenario @wip and execute the command line:
        *The [root_path] to this project is: tests/features/steps*

*  `pytest -m wip -v [root_path] -capture=no` 


**IMPORTANT ---->>>>  You can combine the command lines to execute your project**

Example:

*  `pytest -m wip --environment=dev --browser=chrome -v [root_path] -capture=no`
