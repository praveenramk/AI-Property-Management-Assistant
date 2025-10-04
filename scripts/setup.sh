#!/bin/bash

# This script sets up the AI Property Management Assistant project environment.

# Update package list and install necessary packages
sudo apt-get update
sudo apt-get install -y python3 python3-pip nodejs npm

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install backend dependencies
pip install -r backend/requirements.txt

# Install frontend dependencies
cd frontend
npm install

# Return to the root directory
cd ..

# Print completion message
echo "Setup completed successfully!"