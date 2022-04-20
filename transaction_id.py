import uuid

def get_transaction_id():
    return (uuid.uuid4().hex[:6])

