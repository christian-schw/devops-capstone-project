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
      <a href="#what-i-have-done-as-part-of-the-project">What I have done as part of the project</a></li>
      <ul>
        <li><a href="#task-1---xxxxx">Task 1 - XXXXX</a></li>
        <li><a href="#task-2---xxxxx">Task 2 - XXXXX</a></li>
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
            <li><a href="#data-model">Data Model</a></li>
            <li><a href="#local-kubernetes-development">Local Kubernetes Development</a></li>
        </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>
<br>


## Introduction
This repository was created as part of IBM's "DevOps and Software Engineering" program.<br>
It's a capstone project about building a CI/CD pipeline.<br>
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
TODO: Insert preview images<br>

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
- Client: Myself
- Project Goal: TODO: XXXXX
- Number of Project Participants: 1 (Cloned repository of IBM. Developed the rest on my own)
- Time Period: December, 2024
- Industry / Area: DevOps
- Role: Developer
- Languages: English
- Result: TODO: XXXXXX
<br>

### Tech Stack
With regard to my role:<br>
TODO: Update tech stack
- CI/CD Tool: GitHub Actions
- CI/CD Tool: Tekton
- Container Orchestration: Kubernetes
- Container Orchestration: Red Hat OpenShift
- IBM Cloud IDE (based on Theia and Container)
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>



## What I have done as part of the project
### Task 1 - XXXXX
TODO: XXXX
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br>
<br>


### Task 2 - XXXXX
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


### Data Model
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
