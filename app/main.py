from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from app.resources import scan_file, report_analysis_result

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "It's Run. Container that creates a REST API and uses FastAPI which allows users to upload files and scan them for malware using the VirusTotal API."}

@app.post("/scan-file")
async def scan_for_virus(file: UploadFile = File(...)):
    try:
        scan_result = scan_file(file)
        return JSONResponse(content={
            "filename": file.filename,
            "scan_id": scan_result.get("scan_id"),
            "permalink": scan_result.get("permalink"),
            "report_result": report_analysis_result(scan_result.get("scan_id"))
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


