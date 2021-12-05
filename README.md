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
My project will be based on a database which allows user to input data for video games that were released during the 90s. It will also show what kind of platform that these games were playable on. Furthermore, if users wanted to attached an comment/summary to the entry, they were allowed to.

### Structure of Database

![Entity Relationship Diagram](https://imgur.com/eC5iRfd.jpg)

The image represents a ERD: entity relationship diagram. This shows the structure of the database, displaying the many features I will be adding to my app. The app will be based on a one-to-many relationship, between console and games. Meaning, when user enters a specific console, they can assoicate it will as many games as they want.

### Management Method

![Project Tracking Board](https://imgur.com/8bN9cyv.jpg)

The image shows github project board being used to track the user stories, features and issues. Using the MoSCoW method to sort out and clearly label the issues on the board, helps provide a better understanding on what I need to achieve to build my app. Furthermore, the board has features which detects pushes made and link issues to merges, so it can create an automated proccess of moving the issues along to the correct column: To do > In progress > Done.


## The CI Pipeline

![CI Pipeline](https://imgur.com/DZtmRqW.jpg)


![Jenkins](https://imgur.com/vEQTGSr.jpg)


## Testing

![Cobertura](https://imgur.com/v0FHiPT.jpg)


![Backend Testin](https://imgur.com/Icz9RHy.jpg)


![Frontend Testing](https://imgur.com/0tkFg1w.jpg)


![Junit Test Results](https://imgur.com/OGydIDE.jpg)


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
