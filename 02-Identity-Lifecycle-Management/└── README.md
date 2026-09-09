# Identity Lifecycle Management

## Overview

This project demonstrates how an organization can manage user identities and access throughout the employee lifecycle.

The project focuses on the Joiner, Mover, and Leaver (JML) processes and demonstrates how identity lifecycle controls can reduce the risk of unauthorized, excessive, or retained access.

The process is designed from an enterprise IAM and access governance perspective and is applicable to environments such as banking, financial services, and other organizations with sensitive systems and data.

---

## Business Scenario

A financial institution wants to establish a controlled process for managing employee access from onboarding through role changes and eventual exit from the organization.

Employees may require access to multiple applications and systems based on their job responsibilities. Without a structured identity lifecycle process, the organization may be exposed to risks such as:

- Unauthorized access
- Excessive privileges
- Privilege creep
- Dormant or orphaned accounts
- Delayed access removal
- Inappropriate access following role changes
- Segregation of Duties (SoD) conflicts

The organization therefore requires a controlled Joiner-Mover-Leaver process.

---

## Objective

The objectives of this project are to:

1. Design a structured Identity Lifecycle Management process.
2. Define the activities performed during Joiner, Mover, and Leaver events.
3. Establish appropriate approval and access control requirements.
4. Identify key IAM risks associated with the lifecycle.
5. Define controls that mitigate these risks.
6. Identify evidence that should be retained to demonstrate that access was appropriately managed.
7. Demonstrate how IAM principles can be applied to a realistic business environment.

---

## Identity Lifecycle

The identity lifecycle consists of three major stages:

### 1. Joiner

The Joiner process manages access when a new employee joins the organization.

Typical activities include:

- Creation of the user's identity
- Creation of required accounts
- Assignment of appropriate roles
- Provisioning of application access
- Configuration of authentication and MFA
- Validation that access is approved and appropriate

### 2. Mover

The Mover process manages access when an employee changes role, department, location, or responsibilities.

Typical activities include:

- Identification of the employee's new role
- Review of existing access
- Removal of access no longer required
- Assignment of access required for the new role
- Review for excessive privileges
- Assessment of potential SoD conflicts

### 3. Leaver

The Leaver process manages access when an employee leaves the organization.

Typical activities include:

- Confirmation of employee termination or exit
- Disabling user accounts
- Revoking application access
- Revoking active sessions and credentials
- Removing group and role memberships
- Recovering organizational assets where applicable
- Retaining evidence of access revocation

---

## Key IAM Principles Applied

This project applies the following IAM principles:

- Least Privilege
- Need-to-Know
- Role-Based Access Control (RBAC)
- Segregation of Duties (SoD)
- Strong Authentication
- Accountability
- Timely Provisioning and Deprovisioning
- Periodic Access Review

---

## Expected Outcome

At the completion of this project, the organization should have a documented and controlled process for:

**Employee joins → Access is provisioned → Employee changes role → Access is reviewed and modified → Employee leaves → Access is revoked**

The process should ensure that users receive only the access required for their responsibilities and that access is removed when it is no longer required.

---

## Project Artifacts

The project will include:

- Identity Lifecycle Process
- Joiner-Mover-Leaver (JML) Matrix
- IAM Lifecycle Risk and Control Matrix
- Access Request and Approval Workflow
- Sample Access Provisioning/Deprovisioning Evidence
- Practical IAM Analysis
- Lessons Learned

---

## Status

🟡 In Progress
