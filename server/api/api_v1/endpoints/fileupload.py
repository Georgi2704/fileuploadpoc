from fastapi.routing import APIRouter
from starlette.responses import Response
from fastapi import FastAPI, File, UploadFile
import shutil
import structlog

logger = structlog.get_logger(__name__)

router = APIRouter()


def name_file(column_name, record_name, image_name=""):
    _, _, image_number = column_name.rpartition("_")[0:3]
    current_name = image_name
    extension = "png"  # todo: make it dynamic e.g. get it from mime-type, extra arg for this function?
    if not current_name:
        name = "".join([c if c.isalnum() else "-" for c in record_name])
        name = f"{name}-{image_number}-1".lower()
    else:
        name, _ = current_name.split(".")
        name, _, counter = name.rpartition("-")[0:3]
        name = f"{name}-{int(counter) + 1}".lower()
    name = f"{name}.{extension}"
    logger.info("Named file", col_name=column_name, name_in=image_name, name_out=name)
    return name


@router.get("/")
def get_hello(response: Response) -> str:
    return "Hello Formatics!"


# stores in memory
@router.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

# better for images
@router.post("/uploadfile/")
async def create_upload_file(image: UploadFile = File(...)):

    with open("destination.png", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": image.filename}
