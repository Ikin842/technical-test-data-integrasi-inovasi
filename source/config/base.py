from pydantic_settings import BaseSettings

class Config(BaseSettings):

    POSTGRE_NAME: str
    POSTGRE_HOST: str
    POSTGRE_PORT: int
    POSTGRE_USERNAME: str
    POSTGRE_PASSWORD: str
    POSTGRE_DATABASE: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Config()