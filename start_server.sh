#!/bin/bash

echo "🚀 Starting WorkCRM..."
echo ""
echo "Login Credentials:"
echo "  Akshita - username: akshita, password: akshita123"
echo "  Rohit   - username: rohit, password: rohit123"
echo ""
echo "Server will start at: http://localhost:8000"
echo "Press Ctrl+C to stop the server"
echo ""

cd /home/claude/workcrm
python manage.py runserver 0.0.0.0:8000
