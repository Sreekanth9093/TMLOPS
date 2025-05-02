###############################################################################
# List of Tools to be Installed
###############################################################################

1. Install git (Version Control System)

2. Sign Up for GitHub https://github.com/

3. Install Visual Studio Code https://code.visualstudio.com/download

4. Install Python
    - Create a Directory named 'python' in Drive C  ex: C:\python

5. Verify Python and Pip
       $ python --version
       $ pip --version
       $ which python   (output: C:\python\python.exe)

6. Install Jupyter notebooks and Labs
       $ pip install jupyter lab
       $ pip install jupyter notebook

7. Install Python Libraries for ML
       $ pip install numpy
       $ pip install pandas
       $ pip install scikit-learn   

8. Install Postman
      Link: https://www.postman.com/downloads/

9. Install Flask
      $ pip install Flask

10. Install Docker Desktop

11. DOcker commands
    $ docker build -t <<image-name>> .
    $ docker images
    $ docker run -p 5000:5000 <<image-name>>

12. Install Java JDK 17
    Page: https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html
    - JAVA_HOME = "C:\Program Files\Java\jdk-17\"  # Where you have installed Java

    - PATH = "EXISTING PATH" + C:\Program Files\Java\jdk-17\bin
      OR
      PATH = "EXISTING PATH" + %JAVA_HOME%/bin

    - Verify java
      $ java --version

13. Install Jenkins
    Page: https://www.jenkins.io/download/

    1. Create new folder - jenkins
    2. Move jenkins.war package to new folder jenkins ex: C:\jenkins\jenkins.war
    3. Run the command under C:\jenkins
       $ java -jar jenkins.war

14. Using Jenkins Jobs ( Windows batch Comand)
   # Job1:
       $ python model.py
       $ docker build -t <<name-of-your-docker-image>> .


################################################################################
# KUBERNETES FOR MLAPP DEPLOYMENTS
################################################################################

- # What is Kubernetes?
   Kubernetes, also known as K8s, is an open source system for automating deployment, scaling, and management of containerized applications

- # Install Kubernetes using Kind
   $ curl.exe -Lo kind-windows-amd64.exe https://kind.sigs.k8s.io/dl/v0.27.0/kind-windows-amd64

- Create C:\kind in Drive C and move kind.exe ex: C:\kind\kind.exe

- # Creating a Cluster 
   $ kind create cluster --name my-kind-cluster
   $ kind get clusters

- # Use 'kubectl' to connect and address Kubernetes objects
  https://kubernetes.io/docs/tasks/tools/

   $ kubectl version
   $ curl.exe -LO "https://dl.k8s.io/release/v1.33.0/bin/windows/amd64/kubectl.exe"

- Create C:\kubectl in Drive C and move kubectl.exe ex: C:\kubectl\kubectl.exe



# FOR KUBERENTETS
$ kubectl get nodes
$ kubectl get pods
$ kubectl get svc

# To Create Deployments
$ kubectl apply -f manifests/
$ kuebctl get svc
$ kubectl port-forward svc/mlapp-service 5000:5000

# To Delete the Deployments
$ kubectl delete -f manifests/

###########################################################################################################################
# USING JENKINS
###########################################################################################################################
``` bash
Job1: 01_build_mlapp_artifacts_and_docker_images
      Task1:
       $ python model.py

       Task2:
       $ docker build -t <<docker-hub-name>>/rentalmlapp .
       $ docker push <<docker-hub-name>>/rentalmlapp:latest


Job2: 02_deploy_mlapp_to_kubernetes
      Task1: 
       $ kubectl delete -f manifests/
      Task2: 
       $ kubectl apply -f manifests/
```