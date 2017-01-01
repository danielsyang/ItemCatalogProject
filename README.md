# itemCatalogProject

This project is the fifth project from the Full Stack Nanodegree.

Before you run this project, be sure that you have VirtualBox and Vagrant installed on your computer.

Then run the following command inside this project folder to initialize your virtual machine.
* **sudo su**
* **vagrant up**

Then run the ssh command to access your VM.
* **vagrant ssh**

After that all the code will be available on this path in your vm.
* **/vagrant/tournament**

Finally you have to first create the database and the entities, after taht populate the recent created db and then run the project.

1. **python database_entities.py**

2. **python database_init.py**

3. **python item_catalog_project.py**
