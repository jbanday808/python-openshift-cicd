# Python OpenShift CI/CD Pipeline with SAST, DAST, Trivy, Git OAuth

---

## Overview

This project demonstrates a complete DevSecOps CI/CD pipeline for deploying a Python Flask application to Red Hat OpenShift.

The pipeline automates:

* Source Code Management with GitHub
* Unit Testing with Pytest
* Static Application Security Testing (SAST) with Bandit
* Container Image Build with Podman
* Container Vulnerability Scanning with Trivy
* Container Registry Integration with Quay
* Application Deployment to OpenShift
* Dynamic Application Security Testing (DAST) with OWASP ZAP

---

## Architecture Diagram

![Python OpenShift CI/CD Pipeline](images/python-openshift-ci-cd-diagram-02.png)

---

## CI/CD Pipeline Flow

```text
GitHub Repository
        │
        ▼
Git OAuth Authentication
        │
        ▼
OpenShift Tekton Pipeline
        │
        ▼
Pytest Unit Testing
        │
        ▼
Bandit SAST Scan
        │
        ▼
Container Image Build
        │
        ▼
Trivy Vulnerability Scan
        │
        ▼
Push Image to Quay Registry
        │
        ▼
Deploy to OpenShift
        │
        ▼
Expose Application Route
        │
        ▼
OWASP ZAP DAST Scan
        │
        ▼
Production Application
```

---

## Technology Stack

| Category               | Technology        |
| ---------------------- | ----------------- |
| Language               | Python 3.11       |
| Framework              | Flask             |
| Testing                | Pytest            |
| SAST                   | Bandit            |
| Container Runtime      | Podman            |
| Container Build        | Dockerfile        |
| Container Registry     | Quay              |
| Vulnerability Scanning | Trivy             |
| CI/CD                  | Tekton Pipelines  |
| Platform               | Red Hat OpenShift |
| DAST                   | OWASP ZAP         |
| Authentication         | Git OAuth         |

---

## Project Screenshots

### Unit Testing with Pytest

![Unit Tests](images/unit-tests-pytest.png)

---

### Bandit SAST Scan

![Bandit Scan](images/bandit-sast-scan.png)

---

### Container Image Build

![Docker Image Build](images/docker-image.png)

---

### Trivy Vulnerability Scan

![Trivy Scan](images/trivy-scan-result.png)

---

### GitHub Push

![Git Push](images/git-push.png)

---

### OpenShift ImageStream

![ImageStream](images/image-stream.png)

---

### Quay Registry Repository

![Quay Repository](images/quay-repo.png)

---

### OpenShift Deployment

![OpenShift Deployment](images/openshift-ci-cd-final-deployment.png)

---

### OWASP ZAP DAST Scan

![OWASP ZAP Scan](images/dast-owasp-zap-scan.png)

---

## Features

* Python Flask Web Application
* OpenShift Deployment
* Tekton CI/CD Automation
* GitHub Source Control
* Git OAuth Authentication
* Pytest Unit Testing
* Bandit SAST Scanning
* Trivy Vulnerability Scanning
* Quay Registry Integration
* OWASP ZAP DAST Scanning
* DevSecOps Security Controls

---

## Skills Demonstrated

* DevSecOps
* CI/CD Pipeline Automation
* OpenShift Administration
* Kubernetes Fundamentals
* Containerization
* Python Development
* Git Source Control
* Security Automation
* Vulnerability Management
* Infrastructure as Code
* Troubleshooting and Debugging
* Secure Software Development Lifecycle (SSDLC)

---

## Repository Structure

```text
python-openshift-cicd/
├── .tekton/
├── app/
├── manifests/
├── tests/
├── images/
├── zap-reports/
├── docs/
│   ├── INSTALLATION.md
│   ├── TEKTON-PIPELINE.md
│   ├── SECURITY-SCANS.md
│   └── TROUBLESHOOTING.md
├── Dockerfile
├── requirements.txt
├── devfile.yaml
└── README.md
```

---

## Installation and Setup

Detailed installation instructions are available in:

```text
docs/INSTALLATION.md
```

---

## Tekton Pipeline Configuration

Detailed Tekton Pipeline configuration is available in:

```text
docs/TEKTON-PIPELINE.md
```

---

## Security Scanning

Detailed security scanning procedures are available in:

```text
docs/SECURITY-SCANS.md
```

---

## Troubleshooting

Common troubleshooting commands and solutions are available in:

```text
docs/TROUBLESHOOTING.md
```

---

## Lessons Learned

Throughout this project I gained hands-on experience:

* Building CI/CD pipelines using Tekton
* Deploying applications to OpenShift
* Managing container registries with Quay
* Implementing DevSecOps security controls
* Running SAST and DAST security scans
* Troubleshooting PipelineRuns and TaskRuns
* Managing Kubernetes resources
* Validating secure software delivery pipelines

---

## Results

Successfully implemented:

* Python Flask Application
* OpenShift Deployment
* Tekton CI/CD Pipeline
* GitHub Integration
* Git OAuth Authentication
* Bandit SAST Scanning
* Trivy Vulnerability Scanning
* Quay Registry Integration
* OWASP ZAP DAST Scanning
* End-to-End DevSecOps Workflow

---

## References

### GitHub Documentation

Reference:
GitHub Docs: Provides guidance for source control management, repository administration, authentication, and collaboration workflows.

https://docs.github.com

---

### Flask Documentation

Reference:
Flask Documentation: Provides guidance for building Python web applications.

https://flask.palletsprojects.com

---

### Pytest Documentation

Reference:
Pytest Documentation: Provides instructions for creating and running automated Python tests.

https://docs.pytest.org

---

### Bandit Documentation

Reference:
Bandit Documentation: Provides guidance for Static Application Security Testing (SAST).

https://bandit.readthedocs.io

---

### Podman Documentation

Reference:
Podman Documentation: Provides instructions for building and managing containers.

https://podman.io

---

### Trivy Documentation

Reference:
Trivy Documentation: Provides guidance for container vulnerability scanning.

https://trivy.dev

---

### Quay Documentation

Reference:
Red Hat Quay Documentation: Provides instructions for container image management.

https://docs.projectquay.io

---

### OpenShift Documentation

Reference:
Red Hat OpenShift Documentation: Provides guidance for deploying and managing applications.

https://docs.openshift.com

---

### OpenShift Pipelines Documentation

Reference:
OpenShift Pipelines Documentation: Provides instructions for implementing CI/CD pipelines using Tekton.

https://docs.openshift.com/container-platform/latest/cicd/pipelines

---

### Tekton Documentation

Reference:
Tekton Documentation: Provides guidance for Tasks, Pipelines, and PipelineRuns.

https://tekton.dev/docs

---

### OWASP ZAP Documentation

Reference:
OWASP ZAP Documentation: Provides guidance for Dynamic Application Security Testing (DAST).

https://www.zaproxy.org/docs

---

### Kubernetes Documentation

Reference:
Kubernetes Documentation: Provides guidance for container orchestration and workload management.

https://kubernetes.io/docs

---

## Author

James Banday

GitHub:
https://github.com/jbanday808

LinkedIn:
https://www.linkedin.com/in/james-allen-morta-banday-62a391128

Medium:
https://medium.com/@jamesbanday

---

## License

This project is licensed under the MIT License.
