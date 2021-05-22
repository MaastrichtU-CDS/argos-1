# ARGOS
## ARtificial Intelligence for Gross tumour vOlume Segmentation

### A : Setting up an ARGOS XNAT dicom collection for your clinic

Step 1 : Ensure that you have sufficient space, memory and reasonably up to date hardware including ***at least 1 GPU chip***. For reference, the MAASTRO node is an Amazon AWS Ubuntu Linux 18.04 virtual machine with 10GBit network and 50GB storage (it happens to be the g3.xlarge template instance).

Step 2 : Install Docker Engine (free Community Edition version). Follow the instructions here - https://docs.docker.com/engine/install/ubuntu/

Step 3 : After validating that Docker is working (e.g. do the hello-world demo recommended at the end of the install documentation) please also install docker-compose (https://docs.docker.com/compose/install/).

Step 4 : Install the git library with `sudo apt-get install git`.

Step 5 : Find the XNAT docker-compose registry by the Washington University Neuro-imaging Research Group, and follow the instructions to clone their repository to your system, starting with the `git clone https://github.com/NrgXnat/xnat-docker-compose`.

Step 6 : Create an XNAT instance by switching directory into the xnat-docker-compose master folder `cd xnat-docker-compose` and then run spin up the required XNAT components using docker-compose as follows `sudo docker-compose up -d`.

Step 7 : Depending on your system Step 6 could well take a few minutes to get set up. You can check status using the following command `docker stats`. Once all three docker images in the XNAT package are stable at very low load, it probably means everything is up and running nice in the background.

Step 8 : On the same machine that is hosting your XNAT docker instance, you now need to point a web browser to http://localhost:80. The XNAT welcome screen should come up momentarily.

### B : Populating the XNAT dicom collection point with your clinical data

Step 1 : On the XNAT welcome screen, you will log in as admin and the password is admin.

Step 2 : Create a new project, for instance, I am calling mine "ARGOSnode02". This name is only visible on your side, no one else needs this, so feel free to label your collection as you wish.

Screenshot

Step 3 : There are now several options to populate the XNAT collection with your DICOM CT and DICOM RTSTRUCT. We will provide you some of the options below. The important thing is to end up here with DICOM CT cleaned and properly de-identified, with RTSTRUCT attached such that the ***primary lung tumour has been labelled as GTV-1***.

Screenshot

Screenshot

#### Option 1 : Direct upload with python batch script

#### Option 2 : Clinical Trial Processor pipeline ending with DICOM SEND


#### Option 3 : Clinical Trial Processor pipeline ending with HTTPS SEND





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
