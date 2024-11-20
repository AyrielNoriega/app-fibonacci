from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from core.database import Base

class FibonacciSeries(Base):
    __tablename__ = 'fibonacci_series'

    id = Column(Integer, primary_key=True, autoincrement=True)
    time_str = Column(String, index=True)
    series = Column(String)

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
