# JML Access Management Simulator

## Overview

This practical exercise simulates how an organization can manage user access during Joiner, Mover, and Leaver events.

The exercise uses fictional employee records and role-based access rules to demonstrate how IAM processes can be applied programmatically.

## Objectives

The simulator will demonstrate how to:

- Process Joiner, Mover, and Leaver events
- Determine expected access based on an employee's role
- Provision access for new employees
- Review and modify access when an employee changes roles
- Revoke access when an employee leaves
- Identify potential access issues
- Produce evidence that can support IAM control reviews

## Inputs

The simulator uses two input files:

### `employees.csv`

Contains fictional employee records and their current JML event.

### `access_rules.csv`

Defines the access that each role is expected to have.

## Processing

The Python program will:

1. Read employee records.
2. Read role-based access rules.
3. Determine the appropriate action based on the JML event.
4. Assign, modify, or revoke access.
5. Identify potential access exceptions.
6. Generate an output that can be reviewed as IAM evidence.

## IAM Concepts Demonstrated

- Identity Lifecycle Management
- Joiner-Mover-Leaver (JML)
- Role-Based Access Control (RBAC)
- Least Privilege
- Access Provisioning
- Access Modification
- Access Revocation
- Access Review
- IAM Control Validation

## Technologies

- Python
- CSV
- GitHub

## Status

🟡 In Progress
