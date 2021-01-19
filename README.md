# ERBS-DB-Client

sudo docker build -t erbsImg1 .

sudo docker run -it --name erbsCon1 --volume=$(pwd):/erbs erbsImg1
