# GPT-Clone

## Overview
GPT-Clone is a Streamlit-based web application that provides a user-friendly interface for interacting with OpenAI's GPT models. This project demonstrates how to create a chatbot application, containerize it using Docker, and deploy it to AWS ECS using GitHub Actions for continuous integration and continuous deployment (CI/CD).

## Features
- Streamlit-based web interface
- Integration with OpenAI's GPT models
- Dockerized application
- Automated CI/CD pipeline with GitHub Actions
- AWS ECS deployment

## Prerequisites
- Python 3.9+
- OpenAI API Key
- AWS Account (for deployment)
- Docker (for local development and containerization)

## Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/GPT-Clone.git
cd GPT-Clone
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root with your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
MAX_HISTORY_LENGTH=5
```

### 5. Run the Application
```bash
streamlit run Chatbot.py
```

## Docker Setup

### Build the Docker Image
```bash
docker build --build-arg OPENAI_API_KEY=your_api_key -t gpt-clone .
```

### Run the Docker Container
```bash
docker run -p 8501:8501 gpt-clone
```

## CI/CD Workflow
The project uses GitHub Actions for automated deployment to AWS ECS. The workflow located in `.github/workflows/aws-workflow.yml` handles:
- Code checkout
- AWS credentials configuration
- Docker image build
- Pushing image to Amazon ECR
- Deploying to Amazon ECS

### Workflow Triggers
- Automatic deployment on push to the `main` branch

## AWS Configuration
The project requires the following AWS resources:
- ECR Repository: `chatbot-app`
- ECS Cluster: `devcluster`
- ECS Service: `chatbot-app-service1`
- IAM Roles with appropriate permissions

## Environment Secrets
Configure the following secrets in your GitHub repository settings:
- `AWS_ACCESS_KEY`: AWS access key with ECS deployment permissions
- `AWS_SECRET_ACCESS_KEY`: Corresponding AWS secret access key
- `OPENAI_API_KEY`: Your OpenAI API key

## File Structure
- `Chatbot.py`: Main Streamlit application
- `Dockerfile`: Docker configuration
- `requirements.txt`: Python dependencies
- `.github/workflows/aws-workflow.yml`: GitHub Actions workflow
- `chatbot-app-task-difinition.json`: ECS task definition

## Security Considerations
- Never commit sensitive information like API keys to version control
- Use environment variables and GitHub secrets
- Rotate API keys and credentials regularly

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


## Contact
[ Linkedin](https://www.linkedin.com/in/rehabreda8/) 
