import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "https://www.virustotal.com/vtapi/v2/file/scan"

def scan_file(file):
    
    params = {
        "apikey": API_KEY,  
    }
    files = {"file": (file.filename, file.file, file.content_type)}
    
    try:
        response = requests.post(URL, params=params, files=files)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    

def report_analysis_result(scan_id):
    
    params = {
        "apikey": API_KEY,
        "resource": scan_id,
    }
    url = "https://www.virustotal.com/vtapi/v2/file/report"
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}