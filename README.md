## Running on aws

### [On ec2]

in terminal run: export DEBIAN_FRONTEND=noninteractive


git clone https://github.com/CalebMcAnuff/Cosc-aws-deploy.git
cd Cosc-aws-deploy
chmod 700 install.sh
./install.sh
[edit bashrc]
export PATH=$PATH:/home/ubuntu/.local/bin
[close bashrc]
source ~/.bashrc
aws configure
aws s3 cp s3://<s3-bucket-name>/<model_name> .
python3 main.py
