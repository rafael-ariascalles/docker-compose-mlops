from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests

#We generate a new FastAPI app in the Prod environment
#https://fastapi.tiangolo.com/


#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
