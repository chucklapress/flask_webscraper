pipeline {
  agent { docker { image 'python:2.7.17' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
            agent {
                docker {
                    image 'ython:2.7.17'
                }
            }
            steps {
                sh 'python test_basic.py'
            }

        }
    }
}
