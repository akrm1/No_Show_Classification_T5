
# No Show

This dataset of a hospital in Brazil contains more than 100,000 appointments which display some patient data, such as the date of appointments, diseases, age, and whether they attended on time or not.

## Contents

-[Problem Statement](#Problem_Statement)

-[Data Description](#Data_Description) 

-[Tools](#Tools)

-[Models](#Models)

-[Installation](#Installation)

-[Questions](#Questions)

-[MVP](#MVP)

-[Dataset Resource](#Dataset_Resource)

-[Authors](#Author) 

![Logo](https://www.healthecareers.com/binaries/content/gallery/healthecareers-us-en/article-features/september-2017/no-show-patients.jpg)


## Problem_Statement

Hospitals are affected if patients do not attend their appointments in many ways, causing clear losses to the hospital. One of the most important effects is rescheduling the missed appointments for a large number of patients and wasting a lot of time without any benefits. It is also affected by the knowledge of the categories of patients, such as: providing more medical staff for a certain type of diseases or opening special sections for them, knowing the days of momentum for organizing the hospital. Our company specializes in resource consulting within sectors, whether private or even governmental.
### Data_Description

Dataset: Show no Show

It has 110,527 rows , 14 columns.

| Field Name        | Description| Type|  
| ------------- |:-------------:|:------------:|
| PatientId| Identification of a patient|float64 | 
| AppointmentID| Identification of each appointment|int64   |
| Gender| Male or Female|object  |
|ScheduledDay|The day someone called or registered the appointment, this is before appointment of course |object |
| AppointmentDay| The day of the actuall appointment, when they have to visit the doctor |object  |
| Age|How old is the patient |int64    |
| Neighbourhood| Where the appointment takes place |object  |
| Scholarship| help the poor, This is a broad topic, consider reading this article https://en.wikipedia.org/wiki/Bolsa_Fam%C3%ADlia |int64   |
| Hipertension| True or False |int64   |
| Diabetes|  True or False  |  int64     |
| Alcoholism|  True or False  | int64  |
| Handcap|  True or False  |int64    |
| SMS_received|  Messages sent to the patient   |int64   |
| No-show| True or False   |object    |


## Tools
Jupyter Notebook

Google colab

Pycharm

Language: Python

Libraries: numpy, pandas, seaborn, Plotly, matplotlib, Flask, Sklearn

HTML

## Models

machine learning models: 

KNN, 
Logistic,
Decision Tree,
Random Forest,
xgboost,
Stacking

## Installation

Run pip install command to install related packages.

```bash
!pip install numpy
!pip install pandas
!pip install seaborn
!pip install Plotly
!pip install xgboost
```
    
## Questions
1. Does the age group affect the number of attendees?

2. Is the percentage of people with special needs large?

3. Do text messages affect the number of attendees? Or are there alternatives?

4. Does the waiting time for the appointment have an effect on the attendance rate?

5. What are the busiest days in the hospital? 

6. Does the neighborhood affect the attendance rate?

## MVP

Find out ways to reduce resources and increase efficiency. 
## Dataset_Resource

https://www.kaggle.com/joniarroba/noshowappointments
## Author

[@YasserMohammedK](https://github.com/YasserMohammedK) 

[@GhassanAlrehaili](https://github.com/GhassanAlrehaili)

[@akrm1](https://github.com/akrm1)

[@AYAD2030](https://github.com/AYAD2030)
