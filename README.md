# Kendama-Order-History

## Contents
* [Introduction](#introduction) 
  * [Objective](#objective)
  * [Proposal](#proposal)
* [Architecture](#architecture)
  * [Risk Assessment](#risk-assessment)
  * [Trello Boardd](#trello-board)
  * [Test Analysis](#analysis-of-testing)
* [Infrastructure](#infrastructure)
  * [Jenkins](#jenkins)
  * [Entity Diagram](#entity-diagram)
  * [Docker Swarm](#interactions-diagram)
  * [The 4 Services](#the-4-services)
* [Development](#development)
  * [Front-End Design](#front-end)
  * [Unit Testing](#unit-testing)
* [Footer](#footer)
  * [Future Improvements](#future-improvements)
  * [Author](#author)
  * [Acknowledgements](#acknowledgements)
  * [Versions](#versions)


## Introduction

### Objective

The objective for this project is as follows:
> To create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together.

The other constraint in this project is the technologies that need to be used.
The project needs to utilise the technologies discussed during the training modules:
* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git - using the feature-branch model
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX
* Database Layer: MySQL

### Proposal

At the start of the project, I realised that to meet all the requirements and to ensure the MVP was produced in the time frame provided, I focused on the infrastructure and implementation of my CI/CD pipeline. Therefore the application itself is less important with only the essential features developed.

#### Kendama Ordering
* Service-1 (front-end): Displays the results of the following 3 services for the user to see, as well as a brief history of past results.
* Service-2: Returns a random Kendama from a predefined list.
* Service-3: Returns a random accessory from a predefined list.
* Service-4: Returns the total price from both Kendama and accessory and add £3.50 for shipping.

## Architecture

### Risk Assessment

My detailed risk assessment can be seen below, outlining the minor and major risks that have potential to impact the success of this project. Creating a risk assessment is important in any project as it helps make the project more robust and provides methods of mitigating the impact of any such risk that does occur.

![risk assessment image](./Images/risk_assessment.png)
View the original document [here](https://docs.google.com/spreadsheets/d/166MTAAl1HzXAQWaA2iS9Mz9MXRZpsr7y-s-MHqZk_yk/edit?usp=sharing)

### Trello Board

For project tracking i decided to use [Trello](https://trello.com) over other similar services as Trello is super lightweight and has a visusal representation that is easy to understand and follow.



### Analysis of Testing

## Infrastructure

### Jenkins 

### Entity Diagram

### Docker Swarm

### The 4 Services

## Development

### Front End

### Unit Testing

## Footer

### Future Improvements

### Author
	
Marius Saunders
	
### Acknowledgements

<a href="https://github.com/OliverNichols">Oliver Nichols</a>

### Versions
13/08/21 - v1.0.0