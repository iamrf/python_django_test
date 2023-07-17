# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./services /app

# Install the required dependencies
RUN pip install redis

# Command to run the script
CMD ["python", "price_updater.py"]
