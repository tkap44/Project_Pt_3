pipeline {
  agent any
  stages {
    tage('flask') {
      steps {
        sh 'pip install flask'
      }
    }
    stage('backend') {
      steps {
        sh 'python3 rest_app.py'
      }
    }
    stage('frontend') {
      steps {
        sh 'python3 web_app.py'
      }
    }
    stage('backend testing') {
      steps {
        sh 'python3 backend_testing.py'
      }
    }
    stage('frontend testing') {
      steps {
        sh 'python3 frontend_testing.py'
      }
    }
    stage('combined testing') {
      steps {
        sh 'python3 combined_testing.py'
      }
    }
    stage('clean environment') {
      steps {
        sh 'python3 clean_environment.py'
      }
    }
  }
}
