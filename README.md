Steps to Build and Deploy Python Flask App on EC2 Using Docker
1. Create a Python Flask Static Website
We created a basic static website using Flask (Python web framework).

2. Create Dockerfile
The Dockerfile was written to build an image for the app. Here's the content of the Dockerfile:

Dockerfile
Copy
Edit
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
3. Build Docker Image Locally
Run the following command to build the Docker image locally (on your machine):

bash
Copy
Edit
docker build -t myj .
4. Run the Docker Container Locally
To run the Flask app locally in a container and expose it on port 5000:

bash
Copy
Edit
docker run -d -p 5000:5000 myj
5. Launch EC2 Instance (Ubuntu AMI, Free Tier)
In the AWS console, we created an EC2 instance with the Ubuntu AMI (Free Tier eligible).

We configured the Security Group:

SSH (22) for remote access

HTTP (80) for web traffic

Custom TCP (5000) for Docker container access on port 5000

6. Connect to EC2 Instance via SSH
We connected to the EC2 instance using the following SSH command (replace with your own PEM key and public IP):

bash
Copy
Edit
ssh -i path/to/your-key.pem ubuntu@<EC2-public-ip>
7. Install Docker on EC2
Once connected to EC2, we installed Docker:

bash
Copy
Edit
sudo apt-get update
sudo apt-get install -y docker.io
8. Clone the Project from GitHub
Next, we cloned the Flask project from GitHub onto the EC2 instance:

bash
Copy
Edit
git clone https://github.com/mhasvekarsanika/python-flask.git
cd python-flask
9. Build Docker Image on EC2
Now, we built the Docker image for the Flask app on EC2:

bash
Copy
Edit
docker build -t myj .
10. Run the Flask App in Docker on EC2
We ran the Docker container in the background and exposed port 5000:

bash
Copy
Edit
docker run -d -p 5000:5000 myj
11. Access the App Publicly
Since we exposed port 5000 and set up the security group to allow TCP 5000, the Flask app was now accessible via the EC2 public IP:

cpp
Copy
Edit
http://<your-ec2-public-ip>:5000
Summary:
Flask app → Dockerfile → Build Docker Image → Run Container → EC2 → Expose app to the public internet

Commands:

Docker commands for building and running the container

EC2 SSH commands for connecting and installing Docker

Git clone for pulling the app into EC2
