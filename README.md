### 2020/07 BuRnCycL

Simple script to interact with Blinkstick Strip + Square

Loops through colors in list. Just an example.

Reference: 
- https://www.blinkstick.com/products/blinkstick-square
- https://www.blinkstick.com/products/blinkstick-strip

### Semi-Automated Installation

Assuming a virgin Raspberry Pi running Raspios Buster Lite. Boot and install the following Prerequisites.

Install git
```
sudo apt install git 
```

Clone this repo
```
git clone https://github.com/burncycl/blinkstick-strip-square-colors.git 
```

Execute `install.sh` to install apt packager maintained dependencies.
```
cd blinkstick-strip-square-colors/ 
sudo ./install.sh
```

### Run

IMPORTANT: Must be `root`

Setup Python Virtual Environment with all Python dependencies
```
source ./init.sh
```

**Run**
```
python3 blinkstick.py 
```

