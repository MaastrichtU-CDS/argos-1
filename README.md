# ARGOS
## ARtificial Intelligence for Gross tumour vOlume Segmentation

### Setting up an ARGOS node for your clinic

Step 1 : Ensure that you have sufficient space, memory and reasonably up to date hardware including ***at least 1 GPU chip***. For reference, the MAASTRO node is an Amazon AWS Ubuntu Linux 18.04 virtual machine with 10GBit network and 50GB storage (it happens to be the g3.xlarge template instance).

Step 2 : Install Docker Engine (free Community Edition version). Follow the instructions here - https://docs.docker.com/engine/install/ubuntu/

Step 3 : After validating that Docker is working (e.g. do the hello-world demo recommended at the end of the install documentation) please also install docker-compose with the command line - sudo apt-get install docker-compose.


### Access to machine where the deep learning will run locally
In this study, you will need a local machine where you can hold images until needed, and have the following hardware requirements.
These requirements are also stated in Section 4.1 of the study protocol.
<br>
- We strongly recommend ***either Windows 10 or Ubuntu 18.04 LTS*** operating system
- ***Python version 3.6 or higher***, we recommend Anaconda latest version for Windows 10 or else upgrade python version in Ubuntu
- ***Docker Desktop** community edition (free)
- ***At least 1 GPU***
- ***At least 16GB of RAM***
- Approximately 30GB of hard disk space, at least 10% more than needed to keep your patient images, more is always better
- The clinic researcher needs to have local admin rights on this deep learning machine
- Local IP address and port for HTTPS (we will tell you which port number to enable)

###2

###Setting up your local XNAT to keep the images
