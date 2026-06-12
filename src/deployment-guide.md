# Deployment Guide

---

## Overview

This document provides a detailed deployment guide for the **Python OpenShift CI/CD Pipeline with SAST, DAST, Trivy, and Git OAuth** project.

The goal of this guide is to explain how the Python Flask application is built, deployed, validated, and secured within Red Hat OpenShift.

---

## Deployment Objective

The deployment process automates the delivery of a Python application from source code to a running OpenShift environment.

The deployment workflow includes:

* Source code management
* Container image creation
* Security scanning
* Container registry integration
* OpenShift deployment
* Runtime validation
* Security testing

---

## Deployment Architecture

```text
GitHub Repository
        |
        v
Git OAuth Authentication
        |
        v
Tekton Pipeline
        |
        v
Pytest Testing
        |
        v
Bandit SAST Scan
        |
        v
Container Image Build
        |
        v
Trivy Scan
        |
        v
Quay Registry
        |
        v
OpenShift Deployment
        |
        v
OpenShift Route
        |
        v
OWASP ZAP DAST Scan
        |
        v
Production Application
```

---

## Prerequisites

Before deployment, ensure the following components are available.

### Required Software

* Python 3.11
* Podman
* Git
* OpenShift CLI (oc)
* Tekton CLI (tkn)
* Trivy
* Bandit
* Pytest

---

## Step 1: Clone the Repository

Clone the GitHub repository.

### Command

```bash
git clone https://github.com/jbanday808/python-openshift-cicd.git
```

Move into the project directory.

```bash
cd python-openshift-cicd
```

### Purpose

Downloads the application source code and deployment files.

### Expected Result

The project files are available locally.

---

## Step 2: Install Python Dependencies

Install the required Python packages.

### Command

```bash
pip install -r requirements.txt
```

### Purpose

Installs all application dependencies.

### Expected Result

The Python environment is prepared for testing and deployment.

---

## Step 3: Run Unit Tests

Execute the Pytest unit tests.

### Command

```bash
PYTHONPATH=. pytest tests/test_app.py
```

### Figure 1: Unit Testing with Pytest

![Unit Tests](../images/unit-tests-pytest.png)

**Figure 1.** Pytest validates application functionality and confirms the code passes automated unit testing before deployment.

### Purpose

Verifies that the application functions correctly.

### Expected Result

```text
1 passed
```

---

## Step 4: Run Bandit SAST Scan

Execute the Bandit source code security scan.

### Command

```bash
python3 -m bandit -r app
```

Generate a report:

```bash
python3 -m bandit -r app -f txt -o bandit-report.txt
```

### Figure 2: Bandit SAST Scan

![Bandit Scan](../images/bandit-sast-scan.png)

**Figure 2.** Bandit performs Static Application Security Testing to identify insecure coding practices within the Python source code.

### Purpose

Identifies potential source code security issues.

### Expected Result

Bandit produces a vulnerability report.

---

## Step 5: Build the Container Image

Create the application container image.

### Command

```bash
podman build -t python-openshift-cicd:latest .
```

### Figure 3: Container Image Build

![Container Build](../images/docker-image.png)

**Figure 3.** The Python application is packaged into a portable container image for deployment across environments.

### Purpose

Packages the application and its dependencies.

### Expected Result

A container image is successfully created.

---

## Step 6: Validate the Container Image

Run the container locally.

### Command

```bash
podman run --rm -p 8080:8080 python-openshift-cicd:latest
```

Test the application.

```bash
curl http://127.0.0.1:8080/
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8080/version
```

### Purpose

Confirms the container image functions correctly.

### Expected Result

Application endpoints return successful responses.

---

## Step 7: Run Trivy Vulnerability Scan

Scan the container image.

### Command

```bash
trivy image localhost/python-openshift-cicd:latest
```

Generate a report.

```bash
trivy image localhost/python-openshift-cicd:latest > trivy-report.txt
```

### Figure 4: Trivy Vulnerability Scan

![Trivy Scan](../images/trivy-scan-result.png)

**Figure 4.** Trivy scans the container image for known vulnerabilities, exposed secrets, and insecure packages.

### Purpose

Identifies vulnerabilities before deployment.

### Expected Result

A vulnerability assessment report is generated.

---

## Step 8: Push Source Code to GitHub

Commit and push the project.

### Commands

```bash
git add .
```

```bash
git commit -m "Deploy Python OpenShift CI/CD Pipeline"
```

```bash
git push origin main
```

### Figure 5: Git Push to GitHub

![Git Push](../images/git-push.png)

**Figure 5.** Application source code and configuration files are committed and pushed to GitHub for version control.

### Purpose

Publishes the latest code changes.

### Expected Result

Source code is available in GitHub.

---

## Step 9: Deploy Application to OpenShift

Create the OpenShift build.

### Command

```bash
oc new-build \
--name=python-openshift-cicd \
--binary \
--strategy=docker
```

Start the build.

```bash
oc start-build python-openshift-cicd \
--from-dir=. \
--follow
```

Create the application.

```bash
oc new-app python-openshift-cicd
```

Expose the service.

```bash
oc expose svc/python-openshift-cicd
```

### Purpose

Deploys the application into OpenShift.

### Expected Result

OpenShift creates the application deployment.

---

## Step 10: Verify OpenShift Deployment

Check deployment status.

### Commands

```bash
oc get deployment
```

```bash
oc get pods
```

```bash
oc get route
```

### Figure 6: OpenShift ImageStream

