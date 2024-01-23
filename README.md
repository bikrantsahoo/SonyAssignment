# SonyAssignment

# Country Lookup Service

A simple Flask-based REST service for looking up country information, with routes for health check, API diagnostics, and country name to country code conversion.

## Introduction

This service provides a RESTful API for looking up country information, including health checks, API diagnostics, and country name to country code conversion.

## Prerequisites

Installing the below to the linux vm via the below cmds.
- brew install docker
- brew install minikube

Steps:

1. Cloning the repository:

    ```bash
    git clone https://github.com/your-username/country-lookup-service.git
    cd country-lookup-service
    ```

2. Building the Docker image:

    ```bash
    docker build -t country-lookup-app .
    ```

3. Running the Docker container:

    ```bash
    docker run -p 5000:5000 country-lookup-app
    ```

4. Accessing the service on the  browser or via tools like `curl`:

    - Health: [http://localhost:5000/health](http://localhost:5000/health)
    - Diagnostics: [http://localhost:5000/diag](http://localhost:5000/diag)
    - Convert: [http://localhost:5000/convert/{country_name}](http://localhost:5000/convert/{country_name})

## API Endpoints

- `/health`: Returns the health status of the service.
- `/diag`: Returns the status of the external API (https://www.travel-advisory.info/api).
- `/convert/{country_name}`: Converts a country name to its country code.

## Kubernetes Deployment

To deploy the service on a local Kubernetes cluster (Minikube):

1. Starting Minikube:

    ```bash
    minikube start
    ```

2. Applying the Kubernetes resources:

    ```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```

3. Accessing the service:

    ```bash
    minikube service country-lookup-service
    ```

