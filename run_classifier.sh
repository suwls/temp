# !bin/bash




echo "variable test" 


a=$(/root/openface/demos/classifier_test.py infer /root/openface/embedding/us/classifier.pkl /root/openface/test/us/test1.jpeg)




echo "a variable running finished"
# /root/openface/demos/classifier_test.py infer /root/openface/embedding/us/classifier.pkl /root/openface/test/us/test1.jpeg
#echo "just run"

echo "print a"
echo ${a}
echo $a
