# IAM Core Concepts

## 1. Introduction

Identity and Access Management (IAM) is the set of processes, policies, technologies, and controls used to manage digital identities and regulate access to information systems and resources.

The primary objective of IAM is to ensure that:

> The right identity has the right access to the right resource for the right reason and for the appropriate period of time.

IAM therefore supports both security and business operations by enabling authorized users to access the resources required to perform their responsibilities while preventing unauthorized access.

---

## 2. Identity

An identity represents an individual, system, service, device, or other entity that needs to be recognized within an information environment.

Examples include:

- Employees
- Contractors
- Customers
- Service accounts
- Applications
- Devices
- Administrators

An identity establishes **who or what an entity is**, but does not by itself determine what that entity can access.

### Example

An employee named Ama may have an identity associated with:

- Employee ID
- Name
- Department
- Job title
- Manager
- Employment status

That identity may subsequently be associated with accounts across multiple systems.

---

## 3. Account

An account is a representation of an identity within a specific system or application.

For example, an employee may have:

- Microsoft Entra ID account
- Email account
- Core banking account
- VPN account
- AWS account or assigned AWS access
- HR application account

One identity may therefore have multiple accounts.

### Key distinction

**Identity = who the entity is**

**Account = how that identity is represented in a particular system**

---

## 4. Authentication

Authentication is the process of verifying that an entity is who or what it claims to be.

Authentication answers:

> "Who are you?"

Common authentication factors include:

### Something you know

- Password
- PIN

### Something you have

- Security token
- Mobile device
- Smart card

### Something you are

- Fingerprint
- Facial recognition
- Other biometric characteristics

### Multi-Factor Authentication

Multi-Factor Authentication (MFA) combines two or more independent authentication factors to provide stronger protection against unauthorized access.

---

## 5. Authorization

Authorization determines what an authenticated identity is permitted to do.

Authorization answers:

> "What are you allowed to do?"

For example, after a bank employee successfully authenticates, the system may determine that the employee can:

- View customer information
- Create transactions
- Process certain transactions

but cannot:

- Approve their own transactions
- Access administrator functions
- Modify security configurations

Authentication therefore establishes identity, while authorization determines permitted actions.

---

## 6. Access

Access is the ability granted to an identity to interact with a resource.

Access may include the ability to:

- Read
- Create
- Modify
- Delete
- Execute
- Approve
- Administer

Access should be granted based on legitimate business requirements and should be restricted according to security principles such as least privilege and need-to-know.

---

## 7. Resource

A resource is something an identity may need to access.

Examples include:

- Applications
- Databases
- Files
- Servers
- Cloud resources
- APIs
- Network resources
- Business systems

An IAM control therefore establishes a relationship between an identity and the resources/actions that identity is permitted to access.

---

# 8. IAM Relationship

The relationship between the major IAM concepts can be represented as:

``text
Identity
    |
    v
Account
    |
    v
Authentication
    |
    v
Authorization
    |
    v
Access
    |
    v
Resource


A simplfied Example
Employee
   |
   v
Identity
   |
   v
Microsoft Entra Account
   |
   v
Authentication
   |
   v
Authorization
   |
   v
Assigned Role
   |
   v
Permitted Actions
   |
   v
Application / Data


9. Least Privilege

The principle of least privilege requires that an identity receives only the level of access necessary to perform its authorized responsibilities.

Access should be:

Necessary
Appropriate
Limited
Reviewed periodically
Removed when no longer required
Example

A bank teller may need permission to:

View customer accounts
Process permitted transactions

The teller should not automatically receive:

Database administrator privileges
System administrator privileges
User-management privileges
Ability to approve their own transactions

Granting unnecessary permissions increases the potential impact of compromised or misused accounts.


10. Need-to-Know

The need-to-know principle restricts access to information based on whether the identity has a legitimate business requirement to access that information.

Example

A customer service officer may need access to customer information to perform their duties.

However, this does not necessarily mean the officer should have access to:

Payroll information
Security administration data
Database administration functions
Information belonging to unrelated business units

Least privilege focuses primarily on limiting permissions, while need-to-know focuses on limiting access to information required for legitimate duties.


11. Role-Based Access Control

Role-Based Access Control (RBAC) assigns permissions based on organizational roles rather than assigning permissions individually to every user.

A simplified RBAC model is:
User
  |
  v
Role
  |
  v
Permissions
  |
  v
Resources

Example;
Teller
  |
  +--> View Customer Account
  +--> Create Permitted Transaction
  +--> View Transaction History

  A manager may have a different role:
  Branch Manager
  |
  +--> View Customer Account
  +--> Approve Transactions
  +--> View Branch Reports
  RBAC can improve consistency, simplify access management, and support the principle of least privilege.



  12. Privileged Access

Privileged access provides elevated permissions that allow an identity to perform sensitive administrative or security-related activities.

