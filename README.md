<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

# Capstone Project - DevOps and Software Engineering
<!-- TABLE OF CONTENTS -->
<details open>
  <summary>Table of Contents</summary>
  <ol>
    <li>
        <a href="#introduction">Introduction</a>
        <ul>
            <li><a href="#scenario">Scenario</a></li>
            <li><a href="#preview-images">Preview Images</a></li>
        </ul>
    </li>
    <li>
      <a href="#course-information">Course Information</a>
    </li>
    <li>
      <a href="#information-about-the-project">Information about the Project</a>
      <ul>
        <li><a href="#general">General</a></li>
        <li><a href="#tech-stack">Tech Stack</a></li>
      </ul>
    </li>
    <li>
      <a href="#what-i-have-done-as-part-of-the-project">What I have done as Part of the Project</a></li>
      <ul>
        <li><a href="#task-1---create-and-execute-sprint-plans">Task 1 - Create and execute Sprint Plans</a></li>
        <li><a href="#task-2---develop-a-restful-service-using-test-driven-development">Task 2 - Develop a RESTful Service using Test Driven Development</a></li>
        <li><a href="#task-3---add-continuous-integration-and-security-to-the-repository">Task 3 - Add Continuous Integration and Security to the Repository</a></li>
        <li><a href="#task-4---deploy-the-application-to-kubernetes">Task 4 - Deploy the Application to Kubernetes</a></li>
        <li><a href="#task-5---build-an-automated-cd-devops-pipeline">Task 5 - Build an automated CD DevOps Pipeline</a></li>
      </ul>
    </li>
    <li>
        <a href="#getting-started">Getting Started</a>
        <ul>
            <li><a href="#development-environment">Development Environment</a></li>
            <li>
                <a href="#useful-commands">Useful Commands</a>
                <ul>
                    <li><a href="#activate-the-python-virtual-environment">Activate the Python Virtual Environment</a></li>
                    <li><a href="#installing-python-dependencies">Installing Python Dependencies</a></li>
                    <li><a href="#starting-the-postgres-docker-container">Starting the Postgres Docker Container</a></li>
                </ul>
            </li>
            <li><a href="#project-folder-layout">Project Folder Layout</a></li>
            <li><a href="#data-model---account">Data Model - Account</a></li>
            <li><a href="#local-kubernetes-development">Local Kubernetes Development</a></li>
        </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>
<br>


## Introduction
This capstone project / repository was created as part of IBM's "DevOps and Software Engineering" program.<br>
A template was used - see IBM repository: https://github.com/ibm-developer-skills-network/aolwx-devops-capstone-template.<br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Scenario
You have been asked by the customer account manager at your company to develop an account microservice to keep track of the customers on your e-commerce website.<br>
Since it is a microservice, it is expected to have a well-formed REST API that other microservices can call.<br>
This service initially needs to create, read, update, delete, and list customers.<br>
<br>
You have also been told that someone else has started on this task.<br>
They have already developed the database model and a Python Flask-based REST API with an endpoint to create a customer account.<br>
<br>
Tasks that need to be completed:
- Create and execute sprint plans
- Develop a RESTful Service using Test Driven Development (TDD)
- Add Continuous Integration (CI) and Security to the Repository
- Deploy the application to Kubernetes
- Build an automated CD DevOps Pipeline

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Preview Images
Preview images of the project:<br>
<br>
TODO: Insert preview images. Use at least 1 image from each section<br>

