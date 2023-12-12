sudo apt-get update -yq

# silence gui output
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -yq
sudo apt install python3-pip -yq
sudo apt-get install git-lfs -yq

# python requirements
pip install -r requirements.txt
pip install tensorflow
pip install --upgrade flask jinja2 markupsafe

# add usr/local to PATH
echo "export PATH=$PATH:/home/ubuntu/.local/bin" >> ~/.bashrc
source ~/.bashrc

# get the model with git lfs
git lfs install
git lfs pull

# run the model
python3 main.py


