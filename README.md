# Self-Driving Car in Grand Theft Auto 5

Explorations of Using Python to play Grand Theft Auto 5, mainly for the purposes of creating self-driving cars and other vehicles.

We read frames directly from the desktop, rather than working with the game's code itself. This means it works with more games than just GTA V, and it will basically learn whatever you put in front of it based on the frames as input and key presses as output.

## Setting Up
Here's how to get you started on copying all of the below tutorial codes. Run the below code to clone this repository onto your local computer.  
`git clone https://github.com/cheewoei1997/pygta5.git`

Navigate to the repository that you have cloned and create a virtual environment.

The Python that we are using for this project is Python 3.6.6, which can be download at the [official Python website](https://www.python.org/downloads/release/python-366/). After downloading Python 3.6.6, create a virtual environment to ease the process and complexity of setting up.

Point the creation of the virtual environment at the folder where Python was downloaded. An example is seen below.
`virtualenv --python=C:\Users\cheewoei\AppData\Local\Programs\Python\Python36\python.exe venv`

Activate the virtual environment.
`.\venv\Scripts\activate`

After activating the virtual environment, the `(venv)` should be seen at the leftmost side of the command line interface. An example in Windows 10 is as below.
`(venv) PS C:\GitHub\pygta5>`

Install all the necessary packages.
`pip install -r requirements.txt`

To have your tensorflow run on the GPU, it is necessary to set up cuDNN and CUDA.

### Deep Learning Set Up
Follow the [installation guide](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#install-windows). You would need to upgrade your graphic card's driver and ensure that it is an Nvidia GPU. In the event that your GPU is from AMD, you may look into the [ROCm Stack](https://gpuopen.com/rocm-tensorflow-1-8-release/), but it is severely limited to only several GPUs. 

Installation of [CUDA](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exenetwork) is relatively simple, as there is a wizard. 
Make sure to install according to your system's specifications.

Install the [cuDNN](https://developer.nvidia.com/rdp/cudnn-download) library. Follow the steps specified in the [installation guide](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#install-windows). Only 3 files would need to be manually placed in the Nvidia GPU Computing Toolkit.

### Tensorboard
`tensorboard --logdir=foo:C:\GitHub\pygta5`

## Model
### Data Collection
After setting up everything, tonnes of data would need to be collected to be fed into the model. This can be achieved by running the `1. collect_data.py` file. This script will capture the top left 800 by 600 pixels of the screen. The training files are all kept in the `training` folder.

### Training
After collecting all the data needed for the training of the model, we feed it into the neural network by running the `2. train_model.py` file. This script currently uses Google's Inception v3 model. It has been scripted to keep all the trained models in the `models` folder.

### Testing
Test the model by loading the model that you have trained by running the `3. test_model` file.

## Relevant Links
https://pythonprogramming.net/game-frames-open-cv-python-plays-gta-v/
https://pythonprogramming.net/tensorflow-introduction-machine-learning-tutorial/

## Credits
[sentdex](https://github.com/Sentdex/pygta5)

Feel like contributing? Share it with them at: https://github.com/Sentdex/pygta5/