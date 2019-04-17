#!/bin/bash
echo "DOCKER START"

docker start fervent_hypatia

docker exec -it fervent_hypatia /bin/bash run_classifier.sh

echo "DOCKER EXIT" 


