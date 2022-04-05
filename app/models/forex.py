class forex2_m5(Base):
    __tablename__= "forex2_m5"

    id   = Column(DateTime(timezone=True), primary_key=True, index=True,unique=True,)
    open    = Column(Float())
    high    = Column(Float())
    low     = Column(Float())
    close   = Column(Float())
    volume  = Column(Integer())

class forex2_m30(Base):
    __tablename__= "forex2_m30"

    id   = Column(DateTime(timezone=True), primary_key=True, index=True,unique=True,)
    open    = Column(Float())
    high    = Column(Float())
    low     = Column(Float())
    close   = Column(Float())
    volume  = Column(Integer())
    
class forex2_m240(Base):
    __tablename__= "forex2_m240"

    id   = Column(DateTime(timezone=True), primary_key=True, index=True,unique=True,)
    open    = Column(Float())
    high    = Column(Float())
    low     = Column(Float())
    close   = Column(Float())
    volume  = Column(Integer())