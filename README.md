# Proyecto-Epilepsia

## Installation and initial configuration

The project uses a Docker Compose file to orchestrate all its necessary components. Docker Compose will initialize and configure containers for each necessary service with minimal user intervention.

### Step 1: Requirements

Downloading the repository will be easier with Git installed. To download Git, go to the following site:

- https://git-scm.com


The user must have the **Docker Engine** and **Docker Compose** running on their machine. This can be verified by running `docker compose version`. Should the output not be something similar to `Docker Compose version v2.21.0`, the user must verify that both Docker Engine and Docker Compose are correctly installed in their machine. Docker Engine and Compose is included with typical Docker Desktop installations, or can be installed standalone.

[Instructions to install Docker Desktop \(Recommended for Windows and Mac users\)](https://docs.docker.com/get-docker/)

[Instructions to install Docker Engine (Recommended for Linux and WSL users)](https://docs.docker.com/engine/install/)

[Instructions to install Docker Compose for Docker Engine](https://docs.docker.com/compose/install/)

### Step 2: Clone repository

Download the repository

- Go to the terminal (If you are not acquainted with this term, feel free to look it by yourself)

- git clone https://github.com/SELF-Software-Evolution-Lab/AI-Epilepsy.git

### Step 3: Run the Docker Compose file

Within the user's terminal that has access to `docker compose`, the user should run the following command:

- `docker-compose up`

[optional] If a specific docker compose .yml file should be used instead of the existing `docker-compose.yml`, the command should instead be `docker compose -f {CUSTOM_DOCKER_COMPOSE}.yml up`

[optional] If the user wants to leave the services running in the background, and not have them terminate upon closing the active terminal window, they must add a `-d` flag to the end of the command.

### Step 4: Creating fake initial data

This step is **optional**. To populate the database with example data, follow these instructions:

1) Install Node.js on your machine. LTS versions are recommended (20.10.0 at the time of writing). [Download links can be found here](https://nodejs.org/en/download).
2) Navigate to the backend folder using the command `cd bkAIEp/` and run the following terminal command: `npm i` to install all required dependencies.
3) Run the following command: `npm run cli -- --seeder -d`

### Step 5: accessing the AI-Epilepsy service

Using a web browser, navigate to http://localhost:5002

Congrats, you finally made it 🎉

### Step 6: turning off all services

In the root folder of the project, run the following command:

`docker-compose down`

## Optional configuration

The Docker Compose template will run the project using default local-oriented values. If the user needs to modify some of these values, they will have to create a `.env` file between Step 2 and Step 3.

Copy the existing `.env` file template:

`cp .env.template .env`

Edit the desired values within the `.env` file using a text editor

`nano .env`, `vim .env`, etc.

Finally, you can continue running the `docker-compose.yml` file as demonstrated in Step 3
