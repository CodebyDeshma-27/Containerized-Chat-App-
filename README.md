# Chat App - Docker Setup Instructions

## Prerequisites
- Docker Desktop installed and running

## Build and Run

1. **Build the containers:**
   ```bash
   docker-compose build
   ```

2. **Start the application:**
   ```bash
   docker-compose up
   ```
   
   Or run in detached mode (background):
   ```bash
   docker-compose up -d
   ```

3. **Access the application:**
   - Frontend: http://localhost:8080
   - Backend API: http://localhost:5000

## Useful Commands

- **Stop the application:**
  ```bash
  docker-compose down
  ```

- **View logs:**
  ```bash
  docker-compose logs
  ```
  
  For specific service:
  ```bash
  docker-compose logs backend
  docker-compose logs frontend
  ```

- **Rebuild after code changes:**
  ```bash
  docker-compose up --build
  ```

- **View running containers:**
  ```bash
  docker ps
  ```

## Troubleshooting

- If ports are already in use, edit docker-compose.yml to change port mappings
- Make sure Docker Desktop is running before executing commands
- Use `docker-compose down -v` to remove volumes if needed
