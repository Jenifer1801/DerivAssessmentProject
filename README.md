**Deriv Assessment Automation Solution**
This solution where the automation testing is covered for following scenarios:
-Web automation
-Mobile application automation
-WebSocket API automation

**Pre-Requisites to run the Automation tests**
1. Download Python - [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download PyCharm - [https://www.jetbrains.com/edu-products/download/other-PCE.html](https://www.jetbrains.com/edu-products/download/other-PCE.html)
3. Run command in Pycharm Terminal to install all the required libraries - _pip install -r requirements.txt_
4. Appium - [https://github.com/appium/appium-desktop/releases](https://github.com/appium/appium-desktop/releases)
5. Appium Inspector - [https://github.com/appium/appium-inspector/releases](https://github.com/appium/appium-inspector/releases) 
6. Android Sdk - [https://developer.android.com/studio](https://developer.android.com/studio)
7. Java [https://www.java.com/download/ie_manual.jsp](https://www.java.com/download/ie_manual.jsp)
8. Set environment variables for Python, Java and Android

**Commands to run test cases for WebAutomation**
To run the test cases under 'WebAutomation' directory use below commands
_robot TestCases\WebAutomation\TC1Login.robot_
_robot TestCases\WebAutomation\TC2MyInfo.robot_
_robot TestCases\WebAutomation\TC3Logout.robot_
_robot TestCases\WebAutomation\OrangeHrmTest.robot_

**Commands to run test cases for MobileApplicationAutomation**
To run the test cases under 'WebAutomation' directory use below commands
_pytest CalculatorTest.py --alluredir=._
**Note-** You can right-click and run the python file, but report won't be generated

**Commands to run test cases for WebsocketAPIAutomation**
To run the test cases under 'WebAutomation' directory use below commands
_pytest WebSocketTest.py --alluredir=._
**Note-** You can right-click and run the python file, but report won't be generated






