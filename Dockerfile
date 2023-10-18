# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variables
ENV APP_ENV=production

# Run app.py when the container launches
CMD ["uvicorn", "API.main:app", "--host", "0.0.0.0", "--port", "80"]