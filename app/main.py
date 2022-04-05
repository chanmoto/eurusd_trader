import nest_asyncio
import uvicorn
from fastapi import Body, FastAPI
from sqlalchemy_utils import get_class_by_table
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from sqlalchemy.sql import func

#Binary trader
#Trainデータの作成
#解析期間　WSIZE　96日　-->　a(n=32)+b(n=32)+c(n=32)　　TRAIN時に　Aはa,b、Bはb,cを使う　　
#テンソル　０：終値　１：高値－終値　２：終値－安値
#正規化　MAX-MIN　（A,B別々に正規化）　

#5分足、３０分足、４時間足　バージョン
#df1 = EURUSD.oj5k5.csv'
#df2 = EURUSD.oj5k30.csv'
#df3 = EURUSD.oj5k240.csv'
#HIGH　×　LOW　外積バージョン

app = FastAPI()   

@app.on_event("startup")
async def startup_event():
    print("*** startup event ***")
    
if __name__ == "__main__":
    try:
        b = start()
    except:
        x('Failed Start')
        quit()
    
    nest_asyncio.apply()
    uvicorn.run(app, port=80)