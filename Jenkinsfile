pipeline {
  agent docker
  stages {
  stage("Environment") {
    steps {
    sh "git --version"
  }
}
  stage("Build Containers") {
    steps {
      parallel (
        hs110: {
          sh "docker build -t hs110 hs110/"
        },
        ds18b20: {
          sh "docker build -t ds18b20 ds18b20/"
        },
        dht22: {
          sh "docker build -t dht22 dht22/"
        }
      )
    }
  }
  stage("Tag & Push to Registry"){
    steps {
      parallel (
        hs110: {
          sh "docker tag hs110 localhost:5000/hs110"
          sh "docker push hs110 localhost:5000/hs110"
          },
        ds18b20: {
          sh "docker tag ds18b20 localhost:5000/ds18b20"
          sh "docker push ds18b20 localhost:5000/ds18b20"
          },
        dht22: {
          sh "docker tag dht22 localhost:5000/dht22"
          sh "docker push dth22 localhost:5000/dht22"
        }
      )
    }
  }
  stage("Cleanung"){
    steps {
    sh "docker rmi dht22"
    sh "docker rmi ds18b20"
    sh "docker rmi hs110"
  }
}
}
}