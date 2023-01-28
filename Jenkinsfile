pipeline {
  agent any
  stages{ 
    stage('Create Staging branch'){
      steps{
        echo 'Create Staging branch'
        sh 'git branch --delete staging'
        sh 'git branch staging'
        sh 'git checkout dev'
        sh 'git pull'
        sh 'git push origin staging'
      }
    }
    stage('build'){
      steps{
        sh 'pip install -r requirements.txt'
      } 
    }
    stage('test'){
      steps{
        sh 'python test_main.py'
      }
    } 
    stage('deploy'){
      steps{
        sh 'docker login --username=alixs --password=zD96ZkxqGWRHd5c'
        sh 'docker build -t tp-jenkinsFlask .'
        sh 'docker tag tp-jenkinsFlask alixs/tp-jenkinsFlask:v1.0'
        sh 'docker push alixs/tp-jenkinsFlask:v1.0'
      }
    }
    stage('merge to main'){
      steps{
        sh 'git checkout main'
        sh 'git pull origin main'
        sh 'git merge origin/staging'
        sh 'git push origin main'
      } 
    }  
  } 
}
