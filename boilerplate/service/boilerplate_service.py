import logging
from boilerplate.repository.boilerplate_repository import Repository
from boilerplate.schemas import ServiceResponse, ErrorResponse, ServiceResponse
from boilerplate.database import get_session
from boilerplate.util import helper as helper
from datetime import datetime
from boilerplate.exceptions import BoilerplateValidationError


# initialize logger
logger = logging.getLogger(__file__)

def get(id: int)-> ServiceResponse:
    tstart = datetime.now()
    logger.info('request= %s', id)

    try:
        if id <= 0:
            raise BoilerplateValidationError('id is invalid') 

        session = next(get_session())
        repository = Repository(session)
        result = repository.get_by_id(id=id)

        service_response = ServiceResponse(success=True, apiversion='', data=result, error=None)

        tend = datetime.now()
        timedelta = tend - tstart
        logger.info('Total time taken in milliseconds = %s', timedelta.total_seconds() * 1000)
        return service_response
  
    except BoilerplateValidationError as e:
        logger.error('BoilerplateValidationError raised. Cause = %s', e)
        errorDetails = helper.populate_error_details(e)
        error= ErrorResponse(code=400, message='Get [operation] failed. Validation Errors found.' , errors=errorDetails)
        service_response= ServiceResponse(success=False, apiversion='', data=None, error=error)
        return service_response  
    except Exception as ex:
        logger.error('An error is raised. Cause = %s', exc_info=True)
        errorDetails = helper.populate_error_details(ex)
        error= ErrorResponse(code=400, message='Get [operation] failed. Errors found' , errors=errorDetails)
        service_response= ServiceResponse(success=False, apiversion='', data=None, error=error)
        return service_response  