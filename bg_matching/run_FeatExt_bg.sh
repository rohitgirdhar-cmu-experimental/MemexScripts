CODE_PATH=/home/rgirdhar/data/Work/Code/0001_FeatureExtraction/ComputeFeatures/Features/CNN/ver2/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${CODE_PATH}/../external/caffe/build/lib/
GLOG_logtostderr=0 ${CODE_PATH}/computeFeatures.bin \
    -i /home/rgirdhar/memexdata/Dataset/processed/0001_Backpage/Images/corpus \
    -q /home/rgirdhar/memexdata/Dataset/processed/0001_Backpage/Images/lists/Images.txt \
    -n ${CODE_PATH}/../deploy_memexgpu.prototxt \
    -m /home/rgirdhar/data/Software/vision/caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel \
    -l pool5 \
    -s \
    -x /home/rgirdhar/memexdata/Dataset/processed/0001_Backpage/Features/Segment/segResults \
    -o /home/rgirdhar/memexdata/Dataset/processed/0001_Backpage/Features/CNN/pool5_bg_normed \
    -y \
    -t lmdb \
    -p avg 
