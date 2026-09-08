# IAM Identity Lifecycle

The IAM identity lifecycle ensures that user access is appropriately provisioned, modified, reviewed, monitored, and removed throughout the user's relationship with the organization.

```mermaid
flowchart LR
    A[HR / Business Request] --> B{Identity Lifecycle}

    B --> C[JOINER]
    B --> D[MOVER]
    B --> E[LEAVER]

    C --> C1[Create Identity]
    C1 --> C2[Create Account]
    C2 --> C3[Assign Role / Access]
    C3 --> C4[Enable Authentication & MFA]

    D --> D1[Change in Job Role]
    D1 --> D2[Review Existing Access]
    D2 --> D3[Remove Unnecessary Access]
    D3 --> D4[Assign New Role / Access]

    E --> E1[Termination / Exit]
    E1 --> E2[Disable Account]
    E2 --> E3[Revoke Sessions & Credentials]
    E3 --> E4[Remove Access]

    C4 --> F[Authentication]
    D4 --> F

    F --> G[Authorization]
    G --> H[Applications / Systems / Data]

    H --> I[Logging & Monitoring]
    I --> J[Periodic Access Review]

    J --> K{Access Still Required?}

    K -->|Yes| L[Retain / Adjust Access]
    K -->|No| M[Revoke Access]

    L --> I
    M --> I

    N[Privileged Access] -.-> G
    O[Least Privilege] -.-> G
    P[Segregation of Duties] -.-> G
    Q[Access Governance] -.-> J


Key IAM Lifecycle Activities
| Stage              | Key Activities                                  | Primary Risk                             |
| ------------------ | ----------------------------------------------- | ---------------------------------------- |
| **Joiner**         | Create identity, account and appropriate access | Unauthorized or excessive initial access |
| **Mover**          | Review and modify access following role changes | Privilege creep                          |
| **Leaver**         | Disable account and revoke access               | Former users retaining access            |
| **Authentication** | Verify user identity                            | Account compromise                       |
| **Authorization**  | Determine permitted actions                     | Excessive privileges                     |
| **Monitoring**     | Log and monitor access activity                 | Undetected misuse                        |
| **Access Review**  | Periodically validate access                    | Inappropriate or outdated access         |


Core Principles

The lifecycle is supported by:

Least Privilege
Need-to-Know
Role-Based Access Control (RBAC)
Segregation of Duties (SoD)
Strong Authentication
Access Governance
Periodic Access Reviews
Timely Deprovisioning
Example

A new employee joins a bank as a Teller.

HR confirms the employee's appointment.
An identity is created.
The required user account is provisioned.
The employee receives the Teller role.
Only the applications and transactions required for the Teller role are granted.
MFA is enabled.
User activity is logged and monitored.
Access is periodically reviewed.
If the employee becomes a Supervisor, unnecessary Teller access is removed and appropriate Supervisor access is assigned.
When the employee leaves the organization, the account is disabled and access is revoked.

This demonstrates how IAM supports appropriate access throughout the complete identity lifecycle.


