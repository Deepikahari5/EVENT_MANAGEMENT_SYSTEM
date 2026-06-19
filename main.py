from fastapi import FastAPI
from app.database.base import Base
from app.database.database import engine
from app.api.auth import router as auth_router
from app.api.categories import router as category_router
from app.api.events import router as event_router
from app.api.registrations import router as registration_router
from app.api.ticket import router as ticket_router
from app.api.attendance import router as attendance_router
from app.api.dashboard import router as dashboard_router
from app.api.reports import router as report_router
from app.exceptions.custom_exceptions import NotFoundException, BadRequestException, UnauthorizedException, ForbiddenException
from app.exceptions.handlers import not_found_exception_handler, bad_request_exception_handler, unauthorized_exception_handler, forbidden_exception_handler, validation_exception_handler, generic_exception_handler
from fastapi.exceptions import RequestValidationError

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Event Management API', version='1.0.0')

app.include_router(auth_router)
app.include_router(category_router)
app.include_router(event_router)
app.include_router(registration_router)
app.include_router(ticket_router)
app.include_router(attendance_router)
app.include_router(dashboard_router)
app.include_router(report_router)

app.add_exception_handler(NotFoundException, not_found_exception_handler)
app.add_exception_handler(BadRequestException, bad_request_exception_handler)
app.add_exception_handler(UnauthorizedException, unauthorized_exception_handler)
app.add_exception_handler(ForbiddenException, forbidden_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

@app.get('/')
def root():
    return {'message': 'Event Management API Running'}
