from src.views.http_types.http_response import HttpResponse
from .error_types.http_not_found import HttpNotFoundError
from .error_types.http_bad_request import HttpBadRequestError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpBadRequestError)):
        # Voce poderia armazenar um log com isso
        # Ou entao avisar alguem ...

        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": {
                    "title": error.name,
                    "detail": error.message
                }
            }
        )

    return HttpResponse(
        status_code=error.status_code,
        body={
            "errors": {
                "title": "Server Error",
                "detail": str(error)
            }
        }
    )
