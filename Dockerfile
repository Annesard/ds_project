# Use an official Python runtime as a parent image
FROM python
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy files required for the app to run
COPY templates /app/templates
COPY app.py /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
