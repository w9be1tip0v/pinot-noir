# Base Image of Python 3.9
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /workspace

# Set the environment variable to avoid buffering
ENV PYTHONUNBUFFERED=1

# Set the environment variable to add the current directory to the python path
ENV PYTHONPATH "/workspace:$PYTHONPATH"

# Copy the current directory contents into the container at /app
COPY . ./

# Install the required libraries
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

# Expose the port the app runs on


# Run the command to start the application
CMD ["python", "src/main.py"]