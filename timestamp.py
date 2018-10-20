from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read():
    TIMESTAMP = {
        "timestamp": get_timestamp()
    }
    
    return TIMESTAMP
