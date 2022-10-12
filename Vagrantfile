# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure(2) do |config|
  config.vm.define "nomad-server" do |nomad|
    nomad.vm.box = "bento/ubuntu-22.04" # 22.04 LTS, Jammy
    nomad.vm.hostname = "nomad"
  
    # Expose the nomad api and ui to the host
    nomad.vm.network "forwarded_port", guest: 4646, host: 4646
  
    # Increase memory for Virtualbox
    nomad.vm.provider "virtualbox" do |vb|
          vb.memory = "1024"
          vb.cpus = 4
    end
  
    nomad.vm.provision :shell, path: "install_nomad.sh"

    nomad.vm.synced_folder "nomad-backup/", "/opt/nomad-backup"
  end
end