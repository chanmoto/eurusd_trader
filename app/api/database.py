import os
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, DateTime, ForeignKey, String, Text,Float,Integer
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.types import JSON
from sqlalchemy import desc
from sqlalchemy.schema import CreateSchema
from sqlalchemy import MetaData

import subprocess
import os
import shutil


engine = create_engine(
    DBConfigurations.sql_alchemy_database_url,
    encoding="utf-8",
    pool_recycle=3600,
    echo=False,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# 作成したスキーマを参照するよう変更
Base = declarative_base()
Base.metadata = MetaData(bind=engine, schema='version2')

# スキーマを作成する
db = SessionLocal()
conn = engine.connect()
scheme = 'version2'
if not conn.dialect.has_schema(conn, scheme):
        engine.execute(CreateSchema(scheme))

Base.metadata.create_all(engine, checkfirst=True)
print (engine.table_names(schema=scheme))


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()

@contextmanager
def get_context_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()


import os
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    DBConfigurations.sql_alchemy_database_url,
    encoding="utf-8",
    pool_recycle=3600,
    echo=False,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()

@contextmanager
def get_context_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()
