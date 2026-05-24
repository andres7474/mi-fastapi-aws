import boto3
from fastapi import FastAPI, UploadFile, File, HTTPException
from database import create_table, insert_image, get_image

app = FastAPI(title="FastAPI S3 + RDS")

# ───────────── S3 ─────────────
BUCKET = "user-1014980791-ueia-so"
REGION = "us-east-1"

s3 = boto3.client("s3", region_name=REGION)

ALLOWED_TYPES = {"image/png", "image/jpeg", "image/jpg"}

# ───────────── STARTUP ─────────────
@app.on_event("startup")
def startup():
    create_table()

# ───────────── UPLOAD ─────────────
@app.post("/upload")
async def upload_image(usuario: str, file: UploadFile = File(...)):

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=415,
            detail="Solo PNG o JPG permitidos"
        )

    contents = await file.read()
    s3_key = f"{usuario}/{file.filename}"

    s3.put_object(
        Bucket=BUCKET,
        Key=s3_key,
        Body=contents,
        ContentType=file.content_type
    )

    record_id, fecha = insert_image(usuario, s3_key)

    return {
        "mensaje": "Imagen subida correctamente",
        "id": record_id,
        "usuario": usuario,
        "s3_key": s3_key,
        "fecha": str(fecha)
    }

# ───────────── GET IMAGE ─────────────
@app.get("/image")
def get_image_url(usuario: str, nombre_imagen: str):

    row = get_image(usuario, nombre_imagen)

    if not row:
        raise HTTPException(status_code=404, detail="No encontrada")

    _, _, s3_key, fecha = row

    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": BUCKET, "Key": s3_key},
        ExpiresIn=3600
    )

    return {
        "usuario": usuario,
        "url": url,
        "fecha": str(fecha)
    }