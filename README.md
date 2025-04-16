# my_portfolio_wesbsite

## Running the Project with Docker

To run this project using Docker, follow these steps:

### Prerequisites

- Ensure Docker and Docker Compose are installed on your system.
- Verify that the `requirements.txt` file includes all necessary dependencies.

### Build and Run Instructions

1. Build the Docker image:

   ```bash
   docker-compose build
   ```

2. Start the application:

   ```bash
   docker-compose up
   ```

3. Access the application in your web browser at `http://localhost:8501`.

### Configuration

- The application exposes port `8501` for the Streamlit server.
- Environment variables are set within the Docker Compose file to optimize Python behavior.

For further details, refer to the provided `Dockerfile` and `compose.yaml` files.