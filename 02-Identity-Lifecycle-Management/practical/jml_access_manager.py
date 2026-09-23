import csv

# Load employee data
with open("employees.csv", newline="") as employee_file:
    employees = list(csv.DictReader(employee_file))

# Load role-based access rules
with open("access_rules.csv", newline="") as rules_file:
    access_rules = list(csv.DictReader(rules_file))


def get_role_access(role):
    """Return the approved access for a given role."""
    return [
        rule for rule in access_rules
        if rule["role"].lower() == role.lower()
    ]


print("IAM JOINER-MOVER-LEAVER ACCESS SIMULATOR")
print("=" * 50)

for employee in employees:
    employee_id = employee["employee_id"]
    role = employee["role"]
    event = employee["jml_event"]

    print(f"\nEmployee: {employee_id}")
    print(f"Role: {role}")
    print(f"JML Event: {event}")

    if event == "Joiner":
        print("Action: Provision approved role-based access")

        access = get_role_access(role)

        for item in access:
            print(
                f"  - {item['system']} "
                f"({item['access_level']})"
            )

    elif event == "Mover":
        print("Action: Review existing access and update according to new role")

        access = get_role_access(role)

        for item in access:
            print(
                f"  - Expected: {item['system']} "
                f"({item['access_level']})"
            )

    elif event == "Leaver":
        print("Action: Revoke user access and disable account")

    else:
        print("Action: Unknown JML event - investigate")
