import datetime


from boilerplate.schemas import ErrorDetail



def isBlank(stringValue: str):
    if stringValue is None or not (stringValue and stringValue.strip()):
        return True
    else:
        return False
    
    
def isNotBlank(stringValue: str):
    return not isBlank(stringValue)

def today_utc():
    return datetime.datetime.now(datetime.timezone.utc) 

def today_utc_string():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S %p %Z")

def populate_error_details(e)-> list[ErrorDetail]:
        errors = []
        for errorMsg in e.args:
            errorDetail = ErrorDetail(reason=errorMsg)
            errors.append(errorDetail)

        if errors.count == 0:
            return None

        return errors





