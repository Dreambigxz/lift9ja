import uuid

def deposit_id():
    return (uuid.uuid4().hex[:6])