![ImageStream](../images/image-stream.png)

**Figure 6.** OpenShift ImageStreams track container image versions and manage deployment image updates.

### Purpose

Verifies deployment resources.

### Expected Result

Deployment, pod, and route resources are available.

---

## Step 11: Configure Quay Registry

Create a secure image registry destination.

### Figure 7: Quay Registry Repository

![Quay Repository](../images/quay-repo.png)

**Figure 7.** Quay serves as the secure container registry used to store and distribute application container images.

### Create Registry Secret

```bash
oc create secret docker-registry quay-secret \
--docker-server=quay.io \
--docker-username='<QUAY_ROBOT_USERNAME>' \
--docker-password='<QUAY_ROBOT_TOKEN>' \
--docker-email='<EMAIL_ADDRESS>'
```

Link the secret.

```bash
oc secrets link pipeline quay-secret --for=pull,mount
```

### Purpose

Allows the pipeline to push images to Quay securely.

### Expected Result

OpenShift authenticates to Quay successfully.

---

## Step 12: Execute the Tekton Pipeline

Create the PipelineRun.

### Command

```bash
oc create -f pipelinerun.yaml
```

Monitor execution.

```bash
oc get pipelinerun
```

```bash
oc get taskrun
```

```bash
tkn pipelinerun logs -f <pipelinerun-name>
```

### Purpose

Runs the complete CI/CD workflow.

### Expected Result

Pipeline tasks complete successfully.

---

## Step 13: Validate Final OpenShift Deployment

Verify deployment resources.

### Commands

```bash
oc get deployment
```

```bash
oc get pods
```

```bash
oc get route
```

### Figure 8: OpenShift Final Deployment

![OpenShift Deployment](../images/openshift-ci-cd-final-deployment.png)

**Figure 8.** The Python application is successfully deployed and running in OpenShift after pipeline execution.

### Purpose

Confirms successful application deployment.

### Expected Result

The application is running and accessible.

---

## Step 14: Run OWASP ZAP DAST Scan

Create the report directory.

```bash
mkdir -p zap-reports
```

Execute the scan.

```bash
podman run --rm -t \
-v $(pwd)/zap-reports:/zap/wrk:Z \
ghcr.io/zaproxy/zaproxy:stable \
zap-baseline.py \
-t http://<openshift-route> \
-r zap-report.html
```

### Figure 9: OWASP ZAP DAST Scan

![OWASP ZAP](../images/dast-owasp-zap-scan.png)

**Figure 9.** OWASP ZAP performs Dynamic Application Security Testing against the live application to identify runtime security vulnerabilities.

### Purpose

Validates runtime security controls.

### Expected Result

OWASP ZAP generates a security assessment report.

---

## Deployment Validation Checklist

Verify the following:

* GitHub repository updated
* Unit tests passed
* Bandit scan completed
* Container image built successfully
* Trivy scan completed
* Quay repository updated
* OpenShift deployment running
* OpenShift route accessible
* OWASP ZAP scan completed
* Application accessible to users

---

## Common Troubleshooting Commands

Check project.

```bash
oc project
```

Check deployment.

```bash
oc get deployment
```

Check pods.

```bash
oc get pods
```

Check routes.

```bash
oc get route
```

Check PipelineRuns.

```bash
oc get pipelinerun
```

Check TaskRuns.

```bash
oc get taskrun
```

View pod logs.

```bash
oc logs <pod-name>
```

Describe a pod.

```bash
oc describe pod <pod-name>
```

---

## Deployment Summary

This deployment guide demonstrates how a Python Flask application is securely delivered from GitHub to OpenShift using a complete DevSecOps CI/CD pipeline.

The deployment process includes automated testing, source code security scanning, container vulnerability scanning, secure image management, automated deployment, and runtime security validation.

---

## Interview Summary

This project demonstrates hands-on experience with:

* CI/CD Pipeline Automation
* OpenShift Administration
* Kubernetes Fundamentals
* DevSecOps Practices
* Container Security
* Vulnerability Management
* Application Deployment
* Production Troubleshooting
* Secure Software Delivery

---

## References

### GitHub Documentation

Reference:

GitHub Docs: Provides guidance for source control management, repository administration, authentication, and collaboration workflows.

https://docs.github.com

---

### OpenShift Documentation

Reference:

Red Hat OpenShift Documentation: Provides guidance for deploying, managing, and troubleshooting applications on OpenShift.

https://docs.openshift.com

---

### Tekton Documentation

Reference:

Tekton Documentation: Provides guidance for creating Tasks, Pipelines, PipelineRuns, and CI/CD workflows.

https://tekton.dev/docs

---

### Quay Documentation

Reference:

Red Hat Quay Documentation: Provides instructions for container image repository management.

https://docs.projectquay.io

---

### Trivy Documentation

Reference:

Trivy Documentation: Provides guidance for vulnerability scanning of container images.

https://trivy.dev

---

### OWASP ZAP Documentation

Reference:

OWASP ZAP Documentation: Provides guidance for Dynamic Application Security Testing.

https://www.zaproxy.org/docs

---

### Kubernetes Documentation

Reference:

Kubernetes Documentation: Provides guidance for managing containerized workloads and services.

https://kubernetes.io/docs

---

## Author

James Banday

GitHub:
https://github.com/jbanday808/python-openshift-cicd/blob/main

LinkedIn:
https://www.linkedin.com/in/james-allen-morta-banday-62a391128


---

## License

This project is licensed under the MIT License.
