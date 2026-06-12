# Security Controls

---

## Overview

This document describes the security controls implemented throughout the **Python OpenShift CI/CD Pipeline with SAST, DAST, Trivy, and Git OAuth** project.

The purpose of these security controls is to protect the application throughout the Software Development Lifecycle (SDLC) by integrating security into every stage of development, testing, deployment, and operations.

This approach follows DevSecOps principles by shifting security left and validating security continuously throughout the CI/CD pipeline.

---

## Security Architecture

![Python OpenShift CI/CD Pipeline](../images/python-openshift-ci-cd-diagram-02.png)

**Figure 1.** High-level architecture showing the automated workflow from GitHub source code through testing, security scanning, container image creation, OpenShift deployment, and OWASP ZAP validation.

---

## Security Objective

The primary objective of this project is to ensure that:

* Source code is tested before deployment
* Security vulnerabilities are identified early
* Container images are scanned before deployment
* Trusted images are stored securely
* Applications are validated after deployment
* Runtime vulnerabilities are detected
* OpenShift resources are deployed securely

---

## Security Layers

The project uses multiple layers of security controls.

```text
Source Code Security
        |
        v
Unit Testing
        |
        v
Static Security Testing (SAST)
        |
        v
Container Security
        |
        v
Image Registry Security
        |
        v
OpenShift Platform Security
        |
        v
Dynamic Security Testing (DAST)
```

---

## Security Control 1: Source Code Management

### Tool

GitHub

### Purpose

GitHub serves as the centralized source control repository.

### Security Benefits

* Version control
* Change tracking
* Audit history
* Code review support
* Secure authentication

### Example Commands

```bash
git add .
git commit -m "Security update"
git push origin main
```

### Business Value

Provides traceability and accountability for application changes.

---

## Security Control 2: Git OAuth Authentication

### Tool

Git OAuth

### Purpose

Provides secure authentication between GitHub and OpenShift.

### Security Benefits

* Eliminates hardcoded credentials
* Supports secure repository access
* Improves authentication management

### Business Value

Reduces credential exposure and improves access security.

---

## Security Control 3: Unit Testing

### Tool

Pytest

### Figure 2: Unit Testing with Pytest

![Unit Tests](../images/unit-tests-pytest.png)

**Figure 2.** Pytest validates application functionality and confirms the code passes automated unit testing before deployment.

### Purpose

Validates application functionality before deployment.

### Example Command

```bash
PYTHONPATH=. pytest tests/test_app.py
```

### Security Benefits

* Identifies application defects
* Reduces deployment failures
* Verifies expected behavior

### Business Value

Improves application reliability and quality.

---

## Security Control 4: Static Application Security Testing (SAST)

### Tool

Bandit

### Figure 3: Bandit SAST Scan

![Bandit Scan](../images/bandit-sast-scan.png)

**Figure 3.** Bandit performs Static Application Security Testing to identify insecure coding practices within the Python source code.

### Purpose

Scans source code for security vulnerabilities before deployment.

### Example Command

```bash
python3 -m bandit -r app
```

### Security Benefits

Bandit can identify:

* Hardcoded passwords
* Weak cryptography
* Unsafe functions
* Insecure coding patterns

### Business Value

Reduces security risks early in the development process.

---

## Security Control 5: Container Image Security

### Tool

Podman

### Figure 4: Container Image Build

![Container Build](../images/docker-image.png)

**Figure 4.** The Python application is packaged into a portable container image for deployment across environments.

### Purpose

Creates a consistent and portable application artifact.

### Example Command

```bash
podman build -t python-openshift-cicd:latest .
```

### Security Benefits

* Consistent deployments
* Controlled runtime environment
* Dependency management

### Business Value

Improves deployment reliability and operational consistency.

---

## Security Control 6: Container Vulnerability Scanning

### Tool

Trivy

### Figure 5: Trivy Vulnerability Scan

![Trivy Scan](../images/trivy-scan-result.png)

**Figure 5.** Trivy scans the container image for known vulnerabilities, exposed secrets, and insecure packages.

### Purpose

Scans container images before deployment.

### Example Command

```bash
trivy image localhost/python-openshift-cicd:latest
```

### Security Benefits

Trivy identifies:

* Critical vulnerabilities
* High-risk vulnerabilities
* Exposed secrets
* Misconfigurations
* Vulnerable packages

### Business Value

Prevents vulnerable container images from reaching production.

---

## Security Control 7: Secure Container Registry

### Tool

Quay

### Figure 6: Quay Registry Repository

![Quay Repository](../images/quay-repo.png)

**Figure 6.** Quay serves as the secure container registry used to store and distribute application container images.

### Purpose

Stores approved container images.

### Security Benefits

* Secure image storage
* Controlled image access
* Registry authentication
* Image version tracking

### Business Value

Provides a trusted source for deployment images.

---

## Security Control 8: OpenShift Platform Security

### Tool

Red Hat OpenShift

### Figure 7: OpenShift ImageStream

![ImageStream](../images/image-stream.png)

**Figure 7.** OpenShift ImageStreams track container image versions and manage deployment image updates.

### Purpose

Provides secure orchestration and deployment.

### OpenShift Resources

* Deployments
* Pods
* Services
* Routes
* ImageStreams

### Example Commands

