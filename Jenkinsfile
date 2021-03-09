pipeline {
    agent any
    environment {
        HOME="${WORKSPACE}"
        MIRAGE_DATA="/ifs/jwst/wit/mirage_data/"
        TEST_BIGDATA="https://bytesalad.stsci.edu/artifactory"
        CRDS_SERVER_URL = "https://jwst-crds.stsci.edu"
        CRDS_PATH = "/tmp/crds_cache"
        PATH ="${WORKSPACE}/miniconda3/bin:${PATH}"
        TMPDIR="${WORKSPACE}/tmp"
        XDG_CACHE_HOME="${WORKSPACE}/tmp/.cache"
    }
    stages{
        stage('Setup') {
            steps {
                deleteDir()
                checkout scm
                sh("mkdir -p tmp")
                sh("curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o installer.sh")
                sh("bash installer.sh -b -p ${WORKSPACE}/miniconda3")
                sh("conda config --set always_yes yes --set changeps1 no")
                sh("conda create -n simcal python -y")
            }
        }
        stage('Install') {
            steps {
                sh("""#!/usr/bin/env bash
                      source $WORKSPACE/miniconda/etc/profile.d/conda.sh
                      conda activate simcal

                      pip install -e .
                   """
                )
            }
        }
    }
}
