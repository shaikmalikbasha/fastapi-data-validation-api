from fastapi import APIRouter, Request

test_router = APIRouter(prefix="/test", tags=["TEST ROUTER"])


@test_router.get("/params")
async def test_func(req: Request):
    return dict(req.query_params) or None
