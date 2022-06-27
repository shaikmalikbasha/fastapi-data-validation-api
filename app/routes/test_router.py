import os
from datetime import datetime

import numpy as np
import pandas as pd
from app.config.db_config import engine
from fastapi import APIRouter, Request

test_router = APIRouter(prefix="/test", tags=["TEST ROUTER"])


@test_router.get("/params")
async def test_func(req: Request):
    return dict(req.query_params) or None


@test_router.get("/load-sample-data")
async def load_sample_data(records: int = 75):
    df = pd.read_csv(os.path.join(os.getcwd(), "app", "sample-data", "Movies.csv"))
    df = df.sample(records).head(records)
    df["MD_BATCH_ID"] = records
    df["MD_BATCH_INGESTION_DATE_TIME"] = datetime.now()
    df["MD_RECORD_NUMBER"] = np.arange(records)
    df.to_sql(
        name="MOVIES",
        con=engine,
        if_exists="replace",
        index=False,
        method=None,
    )
    return df.to_dict(orient="records")
