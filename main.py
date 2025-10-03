from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image
import io
from app import image_detector

app = FastAPI()

# Serve static files (optional, e.g., CSS/JS/images)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def main_page():
    # Simple HTML form
    content = """
    <html>
        <head>
            <title>Image Upload</title>
        </head>
        <body>
            <h2>Upload an Image</h2>
            <form action="/upload-image/" enctype="multipart/form-data" method="post">
                <input name="file" type="file" accept="image/*">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=content)


@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Read the image bytes
        image_bytes = await file.read()

        # Load with PIL
        image = Image.open(io.BytesIO(image_bytes))

        output,output_path = image_detector(image)

    
        # Example output
        result = {
            "filename": file.filename,
            "content_type": file.content_type,
            "format": image.format,
            "size": image.size  # (width, height)
        }
        # {"person": {"OBJECT TYPE": 0.0, "Coordinates": [102.14622497558594, 187.94418334960938, 720.0, 1427.615966796875], "PROABABLITY": 0.9673630595207214}}
        # Show results in HTML
        detection_html = "".join(
            [f"<li><b>{lbl}</b>: {det}</li>" for lbl, det in output.items()]
        )

        return HTMLResponse(f"""
        <html>
            <body>
                <h2>Upload Successful</h2>
                <p><b>Filename:</b> {file.filename}</p>
                <p><b>Detected objects:</b></p>
                <ul>{detection_html}</ul>
                <br>
                <img src="/{output_path}" alt="Processed Image" style="max-width:600px;">
                <br><br>
                <a href="/">Go Back</a>
            </body>
        </html>
        """)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)


##uv