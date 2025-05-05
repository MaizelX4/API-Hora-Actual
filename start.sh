#!/bin/bash
uvicorn hora_actual:app --host 0.0.0.0 --port $PORT --reload
