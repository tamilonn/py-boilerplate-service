
import os
import logging.config
from pathlib import Path

import yaml

import logging
from dotenv import load_dotenv, dotenv_values


def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO

    ):
    """Setup logging configuration

    """
    path_dir = Path(os.path.dirname(__file__))
    workdir_path = path_dir.parent.absolute()

    yaml_path = Path( str(workdir_path) + '/' + default_path)
    print('yaml file location is = ', yaml_path)

    if os.path.exists(yaml_path):
        print('Loading from yaml file for logger.')
        with open(yaml_path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        print('Unable to load yaml file.  Using default level for logger.')
        logging.basicConfig(level=default_level)

    print("Configured the logger successfully.")

# call definition
setup_logging()

'------------------------------------------------------------'

# initialize logger
logger = logging.getLogger(__file__)

def load_env_props():
    config_environment = os.environ.get('configEnvironment')
    logger.info('configEnvironment = %s ', config_environment)

    if (config_environment == None):
        logger.error('configEnvironment is missing or incorrect -{}', config_environment)
        raise Exception('configEnvironment is missing or incorrect')

    env_file = ''

    if config_environment.__eq__('dev'):
        env_file = ".env_dev"
    elif config_environment.__eq__('preprod'):
        env_file = ".env_preprod"
    elif config_environment.__eq__('prd'):
        env_file = ".env_prd"
    else:        
        raise Exception('configEnvironment is missing or incorrect')

    # dotenv_path = os.path.join(os.path.dirname(__file__), env_file)
    path_dir = Path(os.path.dirname(__file__))
    workdir_path = path_dir.parent.absolute()
    dotenv_path = Path(str(workdir_path) + '/' + env_file)   
    logger.info('.env file location is = %s', dotenv_path)

    # load .env properties into environment properties to use.
    success = load_dotenv(dotenv_path)
    logger.info('load_dotenv success = %s', success)


# call definition
load_env_props()

