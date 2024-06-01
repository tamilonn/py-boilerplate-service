"""
ORM python model classes.
"""

from sqlalchemy import Column, Integer, String, DATETIME, BOOLEAN, LargeBinary
from boilerplate.database import Base

# createConfigTable.  Config table definition. Jwt config is stored in this table
class Config(Base):
    __tablename__ = 'config'

    config_id = Column("config_id", Integer, primary_key=True)
    action = Column("action", String(20))
    created_date = Column("created_date", DATETIME)
    updated_date = Column("updated_date", DATETIME)
    organization = Column("organization", String(100))
    application = Column("application", String(100))
    token_expiration_time = Column("token_expiration_time", Integer)
    signkey_rotate_time = Column("signkey_rotate_time", Integer)
    kill_jwt = Column("kill_jwt", BOOLEAN)
    comments = Column("comments", String(200))
    algorithm = Column("algorithm", String(20))
    internal = Column("internal", BOOLEAN)
    authId = Column("authId", Integer)
    authSecret = Column("authSecret", String(50))
    identity = Column("identity", String(20))
    curr_rsa_key = Column("curr_rsa_key", LargeBinary)
    curr_rsa_secret = Column("curr_rsa_secret", LargeBinary)
    curr_rsa_keyid = Column("curr_rsa_keyid", String(50))
    prev_rsa_key = Column("prev_rsa_key", LargeBinary)
    prev_rsa_secret = Column("prev_rsa_secret", LargeBinary)
    prev_rsa_keyid = Column("prev_rsa_keyid", String(50))
    signkey_rotate_date = Column("signkey_rotate_date", DATETIME)
    signkey_last_rotated_date = Column("signkey_last_rotated_date", DATETIME)


    def __init__(self, 
                    config_id,
                    action,
                    created_date,
                    updated_date,
                    organization,
                    application,
                    token_expiration_time,
                    signkey_rotate_time,
                    kill_jwt,
                    comments,
                    algorithm,
                    internal,
                    authId,
                    authSecret,
                    identity,
                    curr_rsa_key,
                    curr_rsa_secret,
                    curr_rsa_keyid,
                    prev_rsa_key,
                    prev_rsa_secret,
                    prev_rsa_keyid,
                    signkey_rotate_date,
                    signkey_last_rotated_date):

        self.config_id = config_id
        self.action = action
        self.created_date = created_date
        self.updated_date = updated_date
        self.organization = organization


        self.application = application
        self.token_expiration_time = token_expiration_time
        self.signkey_rotate_time = signkey_rotate_time
        self.kill_jwt = kill_jwt
        self.comments = comments


        self.algorithm = algorithm
        self.internal = internal
        self.authId = authId
        self.authSecret = authSecret
        self.identity = identity


        self.curr_rsa_key = curr_rsa_key
        self.curr_rsa_secret = curr_rsa_secret
        self.curr_rsa_keyid = curr_rsa_keyid
        self.prev_rsa_key = prev_rsa_key
        self.prev_rsa_secret = prev_rsa_secret

        self.prev_rsa_keyid = prev_rsa_keyid
        self.signkey_rotate_date = signkey_rotate_date
        self.signkey_last_rotated_date = signkey_last_rotated_date
    ############# End of Config table definition.

