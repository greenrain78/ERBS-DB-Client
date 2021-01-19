# ERBS-DB-Client

sudo docker build -t erbs_img1 .

sudo docker run -it --name erbs_con1 --volume=$(pwd):/erbs erbs_img1
