# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Install dependencies
WORKDIR /../dependencies

RUN pip install -r ../app/requierments.txt


WORKDIR /../app


# Run show_image_transition.py when the container launches
CMD ["python", "./app/mainNumpyIter.py"]
