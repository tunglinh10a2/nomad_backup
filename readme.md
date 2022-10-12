# Nomad introduction

> This is the project from [Nomad](https://learn.hashicorp.com/tutorials/nomad/get-started-intro?in=nomad/get-started)


## Run project
```
vagrant up
```

## Access 

```
vagrant ssh default
```

## Copy config
```
cp /vagrant/example.nomad /home/vagrant/example.nomad
```

## Start the agent
```
cd /home/vagrant

sudo nomad agent -dev -bind 0.0.0.0 -log-level INFO
```

## Discover agent information
### Open new terminal session
```
nomad node status

nomad server members
```

## Init the job - no need
```
cd /home/vagrant

nomad job init
```

## Run a job

```
cd /home/vagrant

nomad job run example.nomad
```


## Nomad's web interface
```
http://localhost:4646
```
