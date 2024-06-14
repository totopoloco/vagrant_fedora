Vagrant.configure("2") do |config|
  config.vm.box = "bento/fedora-40"
  config.vm.box_version = "202404.23.0"
  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"
  config.vm.boot_timeout = 600
  config.vbguest.auto_update = false
  #config.disksize.size = "40GB"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "8192"
    vb.cpus = 2
    vb.customize ["modifyvm", :id, "--graphicscontroller", "vmsvga"]
    vb.customize ["modifyvm", :id, "--vram", "16"]
    vb.customize ["modifyvm", :id, "--ioapic", "on"]
    vb.customize ["modifyvm", :id, "--clipboard", "bidirectional"]
    vb.customize ["modifyvm", :id, "--draganddrop", "bidirectional"]
  end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell" do |shell|
    shell.path = "provision.sh"
    #shell.args = "> /dev/null 2>&1"
  end
end
