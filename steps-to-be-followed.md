###############################################################################
# List of Tools to be Installed
###############################################################################

1. Install Git (Version Control System)  
       - Download and install Git from https://git-scm.com/.

2. Sign Up for GitHub  
       - Create an account at https://github.com/.

3. Install Visual Studio Code  
       - Download and install VS Code from https://code.visualstudio.com/download.

4. Install Python  
       - Download and install Python from https://www.python.org/downloads/.  
       - Create a directory named `python` in Drive C (e.g., `C:\python`).

5. Verify Python and Pip Installation  
       ```bash
       $ python --version
       $ pip --version
       $ where python   # Output: C:\python\python.exe
       ```

6. Install Jupyter Notebooks and Labs  
       ```bash
       $ pip install jupyter lab
       $ pip install jupyter notebook
       ```

7. Install Python Libraries for Machine Learning  
       ```bash
       $ pip install numpy
       $ pip install pandas
       $ pip install scikit-learn
       ```

8. Install Postman  
       - Download Postman from https://www.postman.com/downloads/.

9. Install Flask  
       ```bash
       $ pip install Flask
       ```

10. Install Docker Desktop  
        - Download and install Docker Desktop from https://www.docker.com/products/docker-desktop/.

11. Docker Commands  
        ```bash
        $ docker build -t <image-name> .
        $ docker images
        $ docker run -p 5000:5000 <image-name>
        ```

12. Install Java JDK 17  
        - Download JDK 17 from https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html.  
        - Set environment variables:  
              ```plaintext
              JAVA_HOME = "C:\Program Files\Java\jdk-17\"  # Path to JDK installation
              PATH = "EXISTING PATH" + C:\Program Files\Java\jdk-17\bin
              OR
              PATH = "EXISTING PATH" + %JAVA_HOME%\bin
              ```
        - Verify Java installation:  
              ```bash
              $ java --version
              ```

13. Install Jenkins  
        - Download Jenkins from https://www.jenkins.io/download/.  
        - Steps:  
              1. Create a new folder named `jenkins`.  
              2. Move the `jenkins.war` package to the folder (e.g., `C:\jenkins\jenkins.war`).  
              3. Run the following command from the `C:\jenkins` directory:  
                     ```bash
                     $ java -jar jenkins.war
                     ```

14. Using Jenkins Jobs (Windows Batch Command)  
        - Job1:  
              ```bash
              $ python model.py
              $ docker build -t <name-of-your-docker-image> .
              ```

15. Install AWS CLI
    KeyPages: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html


16. Install Boto3
     $ pip install boto3

################################################################################
# Kubernetes for ML App Deployments
################################################################################

### What is Kubernetes?  
Kubernetes, also known as K8s, is an open-source system for automating deployment, scaling, and management of containerized applications.

### Install Kubernetes Using Kind  
1. Download Kind:  
       ```bash
       $ curl.exe -Lo kind-windows-amd64.exe https://kind.sigs.k8s.io/dl/v0.27.0/kind-windows-amd64
       ```
2. Create a directory `C:\kind` and move `kind.exe` to it (e.g., `C:\kind\kind.exe`).

### Creating a Cluster  
```bash
       $ kind create cluster --name my-kind-cluster
       $ kind get clusters
```

### Use `kubectl` to Connect and Manage Kubernetes Objects  
1. Download `kubectl`:  
       ```bash
       $ curl.exe -LO "https://dl.k8s.io/release/v1.33.0/bin/windows/amd64/kubectl.exe"
       ```
2. Create a directory `C:\kubectl` and move `kubectl.exe` to it (e.g., `C:\kubectl\kubectl.exe`).

### Common Kubernetes Commands  
```bash
# Get nodes, pods, and services
       $ kubectl get nodes
       $ kubectl get pods
       $ kubectl get svc

       # Create deployments
       $ kubectl apply -f manifests/
       $ kubectl get svc
       $ kubectl port-forward svc/mlapp-service 5000:5000

       # Delete deployments
       $ kubectl delete -f manifests/
```

