BASE_PATH=/home/rgirdhar/data/Work/Code/0001_FeatureExtraction/ComputeFeatures/Features/CNN
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${BASE_PATH}/external/caffe/build/lib/:/home/rgirdhar/data/Software/cpp/zeromq/install/lib/
CODE_DIR=/srv2/rgirdhar/Work/Code/0002_Retrieval/Try/ScalableLSH/Deploy/
GLOG_logtostderr=1 $CODE_DIR/computeFeatAndSearch.bin \
    -n $CODE_DIR/deploy.prototxt \
    -m /home/rgirdhar/data/Software/vision/caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel \
    -l pool5 \
    -i /home/rgirdhar/memexdata/Dataset/processed/0006_BackpageExtended/Search/indexes/fullImg_ITQ_256bit.index \
    -s /home/rgirdhar/memexdata/Dataset/processed/0006_BackpageExtended/Features/CNN/pool5_normed \
    --imgslist /home/rgirdhar/memexdata/Dataset/processed/0006_BackpageExtended/Images/lists/Images.txt
