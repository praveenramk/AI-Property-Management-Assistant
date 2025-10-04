#!/bin/bash

# This script is used to set up the development environment for the AI Property Management Assistant project.

# Navigate to the backend directory and install dependencies
cd backend
pip install -r requirements.txt

# Navigate to the frontend directory and install dependencies
cd ../frontend
npm install

# Start the backend server
cd ../backend
python src/main.py &

# Start the frontend development server
cd ../frontend
npm start &

# Wait for both servers to start
wait