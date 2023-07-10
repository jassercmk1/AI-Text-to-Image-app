# Base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY packages.txt .

# Install dependencies
RUN pip install --no-cache-dir -r packages.txt

# Copy the project files
COPY app.py .

# Run the app
CMD ["streamlit", "run", "app.py"]
