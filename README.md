# ARtificial Intelligence for Gross tumour vOlume Segmentation (ARGOS) Standard Procedures

## ARGOS Standard Procedures

### A : Setting up an ARGOS XNAT dicom collection for your clinic
_The objective of this part is to get a working XNAT docker instance set up locally on your clinic side, and prepare it to receive DICOM data_

<details><summary>Expand step-by-step instructions :</summary>

Step 1 : Ensure that you have sufficient space, memory and reasonably up to date hardware including ***at least 1 GPU chip***. For reference, the MAASTRO node is an Amazon AWS Ubuntu Linux 18.04 virtual machine with 10GBit network and 100GB storage (it happens to be the g3.xlarge template instance).

Step 2 : Install Docker Engine (free Community Edition version). Follow the instructions here - https://docs.docker.com/engine/install/ubuntu/

Step 3 : After validating that Docker is working (e.g. do the hello-world demo recommended at the end of the install documentation) please also install docker-compose (https://docs.docker.com/compose/install/).

Step 4 : Install the git library with `sudo apt-get install git`.

Step 5 : Find the XNAT docker-compose registry by the Washington University Neuro-imaging Research Group, and follow the instructions to clone their repository to your system, starting with the `git clone https://github.com/NrgXnat/xnat-docker-compose`.

Step 6 : Create an XNAT instance by switching directory into the xnat-docker-compose master folder `cd xnat-docker-compose` and then copy the default environment template to the .env file as `sudo cp default.env .env`.

Step 7 : Spin up the required XNAT components using docker-compose as follows `sudo docker-compose up -d`.

Step 8 : Depending on your system Step 7 could well take a few minutes to get set up. You can check status using the following command `sudo docker stats`. Once all three docker images in the XNAT package are stable at very low load, it probably means everything is up and running nice in the background.

Step 9 : On the same machine that is hosting your XNAT docker instance, you now need to point a web browser to http://localhost:80. The XNAT welcome screen should come up momentarily.
</details>

### B : Populating the XNAT dicom collection point with your clinical data
_The objective of this part is to get a populate your XNAT docker instance with de-identified DICOM data, the end point desired will be DICOM CT and DICOM SEGMENTATION file for each patient, with the primary lung GTV identified as such_

Step 1 : On the XNAT welcome screen, you will log in as _admin_ and the password is _admin_.

![](./screenshots/xnat_splash_admin.jpg)

Step 2 : Create a new project, for instance, I am calling mine "ARGOSnode02". This name is only visible on your side, no one else needs this, so feel free to label your collection as you wish.

Screenshot

Step 3 : There are now several options to populate the XNAT collection with your DICOM CT and DICOM RTSTRUCT (for most partners) or DICOM SEGMENTATION (for the minority of partners). We will provide you some of the data transfer options below.

**Note well : If using RTSTRUCT, please have primary lung tumour(s) named as 'GTV-1' (GTV-2, etc. if more than one primary in the lung). Malignant nodes are named as 'GTV-N1' ('GTV-N2', etc. if more than one node) or simply 'GTV-Nsum'. Organs at risk such as 'Esophagus', 'Heart', 'Lung-Left', 'Lung-Right', are all purely optional.**

Screenshot

Screenshot

##### Option 1 : Direct upload with python batching script
_This can only work with adequately de-identified and correctly-cleaned DICOM data_. We provide you with a python notebook script to iterate through every patient folder in a local filesystem directory, it will package each patient folder as a zip object, and then transmit the zip via API into your local XNAT docker instance which will collect it and try to archive it. This requires Python version 3.7 or later.

##### Option 2 : Clinical Trial Processor pipeline ending with DICOM transfer
_This is probably the most useful clinical-integrated workflow_. Here, we need to set you up with Clinical Trial Processor workflow that will (i) consume a copy of your DICOM files exported from your planning system or PACS (b) it will de-identify (using a key file) and change the GTV names (again using a lookup file) into the standard required above (c) it will send it across via standard DICOM protocol across the network to try to reach port number 8104 on your XNAT machine.

##### Option 3 : Clinical Trial Processor pipeline ending with HTTPS transfer
_This is probably one of the options for partners that want to move clinical data to a university department that hosts the ARGOD node_. This will be again done with Clinical Trial Processor and works the same as Option 2 above, except we will send via HTTPS protocol. There needs to be some additional setting up on the XNAT receiving side, but we will have someone from Medical Data Works give you some guidance for this part.

Step 4 : (in progress)


##### Access to machine where the deep learning will run locally
In this study, you will need a local machine where you can hold images until needed, and have the following hardware requirements.
These requirements are also stated in Section 4.1 of the study protocol.
<br>
- We strongly recommend ***either Windows 10 or Ubuntu 18.04 LTS*** operating system
- ***Python version 3.7 or higher***, we recommend Anaconda latest version for Windows 10 or else upgrade python version in Ubuntu
- ***Docker Desktop** community edition (free)
- ***At least 1 GPU***
- ***At least 16GB of RAM***
- Approximately 30GB of hard disk space, at least 10% more than needed to keep your patient images, more is always better
- The clinic researcher needs to have local admin rights on this deep learning machine
- Local IP address and port for HTTPS (we will tell you which port number to enable)


