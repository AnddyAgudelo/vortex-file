from fastapi import APIRouter, Request, Response

files_router: APIRouter = APIRouter(prefix="/files")


@files_router.get(
    path=""
)
async def upload_files(
        request: Request,
        response: Response,
):
    pass
