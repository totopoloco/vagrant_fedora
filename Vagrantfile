Vagrant.configure("2") do |config|
  config.vm.box = "fedora/39-cloud-base"
  config.vm.box_version = "39.20231031.1"
  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"
  config.vbguest.auto_update = false

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "8192"
    vb.cpus = 2
    vb.customize ["modifyvm", :id, "--graphicscontroller", "vmsvga"]
  end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell" do |shell|
    shell.path = "provision.sh"
    #shell.args = "> /dev/null 2>&1"
  end
end