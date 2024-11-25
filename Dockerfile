# Use an official Python runtime as a parent image
FROM python:3.9

ENV OPENAI_API_KEY=${OPENAI_API_KEY}

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt

RUN pip install --upgrade pip
RUN pip install  -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Expose the port streamlit runs on
EXPOSE 8501



# Run app.py when the container launches
CMD ["streamlit", "run", "Chatbot.py", "--server.port", "8501"]
