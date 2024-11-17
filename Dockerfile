# Use a lightweight Python image
FROM python:3.8-slim

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY discordbot.py .

# Make output unbuffered for better logging
ENV PYTHONUNBUFFERED=1

# Command to run the bot
CMD ["python", "discordbot.py"]
