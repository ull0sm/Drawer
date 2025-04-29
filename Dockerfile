FROM python:3

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code (scripts) into the container
COPY src/ /app/src/

# Copy the automation script into the container
COPY automation/auto_run.py /app/automation/auto_run.py

# Copy the data directory into the container
COPY data/ /app/data/

# Set the default command to execute the automation script
CMD ["python", "automation/auto_run.py"]