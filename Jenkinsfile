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
  stage("Tag & Push to Registry"){
      parallel{
        stage('Tag HS110') {
          agent {
            label "Pi_3"
          }
          steps {
            sh "docker tag hs110 fx8350:5000/hs110"
            sh "docker push hs110 fx8350:5000/hs110"
          }
        }
        stage('Tag DHT22') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker tag dht22 fx8350:5000/dht22"
            sh "docker push dth22 fx8350:5000/dht22"
          }
        }
        stage('Tag DS18B20') {
          agent {
            label "Pi_Zero"
          }
          steps {
            sh "docker tag ds18b20 fx8350:5000/ds18b20"
            sh "docker push ds18b20 fx8350:5000/ds18b20"
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
          sh "docker rmi hs110"
        }
      }
      stage('Cleanup DS18B20') {
        agent {
          label "Pi_Zero"
        }
        steps {
          sh "docker rmi ds18b20"
        }
      }
      stage('Cleanup DHT22') {
        agent {
          label "Pi_Zero"
        }
        steps {
          sh "docker rmi dht22"
        }
      }
    }
  }
}
