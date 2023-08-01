# Devops_Project
Devops_first_project

This repository contains a Devops project deploying, testing and building a python applciation.

Python application prints out a ramdon number from 1 to 100.

To test the applications follow the below steps:

1. Pull the repository from github
1. build docker enviroment in terminal 
```
docker build -t pythonapp .
```
1. Run the project on docker
```
docker run pythonapp
```
1. to test CI/CD Pipeline open CircleCi and locate the repository