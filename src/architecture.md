# Architecture Overview

---

## Overview

This document explains the architecture for the **Python OpenShift CI/CD Pipeline with SAST, DAST, Trivy, and Git OAuth** project.

The purpose of this architecture is to show how a Python Flask application moves from GitHub source code to a running OpenShift application using an automated and secure DevSecOps workflow.

---

## Architecture Diagram

![Python OpenShift CI/CD Pipeline](../images/python-openshift-ci-cd-diagram-02.png)

**Figure 1.** High-level architecture showing the automated workflow from GitHub source code through testing, security scanning, container image creation, OpenShift deployment, and OWASP ZAP validation.

---

## Architecture Goal

The goal of this project is to create a secure, repeatable, and automated CI/CD pipeline that supports application delivery from development to production validation.

This architecture supports:

* Source code management
* Secure GitHub authentication
* Automated unit testing
* Static source code security scanning
* Container image creation
* Container vulnerability scanning
* Secure image registry storage
* OpenShift application deployment
* Runtime security validation

---

## High-Level Pipeline Flow

```text
GitHub Repository
        |
        v
Git OAuth Authentication
        |
        v
OpenShift Tekton Pipeline
        |
        v
Unit Testing with Pytest
        |
        v
SAST Scan with Bandit
        |
        v
Container Image Build
        |
        v
Trivy Vulnerability Scan
        |
        v
Push Image to Quay Registry
        |
        v
Deploy to OpenShift
        |
        v
Expose Application with OpenShift Route
        |
        v
DAST Scan with OWASP ZAP
        |
        v
Production Application
```

---

## Step 1: GitHub Repository

GitHub is used as the source code repository for the Python application and project configuration files.

### Purpose

GitHub stores:

* Python application code
* Unit tests
* Dockerfile
* OpenShift manifests
* Tekton pipeline files
* Security scan reports
* Project documentation

### Business Value

GitHub provides a central source of truth for the project and allows changes to be tracked, reviewed, and version controlled.

---

## Step 2: Git OAuth Authentication

Git OAuth provides secure authentication between GitHub and the pipeline.

### Purpose

Git OAuth allows the pipeline to access the GitHub repository securely without manually copying source code into OpenShift.

### Business Value

Git OAuth improves security by using controlled authentication instead of hardcoded credentials.

---

## Step 3: OpenShift Tekton Pipeline

OpenShift Pipelines uses Tekton to automate the CI/CD workflow.

### Purpose

The Tekton pipeline controls the full delivery process from code retrieval to deployment.

### Pipeline Tasks

The pipeline includes:

* `git-clone`
* `pytest-test`
* `bandit-sast`
* `s2i-python`
* `trivy-scan`
* `push-to-quay`

### Business Value

Tekton reduces manual deployment work and creates a repeatable process for testing, scanning, building, and deploying the application.

---

## Step 4: Unit Testing with Pytest

Pytest is used to validate that the Python Flask application works correctly.

### Purpose

Pytest checks the `/health` endpoint and confirms the application responds as expected.

### Example Command

```bash
PYTHONPATH=. pytest tests/test_app.py
```

### Business Value

Automated testing helps prevent broken code from moving further through the pipeline.

---

## Step 5: SAST Scan with Bandit

Bandit performs Static Application Security Testing on the Python source code.

### Purpose

Bandit scans the application before deployment to identify insecure coding practices.

### Example Command

```bash
python3 -m bandit -r app
```

### Business Value

SAST helps catch security issues early before the application is built into a container image.

---

## Step 6: Container Image Build

The Python application is packaged into a container image using a Dockerfile.

### Purpose

The container image includes the application code, dependencies, runtime configuration, and startup command.

### Example Command

```bash
podman build -t python-openshift-cicd:latest .
```

### Business Value

Containerization ensures the application runs consistently across local, test, and OpenShift environments.

---

## Step 7: Trivy Vulnerability Scan

Trivy scans the container image for known vulnerabilities.

### Purpose

Trivy checks the image for:

* Vulnerable packages
* Known CVEs
* Misconfigurations
* Exposed secrets

### Example Command

```bash
trivy image localhost/python-openshift-cicd:latest
```

### Business Value

Trivy helps prevent vulnerable container images from being promoted into the deployment process.

---

## Step 8: Quay Container Registry

Quay is used as the container registry for storing application images.

### Purpose

Quay stores the approved container image after it is built and scanned.

### Business Value

Quay provides a secure registry location where OpenShift and pipeline tools can pull trusted images.

---

## Step 9: OpenShift Deployment

OpenShift runs the Python application as a containerized workload.

### Purpose

OpenShift deploys the application using Kubernetes resources such as:

* Deployment
* Pod
* Service
* Route
* ImageStream

### Example Commands

```bash
oc get deployment
oc get pods
oc get route
```

### Business Value

OpenShift provides a scalable, managed platform for running the application securely.

---

## Step 10: OpenShift Route

The OpenShift Route exposes the Python application so users and security tools can access it.

### Purpose

The route provides a public application URL for testing and validation.

### Example Command

```bash
oc get route
```

### Business Value

The route makes the application available for users, validation checks, and DAST scanning.

---

## Step 11: DAST Scan with OWASP ZAP

