from service.postgres_service import PostgresService
from config.base import settings

postgres_svc = PostgresService(**settings.dict())