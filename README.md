<!-- Intro -->
# **CHRISTMAS_RANDOM_FRIEND**
> **Lucas Arroyo Blanco**  
> 
> _PatoOsoPatoso_  

&nbsp;

<!-- Index -->
# Table of contents
## &nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;)&nbsp;&nbsp;[Description](#description)
## &nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;)&nbsp;&nbsp;[Requirements](#requirements) 
## &nbsp;&nbsp;&nbsp;&nbsp;3&nbsp;)&nbsp;&nbsp;[Modifications to be used](#modifications-to-be-used)  

&nbsp;  
&nbsp; 

<!-- Description -->
## **Description**

It's a simple python script to make it easier to decide which person is going to gift who, it's pretty useful in a large group of people who can't meet in person to make the raffle.  

The plus of this script is that it uses your whatsapp account or any account that you have logged into [whatsapp web](https://web.whatsapp.com/) in your browser.

&nbsp;  

<!-- Requirements -->
## **Requirements**
There are 2 requirements to use this script:  

* An active whatsapp web session in the browser.  
* A **.env** file with the names and phone numbers.

&nbsp;

<!-- Modifications -->
## **Modifications to be used**
To use the code as it is right now first you are going to need to create a **.env** file.  
The file should look like this:  
&nbsp;
```
PHONE_NUMBERS=Lucas:34123456789,Pablo:34111111111,Sandra:34999999999,Julio:34000000000
```  
This is just an example of the pattern that it's used to parse the names and the phones into a list. To modify it just use a `:` to separate the name from the phone number of one person and a `,` to separate different persons.  
&nbsp;

The browser data and binary executable where the whatsapp session is active are necessary aswell. Here is my case with google chrome:  
```python
if os.name == 'nt':
    user_data_dir = rf'C:\Users\{getpass.getuser()}\AppData\Local\Google\Chrome\User Data'
    user_binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
else:
    user_data_dir = rf'/home/{getpass.getuser()}/.config/google-chrome/Default'
    user_binary_location = r'/usr/bin/google-chrome'
```  

Modify for Windows or Linux with the actual path for your user data and binary executable.

&nbsp;  
&nbsp;

<!-- Bye bye -->
<img src="https://static.wikia.nocookie.net/horadeaventura/images/c/c2/CaracolRJS.png/revision/latest?cb=20140518032802&path-prefix=es" alt="drawing" style="width:100px;"/>**_bye bye_**