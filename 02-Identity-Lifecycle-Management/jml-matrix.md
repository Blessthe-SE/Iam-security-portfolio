# Joiner-Mover-Leaver (JML) Matrix

## Purpose

The JML matrix defines the activities, responsibilities, approvals, controls, risks, and evidence required to manage user access 
throughout the employee lifecycle.

It provides a structured approach for ensuring that access is appropriately granted, modified, reviewed, and revoked.

---

## JML Control Matrix

| Lifecycle Event | Trigger | Key Activities | Approval / Authorization | Key Control | Evidence |
|---|---|---|---|---|---|
| **Joiner** | New employee joins | Create identity and required accounts; assign role-based access; enable MFA | Manager / Application Owner | Access must be based on approved job responsibilities | Access request, approval, provisioning record |
| **Mover** | Employee changes role or department | Review existing access; remove unnecessary access; assign new access | New Manager / Application Owner | Existing access must be reassessed before new access is granted | Role-change request, access review, approval |
| **Leaver** | Employee leaves organization | Disable account; revoke access; remove group memberships and active sessions | HR / Authorized Management | Access must be revoked promptly upon termination | Termination notification, disablement log, revocation record |

---

## Detailed JML Activities

### Joiner

| Activity | Responsible Party | Control Objective |
|---|---|---|
| Employee record created | HR | Ensure employee information is formally established |
| Access requirement identified | Hiring Manager | Ensure access is based on business need |
| Access request submitted | Manager / Authorized Requestor | Ensure access requests are formally initiated |
| Access approved | Manager / Application Owner | Ensure access is authorized |
| Account provisioned | IAM / IT Support | Ensure only approved access is provisioned |
| MFA configured | IAM / IT Support | Strengthen authentication |
| Provisioning validated | Manager / User | Confirm required access is available and appropriate |

### Mover

| Activity | Responsible Party | Control Objective |
|---|---|---|
| Role change identified | HR / Manager | Ensure changes affecting access are identified |
| Existing access reviewed | Manager / Application Owner | Identify access no longer required |
| Unnecessary access removed | IAM / IT Support | Prevent privilege creep |
| New access requested | Manager | Ensure new access is business justified |
| New access approved | Manager / Application Owner | Ensure access is authorized |
| New access provisioned | IAM / IT Support | Ensure only approved access is granted |
| Access validated | Manager / User | Confirm access aligns with the new role |

### Leaver

| Activity | Responsible Party | Control Objective |
|---|---|---|
| Employee exit identified | HR | Ensure termination events are communicated |
| Termination notification issued | HR | Trigger timely access revocation |
| Account disabled | IAM / IT Support | Prevent further authentication |
| Application access revoked | Application Owners / IAM | Remove access to business systems |
| Group and role memberships removed | IAM / IT Support | Remove inherited privileges |
| Sessions / credentials revoked | IAM / IT Support | Prevent continued access |
| Revocation validated | IAM / Application Owner | Confirm access has been removed |
| Evidence retained | IT / IAM | Demonstrate that access was revoked |

---

## Key Risks

### Joiner Risks

- Access granted without appropriate approval
- Excessive access assigned during onboarding
- Accounts created without business justification
- Weak authentication configuration

### Mover Risks

- Previous access not removed
- Privilege creep
- Conflicting roles or Segregation of Duties violations
- New access granted without appropriate approval

### Leaver Risks

- Delayed account disablement
- Former employees retaining application access
- Active sessions or credentials remaining valid
- Orphaned accounts

---

## Key Control Principles

The JML process should be designed around the following principles:

1. **Business Need** — access should support legitimate job responsibilities.
2. **Least Privilege** — users should receive only the access required.
3. **Authorization** — access should be approved before provisioning.
4. **Timeliness** — access changes should occur promptly.
5. **Segregation of Duties** — conflicting access should be identified and prevented.
6. **Accountability** — actions should be attributable to individual users.
7. **Evidence** — access decisions and changes should be traceable.
8. **Periodic Review** — access should be reviewed to confirm continued appropriateness.

---

## Example Scenario

### Employee Transfer

An employee moves from the **Customer Service Department** to the **IT Support Department**.

The IAM process should not simply add IT Support access to the employee's existing account.

Instead:

1. The role change is communicated by HR or the manager.
2. The employee's existing access is reviewed.
3. Customer Service access that is no longer required is identified.
4. New IT Support access is requested.
5. The required access is approved.
6. Approved IT Support access is provisioned.
7. Potential SoD conflicts are assessed.
8. Evidence of the access changes is retained.

This prevents **privilege creep**, where users accumulate access as they move between roles.

---

## Expected Evidence

Examples of evidence that may demonstrate effective JML controls include:

- HR onboarding records
- Access request forms
- Manager approvals
- Application Owner approvals
- IAM provisioning logs
- Account creation records
- Role/group membership records
- Access review records
- Termination notifications
- Account disablement logs
- Access revocation reports
- Audit logs

---

## Key Takeaway

A strong JML process ensures that:

**Access is appropriately granted → Access is appropriately modified → Access is appropriately removed.**

The objective is not simply to create and delete accounts, but to ensure that **identity and access remain aligned with a user's 
current business responsibilities throughout the entire employment lifecycle.**
