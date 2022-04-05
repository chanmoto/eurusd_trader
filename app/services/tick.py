from typing import Dict, List, Optional

def select_forex_by_name(db: Session,table_name:str):
    return get_class_by_table(Base,Base.metadata.tables.get(table_name))

def get_last_time(db: Session,table_name:str):
    try:
        model = select_forex_by_name( db=db, table_name=table_name, )
        q = db.query( func.max(model.id).label('id_max')).subquery('sub1')
        r = db.query(model).filter(model.id == q.c.id_max ).all()
        return str(r[0].id).replace("-",".")
    except:
        pass
    return
    
@app.get("/getlasttime/")
async def gettime(db:Session = Depends(get_db),):    
    return {"m1":get_last_time(db=db,table_name = "forex_m1"),
            "m5":get_last_time(db=db,table_name = "forex_m5"),
            "m15":get_last_time(db=db,table_name = "forex_m15")
           }
           
def add_forex(    db: Session,    table_name: str,    time: Optional[str] = None,    value: Optional[str] = None,    commit: bool = True,):

    dataframe = select_forex_by_name(        db=db,        table_name=table_name,    )
    
    data = dataframe(id=time,close=value,)
    db.add(data)
    if commit:
        db.commit()
        db.refresh(data)
    return data

@app.post("/gettick/")
async def gettick(db:Session = Depends(get_db),body=Body(...)):
       
        time,peristr,value = body["content"].split(",")       

        r = add_forex(
        db=db,
        table_name=peristr,
        time = time,
        value = value,
        commit=True,
    )    
        return {"msg":peristr}
    
