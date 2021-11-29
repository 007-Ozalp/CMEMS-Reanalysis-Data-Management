cdo=/users_home/opa/lm09621/usr/menta_cdo.sh

echo "merging BFM files"
$cdo mergetime BFM_1d_*_bfm.nc BFM_1d_2019_bfm_merged.nc > merge_bfm.log 2>&1 &

echo "merging U files"
$cdo mergetime BFM_1d_*_U.nc BFM_1d_2019_U_merged.nc > merge_U.log 2>&1 &

echo "merging V files"
$cdo mergetime BFM_1d_*_V.nc BFM_1d_2019_V_merged.nc > merge_V.log 2>&1 &

echo "merging W files"
$cdo mergetime BFM_1d_*_W.nc BFM_1d_2019_W_merged.nc > merge_W.log 2>&1 &

wait




