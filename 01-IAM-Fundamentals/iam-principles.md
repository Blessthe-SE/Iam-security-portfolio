This file will explain the principles that should guide IAM decisions.

# IAM Security Principles

## 1. Introduction

IAM principles provide the security foundation for determining how identities should be granted, managed, monitored, and removed from organizational systems.

These principles help organizations balance business requirements with security and risk considerations.

The key principles covered in this document are:

- Least Privilege
- Need-to-Know
- Separation of Duties
- Zero Trust
- Accountability
- Strong Authentication
- Access Reviews
- Timely Provisioning and Deprovisioning
- Defense in Depth

---

# 2. Least Privilege

## Definition

The principle of least privilege requires an identity to receive only the minimum permissions necessary to perform its authorized responsibilities.

Access should not be granted simply because a user belongs to a particular department or because the access may be useful in the future.

### Example

A bank teller may require access to:

- View customer accounts
- Process permitted transactions
- View transaction history

The teller should not automatically receive:

- Database administrator privileges
- System administrator privileges
- User administration privileges
- Security configuration privileges

### Security Objective

Reduce the potential impact of:

- Compromised accounts
- Insider threats
- Human error
- Unauthorized activity

### IAM Controls

- RBAC
- Access approval
- Privileged access management
- Periodic access reviews
- Removal of unnecessary permissions

---

# 3. Need-to-Know

## Definition

Need-to-know limits access to information based on whether an identity has a legitimate business requirement to access that information.

### Example

A Customer Service Officer may require access to customer information to perform their responsibilities.

However, the officer may not need access to:

- Employee payroll information
- Database administration information
- Security administration data
- Information belonging to unrelated business functions

### Least Privilege vs Need-to-Know

These principles are related but not identical.

**Least Privilege** focuses primarily on limiting the permissions and capabilities assigned to an identity.

**Need-to-Know** focuses on limiting access to information based on legitimate business requirements.

Both principles help reduce unnecessary exposure.

---

# 4. Separation of Duties

## Definition

Separation of Duties (SoD) requires sensitive or conflicting responsibilities to be divided among different individuals or roles.

The objective is to prevent one individual from having sufficient control to complete a sensitive process without appropriate oversight.

### Example

A user should not normally be able to:

``text
Create Payment
      +
Approve Payment
      +
Execute Payment

Instead, responsibilities should be separated:
User A
Create Payment
      |
      v
User B
Approve Payment
      |
      v
User C
Execute Payment



IAM Controls
SoD rules
Role design
Access approval
Conflict detection
Periodic access reviews
Compensating controls for approved exceptions
Risk
Poorly designed access may allow an individual to bypass controls or commit and conceal unauthorized activity.


5. Zero Trust
Definition

Zero Trust is a security approach based on the principle that access should not be trusted automatically based solely on network location, device location, or previous access.

A simplified principle is:

Never trust implicitly; continuously verify.

IAM plays an important role in Zero Trust because access decisions should consider factors such as:

Identity
Authentication strength
Device
Location
Application
Resource
Risk
Context
Example

An employee accessing a sensitive application from an unfamiliar device may be required to provide additional authentication even if the employee has previously accessed the application.

IAM Controls
MFA
Conditional access
Risk-based authentication
Device controls
Session controls
Continuous monitoring


6. Accountability
Definition

IAM should enable activities performed within systems to be attributed to a specific identity.

Every user should ideally have a unique account rather than relying on shared accounts.

Example

Instead of:
User → SHARED_ADMIN
use:
Ama → Ama.Admin
Kofi → Kofi.Admin


This improves the ability to determine who performed an administrative or sensitive action.

IAM Controls
Unique user accounts
Individual administrator accounts
Authentication logging
Privileged activity monitoring
Audit trails
Controlled use of service accounts
Risk of Shared Accounts

Shared accounts can make it difficult to:

Attribute activities
Investigate incidents
Establish responsibility
Perform effective monitoring


7. Strong Authentication
Definition

