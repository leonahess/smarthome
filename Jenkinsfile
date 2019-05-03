pipeline {
  agent any
  stages {
    stage("Build Containers") {
      parallel {
        stage('Build HS110') {
          agent {
            label "Pi_3"
          }
          steps {
            sh "docker build -t hs110 hs110/"
          }
        }
        stage('Build DHT22') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker build -t dht22 dht22/"
          }
        }
        stage('Build DS18B20') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker build -t ds18b20 ds18b20/"
          }
        }
      }
    }
    stage("Tag Images"){
      parallel{
        stage('Tag HS110') {
          agent {
            label "Pi_3"
          }
          steps {
            sh "docker tag hs110 fx8350:5000/hs110:latest"
            sh "docker tag hs110 fx8350:5000/hs110:${env.BUILD_NUMBER}"
            sh "docker tag hs110 leonhess/hs110:latest"
            sh "docker tag hs110 leonhess/hs110:${env.BUILD_NUMBER}"
          }
        }
        stage('Tag DHT22') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker tag dht22 fx8350:5000/dht22:latest"
            sh "docker tag dht22 fx8350:5000/dht22:${env.BUILD_NUMBER}"
            sh "docker tag dht22 leonhess/dht22:latest"
            sh "docker tag dht22 leonhess/dht22:${env.BUILD_NUMBER}"
          }
        }
        stage('Tag DS18B20') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker tag ds18b20 fx8350:5000/ds18b20:latest"
            sh "docker tag ds18b20 fx8350:5000/ds18b20:${env.BUILD_NUMBER}"
            sh "docker tag ds18b20 leonhess/ds18b20:latest"
            sh "docker tag ds18b20 leonhess/ds18b20:${env.BUILD_NUMBER}"
          }
        }
      }
    }
    stage('Push to Local Registry') {
      parallel {
        stage('Push HS110 local') {
          agent {
            label "Pi_3"
          }
          steps {
            sh "docker push fx8350:5000/hs110:latest"
            sh "docker push fx8350:5000/hs110:${env.BUILD_NUMBER}"
          }
        }
        stage('Push DHT22 local') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker push fx8350:5000/dht22:latest"
            sh "docker push fx8350:5000/dht22:${env.BUILD_NUMBER}"
          }
        }
        stage('Push DS18B20 local') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker push fx8350:5000/ds18b20:latest"
            sh "docker push fx8350:5000/ds18b20:${env.BUILD_NUMBER}"
          }
        }
      }
    }
    stage('Push to DockerHub') {
      parallel {
        stage('Push HS110 DockerHub') {
          agent {
            label "Pi_3"
          }
          steps {
            withDockerRegistry([credentialsId: "dockerhub", url: ""]) {
              sh "docker push leonhess/hs110:latest"
              sh "docker push leonhess/hs110:${env.BUILD_NUMBER}"
            }
          }
        }
        stage('Push DHT22 DockerHub') {
          agent {
            label "Pi_Zero"
          }
          steps {
            withDockerRegistry([credentialsId: "dockerhub", url: ""]) {
              sh "docker push leonhess/dht22:latest"
              sh "docker push leonhess/dht22:${env.BUILD_NUMBER}"
            }
          }
        }
        stage('Push DS18B20 DockerHub') {
          agent {
            label "Pi_Zero"
          }
          steps {
            withDockerRegistry([credentialsId: "dockerhub", url: ""]) {
              sh "docker push leonhess/ds18b20:latest"
              sh "docker push leonhess/ds18b20:${env.BUILD_NUMBER}"
            }
          }
        }
      }
    }
    stage("Cleanup"){
      parallel {
        stage('Cleanup HS110') {
          agent {
            label "Pi_3"
          }
          steps {
            sh "docker rmi fx8350:5000/hs110"
            sh "docker rmi leonhess/hs110"
          }
        }
        stage('Cleanup DS18B20') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker rmi fx8350:5000/ds18b20"
            sh "docker rmi leonhess/ds18b20"
          }
        }
        stage('Cleanup DHT22') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker rmi fx8350:5000/dht22"
            sh "docker rmi leonhess/dht22"
          }
        }
      }
    }
  }
}
