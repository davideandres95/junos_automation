# junos_automation
This repository includes some basic examples for using Juniper's PyEZ and Ansible modules

## Requirements
For PyEZ
```
pip install junos-eznc
```
You can also create a virtual environment to isolate this python project by doing:

```
virtualenv --python python3 .
source bin/activate #starts the venv
pip install -r requirements.txt #this will install all required dependencies
```
Once you want to leave the venv:
```
deactivate
```
For Ansible you must install it as well as the Juniper.junos roles module
(example for Ubuntu)
```
sudo apt-get install ansible
ansible-galaxy install juniper.junos
```

## OSPF provisioning with PyEZ
Please modify the hardcoded variables as needed in *example_ospf.py*
The ospf.j2 jinja template is stored in the /templates folder
Variables are being loaded from the host_vars folder. Please rename according to the hostnames you are using
Finally, to run the script:
```
python3 example-ospf.py
```

## BGO provisioning with Ansible
According to ansible best practices, credentials for the devices are stored inside a provider in the *group_vars* folder for each device group listed in your *./hosts* file.
Specific host variables are stored in *host_vars* which will be used to render the templates.
To trigger the ansible playbook:
```
ansible-playbook pb-provision-bgp.yml
```

## Other examples
There are two more very simple scripts in this repository. Try them out if you wish
