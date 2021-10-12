# ARtificial Intelligence for Gross tumour vOlume Segmentation (ARGOS)

## ARGOS Standard Procedures (growing document - works in progress)

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
_The objective of this part is to get a populate your XNAT docker instance with de-identified DICOM data, the end point desired will be DICOM CT and DICOM SEGMENTATION file for each patient, with the primary lung GTV attached with the SNOMED CT attribute 86049000 (i.e. "Neoplasm, Primary)_

<details><summary>Expand step-by-step instructions :</summary>

Step 1 : On the XNAT welcome screen, you will log in as _admin_ and the password is _admin_.
![](./screenshots/xnat_splash_admin.jpg)

Step 2 : Create a new project, for instance, I am calling mine "ARGOSnode02". This name is only visible on your side, no one else needs this, so feel free to label your collection as you wish.
![](./screenshots/xnat-new-projecr.png)

Step 3 : There are now several options to populate the XNAT collection with your DICOM CT and DICOM RTSTRUCT (for most partners) or DICOM SEGMENTATION (for the minority of partners). We will provide you some of the data transfer options below.

**Note well : If using RTSTRUCT, please have primary lung tumour(s) named as 'GTV-1' (GTV-2, etc. if more than one primary in the lung). Malignant nodes are named as 'GTV-N1' ('GTV-N2', etc. if more than one node) or simply 'GTV-Nsum'. Organs at risk such as 'Esophagus', 'Heart', 'Lung-Left', 'Lung-Right', are all purely optional.**

##### Option 1 : Direct upload with python batching script
_This can only work with adequately de-identified and correctly-cleaned DICOM data_. We provide you with a python notebook script to iterate through every patient folder in a local filesystem directory, it will package each patient folder as a zip object, and then transmit the zip via API into your local XNAT docker instance which will collect it and try to archive it. This requires Python version 3.7 or later.

##### Option 2 : Clinical Trial Processor pipeline ending with DICOM transfer
_This is probably the most useful clinical-integrated workflow_. Here, we need to set you up with Clinical Trial Processor workflow that will (i) consume a copy of your DICOM files exported from your planning system or PACS (b) it will de-identify (using a key file) and change the GTV names (again using a lookup file) into the standard required above (c) it will send it across via standard DICOM protocol across the network to try to reach port number 8104 on your XNAT machine.
  * Download and install Java JRE/JDK _version 8_ (no higher than 8 please)
  * Download and install CTP as per the guidance here : https://mircwiki.rsna.org/index.php?title=MIRC_CTP
  * Extract the contents of the zip package called 'ctp_config_dicom' and replace the files in your CTP directory if needed.
  * Please follow the README notes in this zip package to set up your de-identification and GTV renaming correctly.

##### Option 3 : Clinical Trial Processor pipeline ending with HTTPS transfer
_This is probably one of the options for partners that want to move clinical data to a university department that hosts the ARGOS node_. This will be again done with Clinical Trial Processor and works in similar fashion as Option 2 above, except we will need an EXTRA CTP instance on the RECEIVING SIDE to pick up data via http/http and forward it sideways to XNAT.
  * Download and install Java JRE/JDK _version 8_ (no higher than 8 please)
  * Download and install CTP as per the guidance here : https://mircwiki.rsna.org/index.php?title=MIRC_CTP
  * Note you will need CTP installed on the SENDER SIDE, and also a CTP installed on the RECEIVER SIDE.
  * For the sender : Extract the contents of the zip package called 'ctp_config_http_SENDER' and replace the files in your CTP directory if needed. Please follow the README notes in this zip package to set up your de-identification and GTV renaming correctly.
  * For the receiver : Extract the contents of the zip package called 'ctp_config_http_RECEIVER', then follow the README notes in this zip package to set up your receiver and forward the data into XNAT.

Step 4 : First try a testrun with a dummy case (eg delineated RANDO phantom, or use one of our public access cases from The Cancer Imaging Archive) e.g. LUNG-001 included in this repository. This is to make sure the transfer into XNAT is going as expected. Try downloading this dummy case back from XNAT and open it with your Dicom tools; check if it compares well to the original (must be same other than patient de-identification and GTV renaming). An example of one of my cases in XNAT is in the screenshot below, you see this one has multiple CT slices and one single SEG (or RTSTRUCT if this is your case) assigned to this patient.
![](./screenshots/xnat-dicom-ct-seg.png)

Step 5: Instructions for converting RTSTRUCT to SEGMENTATION following shortly .....
</details>


### C : Access to machine where the deep learning will run locally
You will need a deep learning machine where you can hold images until needed for the training run, and have the following hardware requirements. These requirements are also stated in Section 4.1 of the study protocol.

<details><summary>Expand step-by-step instructions :</summary>

  * We strongly recommend ***Ubuntu 18.04 LTS*** operating system
  * ***Python version 3.7 or higher***
  * ***Docker Desktop*** community edition (free)
  * ***At least 1 GPU with the most up to date drivers; we plan to use TensorFlow v2.4 so we need updated GPU drivers***
  * ***At least 16GB of RAM***
  * At least ***50GB of disk space but more space will be much better*** (50GB corresponds very roughly to 100 patients with 1 Lung CT study and 1 RTSTRUCT file each)
  * The clinic researcher needs to have local admin rights on this deep learning machine
  * Local IP address and port for HTTPS (we will tell you which port number to enable)
  
</details>

When you have your GPU machine ready, please reach out to Leonard ASAP and try to run the stand-alone GPU-only test; we will provide you with the complete test package including open access test images.

### D : Installing the VANTAGE node client for federated learning
For more detailed understanding of the Vantage6 infrastructure please refer to their documentation located [here](https://vantage6.ai/). This section provides instructions for installing the pre-requisites and setting up the infrastructure on your local machine.

***Important note : You must set up the node client for federated learning on your UBUNTU GPU machine.***

<details><summary>Expand step-by-step instructions :</summary>

Step 1 : Confirm that you have Python 3.6 or higher (this almost always ships with the Ubuntu operating system). Upgrade if necessary.

Step 2 : Confirm that you have Docker Community Edition (i.e. the free for research/education version), and if not yet, check the appropriate instructions [here](https://docs.docker.com/engine/install/ubuntu/).

Step 3 : A python virtual environment is strongly recommended. You may use the commands below in your Ubuntu command line console to install, create and then activate a virtual enviroment named "vantage6" (you are welcome to name it anything you wish e.g. "argos01" etc. etc.)
 ```
    sudo apt install python3-venv
    python3 -m venv vantage6
    source vantage6/bin/activate
``` 

Step 4 : Install python pip3 and check the version. You may use the commands below in your Ubuntu command line console.
```
sudo apt update
sudo apt install python3-pip
pip3 --version
```

Step 5 : Node Client Installation; the Vantage6 infrastructure has been modified slightly to accomodate ARGOS and will be installed within the python virtual enviroment you created in step 3 above. You may download only the file in this repository called "vantage6-requirements.txt" or git clone the entire contents to your python virtual environment. The command (assuming you wish to clone the whole git) is :
``` 
git clone https://gitlab.com/UM-CDS/argos-1.git
cat argos-1/vantage6-requirements.txt | xargs -n 1 -L 1 pip3 install
```
Please note : If you wish to download only the vantage6-requirements.txt file, then you have to change the path immediately in front of the "cat" command above to where you had saved the vantage6-requirements.txt file.

Step 6 : At this point, you are ready to configure your node client. For this you will need some information and a couple of online support steps from Medical Data Works, such as an API private key and port numbers/IP addresses etc. Please contact Leonard ASAP to complete this step.
</details>

### E : Connecting to the Medical Dataworks Infrastructure
You will be able to execute these next steps after installing the node client and signing the documents with Medical Data Works.

<details><summary>Expand step-by-step instructions :</summary>

Step 7 : At this point, we are ready to setup a new node. At the terminal where you installed the Vantage node client now type ```vnode new``` and follow the given instructions. For setting up the node, you will require specific information from the server provider. The new node procedure will ask you for a **base url of server** and an **api_key** to authenticate with the server.
  * The base URL of the server you need to enter is exactly this **https://mdw-vantage6-argos.azurewebsites.net/**
  * Port to which the server listens is **5000**
  * The API key will be given to you directly by private email addressed specifically to you.
  * You may leave the default database path empty for the moment.
  * Default settings are fine for the rest of the options.


On successful completion, a configuration file(.yaml) will be created. This configuration file holds the key information necessary for all further communication between the node and the server. 


Step 8 : Additional environment variables in the configuration file. Add the following environment variables in the configuration file by editing the configuration file using the ```nano``` command. The public IP address that you now need to enter for the aggregation point, that is, make sure the line reads as ***public_ip:'20.93.147.169'*** (please note the single quotation marks).
``` 
    vnode files
    nano [/path/to/yourconfigurationFile.yaml]
 ```


Step 9 : Creating and uploading a public/private key. A final step before the node can connect to the server is to generate a public/private key pair and log it with the server. To do this, run the following command (make sure to select the correct configuration name that you created in the previous steps) ``` vnode create-private-key ```

This procedure is going to ask for a username and password for creating and uploading a public/private key pair; this info shall be provided to you beforehand by direct email addressed to you.


Step 10 : Starting the node. You are now ready to start the node type at the terminal :

``` vnode start --image harbor2.vantage6.ai/infrastructure/maastro-node --attach ```

The Vantage node should now be up and waiting to receive tasks from the central server. You can capture a few screenshots of the above steps for us and send it to Len, if you would like us to check that everything went well.
</details>
