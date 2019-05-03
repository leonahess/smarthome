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
    stage("Tag & Push to Registry"){
      parallel{
        stage('Tag HS110') {
          agent {
            label "Pi_3"
          }
          steps {
            sh "docker tag hs110 fx8350:5000/hs110:latest"
            sh "docker push fx8350:5000/hs110:latest"
          }
        }
        stage('Tag DHT22') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker tag dht22 fx8350:5000/dht22:latest"
            sh "docker push fx8350:5000/dht22:latest"
          }
        }
        stage('Tag DS18B20') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker tag ds18b20 fx8350:5000/ds18b20:latest"
            sh "docker push fx8350:5000/ds18b20:latest"
          }
        }
      }
    }
    stage("Cleanup"){
      parallel {
        stage('Cleanup HS110') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker rmi fx8359:5000/hs110"
          }
        }
        stage('Cleanup DS18B20') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker rmi fx8359:5000/ds18b20"
          }
        }
        stage('Cleanup DHT22') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker rmi fx8359:5000/dht22"
          }
        }
      }
    }
  }
}
