from rolepermissions.roles import AbstractUserRole

class HeadAdmissionService(AbstractUserRole):
    available_permissions = {
        'enter_admission_process': True,
        'delete_registration':True,
    }

class AssistantAdmissionService(AbstractUserRole):
    available_permissions = {
        'Enter_registrations': True,
    }

