Cloud-Native GKE Application: Welcome to the Cloud-Native GKE Application repository. This professional project showcases the implementation of a cloud-native application using Google Kubernetes Engine (GKE) on Google Cloud Platform (GCP). Through this repository, we explore the world of containerization, CI/CD pipelines, and Kubernetes, creating a robust cloud-native solution.

---

## Overview

Dive into the realm of cloud-native applications with the Cloud-Native GKE Application repository. This project exemplifies the use of containerization, CI/CD pipelines, and Kubernetes to develop and deploy a powerful microservices-based application on GCP's GKE. From microservices communication to persistent data storage, this project covers it all.

### Learning Outcomes

This repository embodies the mastery of the following concepts:

- Containerization using Docker
- Building CI/CD pipelines with GCP tools
- Harnessing the power of Kubernetes, both through the GCP console and Infrastructure as Code (IaC) tools like Terraform
- Deploying applications on GKE clusters using CI/CD pipelines
- Configuring and utilizing persistent volumes in GKE
- Effective usage of Kubernetes tools like kubectl for container management and cluster diagnosis
- Understanding application update strategies and version control in GKE

### Key Requirements

1. **Microservices Development:** Develop two microservices in your preferred programming language. These services should be designed to interact with each other, showcasing a seamless integration.

2. **CI/CD Pipeline:** Create a robust CI/CD pipeline using GCP tools such as Cloud Source Repository and Cloud Build. The pipeline should enable automated deployments to the GKE cluster whenever new code commits are made.

3. **Persistent Volume:** Configure a persistent volume in your GKE cluster, accessible to both microservices. Your application must be able to read from and write to this volume.

4. **GKE Cluster Setup:** Create a GKE cluster using Terraform. The configuration should align with the specifications outlined in the assignment.

5. **Exposing Services:** The deployment yaml file should not only deploy your microservices but also expose the services to the internet.

### Repository Contents

This repository includes:

- Microservices source code
- Configuration files for the CI/CD pipeline using Cloud Build
- Terraform script for creating the GKE cluster
- Deployment yaml file for deploying microservices and exposing services
- Detailed documentation outlining the project's architecture, design principles, and instructions for setup and execution

  <img width="595" alt="Screenshot 2023-08-08 at 8 00 27 PM" src="https://github.com/AlagappanVeerappan32/Cloud-Native-GKE-Application/assets/133504573/2ed4dc5f-41ad-4280-8905-5c7739c28758">


---

## How to Explore

1. Clone this repository
2. Study the microservices source code and gain insights into their communication.
3. Explore the CI/CD pipeline configuration files and understand the automation behind deployments.
4. Review the Terraform script for creating the GKE cluster and understand how it aligns with the specified configurations.
5. Examine the deployment yaml file to grasp the process of deploying microservices and exposing services.
6. Dive into the detailed documentation to gain a comprehensive understanding of the project's architecture and design principles.
