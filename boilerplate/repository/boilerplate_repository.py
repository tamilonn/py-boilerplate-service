from typing import List, Optional, Type
from sqlalchemy.orm import Session

from automapper import mapper
import logging

# initialize logger
logger = logging.getLogger(__file__)

class Repository:
    def __init__(self, session: Session):
        self.session = session


    def get_by_id(self, id: int) -> Type[object]:
        return self.session.query(object).filter_by(id=id).first()
    
    
    def get_all(self) -> List[Optional[object]]:
        objLst = self.session.query(object).all()
        return objLst
    

    def create(self, config: object) -> None: 
        self.session.add(object)
        self.session.commit()
        logger.info('create successful!!')


    def update(self, obj: object) -> None:
        self.session.commit()
        self.session.refresh(obj)
        logger.info('object update successful!!')


    def delete(self, obj: object) -> bool:
        self.session.delete(obj)
        self.session.commit()
        return True