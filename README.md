# kubernetes

<img src="kubernetes_logo.png" width="96">

[Kubernetes](https://kubernetes.io/) is a container-orchestration system.
It provides a platform for automating deployment, scaling, and operations of application containers across clusters of hosts. It works with a range of container tools, including Docker.

[Helm](https://helm.sh/) is increasingly becoming a standard way for managing applications on Kubernetes. The easiest way to think about Helm is as a package manager for Kubernetes. More details here: [Deploying the ELK Stack on Kubernetes with Helm](https://logz.io/blog/deploying-the-elk-stack-on-kubernetes-with-helm/)

[Kubernetes network-plugins](https://kubedex.com/kubernetes-network-plugins/): Differences between Flannel, Calico, Weave, Cilium, Kube Router, Romana and Contiv.

## machine learning & kubernetes
[Dask Kubernetes](https://kubernetes.dask.org/en/latest/): Dask Kubernetes deploys Dask workers on Kubernetes clusters using native Kubernetes APIs and it is designed for deployments of workers during the lifetime of a Python process.

[Machine Learning im Kubernetes-Cluster](https://m.heise.de/developer/artikel/Machine-Learning-im-Kubernetes-Cluster-4226233.html?seite=all). Heise-Artikel

[Machine Learning auf Kubernetes leicht gemacht](https://jaxenter.de/kubernetes/kubeflow-1-0-machine-learning-auf-kubernetes-leicht-gemacht-92380)

[Kubeflow](https://medium.com/kubeflow/kubeflow-1-0-cloud-native-ml-for-everyone-a3950202751) is a Cloud Native platform for machine learning based on Google’s internal machine learning pipelines.

[Kubeflow - Github](https://github.com/kubeflow/kubeflow)

## other basic links
[training material](https://github.com/loodse/k8s-exercises/tree/master/containers/fundamentals)

[how to log](https://github.com/loodse/k8s-exercises/blob/master/containers/fundamentals/10_logs.md)

## docker essentials & links

<img src="docker_logo.png" align="left" width="96">


#### Docker Image vs. Container
There are some important differences between Docker Images and Docker Containers. A Docker Image consists of a Docker file and all the required dependencies. A Docker Container, in somewhat simplified terms, is a Docker Image that has been started. However, each image can run multiple containers. One can think of an Image as the class of a program while the container is the running instance of the class
blueprint|object
---|---|
class|instance|
image|container|

#### The general structure of commands in Docker looks like this:

* They always start with "docker" followed by a space
* Then comes the management category followed by a space
* And finally, the actual command

#### Commands for Docker images
For images, **docker image** is followed by the respective command. Here is an overview of the most important commands:

command|meaning
---|---|
**build** |Builds an image|
**push** |Pushes an image to a remote registry|
**pull** |Pulls an image or repository from a registry|
**ls** |Lists all existing images|
**history** |Displays all information about an intermediate image|
**inspect** |Displays detailed information about an image, including the individual layers|
**rmi** |Deletes an image|


#### Commands for Docker Containers
Analogous to the commands for Docker images, the commands for Docker containers are structured: **docker container** is followed by the respective command. Here are the most important ones:

command|meaning
---|---|
**create** |Creates a container from an image|
**start** |Starts an existing container|
**run** |Creates a new container and starts it|
**ls** |Lists all running containers|
**inspect** |Displays detailed information about a container|
**stop** |Stops a running container|
**kill** |Stops the main process in a container abruptly|
**rm** |Deletes a stopped container|
**logs** |Prints logs|


#### Other useful Docker commands
Following commands are also useful:

command|meaning
---|---|
**docker version** |Displays the Docker version of Echo client and server|
**docker images** |Lists all Docker images|
**docker save \<path> \<image>** |Saves a Docker image to a .tar file further specified by "path"|
**docker export** |Exports a container's filesystem as a tar archive|
**docker exec** |Executes a command in a running container|
**docker ps -a** |Displays all containers (the -a stands for the -all flag)|
**docker ps -l** |Displays the last container created|
**docker search** |Searches the Docker Hub for images|
**docker attach** |Attaches something to a running container|
**docker commit** |Creates a new image with the changes made to a container|

#### Commands for volumes:
listing, creating, and deleting volumes

command|meaning
---|---|
**docker volume ls**|Lists volumes|
**docker volume create**|Creates volumes|
**docker volume rm**|Deletes volumes|

#### Workflow for creating/handling images and containers
![alt text](https://github.com/hadze/kubernetes-docker/blob/master/images/docker.png)

#### Links

[docker hub official](https://hub.docker.com/search?q=&type=image)  

[dockerfile best practices](https://youtu.be/JofsaZ3H1qM)

[docker samples](https://docs.docker.com/samples/)

[docker playground](https://labs.play-with-docker.com)

my docker hub
<a href="https://hub.docker.com/u/thehadz" alt="my docker account">
  <img src="docker_logo.png" align="left" width="96" >
</a>

<br>
<br>
<br>
<br>

## examples
[flask application as container](https://github.com/hadze/kubernetes-docker/tree/master/flask)

[Kubernetes Guestbook Example](https://github.com/loodse/k8s-exercises/tree/master/k8s/fundamentals/kubernetes_example): 

Based on the Kubernetes tutorial this example will show how a multi-tier web application is built and deployed to a Kubernetes cluster. It consists of Redis as a database backend and a PHP guestbook. Redis will get a single-instance master to store the entries together with multiple replicated instances for reading. The guestbook will run on multiple frontend instances.

[simple docker example with unit tests](https://github.com/hadze/kubernetes-docker/tree/master/unittest)

Run the following commands:

$ docker build . -t unittestexample
$ docker run --rm unittestexample sh -c "python test.py"

First line builds the image defined by the content within the Dockerfile.
Second line starts the container and executes the unittest (test.py). Notice that the container is going to be removed after the test has been executed (--rm)
