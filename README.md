# vagrant_fedora
A Vagrant setup for building RPM packages on Fedora

## Introduction
This project is a Vagrant setup for building RPM packages on Fedora. 
It includes a basic example of an RPM package that installs a simple Hello World script.
The project is based on the Fedora 39 cloud base box.
Feel free to use this project as a starting point for building your own RPM packages.

## Usage
1. Install Vagrant and VirtualBox on your host machine (https://www.vagrantup.com/docs/installation/ and https://www.virtualbox.org/wiki/Downloads)
2. Clone this repository from GitHub to your host machine and navigate to the directory in a terminal
3. Run `vagrant up --provision` to start the VM and install the necessary packages (this will take a while)
4. Run `vagrant ssh` to connect to the VM
5. Modify the file .rpmmacros in the home directory, the new content should be as follows:
From:
```shell
%_topdir %(echo "$PWD")/rpmbuild
```

```shell
...
%_topdir %(echo "$PWD")/rpmbuild
...
```
6. Move to the directory `/vagrant/project` to build the RPM

## RPM Build
A basic example is already included in the `rpmbuild` directory. 
To build the example RPM, follow these steps:
1. Run `rpmbuild -ba rpmbuild/SPECS/hello.spec`
2. The RPM will be built and placed in the `RPMS` directory
3. You can install the RPM with `sudo rpm -ivh rpmbuild/RPMS/x86_64/hello-0.0.1-1.fc39.x86_64.rpm`

## Testing and cleaning up of RPM
1. The Hello World RPM can be tested by running `hello.sh` in the terminal
2. Execute `rpm -ql hello` to see the files installed by the RPM
3. Execute `rpm -q hello --changelog` to see the changelog of the RPM
4. To remove the RPM, run `sudo rpm --verbose --erase hello`

## Virtual box cleanup
1. Exit the VM by running `exit` in the terminal
2. Run `vagrant halt` to stop the VM
3. Run `vagrant destroy` to remove the VM from your host machine
4. Run `vagrant box remove fedora/33-cloud-base` to remove the base box from your host machine
5. You can now delete the cloned repository from your host machine with `rm -rf vagrant_fedora`

## Notes
- The hello.sh script was packed with the following command:
```shell
vagrant@localhost:/vagrant/project$ tar --create --file hello-0.0.1.tar.gz hello-0.0.1
vagrant@localhost:/vagrant/project$ mv hello-0.0.1.tar.gz rpmbuild/SOURCES/
```

## References
- https://www.vagrantup.com/docs/installation/
- https://www.virtualbox.org/wiki/Downloads
- https://rpm-packaging-guide.github.io/
- https://www.redhat.com/sysadmin/create-rpm-package

## License
This project is licensed under the MIT License for complete license see the [LICENSE](LICENSE) file.