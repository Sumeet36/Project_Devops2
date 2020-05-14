## Jenkins Automation Project
### (Integration with Docker)
Problem Statement :

1. Create a container image using Docker file that has Jenkins installed in it.

2. When a container is launched using this image, it should automatically start Jenkins service in the container.

3. Create a job chain of job1, job2, job3 and job4 using build pipeline plugin in Jenkins.

4. Job1 : To Pull the Github repository automatically when some developer pushes a repository to the Github.

5. Job2 : By looking at the program file, Jenkins should automatically start a language interpreter container to deploy code according to the requirement.( eg. If code is of PHP, then Jenkins should start the container with PHP already installed in it ).

6. Job3 : Tests if the app is working or not. In case the app is not working , then it sends an email to the developer with messages stating the errors.

7. We need to create one more job ( job4 ) for monitoring : If container where the app is running fails due to some reason, then this job should automatically start the container again and keep the service running.

### Steps:

1. Create a docker image that has Jenkins already installed using Dockerfile.

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/Dockerfile.png)

2. Using the Dockerfile build the docker image. It can be done using the following command - docker build -t jenkins:v1 .

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/docker_images.png)

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/container_command.png)
3. After building the image. Run a container using the image, check on which port this container is running and start jenkins service.

4. Create First job  (j1) : This job will copy the code from the Github Repository to the specified directory.

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/j1_1.png)

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/j1_2.png)

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/j1_3.png)

5. Now create second job (j2) : Thus job will run aftter first one is successfully executed.

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/j2_1.png)

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/j2_2.png)

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/j2_3.png)

6. Create next job (j3) : It wil check the code and in case the code fails, it will send an email to the developer .

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/j3_1png)

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/j3_2.png)

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/j3_3.png)


#### note : Before setting the post-build, We need to install Email plugin and configure the following settings in Manage Jenkins --> configure System.


![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/j3_4.png)

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/j3_5.png)

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/j3_6.png)

7. Create a build pipeline view for the above jobs. It will look like :

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/build_pipeline.png)

8.Finally build a job (j4) : for monitoring if the containers are running or not.

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/j4_1.png)

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/j4_2.png)

Following are the docker containers that should be running:

![](https://github.com/Sumeet36/Project_Devops2/blob/master/devs2/containers.png)
