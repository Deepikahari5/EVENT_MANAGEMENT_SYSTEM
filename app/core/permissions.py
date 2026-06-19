from app.core.role_checker import RoleChecker

admin_only = RoleChecker(["Admin"])
organizer_only = RoleChecker(["Organizer"])
participant_only = RoleChecker(["Participant"])
admin_or_organizer = RoleChecker(["Admin", "Organizer"])