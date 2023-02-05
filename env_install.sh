# Install swig make cmake
sudo apt install swig cmake

# Install anaconda swig
conda install -c anaconda swig

# Install the requirements
pip install -r pip_requirements.txt

# Install opengl ffmpeg and xvfb
sudo apt-get update
sudo apt install python-opengl
sudo apt install ffmpeg
sudo apt install xvfb

# Install the virtual display
pip install pyvirtualdisplay