#!/bin/bash

# clone repository
git clone https://github.com/Riyantttsjddj/sub-domain.git
cd sub-domain

# Meminta input domain dari pengguna
read -p "input domain (sampel: domain.com): " domain

# running
python3 subdomain.py $domain
