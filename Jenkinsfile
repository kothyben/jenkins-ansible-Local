pipeline{
    agent any
    stages{
        stage("SCM checkout"){
            steps{
                git ' https://github.com/kothyben/jenkins-ansible-Local.git'
            }
        }
        
        stage("execute playbook ping"){
            steps{
               ansiblePlaybook credentialsId: 'Private_SSH_Jenkins_Ubuntu_Local', disableHostKeyChecking: true, installation: 'ansible', inventory: 'hosts', playbook: 'pingToHosts.yaml'
            }
        }
        
        stage("create text file"){
            steps{
                ansiblePlaybook credentialsId: 'Private_SSH_Jenkins_Ubuntu_Local', disableHostKeyChecking: true, installation: 'ansible', inventory: 'hosts', playbook: 'type.yaml'
            }
        }
    }
    }
        
