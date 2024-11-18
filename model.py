from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Text, Numeric

Base = declarative_base()


class SearchData(Base):
    __tablename__ = "SearchData"
    id = Column(Integer, primary_key=True, index=True)
    cadastral_number = Column(String(20), index=True)
    date = Column(Date, index=True)
    normative_act = Column(Text, index=True)
    cadastral_value = Column(Numeric, index=True)
    note = Column(Text, index=True)
