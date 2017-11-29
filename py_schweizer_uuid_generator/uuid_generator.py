import uuid


class UuidGenerator:
    def __init__(self):
        pass

    def __generate_uuid__(self):
        self.uuid = str(uuid.uuid3(uuid.NAMESPACE_DNS, '123')).replace('-', '')


print uuid
