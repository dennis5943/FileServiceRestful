from typing import Union
from fastapi import FastAPI, File, Form, UploadFile
import uvicorn
import aiofiles
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/upload-file")
async def create_file(file: UploadFile = File(None)):
    
    try:
        contents = await file.read()
        with open('./files/' + file.filename, 'wb') as f:
            f.write(contents)
    except Exception as e:
        return {"message": str(e)}
    finally:
        file.close()

    return {
        "file_size": len(contents),
        "fileb_content_type": file.content_type,
        "fileb_name": file.filename
    }

@app.post("/upload-files")
async def create_upload_files(files: List[UploadFile] = File(...)):
    for file in files:
        destination_file_path = "/app/files/"+file.filename #output file path
        async with aiofiles.open(destination_file_path, 'wb') as out_file:
            while content := await file.read(1024):  # async read file chunk
                await out_file.write(content)  # async write file chunk
    return {"Result": "OK", "filenames": [file.filename for file in files]}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=80)
    print("running")