![planning-kanban-done](https://github.com/user-attachments/assets/c25154e1-6da6-4fd2-b55f-c18f23680953)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>



## Course Information
Title: DevOps and Software Engineering<br>
Type: Capstone Project<br>
Course Provider: IBM<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>



## Information about the Project
### General
TODO: Update General Section after completion of project
- Client: Myself
- Project Goal: Demonstrate the knowledge gained in the IBM Program “DevOps and Software Engineering” with a Capstone Project.
- Number of Project Participants: 1 (Cloned repository of IBM. Developed the rest on my own)
- Time Period: December, 2024
- Industry / Area: DevOps, Software Engineering
- Role: Developer
- Languages: English
- Result: XXX <!-- Successfully built an account microservice. Demonstrated skills and acquired new knowledge. -->
<br>

### Tech Stack
With regard to my role:<br>
TODO: Update tech stack
- GitHub (Version Control, Kanban Board, Actions, ...)
- XXX
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>



## What I have done as Part of the Project
### Task 1 - Create and execute Sprint Plans
The RESTful microservice is created with the help of an agile plan (Scrum).<br>
This means, the first task is the Sprint 0.<br>
<br>
The main goal of Sprint 0 is to set up the team for future delivery by creating the basic project skeleton, defining the vision and preparing the product backlog.<br>
<br>
First, a user story template was created (can be found in: .github/ISSUE_TEMPLATE):<br>

![planning-storytemplate-done](https://github.com/user-attachments/assets/0e30e5a5-c3f7-4cfd-8ecf-ac187585454e)

The template provides the basis for the user stories to be created for the sprints.<br>
It uses the Gherkin Syntax.<br>
Gherkin is a simple description language with very few rules for the structured formulation of scenarios in the context of behavior-driven software development according to BDD principles.<br>
<br>
Next, the user stories were created.<br>
The titles were provided by IBM as part of the project (e.g. "Update an account in the service") and I filled them with content.<br>
Two examples (Note: Screenshots were taken later, therefore they are already labeled and assigned to a project):<br>

![Issue Update an account in the service](https://github.com/user-attachments/assets/720a2d0c-ae14-4fc8-bbe1-4bdb22893df4)

![Issue Containerize microservice using docker](https://github.com/user-attachments/assets/34ad0d12-b211-4876-90c5-f9d2e94912ef)

The acceptance criteria define the status of "Done".<br>
<br>
After the user stories were completed, a GitHub project (Kanban board) was created.<br>
All issues were assigned to the "New Issues" column:<br>

![planning-userstories-done](https://github.com/user-attachments/assets/4f044fb0-be53-48a6-8c76-629379606fc5)

The issues were then moved either to the icebox or the product backlog, depending on their priority.<br>
For example, deploying is one of the last steps, which is why it ended up in the icebox.<br>
<br>
The priorities of the issues in the backlog have also been defined.<br>
P0 is the highest priority and is therefore listed at the top.<br>
P2 is the lowest priority and is therefore listed at the bottom.<br>

![planning-labels-done](https://github.com/user-attachments/assets/47682d10-bf71-46ca-9d49-7948e675ef11)

The following was also assigned to the issues at the end:
- An iteration field "Sprint" which has a duration of 1 week. At this point, the date is 14/12/2024. This means that the 1st sprint starts on 14/12/2024 and ends on 20/12/2024.
- The size and estimated story points were also determined. The scale (provided by IBM) is 3, 5, 8, 13 = S, M, L, XL.

The issues were moved from the product backlog to the sprint backlog and the result is as follows:<br>

![planning-kanban-done](https://github.com/user-attachments/assets/c25154e1-6da6-4fd2-b55f-c18f23680953)

Task 1 is finished. Task 2 can be started.<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Task 2 - Develop a RESTful Service using Test Driven Development
TODO: XXXX<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Task 3 - Add Continuous Integration and Security to the Repository
TODO: XXXX<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Task 4 - Deploy the Application to Kubernetes
TODO: XXXX<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Task 5 - Build an automated CD DevOps Pipeline
TODO: XXXX<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


## Getting Started
### Development Environment
Important: This project is designed to be executed in the IBM Developer Skills Network Cloud IDE with OpenShift.<br>
Run the following command after cloning the repository (*Note: DO NOT run this program as a bash script. It sets environment variable and so must be sourced*):<br>

```bash
source bin/setup.sh
```

This will install Python 3.9, make it the default, modify the bash prompt, create a Python virtual environment and activate it.<br>
After sourcing it, the prompt should look like this:<br>

```bash
(venv) theia:project$
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Useful Commands
Under normal circumstances you should not have to run these commands.<br>
They are performed automatically at setup but may be useful when things go wrong:<br>

#### Activate the Python Virtual Environment
Activate the Python 3.9 environment with:<br>

```bash
source ~/venv/bin/activate
```

#### Installing Python Dependencies
These dependencies are installed as part of the setup process but should you need to install them again, first make sure that the Python 3.9 virtual environment is activated and then use the `make install` command:<br>

```bash
make install
```

#### Starting the Postgres Docker Container
This project uses Postgres running in a Docker container.<br>
If for some reason the service is not available you can start it with:<br>

```bash
make db
```

You can use the `docker ps` command to make sure that postgres is up and running.<br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Project Folder Layout
The code for the microservice is contained in the `service` package. All of the test are in the `tests` folder.<br>
The code follows the **Model-View-Controller** pattern with all of the database code and business logic in the model (`models.py`), and all of the RESTful routing on the controller (`routes.py`).<br>

```text
├── service         <- microservice package
│   ├── common/     <- common log and error handlers
│   ├── config.py   <- Flask configuration object
│   ├── models.py   <- code for the persistent model
│   └── routes.py   <- code for the REST API routes
├── setup.cfg       <- tools setup config
└── tests                       <- folder for all of the tests
    ├── factories.py            <- test factories
    ├── test_cli_commands.py    <- CLI tests
    ├── test_models.py          <- model unit tests
    └── test_routes.py          <- route unit tests
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Data Model - Account
The Account model contains the following fields:

| Name | Type | Optional |
|------|------|----------|
| id | Integer| False |
| name | String(64) | False |
| email | String(64) | False |
| address | String(256) | False |
| phone_number | String(32) | True |
| date_joined | Date | False |

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Local Kubernetes Development
This repo can also be used for local Kubernetes development.<br>
It is not advised that you run these commands in the Cloud IDE environment.<br>
The purpose of these commands are to simulate the Cloud IDE environment locally on your computer. <br>
<br>
At a minimum, you will need [Docker Desktop](https://www.docker.com/products/docker-desktop) installed on your computer.<br>
For the full development environment, you will also need [Visual Studio Code](https://code.visualstudio.com) with the [Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension from the Visual Studio Marketplace.<br>
All of these can be installed manually by clicking on the links above or you can use a package manager like **Homebrew** on Mac of **Chocolatey** on Windows.<br>
<br>
Please only use these commands for working stand-alone on your own computer with the VSCode Remote Container environment provided.<br>
<br>
1. Bring up a local K3D Kubernetes cluster

    ```bash
    $ make cluster
    ```

2. Install Tekton

    ```bash
    $ make tekton
    ```

3. Install the ClusterTasks that the Cloud IDE has

    ```bash
    $ make clustertasks
    ```

You can now perform Tekton development locally, just like in the Cloud IDE lab environment.<br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


## Contact
If you have any questions, please feel free to reach out via email: christian-schwanse (at) gmx.net<br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
