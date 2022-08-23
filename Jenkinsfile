pipeline {
  agent any
  stages {
    stage('git clone') {
      steps {
        git 'https://github.com/tkap44/Project_Pt_3.git'
      }
    }
    stage('dependencies') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('backend') {
      steps {
        sh 'nohup python3 rest_app.py&'
      }
    }
    stage('backend testing') {
      steps {
        sh 'python3 backend_testing.py'
      }
    }
    stage('clean environment') {
      steps {
        sh 'python3 clean_environment.py'
      }
    }
  }
}
