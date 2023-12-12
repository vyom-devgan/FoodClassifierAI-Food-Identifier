sudo apt-get update -y

# silence gui output
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -yq
sudo apt install python3-pip
sudo apt install awscli
sudo apt-get install git-lfs

# python requirements
pip install -r requirements.txt
pip install tensorflow
pip install --upgrade flask jinja2 markupsafe

# add usr/local to PATH
echo "export PATH=$PATH:/home/ubuntu/.local/bin" >> ~/.bashrc
source ~/.bashrc


