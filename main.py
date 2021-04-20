# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:57:36 2021

@author: Stanisław Krześniak
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/method")
def root():
    return {"method": "GET"}