Welcome to the RFW-POC wiki!

# Installation Instructions
**1.** Install Python Latest Version (v3.7) to Target Machine.   Link>> [Download Python](https://www.python.org/downloads/)
<br>**Note:** Upon Installing Python to target machine, tick the _"Add Python to PATH"_ checkbox.
<br>![Python Path Setting Sample](https://github.com/ajith-geon/RFW-POC/blob/master/Wiki/Adding%20to%20Path%20Sample.png?raw=true)

**2.** Download/Clone the code from repo- [RFW-POC](https://github.com/ajith-geon/RFW-POC) <br>
![Git Clone Sample](https://github.com/ajith-geon/RFW-POC/blob/master/Wiki/Git%20Clone%20Sample.png?raw=true)

**3.** All the required python modules (including Robot Framework and Selenium Webdrivers)  are bundled inside the **Modules** folder. <br>The same can be deployed/installed to any target environment in a single click. [Internet NOT required]. <br>Double Click the _**"setup.bat"**_ file inside the /Modules folder. [This will install all the required modules into the target machine]
<br>![Run Setup sample](https://github.com/ajith-geon/RFW-POC/blob/master/Wiki/Module%20Installation%20Sample3.png?raw=true)
<br><br>**Note:** Modules folder contain the standard distribution of the required modules _(like selenium,requests,json..)_ plus custom made distributions/package _(like webdriver-0.0.1)_. Reason for adopting this strategy is that this will enable code moderator to have a better control over the versions of package being deployed to the target machine and could do modifications in the package if necessary. This could avoid any possible issues of version mismatch. 

**4.** Once the setup finishes installation, environment is all set. Now we could start executing Test Cases, either through the CLI or through any IDE. (Pycharm-Community Version is the one we used)
<br> Open Terminal/cmd and navigate to the Testscripts folder. (In the Cloned Repo /Testscripts)
<br>Robot Command to run specific Test Case is:  "_robot -t testcase1 mytestsuite.txt_" <br>
_**In our case it is;**_<br> _**robot -t "Test case C001: SID: Create a New Company for Automation" 1_PreConfiguration.txt**_
<br>This will start the Test Execution.<br>
**Robot Command to run all suites is: "_robot Testscripts_"** (This will run all the suites in the Testscripts folder)<br> 
More details on running specific set of TCs or Suites are available at;
([Robot Framework CLI Options](https://github.com/robotframework/robotframework/blob/master/doc/userguide/src/Appendices/CommandLineOptions.rst) &
[CLI Commands Usage Sample](https://gist.github.com/GLMeece/c26aae72fb1f8aa5192065793aab3477))

**5.** Test Rail Integration : For the results to get updated in the TestRail, user will have to provide the necessary details in the _**Framework_Properties.py**_ file in the _ConfigurationBase_ folder.
Test Results will be updated to the TCs available in the Test Run. (If the Suite Contains other TCs, they will get executed but won't post back the result to Test Rail)

![TestRail Integration Sample](https://github.com/ajith-geon/RFW-POC/blob/master/Wiki/TestRail%20Integration%20Sample.png?raw=true)

**6.** For Running any individual Test Case other than Company Creation, user will have to specify which company to be used. The details of the Environment (_like QA, DEV_) are also need to be provided in the _**Testdata_web.py**_ file in _TestData_ folder (default data is already filled in).
<br>![TestData Sample](https://github.com/ajith-geon/RFW-POC/blob/master/Wiki/TestData%20Sample.png?raw=true)


## Setting Up Pycharm IDE for Robot Framework
1. Download and install Pycharm Community Version from [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) <br>

2. Open Pycharm, choose KoreAutomation as Project.<br>
![Project Structure Sample](https://github.com/ajith-geon/RFW-POC/blob/master/Wiki/Project%20Structure.png?raw=true)

3. Go To File>>Settings >>Plugins>> Browse Repositories >>and search for "robot".
![Pycharm Tweak Sample](https://github.com/ajith-geon/RFW-POC/blob/master/Wiki/Pycharm%20Plugin%20Install%20Sample.png?raw=true) <br>
Install the highlighted Plugins (Restart of Pycharm is required for every install) <br>
![Plugins List](https://github.com/ajith-geon/RFW-POC/blob/master/Wiki/Plugins%20List.png?raw=true) <br>

4. Renaming the TestSuite from **_.txt_** to **_.robot_** will now render syntax highlighting. The installed plugins could allow user to run Test cases/ Suites through the readily available **PLAY** button. <br>
![Syntax Highlighting Sample](https://github.com/ajith-geon/RFW-POC/blob/master/Wiki/Pycharm%20Syntax%20Highlighting%20Sample.png?raw=true)
 


