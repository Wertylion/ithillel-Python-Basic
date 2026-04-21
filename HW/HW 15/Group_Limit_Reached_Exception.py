class GroupLimitReachedException(Exception):
    def __init__(self, message, group_number):
        self.message = message
        self.group_number = group_number