################################################################################
# USING JENKINS FOR MLAPP DEPLOYMENT
################################################################################
#### Job1: Build ML App Artifacts and Docker Images  
```bash
       Task1:
       $ python model.py

       Task2:
       $ docker build -t <docker-hub-name>/rentalmlapp .
       $ docker push <docker-hub-name>/rentalmlapp:latest
```
#### Job2: Deploy ML App to Kubernetes  
```bash
       Task1:
       $ kubectl delete -f manifests/

       Task2:
       $ kubectl apply -f manifests/
```

################################################################################
# Using Kubeflow for MLOPS
################################################################################

- To get started with the tutorials, pip install kfp v2:
```bash
   $ pip install kfp==2.13.0
```
# What is Kubeflow Component?
 - Components are the building blocks of KFP pipelines. 
 - A component is a remote function definition; 
       - it specifies inputs, has user-defined logic in its body, and can create outputs. 
 - When the component template is instantiated with input parameters, we call it a task.

kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80


################################################################################
# USING JENKINS FOR MLAPP DEPLOYMENT USING KUBEFLOW
################################################################################
#### Job1: Build ML App Artifacts and Docker Images  
Name: 01_build_mlapp_artifacts_and_docker_images_using_kubeflow
```bash
       Task1:
       $ cd 01_using_kubeflow
       $ mkdir model
       $ python model.py
       $ aws s3 cp s3://iriscloudbt-mlapp/model/rental_prediction_model.pkl model/model.pkl

       Task2:
       $ cd 01_using_kubeflow
       $ docker build -t <docker-hub-name>/rentalmlapp .
       $ docker push <docker-hub-name>/rentalmlapp:latest
```
#### Job2: Deploy ML App to Kubernetes  
```bash
       Task1:
       $ cd 01_using_kubeflow
       $ kubectl delete -f manifests/

       Task2:
       $ cd 01_using_kubeflow
       $ kubectl apply -f manifests/
```

 ####################################################################################
# 13. Commonly Used API From Kubeflow Pipelines
####################################################################################
list_of_apis.py

```python

   # Library Imports
   import kfp
   import logging

   # Configure logging
   logging.basicConfig(level=logging.INFO)

   # Set your Kubeflow Pipelines endpoint here
   kfp_endpoint = None
   client = kfp.Client(host=kfp_endpoint)

   # Experiment name
   experiment_name = "My Experiment"

   # Create a new experiment
   def create_experiment(client, experiment_name):
      experiment = client.create_experiment(name=experiment_name)
      logging.info(f"Created experiment: {experiment.name}")
      return experiment


   # List all experiments
   def list_experiments(client):
      experiments = client.list_experiments()
      logging.info(f"Experiments: {experiments}")
      return experiments

   # Create a Run from a pipeline function
   def create_run_from_pipeline_func(client, pipeline_func, experiment_name, enable_caching=False):
      run = client.create_run_from_pipeline_func(
         pipeline_func,
         experiment_name=experiment_name,
         enable_caching=enable_caching
      )
      logging.info("Pipeline run initiated")
      return run

   # List all runs for a given experiment
   def list_runs(client, experiment_id):
      runs = client.list_runs(experiment_id=experiment_id)
      logging.info(f"Runs: {runs}")
      return runs

   # Delete a specific run by run_id
   def delete_run(client, run_id):
      client.delete_run(run_id)
      logging.info(f"Deleted run: {run_id}")

   # List all runs for a given experiment and delete the first run
   def delete_previous_run(client, experiment_id):
      runs = list_runs(client, experiment_id)
      if runs and runs.runs:
         run_id = runs.runs[0].run_id
         logging.info(f"Deleting run: {run_id}")
         delete_run(client, run_id)

   # Delete a specific experiment by experiment_id
   def delete_experiment(client, experiment_id):
      client.delete_experiment(experiment_id)
      logging.info(f"Deleted experiment: {experiment_id}")


   # Example usage
   # experiment = create_experiment(client, "New Experiment")
   # experiments = list_experiments(client)
   # runs = list_runs(client, experiment.experiment_id)
   # delete_run(client, runs.runs[0].run_id)
   # delete_previous_run(client, experiment.experiment_id)
   # delete_experiment(client, experiment.experiment_id)

```