OWASP ZAP performs Dynamic Application Security Testing against the running application.

### Purpose

OWASP ZAP scans the live application from an external user perspective.

### Example Command

```bash
podman run --rm -t \
-v $(pwd)/zap-reports:/zap/wrk:Z \
ghcr.io/zaproxy/zaproxy:stable \
zap-baseline.py \
-t http://<openshift-route> \
-r zap-report.html
```

### Business Value

DAST validates the security of the deployed application at runtime.

---

## Architecture Components

| Component       | Tool                | Role                            |
| --------------- | ------------------- | ------------------------------- |
| Source Control  | GitHub              | Stores project source code      |
| Authentication  | Git OAuth           | Secures repository access       |
| CI/CD Engine    | Tekton              | Automates pipeline workflow     |
| Platform        | OpenShift           | Runs containerized applications |
| Unit Testing    | Pytest              | Validates functionality         |
| SAST            | Bandit              | Scans source code               |
| Container Build | Dockerfile / Podman | Builds application image        |
| Image Scan      | Trivy               | Scans container vulnerabilities |
| Registry        | Quay                | Stores container images         |
| DAST            | OWASP ZAP           | Scans live application          |

---

## Security Architecture

This project applies security checks throughout the software delivery lifecycle.

### Security Layers

| Layer             | Tool      | Purpose                            |
| ----------------- | --------- | ---------------------------------- |
| Code Security     | Bandit    | Finds insecure Python code         |
| Test Validation   | Pytest    | Confirms application functionality |
| Image Security    | Trivy     | Finds container vulnerabilities    |
| Registry Security | Quay      | Stores trusted images              |
| Runtime Security  | OWASP ZAP | Tests live application security    |
| Platform Security | OpenShift | Manages container workloads        |

---

## Deployment Architecture

The deployment architecture follows this flow:

```text
Container Image
        |
        v
OpenShift ImageStream
        |
        v
OpenShift Deployment
        |
        v
OpenShift Pod
        |
        v
OpenShift Service
        |
        v
OpenShift Route
        |
        v
End User / Security Scanner
```

---

## Reliability Design

This architecture improves reliability by using:

* Automated testing
* Automated builds
* Repeatable pipeline tasks
* Containerized deployment
* OpenShift health validation
* Route-based application testing
* Pipeline logs for troubleshooting

---

## Troubleshooting Design

The architecture supports troubleshooting through:

* PipelineRun logs
* TaskRun logs
* OpenShift pod logs
* Deployment status
* Route testing
* Container scan reports
* DAST scan reports

### Common Troubleshooting Commands

```bash
oc get pods
oc get deployment
oc get route
oc get pipelinerun
oc get taskrun
oc logs <pod-name>
oc describe pod <pod-name>
tkn pipelinerun logs -f <pipelinerun-name>
```

---

## Final Architecture Summary

This architecture demonstrates a secure and automated DevSecOps workflow for deploying a Python Flask application to OpenShift.

The pipeline starts with source code in GitHub, validates the application with Pytest, scans the code with Bandit, builds a container image, scans the image with Trivy, stores the image in Quay, deploys the application to OpenShift, and validates the running application with OWASP ZAP.

---

## Interview Summary

This project shows hands-on experience with CI/CD pipeline automation, containerization, OpenShift deployment, security scanning, and production-style troubleshooting.

It demonstrates the ability to build and support a secure application delivery pipeline from code commit to production validation.

---

## References

### GitHub Documentation

Reference:
GitHub Docs: Provides guidance for source control management, repository administration, authentication, and collaboration workflows.

https://docs.github.com

---

### Flask Documentation

Reference:
Flask Documentation: Provides guidance for building Python web applications using the Flask framework.

https://flask.palletsprojects.com

---

### Pytest Documentation

Reference:
Pytest Documentation: Provides instructions for creating and running automated Python unit tests.

https://docs.pytest.org

---

### Bandit Documentation

Reference:
Bandit Documentation: Provides guidance for Static Application Security Testing on Python source code.

https://bandit.readthedocs.io

---

### Podman Documentation

Reference:
Podman Documentation: Provides instructions for building, running, and managing containers.

https://podman.io

---

### Trivy Documentation

Reference:
Trivy Documentation: Provides guidance for vulnerability scanning of container images, filesystems, and repositories.

https://trivy.dev

---

### Quay Documentation

Reference:
Red Hat Quay Documentation: Provides instructions for managing container image repositories and registry authentication.

https://docs.projectquay.io

---

### OpenShift Documentation

Reference:
Red Hat OpenShift Documentation: Provides guidance for deploying, managing, and troubleshooting applications on OpenShift.

https://docs.openshift.com

---

### OpenShift Pipelines Documentation

Reference:
OpenShift Pipelines Documentation: Provides instructions for implementing CI/CD pipelines using Tekton.

https://docs.openshift.com/container-platform/latest/cicd/pipelines

---

### Tekton Documentation

Reference:
Tekton Documentation: Provides guidance for creating Tasks, Pipelines, PipelineRuns, and CI/CD workflows.

https://tekton.dev/docs

---

### OWASP ZAP Documentation

Reference:
OWASP ZAP Documentation: Provides guidance for Dynamic Application Security Testing of running web applications.

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


