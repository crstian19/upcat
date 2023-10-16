import os
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import File
from fastapi import UploadFile
from fastapi import Depends
from fastapi import Header

app = FastAPI()

# Set the file storage backend to the local file system
UPLOAD_FOLDER = './config'

# Create the file storage folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.post("/files/")
def create_file(file: UploadFile = File(...)):
    # Save the uploaded file to the local file system
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    # Return the file's URL
    return {"url": f"http://localhost:8000/files/{file.filename}"}

@app.delete("/files/{filename}")
def delete_file(filename: str):
    # Delete the file from the local file system
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return {"message": "File deleted"}
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/files/{filename}")
def read_file(filename: str):
    # Serve the file from the local file system
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        return {"file_content": open(file_path, "rb").read()}
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/files/")
def list_files():
    # Get a list of all files in the storage folder
    files = os.listdir(UPLOAD_FOLDER)
    # Return the list of files
    return {"files": files}

@app.put("/files/{filename}")
def rename_file(filename: str, new_filename: str):
    # Rename the file in the local file system
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    new_file_path = os.path.join(UPLOAD_FOLDER, new_filename)
    if os.path.exists(file_path):
        os.rename(file_path, new_file_path)
        return {"message": "File renamed"}
    else:
        raise HTTPException(status_code=404, detail="File not found")

