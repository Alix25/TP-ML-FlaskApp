pipeline {
  agent any
  stages{ 
    stage('Create Staging branch'){
      steps{
        echo 'Create Staging branch'
        bat 'git checkout dev'
        bat 'git pull'
        bat 'git checkout -b staging'
        // withCredentials([usernamePassword(credentialsId: 'github', usernameVariable: 'Alix25', passwordVariable: 'ToTheStars33')]) {
        //   script {
        //       bat 'git push --set-upstream origin staging' 
        //   }
        // }
      }
    }
    stage('build'){
      steps{
        bat 'pip install -r requirements.txt'
      } 
    } 
    stage('test'){
      steps{
        bat 'python test_main.py'
      } 
    } 
    stage('deploy'){
      steps{
        bat 'docker login --username=alixs --password=zD96ZkxqGWRHd5c'
        bat 'docker build -t tp-jenkinsflask .'
        bat 'docker tag tp-jenkinsflask alixs/tp-jenkinsflask:v1.0'
        bat 'docker push alixs/tp-jenkinsflask:v1.0'
      }
    }
    stage('merge to main'){
      steps{
        bat 'git config --global user.email "alix.stirling@efrei.net"'
        bat 'git config --global user.name "Alix25"'
        bat 'git checkout main'
        bat 'git pull origin main'
        bat 'git merge origin/dev'  
        //bat 'git push origin main' 
      } 
    }  
  } 
}