```bash
oc get deployment
oc get pods
oc get route
```

### Security Benefits

* Container isolation
* Resource management
* Controlled networking
* Deployment tracking

### Business Value

Provides a secure and scalable application platform.

---

## Security Control 9: CI/CD Pipeline Security

### Tool

Tekton Pipelines

### Purpose

Automates secure application delivery.

### Pipeline Stages

```text
Git Clone
      |
      v
Pytest
      |
      v
Bandit
      |
      v
Container Build
      |
      v
Trivy
      |
      v
Quay
      |
      v
Deployment
```

### Security Benefits

* Repeatable process
* Automated validation
* Reduced human error
* Security enforcement

### Business Value

Improves deployment speed and consistency while maintaining security.

---

## Security Control 10: Dynamic Application Security Testing (DAST)

### Tool

OWASP ZAP

### Figure 8: OWASP ZAP DAST Scan

![OWASP ZAP](../images/dast-owasp-zap-scan.png)

**Figure 8.** OWASP ZAP performs Dynamic Application Security Testing against the live application to identify runtime security vulnerabilities.

### Purpose

Scans the deployed application after deployment.

### Example Command

```bash
podman run --rm -t \
-v $(pwd)/zap-reports:/zap/wrk:Z \
ghcr.io/zaproxy/zaproxy:stable \
zap-baseline.py \
-t http://<openshift-route> \
-r zap-report.html
```

### Security Benefits

OWASP ZAP can identify:

* Missing security headers
* Authentication weaknesses
* Information disclosure
* Misconfigurations
* Runtime vulnerabilities

### Business Value

Validates the security posture of the running application.

---

## Defense-in-Depth Strategy

This project follows a Defense-in-Depth approach.

| Layer           | Tool      | Security Function                |
| --------------- | --------- | -------------------------------- |
| Source Control  | GitHub    | Version control and auditing     |
| Authentication  | Git OAuth | Secure repository access         |
| Unit Testing    | Pytest    | Functional validation            |
| SAST            | Bandit    | Source code security             |
| Container Build | Podman    | Standardized deployment artifact |
| Image Scan      | Trivy     | Vulnerability assessment         |
| Registry        | Quay      | Secure image storage             |
| Platform        | OpenShift | Secure application hosting       |
| DAST            | OWASP ZAP | Runtime security validation      |

---

## Security Validation Process

The project validates security at multiple stages.

### Before Deployment

* Unit Testing
* Bandit SAST Scan
* Trivy Vulnerability Scan

### During Deployment

* OpenShift Deployment Controls
* Secure Image Management

### After Deployment

* Route Validation
* OWASP ZAP DAST Scan

---

## Security Monitoring and Troubleshooting

Security validation requires continuous monitoring.

### Common Commands

Check deployment status:

```bash
oc get deployment
```

Check running pods:

```bash
oc get pods
```

Check routes:

```bash
oc get route
```

Check PipelineRuns:

```bash
oc get pipelinerun
```

Check TaskRuns:

```bash
oc get taskrun
```

View logs:

```bash
oc logs <pod-name>
```

Describe resources:

```bash
oc describe pod <pod-name>
```

### Business Value

Monitoring improves visibility and accelerates issue resolution.

---

## Security Challenges Encountered

Several security-related challenges were encountered.

### Challenge 1

Container image push failures.

### Resolution

Validated Quay authentication and service account permissions.

---

### Challenge 2

Pipeline task execution failures.

### Resolution

Reviewed TaskRun logs and corrected task configurations.

---

### Challenge 3

Deployment validation issues.

### Resolution

Validated OpenShift deployments, services, and routes.

---

## Future Security Enhancements

Potential future improvements include:

* SonarQube Integration
* Secret Scanning
* Automated Compliance Validation
* Admission Controllers
* OpenShift GitOps
* Argo CD
* Multi-Environment Security Gates
* Container Signing
* Software Bill of Materials (SBOM)

---

## Final Security Summary

This project demonstrates how security can be integrated throughout the CI/CD pipeline using a layered DevSecOps approach.

Security controls were implemented at the source code, container image, registry, deployment platform, and runtime levels.

The combination of GitHub, Git OAuth, Pytest, Bandit, Podman, Trivy, Quay, OpenShift, Tekton, and OWASP ZAP provides a comprehensive security framework for modern application delivery.

---

## Interview Summary

This project demonstrates hands-on experience with:

* DevSecOps
* CI/CD Pipeline Security
* OpenShift Administration
* Kubernetes Fundamentals
* Container Security
* Vulnerability Management
* Security Automation
* Application Deployment
* Production Troubleshooting
* Secure Software Delivery

It highlights the ability to implement security controls throughout the software development lifecycle and support secure production deployments.

---

## References

### GitHub Documentation

Reference:

GitHub Docs: Provides guidance for source control management, repository administration, authentication, and collaboration workflows.

https://docs.github.com

---

### Pytest Documentation

Reference:

Pytest Documentation: Provides instructions for creating and running automated Python tests.

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

Trivy Documentation: Provides guidance for vulnerability scanning of container images.

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

### Tekton Documentation

Reference:

Tekton Documentation: Provides guidance for creating Tasks, Pipelines, PipelineRuns, and CI/CD workflows.

https://tekton.dev/docs

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
