# Retro Video Games 90s Database

## Table of contents
- [Table of contents](#table-of-contents)
  - [Project info](#project-info)
    - [Brief](#brief)
    - [App Specification](#app-specification)
    - [Structure of Database](#structure-of-database)
    - [Management Method](#management-method)
  - [The CI Pipeline](#the-ci-pipeline)
  - [Testing](#testing)
  - [Risk Assessment](#risk-assessment)
  - [Future Improvements](#future-improvements)
    - [More Testing](#more-testing)
    - [Block before 1990 and after 1999](#block-before-1990-and-after-1999)
    - [Better UI](#better-ui)
  - [Misc](#misc)

## Project Info
### Brief
This project will summariezed all the skills and knowledge I have gained throughout my time during the 9 weeks at QA Limited DevOps Skill Bootcamp. For this project I aim to create a web application that shows the fucntiality of CRUD: Create, Read, Update and Delete. Then I am to host the app within a container using Docker and deploy it. This will display my competence at creating a CI/CD pipeline that is automated for test, build and deploying the app.

### App Specification
My project will be based on a database which allows user to input data for video games that were released during the 90s. It will also show what kind of platform that these games were playable on. Furthermore, if users wanted to attached an comment/summary to the entry, they were allowed to. The demo at the misc section will give an more detailed look at how my app operates.

### Structure of Database

![Entity Relationship Diagram](https://imgur.com/eC5iRfd.jpg)

The image represents a ERD: entity relationship diagram. This shows the structure of the database, displaying the many features I will be adding to my app. The app will be based on a one-to-many relationship, between console and games. Meaning, when user enters a specific console, they can assoicate it will as many games as they want.

### Management Method

![Project Tracking Board](https://imgur.com/8bN9cyv.jpg)

The image shows github project board being used to track the user stories, features and issues. Using the MoSCoW method to sort out and clearly label the issues on the board, helps provide a better understanding on what I need to achieve to build my app. Furthermore, the board has features which detects pushes made and link issues to merges, so it can create an automated proccess of moving the issues along to the correct column: To do > In progress > Done.


## The CI Pipeline

The following images will give you an idea on how I carried out the CI (continuous intergration) pipeline, with what services and framework.

![CI Pipeline](https://imgur.com/DZtmRqW.jpg)

This approach allows developers to implament new codes easily and frequently, all done so via a automated system that pulls from repo, builds the image into containers, test and then finally deploy. Thus, allowing devlopers to simplfiy this repetitious process and instead focus on coding.

![Jenkins](https://imgur.com/vEQTGSr.jpg)

Here I show the stages I had automated via a script to be ran by using Jekings:
* Checkout SCM: Using webhook to pull the code from designated branch in a repo
* Setup: Installing dependencies, services and provding the credentials needed for said services.
* Test: Installing and using pytest, junit and coberture reports.
* Build: Building the backend and frontend image into a container (can also scale the app with replicas if more resources is required). 
* Push: Pushing the container onto docker hub.
* Deploy: Deploying it to docker swarm service. So when the app is running, it can load balance any incoming users traffic equally to the VMs.

## Testing
For the testing process of the app, the following images below shows the many test reports I had included with in the test to maximise the amount of information output. Meaning it can produce a better overall picture on how many codes has passed and failed.

![Cobertura](https://imgur.com/v0FHiPT.jpg)

Here I use a plugin on Jenkins called Cobertura to provide a better summary on how much coverage of the code my test has picked up for the overall app.

![Backend Testin](https://imgur.com/Icz9RHy.jpg)

On the source code itself, I used pytest to run unit test. This is for my Backend.

![Frontend Testing](https://imgur.com/0tkFg1w.jpg)

Here is for the Frontend. Both of these process are then later put into a script so it can be automated via Jenkins.

![Junit Test Results](https://imgur.com/OGydIDE.jpg)

Here is a image of Junit displaying the pass and failed results in graph form.
## Risk Assessment


## Future Improvements
### More Testing


I want to do more tests but I am at an stage where I no longer know what to aim for. I hope that in the future when as I gain more experience, I could return to this project and try for better test coverage/results.

### Block before 1990 and after 1999

I had hope to implament an rule which prevents certain dates to be entered into the database, as this app is based around the 90s. It would make no sense for any entries before or after this certain period.

### Better UI

Very basic look with basic app features. I wanted to add the abilities to include images of both games and consoles. Also, to improve the design on the website to look more up to date/modern silimar to what websites we have today.


## Misc
Video for demonstrating the CI/CD Pipeline:
https://drive.google.com/drive/folders/1V8IrSStN_5a9R3Nz6rTeKd0R_dDHrW9J?usp=sharing
