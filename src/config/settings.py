
# from enum import Enum
# from functools import lru_cache
# from typing import Any, List

# import yaml
# from pydantic import BaseSettings, Field, PostgresDsn
# from pydantic.networks import HttpUrl

import logging
from typing import ClassVar
import os

#initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)

'This class is used to obtain the environment name such as "dev, preprod, prod" from system variable '
'Usage ConfigEnvironment.environment will provide environment name value from all modules and packages'
class ConfigEnvironment(object):
    environment: ClassVar[str]='local'

    #Make a singleton object creation
    def __new__(cls):
        'This is a singleton class'

        logger.info('ConfigEnvironment: __new__()...')
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConfigEnvironment, cls).__new__(cls)

        return cls.instance
    

    def __init__(self):
        
        env = os.environ.get('configEnvironment')
        logger.info('configEnvironment =%s ',env)

        if env.__eq__('dev'):
            ConfigEnvironment.environment = 'dev'
        elif env.__eq__('preprod'):
            ConfigEnvironment.environment = 'preprod'
        elif env.__eq__('prd'):
            ConfigEnvironment.environment = 'prd'
        else:
            logger.error('configEnvironment is missing or incorrect -{}', env)
            raise Exception('configEnvironment is missing or incorrect')


# if __name__ == '__main__':
#      obj = ConfigEnvironment()

#      logger.info('obj env= %s', obj.environment)
#      logger.info('class env= %s', ConfigEnvironment.environment)




# class LogLevels(str, Enum):
#     """Enum of permitted log levels."""

#     debug = "debug"
#     info = "info"
#     warning = "warning"
#     error = "error"
#     critical = "critical"


# class UvicornSettings(BaseSettings):
#     """Settings for uvicorn server"""

#     host: str
#     port: int = Field(ge=0, le=65535)
#     log_level: LogLevels
#     reload: bool


# class ApiConfigSettings(BaseSettings):
#     """Settings for FastAPI Server"""

#     title: str = ""
#     description: str = ""
#     version: str
#     docs_url: str


# class DatabaseConnectionSettings(BaseSettings):
#     """Settings for database connection"""

#     postgres_user: str
#     postgres_password: str
#     postgres_database: str
#     postgres_server: str

#     @property
#     def postgres_uri(self) -> str:
#         return PostgresDsn.build(
#             scheme="postgresql",
#             user=self.postgres_user,
#             password=self.postgres_password,
#             host=self.postgres_server,
#             path=f"/{self.postgres_database}",
#         )


# class NewsServerSettings(BaseSettings):
#     url: HttpUrl
#     article_header_tags: List[str]


# class NewsConfigSettings(BaseSettings):
#     """Settings for Article News Server"""

#     bbc: NewsServerSettings
#     idnes: NewsServerSettings
#     ihned: NewsServerSettings


# class Settings(BaseSettings):
#     uvicorn: UvicornSettings
#     db_connection: DatabaseConnectionSettings
#     news_config: NewsConfigSettings
#     api_config: ApiConfigSettings


# def load_from_yaml() -> Any:
#     # uncomment the following line for running the article scraping from src.tasks.scraper
#     # with open("../../appsettings.yaml") as fp:
#     with open("appsettings.yaml") as fp:
#         config = yaml.safe_load(fp)
#     return config


# @lru_cache()
# def get_settings() -> Settings:
#     yaml_config = load_from_yaml()
#     settings = Settings(**yaml_config)
#     return settings
