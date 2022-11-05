# Computer-Networks-Project
Identifies type of device connected in <b>Bluetooth</b> network.<br>
<br> Python script uses <code>hcitool con</code> UNIX terminal command to fetch the MAC address of any Bluetooth device connected to the computer.
<br>The MAC address is then input to an API to get the company name and company address of the connected device manufacturer.
<br>The details are written to <code>output.txt</code> and displayed on the webpage accordingly.
<br><br><b>Output Screenshots (laptop connected to boAt wireless earphones)</b><br><br>
![image](https://user-images.githubusercontent.com/75639351/200125293-caf439c7-5534-4831-862f-f889375ed9e5.png)
![image](https://user-images.githubusercontent.com/75639351/200125301-95ef5f71-c028-4fba-8756-8bd6af8892c0.png)
<br><br><b>Note:</b> The following command must be run beforehand:<br><code>pip install maclookup</code>
<br>Must be run on Linux OS
<br><br><b>Steps to execute:</b>
<br>1. Run <code>python3 main.py</code> in project directory
<br>2. Open webpage to view the details
<br><br><br>
<em>Made by Udeet Mittal & Pradyumn Kamath<br>
CSE 5th sem CN mini-project
