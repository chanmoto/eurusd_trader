from PIL import Image
import matplotlib.pyplot as plt
from tqdm import tqdm
import pdb

def min_max(x, axis=None):
    min = x.min(axis=axis, keepdims=True)
    max = x.max(axis=axis, keepdims=True)
    result = (x-min)/(max-min)
    return result

def imagemake(dfspan1,dfspan2,dfspan3):
    a = min_max(np.array(dfspan1))
    d = min_max(np.array(dfspan2))
    g = min_max(np.array(dfspan3))
    
    m = np.outer(a,a).astype(np.float32)
    n = np.outer(d,d).astype(np.float32)
    o = np.outer(g,g).astype(np.float32)
    
    m1 = min_max(m[0:64,0:64])
    m2 = min_max(m[16:80,16:80])
    n1 = min_max(n[0:64,0:64])
    n2 = min_max(n[16:80,16:80])
    o1 = min_max(o[0:64,0:64])
    o2 = min_max(o[16:80,16:80])

    te1 = np.stack([m1,n1,o1])
    te2 = np.stack([m2,n2,o2])
    te3=np.concatenate([te2,te2], 2)#real = fake = te2で与える
    
    te4=np.kron(te3, np.ones((4,4)))
    tmp = torch.from_numpy(te4).clone()
    return  transforms.ToPILImage(mode='RGB')(tmp)   

def getprice(img,transform,info):

    fake = transform(Image.open(img['fakeB'])) 
    fake=fake.numpy()
  
    fake1x = fake[info,:,0]
    fake1y = fake[info,0,:]
    fake2=(fake1x+fake1y)/2   
    
    return min_max(fake2),img['date']

def GetSignal(item):
    
    y1 = np.mean(item[162:192])
    y2 = np.mean(item[192:222])
    return y2/y1


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
    