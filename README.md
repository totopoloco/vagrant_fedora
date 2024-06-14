# vagrant_fedora
A Vagrant setup for building RPM packages on Fedora

## Introduction
This project is a Vagrant setup for building RPM packages on Fedora. 
It includes a basic example of an RPM package that installs Spring Boot application as a service exposing it as a Rest service.
The project is based on the Fedora 40 box.
Feel free to use this project as a starting point for building your own RPM packages.

## Usage
1. Install Vagrant and VirtualBox on your host machine (https://www.vagrantup.com/docs/installation/ and https://www.virtualbox.org/wiki/Downloads)
2. Clone this repository from GitHub to your host machine and navigate to the directory in a terminal
3. Run `vagrant up --provision` to start the VM and install the necessary packages (this will take a while)
4. Run `vagrant ssh` to connect to the VM
5. Modify the file .rpmmacros in the home directory, the new content should be as follows:
```shell
%_topdir %(echo "$PWD")/rpmbuild
```

6. Move to the directory `/vagrant/project` to build the RPM

## RPM Build
A basic example is already included in the `rpmbuild` directory. 
To build the example RPM, follow these steps:
1. Run `rpmbuild -ba rpmbuild/SPECS/hours-distribution.spec`
2. The RPM will be built and placed in the `RPMS` directory
3. You can install the RPM with `sudo rpm -ivh rpmbuild/RPMS/noarch/hours-distribution-0.0.1-1.fc40.noarch.rpm`
4. If the following error occurs:
```shell
error: Failed dependencies:
	java-21-openjdk is needed by hours-distribution-0.0.1-1.fc40.noarch
```
5. Install the required package with `sudo dnf install -y java-21-openjdk`
6. Try again (see step 3)
  

## Testing and cleaning up of RPM
1. Check the state of the service by running `systemctl status hours-distribution`
2. The following output should be displayed:
```shell
hours-distribution.service - Hours Distribution Service
     Loaded: loaded (/etc/systemd/system/hours-distribution.service; enabled; preset: disabled)
    Drop-In: /usr/lib/systemd/system/service.d
             └─10-timeout-abort.conf
     Active: active (running) since Thu 2024-06-13 09:12:46 UTC; 1min 4s ago
   Main PID: 4196 (java)
      Tasks: 29 (limit: 9483)
     Memory: 266.9M (peak: 271.6M)
        CPU: 38.782s
     CGroup: /system.slice/hours-distribution.service
             └─4196 /usr/bin/java -jar /usr/bin/hours-distribution.jar
```
3. Another way to test the service is by running `sudo netstat -nalp | grep java`
4. Execute `rpm -ql hours-distribution` to see the files installed by the RPM
5. Execute `rpm -q hours-distribution --changelog` to see the changelog of the RPM
6. Test the service by running `curl -X GET -H "Pragma: no-cache" http://localhost:8384/rangesWith/9/12/30 | jq`
7. To remove the RPM, run `sudo rpm --verbose --erase hours-distribution`

## Virtual box cleanup
1. Exit the VM by running `exit` in the terminal
2. Run `vagrant halt` to stop the VM
3. Run `vagrant destroy` to remove the VM from your host machine
4. Run `vagrant box remove bento/fedora-40` to remove the base box from your host machine
5. You can now delete the cloned repository from your host machine with `rm -rf vagrant_fedora`

## Notes
The jar file was copied from my other project on Github: [hours](https://github.com/totopoloco/hours)

## References
- https://www.vagrantup.com/docs/installation/
- https://gist.github.com/wpscholar/a49594e2e2b918f4d0c4
- https://www.virtualbox.org/wiki/Downloads
- https://rpm-packaging-guide.github.io/
- https://www.redhat.com/sysadmin/create-rpm-package

## License
This project is licensed under the MIT License for complete license see the [LICENSE](LICENSE) file.
