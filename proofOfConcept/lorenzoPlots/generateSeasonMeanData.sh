cdo=/users_home/opa/lm09621/usr/menta_cdo.sh

$cdo -yearavg -select,season=JASO BFM_1d_2019_U_merged.nc BFM_JJAS_avg_U.nc &
$cdo -yearavg -select,season=JFMA BFM_1d_2019_U_merged.nc BFM_JFMA_avg_U.nc &

$cdo -yearavg -select,season=JASO BFM_1d_2019_V_merged.nc BFM_JJAS_avg_V.nc &
$cdo -yearavg -select,season=JFMA BFM_1d_2019_V_merged.nc BFM_JFMA_avg_V.nc &

$cdo -yearavg -select,season=JASO BFM_1d_2019_W_merged.nc BFM_JJAS_avg_W.nc &
$cdo -yearavg -select,season=JFMA BFM_1d_2019_W_merged.nc BFM_JFMA_avg_W.nc &

$cdo -yearavg -select,season=JASO BFM_1d_2019_bfm_merged.nc BFM_JJAS_avg_bfm.nc &
$cdo -yearavg -select,season=JFMA BFM_1d_2019_bfm_merged.nc BFM_JFMA_avg_bfm.nc &

wait

$cdo mergetime BFM_JFMA_avg_U.nc BFM_JJAS_avg_U.nc BFM_1d_2019_grid_U_seasavg.nc
$cdo mergetime BFM_JFMA_avg_V.nc BFM_JJAS_avg_V.nc BFM_1d_2019_grid_V_seasavg.nc
$cdo mergetime BFM_JFMA_avg_W.nc BFM_JJAS_avg_W.nc BFM_1d_2019_grid_W_seasavg.nc
$cdo mergetime BFM_JFMA_avg_bfm.nc BFM_JJAS_avg_bfm.nc BFM_1d_2019_grid_bfm_seasavg.nc

