FROM ubuntu

# Update package lists and install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    && pip3 install --upgrade pip \
    && pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create directory for the dataset
RUN mkdir -p /home/doc-bd-a1/

# Copy the dataset into the container
COPY train_titanic.csv /home/doc-bd-a1/

# Set the working directory
WORKDIR /home/doc-bd-a1/

# Specify the command to run when the container starts
CMD ["/bin/bash"]
