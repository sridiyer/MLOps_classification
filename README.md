# MLOps_classification

This project trained a NLP model for detecting (positive or negative) sentiments expressed in sentences.
The main components of the projects are:

<ul>
  <li>Pre-trained Transformer model finetuned for sentiment analysis using the IMDB dataset. </li>
  <li>FastAPI based access to the model for real-time inference. </li>
  <li>Dockerized deployment - public access to docker image via AWS Container Registery</li>
  <li>Delpyment via Cloud Service (update </li>
</ul>

<h5>Step 1. Finetuning pre-trained Transformer Model</h5>
  
Model finetuning was carried out in a notebook. (mlops_hw6_nlpsentiment.ipynb). The primary motivation for 
the notebook approach is the availability of free GPU in Google Colab. Huggingface dataset and pretrained
classification model were used to fine tune the model for sentiment analysis. The dataset used is IMDB Movie
Reviews dataset (which is easily available from several sources). IMDB dataset from huggingface library was 
used in this project. The trained model was saved for use during deployment.
  
<h5>Step 2. Fast API based Real-time Inference </h5>

FastAPI based access to the model including pydantic based validation of inputs and outputs are included.
Dependency injection is also supported to utilize any future model in the system. Code is in the file
api.py which is the main entry point.

[[img1.png]]

<h5>Step 3. Containarized Deployment </h5>

After validating that the model works as it should, Dockerfile was created to package the fully tested app
(including model artifacts). The dockerized version of the application was also tested on a local machine.
Details of the build are given in the Dockerfile.
[[img2.png]]

[[img3.png]]
  
<h5>Step 4. Cloud Service </h5>

The docker image was uploaded to AWS container registery. The docker image is publically avialable
(via AWS) at: public.ecr.aws/d4e8a7g0/mlops_sridiyer . The app was defined as a task under the
framework of Fargate / Container Service and run.

