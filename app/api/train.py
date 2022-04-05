from sqlalchemy import desc
import datetime
import re

def get_dataframe_span( db: Session,table_name: str,    framesize: int, dt : datetime):
    df = select_forex_by_name(  db=db, table_name=table_name )
    q = db.query(df).distinct(df.id).where(df.id <= dt).order_by(desc(df.id)).limit(framesize).subquery('sub1')
    r = db.query(df).filter(df.id == q.c.id ).order_by(df.id).all()
    return r

#@app.get("/train1/")
def train1(db:Session = Depends(get_db)):            
    wsize = 96
    count = 20000
    
    m1_last = get_time_series(db=db,table_name = TableM1)
    m5_last = get_time_series(db=db,table_name = TableM5)
    m15_last = get_time_series(db=db,table_name =TableM15)
    
    dt = min([m1_last[-1],m5_last[-1],m15_last[-1]])
    start = m1_last.index(dt)
    
    if start<count:
        count=start
    
    for dt in tqdm(m1_last[start:start-count:-1]):
        #print(start,dt)
        df11 = get_dataframe_span(db=db, table_name=TableM1, framesize = wsize,  dt=dt)
        df22 = get_dataframe_span(db=db, table_name=TableM5, framesize = wsize,  dt=dt)
        df33 = get_dataframe_span(db=db, table_name=TableM15, framesize = wsize, dt=dt)
        
        img = imagemake( df11, df22, df33) 
        fname = "datasets/facades1/train/" +  dt.replace(":","_").replace(".","-") + ".png"
        img.save(fname)
        
#@app.get("/train2/")
def train2(db:Session = Depends(get_db)):
    
        cmd = 'python train.py --dataroot ./datasets/facades1 --name facades_pix2pix1 --model pix2pix --direction AtoB --batch_size 32 --gpu_ids 0,1 --no_flip --contine_train'

        subprocess.check_output(cmd, shell=True)
                
        return {"msg","pass1"}
    
train2(db=SessionLocal())