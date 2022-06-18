# Project 3 Python Essentials: Brew That
Brew That is a python essentials terminal project that is run using the Code Institute mock terminal on Heroku.
<img width="952" alt="image" src="https://user-images.githubusercontent.com/97494070/174244013-d4b76bf3-86ad-4728-9153-b986ff1adf53.png">


## Author
Sashen Govender

## Project Overview
Brew That is a mobile coffee station that services popular cycling routes and aims to fuel cyclist during their social rides on the weekend. The idea is to provide a quick and streamlined way to get them fuelled and riding again.
The goal of this project was to showcase my understand of python essentials and allow for future opportunities once my skillset has improved.

- Below you can find the basic terminal interaction, this shows the interaction when all requirements are met from the user. Errors will be provided should invalid data be provided prompting the user to try again.
![Screen Recording 2022-06-18 at 07 52 17](https://user-images.githubusercontent.com/97494070/174413697-839f8c94-ef4a-4457-bd3c-785c255c7983.gif)

- Click on this link to view the deployed site link [Deployed url](https://brew-that.herokuapp.com/) 

## Table of Contents
GENERATE THIS LATER!!!

## How To Use
1. The user initiates the progamme and is presented with a welcome message and asked to provide their name.
<img width="740" alt="image" src="https://user-images.githubusercontent.com/97494070/174414219-cc8bd544-9f5d-4411-aa43-3646b8e0c7d8.png">

2. The user is then presented with a drinks menu order options 1-6 and required to input a numeric value. Should the user input any other value they will be presented with the menu again (repeat order function).
<img width="740" alt="image" src="https://user-images.githubusercontent.com/97494070/174414369-e69e7e5b-d6b9-49ef-ab9b-8ed7c34e9bd9.png">

3. User is then asked if they would like to add to their order or not. If yes, the user is taken back to the menu.
<img width="737" alt="image" src="https://user-images.githubusercontent.com/97494070/174414394-c29cec83-a7da-4f26-9abf-eab7b444c2fe.png">

4. Once the user chooses no, they will be taken to the total cost section that shows a summary of the order with the total cost.
<img width="738" alt="image" src="https://user-images.githubusercontent.com/97494070/174414453-b74cde8f-864e-4946-9b2e-c190cb2de161.png">

## Features
This section includes both the implemented and future features associated with this project.

### Implemented Features

* Users are able to input their name to make their order personal. Program validates if the name is acceptable and proceeds if true.
<img width="737" alt="image" src="https://user-images.githubusercontent.com/97494070/174411545-2ccacac1-af58-4889-be29-3de61a53de8e.png">

* Users can add to their order or proceed to submit order.
<img width="736" alt="image" src="https://user-images.githubusercontent.com/97494070/174411569-1887d60d-a8ea-4de2-9e84-37bfc005312e.png">

* Users are able to see a total cost and order list once agreeing to their order. Message indicating that order is successful and being made is presented.
<img width="741" alt="image" src="https://user-images.githubusercontent.com/97494070/174411590-3fb7c00e-bda4-49e3-9c81-89d2df2940b0.png">


### Future Features

* Allow program to distinguish between new and previous users using a database according to an email.
* Allow frequent and new users to build a profile and make drink suggestions based on their past purchases.
* Provide users with a credit balance to make purchases.


## Design Documents

Below is a diagram showing the intended logic of the terminal project. Areas marked in orange (registration of user) should be regarded as a future feature and is not included in this deployment.
<img width="834" alt="Screenshot 2022-06-17 at 14 45 11" src="https://user-images.githubusercontent.com/97494070/174320288-b51bcbf5-1ef4-4708-8469-ecc006fb99ad.png">


## Data Model/ Classes
Below you can find a link that shows the data model(s) and class used for this project.


## Libraries used
* cachetools
    - Python module which provides various memoizing collections and decorators.
* google-auth
     - This library simplifies using Google’s various server-to-server authentication mechanisms to access Google APIs.
* google-auth-oauthlib
    - This library provides oauthlib integration with google-auth.
* gspread
     - Interface for working with Google Sheets.
* oauthlib
    - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python 3.6+.
* pyasn1
    - Pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208)
* pyasn1-modules
    - A collection of ASN.1 modules expressed in form of pyasn1 classes. Includes protocols PDUs definition (SNMP, LDAP etc.) and various data structures (X.509, PKCS etc.).
* requests-oauthlib
    - Provides first-class OAuth library support for Requests.
* rsa
    - It supports encryption and decryption, signing and verifying signatures, and key generation according to PKCS#1 version 1.5.

## Testing
Testing results using validators, manual (tables) have been provided below.

### Validation Testing
The pep8online validator was used to check the code for indentation and other generic errors. See results below.

- [PEP8 Validator](http://pep8online.com/) 

### Manual Testing

You can view manual testing for this project [here](https://docs.google.com/spreadsheets/d/1-48gLQhrg9fVBXcf1gJaQ-q30t13I0yI/edit?usp=sharing&ouid=116957584173833035665&rtpof=true&sd=true)

You can view the data model for this application [here](https://docs.google.com/spreadsheets/d/1RJ4_lpXP1gQvgw3ujhy7llhUdO5Oe41z-9dLQ2SU6jY/edit?usp=sharing)

### Defect Tracking

Try to create issues in real time as it better reflects the daily life of a developer.

The easiest way to track defects is by using GITHUB's Issues to track these as it's really easy to copy/paste screenshots in and then write up how you closed them. At this stage you don't need a custom template or labels, that comes in P4.


### Defects of Note
-Initializing the repeat order function to allow the users to add to their order.
-Printing a list of items that were selected by the user.
-Printing sales data to Googlesheets in the correct order, error with not using an array.


### Outstanding Defects
Below is a list of defect/s that were not resolved, but do not influence the core experience for the user.
- Removing the round brackets from the prices for each item when shown in the Total cost section.

## Deployment

### Heroku

This application was deployed via Heroku

- Log into Heroku.
- Navigate to Dashboard.
- Click "New" and select "create new app" from the drop-down menu. This is found in the upper right portion of the window. Provide a name for your application, this needs to be unique, and select your region.

<img width="1003" alt="Screenshot 2022-06-15 at 23 07 47" src="https://user-images.githubusercontent.com/97494070/174413018-8de2decd-feca-49d2-ae70-f1180f61ae97.png">
<img width="896" alt="Screenshot 2022-06-15 at 23 09 44" src="https://user-images.githubusercontent.com/97494070/174413019-09fcb2b2-6071-4974-88d2-435216d557d5.png">

- Click "Create App".
- Navigate to "Settings" and scroll down to "config vars".
- Click "Reveal Config Var", in the field key I entered the CREDS word and in the value field I copied my creds.json content as past there.
<img width="1227" alt="image" src="https://user-images.githubusercontent.com/97494070/174413116-971d7f47-d42d-4934-b3b5-529979c7d4fd.png">

- Then scroll down to "build packs", click "build packs" and then click both "python" and "node.js"(node.js is needed for the mock terminal.)
- <img width="605" alt="Screenshot 2022-06-15 at 23 12 27" src="https://user-images.githubusercontent.com/97494070/174413134-3cb79ed1-eb7f-41b5-ae4b-ec97fb0b447d.png">
<img width="1222" alt="Screenshot 2022-06-15 at 23 13 16" src="https://user-images.githubusercontent.com/97494070/174413135-571e88e5-9e34-40c9-93df-80b3d8443b82.png">

- Navigate to the "Deploy" section.
- Scroll down to "Deployment Method" and select "GitHub".
<img width="957" alt="Screenshot 2022-06-15 at 23 14 01" src="https://user-images.githubusercontent.com/97494070/174413189-4421636d-18b1-474b-aecc-57ff50b8c593.png">

- Authorise the connection of Heroku to GitHub.
- Search for your GitHub repository name, and select the correct repository.
<img width="499" alt="Screenshot 2022-06-15 at 23 14 26" src="https://user-images.githubusercontent.com/97494070/174413228-3ba265e4-0a18-4596-9973-667845ebffa3.png">
<img width="1253" alt="Screenshot 2022-06-15 at 23 21 05" src="https://user-images.githubusercontent.com/97494070/174413231-2771d724-2abd-4bd3-8e80-2182d0f46c79.png">

- For Deployment there are two options, Automatic Deployments or Manual, I chose Automatic Deployment so Heroku will re-build each time code is pushed to GitHub.
- Ensure the correct branch is selected "master/Main", and select the deployment method that you desire.
<img width="1257" alt="Screenshot 2022-06-15 at 23 25 51" src="https://user-images.githubusercontent.com/97494070/174413303-6c7c69a2-1bc4-45c8-95b6-90f42f57a2dc.png">

### Gitpod
Before deploying, the Gitpod workspace needs the following setup steps for Heroku to build the project:

1. Install the dependencies for Heroku using the following instruction to the terminal:
```$python
pip3 freeze > requirements.txt
```
<img width="583" alt="image" src="https://user-images.githubusercontent.com/97494070/174414657-e759681c-9b44-4da4-a001-35d2162cff29.png">

2. The project creds.json file from the Google Drive and Google Sheets API access used when adding Config Var, see example below:
<img width="1244" alt="image" src="https://user-images.githubusercontent.com/97494070/174414699-1d288869-4b84-46ca-8800-7367ab8b781e.png">

## Credits
* Code Institute: Love Sandwiches Project
    - [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.
    - Steps to declare and connect the Google APIs to my worksheet.
    - Function to update the worksheet.
    - Steps to deploy the project to Heroku.
                
* Coders Bistro by arthur Mezaonik
    - Ideas for Deployment section steps in README.
    - Libraries section used and descriptions in README.

* Cara McAvinchey- The Scoop project for direction and guidance on features.
* Flowchart created using [diagrams.net](https://www.geeksforgeeks.org/python-randint-function/?ref=gcse)

-[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.
* Deployment template for students to use for P3

### Media
No images were used.

### Acknowledgments

*I would like to thank my mentor Malia Havlicek for facilitating both detailed and useful project meetings and the support of the CI tutor team for assisting with overcoming challenges during this project.
* The tutors at Code Institute for their patience and support.
* The Code Institute Slack community for tips and guidance.
