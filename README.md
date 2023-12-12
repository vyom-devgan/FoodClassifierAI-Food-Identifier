## Running on aws

### [On ec2]

in terminal run: export DEBIAN_FRONTEND=noninteractive


git clone https://github.com/vyom-devgan/FoodClassifierAI-Food-Identifier.git  
cd FoodClassifierAI-Food-Identifier  
git checkout caleb-version  
chmod 700 install.sh  
./install.sh  
git checkout yummyinmytummy
git lfs install  
git lfs pull  
cp vgg ~/  
git checkout caleb-version  
mv ~/vgg .  
python3 main.py
