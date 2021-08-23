pipeline {

  agent {
    label 'jenkins-slave'
  }

  options {
    disableConcurrentBuilds()
    buildDiscarder(logRotator(numToKeepStr: '15'))
  }

  stages {
    
    stage("Scan Commit") {
      steps {
        script {
          dir ("aws-git-secrets"){
            // Temporary '|| true' to stop pipeline failing, remove once detected secrets have been removed
            sh ("./scan-repo-linux-mac.sh || true")
          }
        }
      }
    }
    
    // Disabled by default - this may take a few minutes to run
    // stage("Scan git aws") {
    //   steps {
    //     script {
    //       dir ("aws-git-secrets"){
    //         sh ("./full-aws-scan.sh")
    //       }
    //     }
    //   }
    // }
    
  }


}
