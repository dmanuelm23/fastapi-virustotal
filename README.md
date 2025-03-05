# fastapi-virustotal

## Description 
Container that creates a REST API and uses FastAPI which allows users to upload files and scan them for malware using the VirusTotal API.

## Technical Requirements

### Core Functionality
API endpoint:
- Accepts file uploads via POST request
- Submits the file to VirusTotal's scanning service
- Returns the scan results in a structured format

### Framework & Platform
- FastAPI is used for API implementation
- The application runs Docker containers

### VirusTotal API Reference
Endpoint for file scanning:
```
https://www.virustotal.com/vtapi/v2/file/scan
```

Parameters:
- apikey: Your VirusTotal API key
- file: The file to be scanned

Example curl request:
```bash
curl --request POST \
  --url 'https://www.virustotal.com/vtapi/v2/file/scan' \
  --form 'apikey=<apikey>' \
  --form 'file=@/path/to/file'
```
### Docker configuration

- Copy .env.example file and rename by .env
- Edit the .env file and add the token provided by total virus
  - Register for a free VirusTotal API key at https://www.virustotal.com/
  - ``` API_KEY=<token-virus-total> ```
  

   
#### Create the container image

```bash
docker build -t <image_name> .
```
#### Run the image

```bash
 docker run -d -p 8000:8000 -v $(pwd):/app --name <container-name> <image-name>
```

#### Verify that the container is running

```bash
 docker ps
 docker ps -a
```

### Run with CURL from the container 
```bash
docker exec -it <container-name> curl -X POST -F "file=@app/files/<filename>" http://localhost:8000/scan-file
```
### You can run the scan of any file on your computer using CURL or Postman or any program to run API's because port 8000 is open on your local network.
```bash
curl -X POST -F "file=@/<route>/<your>/<file>" http://localhost:8000/scan-file
```









