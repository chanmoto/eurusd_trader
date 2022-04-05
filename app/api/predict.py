from sqlalchemy import desc
import re

def get_dataframe( db: Session,    table_name: str,    framesize: int,):

    try:
        dataframe = select_forex_by_name(  db=db, table_name=table_name,    )
        q = db.query(dataframe).distinct(dataframe.id).order_by(desc(dataframe.id)).limit(framesize).subquery('sub1')
        r = db.query(dataframe).filter(dataframe.id == q.c.id ).order_by(dataframe.id).all()
        return [float(result.close) for result in r]

    except:
        pass
    return

@app.get("/predict/")
async def predict(db:Session = Depends(get_db)):
             
    wsize = 96
    
    df11 = get_dataframe( db=db, table_name="forex_m1", framesize = wsize,  )  
    df22 = get_dataframe( db=db, table_name="forex_m5", framesize = wsize,  )  
    df33 = get_dataframe( db=db, table_name="forex_m15", framesize = wsize,  )  
    
    print(df11[-1],df22[-1],df33[-1])
    
    img = imagemake( df11, df22, df33)
    
    fn = get_last_time(db=db,table_name = "forex_m1")
        
    shutil.rmtree('datasets/facades2/test/')
    os.mkdir('datasets/facades2/test/')
    shutil.rmtree("results/facades_pix2pix2/test_latest/images")
    os.mkdir("results/facades_pix2pix2/test_latest/images")

    fname = "datasets/facades2/test/" + fn.replace(":","_").replace(".","-") + "sk.png"
          
    img.save(fname)
        
    return {"msg",fname}
        
@app.get("/predict1/")
async def predict1(db:Session = Depends(get_db)):
    
        cmd = 'python test.py --dataroot ./datasets/facades2 --name facades_pix2pix2 --model pix2pix --direction AtoB'

        subprocess.check_output(cmd, shell=True)
                
        return {"msg","pass1"}
    
@app.get("/predict2/")
async def predict2(db:Session = Depends(get_db)):
        path = os.getcwd()
        new_dir_path = "results/facades_pix2pix2/test_latest/images"
                
        img=[]
        image={}

        for imageName in os.listdir(new_dir_path):
            inputPath = os.path.join(path, new_dir_path,imageName)
            if "fake_B" in  imageName : image['fakeB']=inputPath
            if "real_A" in  imageName: image['realA']=inputPath
            if "real_B" in  imageName: image['realB']=inputPath
            if len(image)==3:
                ddd=re.findall(r"\d\d\d\d-\d\d-\d\d \d\d_\d\d_\d\d",inputPath)
        
            try:
                image['date']=ddd[0].replace("_",":")
                img.append(image)
                image={}
            except:
                pass
        
        signal = 0
        
        transform = transforms.PILToTensor()
        
        for item in img:
            v2,date = getprice(item,transform,0)   
            signal =GetSignal(v2)

        return signal


        from PIL import Image
import matplotlib.pyplot as plt
from tqdm import tqdm
from torchvision import transforms
import pdb

def min_max(x, axis=None):
    min = x.min(axis=axis, keepdims=True)
    max = x.max(axis=axis, keepdims=True)
    result = (x-min)/(max-min)
    return result

def imagemake(dfspan1,dfspan2,dfspan3):
    a = min_max(np.array([r.high for r in dfspan1]))
    d = min_max(np.array([r.high for r in dfspan2]))
    g = min_max(np.array([r.high for r in dfspan3]))
    b = min_max(np.array([r.low for r in dfspan1]))
    e = min_max(np.array([r.low for r in dfspan2]))
    h = min_max(np.array([r.low for r in dfspan3]))
    
    m = np.outer(a,b).astype(np.float32)
    n = np.outer(d,e).astype(np.float32)
    o = np.outer(g,h).astype(np.float32)
    
    m1 = min_max(m[0:64,0:64])
    m2 = min_max(m[16:80,16:80])
    n1 = min_max(n[0:64,0:64])
    n2 = min_max(n[16:80,16:80])
    o1 = min_max(o[0:64,0:64])
    o2 = min_max(o[16:80,16:80])

    te1 = np.stack([m1,n1,o1])
    te2 = np.stack([m2,n2,o2])
    te3= np.concatenate([te1,te2],2)#real <> fake 
    
    te4 = np.kron(te3, np.ones((4,4)))
    tmp = torch.from_numpy(te4).clone()

    return  transforms.ToPILImage(mode='RGB')(tmp)   

    