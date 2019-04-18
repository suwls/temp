# !bin/bash




echo "Face Recognition Start"

#for i in 1 2 3
#do 

#	a=$(/root/openface/demos/classifier_test.py infer /root/openface/embedding/us/classifier.pkl /root/openface/temp/test_$i.png)

#	echo $a
#done
python3 /root/openface/temp/receiveImage2.py


echo "Face Recognition Finished"



echo "Recognition Result"

echo $a
