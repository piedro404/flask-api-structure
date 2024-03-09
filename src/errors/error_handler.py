from src.views.http_types.http_response import HttpResponse

# Error Types
from .error_types.http_bad_request import HttpBadRequestError

'''
    Responsibility for validating HTTP request input
'''

def error_handler(error: Exception) -> HttpResponse: 
    
    if isinstance(error, HttpBadRequestError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "status":False,
                "errors": {
                    "title": error.name,
                    "details": error.message
                }
            }
        )
    
    return HttpResponse(
        status_code=500,
        body={
            "status":False,
            "errors": {
                "title": "Server Error",
                "details": str(error)
            }
        }
    )
