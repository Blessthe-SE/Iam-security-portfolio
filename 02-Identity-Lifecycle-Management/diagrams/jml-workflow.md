
# Joiner-Mover-Leaver (JML) Workflow

The JML workflow illustrates the key stages involved in managing user access throughout the employee lifecycle.

JOINER → Request → Approval → Provision → MOVER → Review/Update → LEAVER → Revoke

```mermaid
flowchart LR
    A[JOINER] --> B[Access Request]
    B --> C[Approval]
    C --> D[Access Provisioned]
    
    D --> E[MOVER]
    E --> F[Access Reviewed & Updated]
    
    F --> G[LEAVER]
    G --> H[Access Revoked]

Key Control Points
Access should be requested based on business need.
Access should be approved before provisioning.
Existing access should be reviewed when an employee changes roles.
Access that is no longer required should be removed.
User access should be revoked when employment ends.
