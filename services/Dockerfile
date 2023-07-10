# Use an official Python runtime as the base image
FROM python:3.9

# Copy the application files to the working directory
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
CMD ["python", "price_updater.py"]
