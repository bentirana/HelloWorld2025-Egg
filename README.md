# REST API Wrapper for Purdue Menu's API

A FastAPI web service that provides easy access to Purdue University dining hall menu data.

**HelloWorld2025 Submission** - Team: Charles, Ben, Julius, and Gurpreet

## Overview

This project creates a REST API wrapper around Purdue University's Housing & Food Services (HFS) API, making it simple to fetch and display dining hall menu information. The service fetches real-time menu data from Purdue's official dining API and provides clean, easy-to-use endpoints for accessing this information.

## Features

- 🍽️ **Real-time Menu Data**: Fetches current menu information from Purdue's official dining API
- 🚀 **FastAPI Backend**: High-performance, modern Python web framework
- 📅 **Date-specific Queries**: Get menus for any specific date
- 🏢 **Multi-location Support**: Access menus from different dining halls
- 💾 **Data Persistence**: Automatically saves fetched data to JSON files
- ⚡ **Async Support**: Non-blocking API calls for better performance

## API Endpoints

### GET `/`
Returns menu data for Hillenbrand dining hall for September 21, 2025.

**Response**: JSON object containing menu data

### GET `/menus/{location}/{date}`
Fetches menu data for a specific dining location and date.

**Parameters**:
- `location` (string): Name of the dining hall (e.g., "Hillenbrand", "Wiley", "Ford")
- `date` (string): Date in YYYY-MM-DD format (e.g., "2025-09-21")

**Example**: `/menus/Hillenbrand/2025-09-21`

**Response**: JSON object containing menu data for the specified location and date

### Additional Endpoints
- `GET /items/{item_id}`: Example endpoint for item queries
- `PUT /items/{item_id}`: Example endpoint for item updates

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bentirana/HelloWorld2025-Egg.git
   cd HelloWorld2025-Egg
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the API Server

1. **Start the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   - Base URL: `http://localhost:8000`
   - Interactive API docs: `http://localhost:8000/docs`
   - Alternative docs: `http://localhost:8000/redoc`

### Running the Backend Test

To test the data fetching functionality independently:

```bash
python backend_test.py
```

This will fetch menu data and save it to `output.json`.

## Project Structure

```
HelloWorld2025-Egg/
├── main.py              # FastAPI application and route definitions
├── backend_test.py      # Data fetching logic and utility functions
├── requirements.txt     # Python dependencies
├── output.json         # Generated JSON file with fetched menu data
├── README.md           # Project documentation
└── __pycache__/        # Python bytecode cache
```

## Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Requests**: HTTP library for making API calls
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server for running the FastAPI application

## Data Source

This application fetches data from Purdue University's official Housing & Food Services API:
- Base URL: `https://api.hfs.purdue.edu/menus/v2/locations/`
- Format: `{base_url}/{location}/{date}`

## Error Handling

The API includes comprehensive error handling for:
- Network connectivity issues
- Invalid location names
- Invalid date formats
- API endpoint failures
- Data processing errors

All errors are returned as JSON objects with descriptive error messages.

## Contributing

This is a HelloWorld2025 submission project. For any questions or suggestions, please contact the team members: Charles, Ben, Julius, and Gurpreet.

## License

This project is created for educational purposes as part of HelloWorld2025.