Authentication controls should provide sufficient assurance that an identity is legitimate before access is granted.

Where appropriate, organizations should use Multi-Factor Authentication (MFA).

Authentication Factors

Something you know

Password
PIN

Something you have

Security token
Mobile device

Something you are

Biometric characteristic
Higher-Risk Access

Stronger authentication should generally be applied to sensitive access such as:

Privileged accounts
Financial systems
Production environments
Security systems
Sensitive information


8. Access Reviews
Definition

Access should not be considered permanent simply because it was appropriately approved when initially granted.

Organizations should periodically review access to determine whether it remains:

Appropriate
Authorized
Necessary
Consistent with the user's current role
Example

An employee who moved from:
Teller
   ↓
IT Support

may still retain access originally granted for the teller role.

This is an example of potential privilege creep.

Access Review Process
Identify Users
      ↓
Identify Access
      ↓
Compare Against Role
      ↓
Manager/Owner Review
      ↓
Identify Exceptions
      ↓
Remediate
      ↓
Document Results


9. Timely Provisioning and Deprovisioning
Definition

Access should be provisioned and removed according to defined processes and timelines.

Joiner

Appropriate access is granted when a user joins.

Mover

Access is updated when a user's responsibilities change.

Leaver

Access is removed when a user leaves.

Example

If an employee leaves an organization, their access should not remain active indefinitely while waiting for a periodic access review.

Key Controls
HR/IAM integration
Automated provisioning
Automated deprovisioning
Termination notifications
Defined SLAs
Monitoring and exception reporting


10. Defense in Depth
Definition

Defense in depth uses multiple layers of security controls so that the failure of one control does not automatically result in unauthorized access.

IAM Example
Identity Verification
        ↓
Strong Authentication
        ↓
MFA
        ↓
Authorization
        ↓
Least Privilege
        ↓
Privileged Access Controls
        ↓
Logging & Monitoring
        ↓
Access Review

If a password is compromised, MFA may prevent unauthorized access.

If MFA is bypassed or an account is compromised, least privilege can limit what the attacker can access.

If unauthorized activity occurs, logging and monitoring can support detection and investigation.


11. Principle Interaction

IAM principles should not be treated as isolated controls.

For example:
              Strong Authentication
                       ↓
                  Identity
                       ↓
                  Authorization
                       ↓
                Least Privilege
                       ↓
                Need-to-Know
                       ↓
              Separation of Duties
                       ↓
                Monitoring
                       ↓
                Access Review

Together, these principles create a layered approach to identity security.


12. IAM Principle-to-Control Mapping
| Principle             | Example Control            | Risk Addressed              |
| --------------------- | -------------------------- | --------------------------- |
| Least Privilege       | RBAC                       | Excessive access            |
| Need-to-Know          | Data access restrictions   | Information exposure        |
| Separation of Duties  | SoD rules                  | Fraud/control circumvention |
| Zero Trust            | MFA/Conditional Access     | Unauthorized access         |
| Accountability        | Unique accounts/logging    | Lack of attribution         |
| Strong Authentication | MFA                        | Account compromise          |
| Access Reviews        | Periodic recertification   | Privilege creep             |
| Timely Deprovisioning | Automated offboarding      | Orphaned accounts           |
| Defense in Depth      | Multiple security controls | Control failure             |



13. Practical Application

The principles in this document will be tested and demonstrated through subsequent IAM projects.

Examples include:

Designing RBAC for a fictional financial institution
Performing user access reviews
Identifying excessive privileges
Detecting Segregation of Duties conflicts
Implementing MFA
Implementing IAM controls in Microsoft Entra ID
Implementing IAM controls in AWS
Assessing privileged access
Performing an IAM risk assessment
Conducting an IAM audit


14. Key Takeaway

Effective IAM is not simply about granting or removing access.

It is about ensuring that access is:

Appropriate → Authorized → Necessary → Limited → Monitored → Reviewed → Removed when no longer required

These principles will form the basis for the practical IAM implementations and assessments developed throughout this portfolio.