Examples include:

System administrator
Database administrator
Network administrator
Cloud administrator
Security administrator

Privileged accounts present greater risk because their compromise may provide extensive control over systems or data.

Controls for privileged access may include:

Separate administrator accounts
MFA
Privileged Access Management (PAM)
Time-limited access
Approval workflows
Session monitoring
Activity logging
Periodic access reviews


13. Segregation of Duties

Segregation of Duties (SoD) is a control principle designed to prevent one individual from having conflicting responsibilities that could enable unauthorized activity or fraud.

Example

A user should not normally be able to:
Create Payment
      +
Approve Payment

The responsibilities should be separated:
User A
Create Payment
      |
      v
User B
Approve Payment

SoD is particularly important in financial environments where users may otherwise be able to initiate, approve, and execute sensitive transactions.



14. Identity Lifecycle Management

Identity lifecycle management manages an identity throughout its relationship with an organization.

A common model is:
JOINER
   |
   v
Identity Created
   |
   v
Access Provisioned
   |
   v
MOVER
   |
   v
Access Modified
   |
   v
LEAVER
   |
   v
Access Revoked

Joiner

When a person joins the organization:

Identity is created
Account is provisioned
Appropriate access is requested
Access is approved
Access is granted
Mover

When a person's role changes:

Existing access is reviewed
Unnecessary access is removed
New access is requested
Appropriate approvals are obtained
New access is provisioned
Leaver

When a person leaves:

Accounts are disabled or removed
Application access is revoked
Privileged access is removed
Authentication credentials are invalidated
Organizational resources are recovered where applicable

Timely deprovisioning is important because former employees or users should not retain unnecessary access to organizational systems.


15. Access Governance

Access governance establishes the policies, processes, responsibilities, and controls used to ensure that access remains appropriate throughout the identity lifecycle.

Important activities include:

Access requests
Access approvals
Provisioning
Access reviews
Privileged access management
Segregation of Duties
Deprovisioning
Exception management
Reporting
Monitoring

Effective governance ensures that IAM is not treated solely as a technical function but as an organizational security and risk-management process.


16. Common IAM Risks
**Excessive Privileges
Users receive more access than required for their responsibilities.
Potential impact:
Unauthorized activity
Data exposure
Fraud
Increased impact of account compromise


**Orphaned Accounts
Accounts remain active even though the associated identity is no longer valid.
Potential impact:
Unauthorized access
Reduced accountability


**Privilege Creep
Users accumulate access over time as they change roles without having unnecessary permissions removed.
Potential impact:
Excessive access
Increased security risk


**Delayed Deprovisioning
Access is not removed promptly when a user leaves the organization.
Potential impact:
Former employees retaining access
Unauthorized system activity


**Shared Accounts
Multiple individuals use the same account.
Potential impact:
Poor accountability
Difficulty attributing activities to individuals


**Weak Authentication
Systems rely on inadequate authentication controls.
Potential impact:
Account compromise
Unauthorized access


**SoD Conflicts
Users receive combinations of permissions that create conflicting responsibilities.
Potential impact:
Fraud
Unauthorized transactions
Control circumvention

17. IAM Control Objectives

An organization should establish controls to ensure that:

User identities are uniquely identified.
Access is authorized before provisioning.
Access is based on business requirements.
Least privilege is applied.
Privileged access is appropriately controlled.
Access changes are authorized.
User access is periodically reviewed.
Conflicting access is identified and addressed.
Access is promptly revoked when no longer required.
IAM activities are appropriately logged and monitored.


18. IAM and the CIA Triad

IAM supports the three core objectives of information security:

Confidentiality

IAM helps prevent unauthorized individuals from accessing sensitive information.

Integrity

IAM helps ensure that only authorized users can modify information or perform sensitive actions.

Availability

IAM helps ensure that legitimate users can access the resources required to perform their responsibilities.

Therefore:
             IAM
              |
       +------+------+ 
       |      |      |
       v      v      v
 Confidentiality Integrity Availability


 19. Practical IAM Perspective
IAM should not be viewed simply as creating and deleting user accounts.
An effective IAM program considers:
Who is the identity?
What access does the identity have?
Why does the identity need that access?
Who approved the access?
Is the access appropriate for the identity's role?
Is the access still required?
Is the access being monitored?
When should the access expire?
What happens when the identity changes roles?
What happens when the identity leaves?
These questions form the basis for the practical IAM projects that follow in this portfolio.


Next Steps
The concepts documented here will be applied practically through:
Identity Lifecycle Management
RBAC and Least Privilege
User Access Reviews
Microsoft Entra ID
AWS IAM
AWS IAM Identity Center
Privileged Access Management
Segregation of Duties
IAM Risk Assessment
IAM Audit
Enterprise IAM Capstone
