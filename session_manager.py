pending_update={
    "key":None,
    "value":None
}

def set_pending(key,value):
    pending_update["key"]=key
    pending_update["value"]=value

def get_pending():
    return pending_update

def clear_pending():
    pending_update["key"]=None
    pending_update["value"]=None

    