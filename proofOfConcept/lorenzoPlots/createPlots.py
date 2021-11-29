import numpy as np
import netCDF4

from matplotlib import pyplot as plt
from matplotlib import gridspec
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from sklearn.neighbors import NearestNeighbors

  

def plotHorizontalVelocity(lon, lat, U, V, title, maxval=None, zoomArea=None, quiverSkip=7):
  fig = plt.figure(figsize=(8, 6))
  ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
  uh = np.sqrt((U**2 + V**2))
 #maxval = np.nanpercentile(uh[uh>0], 99.5) if maxval is None else maxval 
  maxval = np.nanmax(uh) if maxval is None else maxval 
  maxval = maxval + 1e-7
 #uabslevels = np.linspace(0, maxval, 51)
 #plt.contourf(lon, lat, uh, cmap='rainbow', levels=uabslevels)
  plt.pcolor(lon, lat, uh, cmap='rainbow')
  cbar = plt.colorbar()
  cbar.set_label("currents (m/s)")
  skip=(slice(None,None,quiverSkip),slice(None,None,quiverSkip))
  uqvr, vqvr = U/uh, V/uh
  plt.quiver(lon[skip], lat[skip], uqvr[skip], vqvr[skip], scale=60, width=.0015)
  ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor='w'))
  ax.coastlines()
  if not zoomArea is None:
    ax.set_extent(zoomArea)
  plt.title(title)
  plt.tight_layout()



def plotHorzVelocitiesFromNc(itime, idepth, title,
      uncflpth='BFM_1d_2019_grid_U_seasavg.nc',
      vncflpth='BFM_1d_2019_grid_V_seasavg.nc',
      wncflpth='BFM_1d_2019_grid_W_seasavg.nc',
      **kwargs):
  dsu = netCDF4.Dataset(uncflpth)
  dsv = netCDF4.Dataset(vncflpth)
  dsw = netCDF4.Dataset(wncflpth)
  dsmsk = netCDF4.Dataset('adriaclimMask4Plot.nc')
  
  uocetr = dsu.variables['uocetr_eff'][itime, :]
  vocetr = dsv.variables['vocetr_eff'][itime, :]
  wocetr = dsw.variables['wocetr_eff'][itime, :]
  
  lon = dsmsk.variables['nav_lon'][:]
  lat = dsmsk.variables['nav_lat'][:]
  
  nz = uocetr.shape[0]
  zindx = np.zeros((nz)).astype(int)
  e2u = dsmsk.variables['e2u'][:]
  e2u = e2u[zindx,:,:]
  e1v = dsmsk.variables['e1v'][:]
  e1v = e1v[zindx,:,:]
  e3u_0 = dsmsk.variables['e3u_0'][:].squeeze()
  e3v_0 = dsmsk.variables['e3v_0'][:].squeeze()
  e1t = dsmsk.variables['e1t'][:]
  e1t = e1t[zindx,:,:]
  e2t = dsmsk.variables['e2t'][:]
  e2t = e2t[zindx,:,:]
  e1e2t = e1t*e2t

  dsu.close()
  dsv.close()
  dsw.close()
  dsmsk.close()
  
  u = uocetr/e2u/e3u_0
  v = vocetr/e1v/e3v_0
  w = wocetr/e1e2t

  ttl = 'itime=' + str(itime).zfill(3) + '; idepth=' + str(idepth).zfill(3)  

  plt.close('all')

  plotHorizontalVelocity(lon, lat, u[idepth], v[idepth], title, **kwargs)

  

def plotVerticalVelocity(lon, lat, W, title, maxval=None, zoomArea=None):
  fig = plt.figure(figsize=(8, 6))
  ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
  maxval = np.nanmax(np.abs(W)) if maxval is None else maxval 
  maxval = maxval + 1e-7
 #uabslevels = np.linspace(-maxval, maxval, 51)
 #plt.contourf(lon, lat, W, cmap='rainbow', levels=uabslevels)
  plt.pcolor(lon, lat, W, cmap='rainbow')
  cbar = plt.colorbar()
  cbar.set_label("vertical velocity (m/s)")
  ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor='w'))
  ax.coastlines()
  if not zoomArea is None:
    ax.set_extent(zoomArea)
  plt.title(title)
  plt.tight_layout()



def plotVertVelocitiesFromNc(itime, idepth, title,
      uncflpth='BFM_1d_2019_grid_U_seasavg.nc',
      vncflpth='BFM_1d_2019_grid_V_seasavg.nc',
      wncflpth='BFM_1d_2019_grid_W_seasavg.nc',
      **kwargs):
  dsu = netCDF4.Dataset(uncflpth)
  dsv = netCDF4.Dataset(vncflpth)
  dsw = netCDF4.Dataset(wncflpth)
  dsmsk = netCDF4.Dataset('mask.nc')
  
  uocetr = dsu.variables['uocetr_eff'][itime, :]
  vocetr = dsv.variables['vocetr_eff'][itime, :]
  wocetr = dsw.variables['wocetr_eff'][itime, :]
  
  lon = dsw.variables['nav_lon'][:]
  lat = dsw.variables['nav_lat'][:]
  
  nz = uocetr.shape[0]
  zindx = np.zeros((nz)).astype(int)
  e2u = dsmsk.variables['e2u'][:]
  e2u = e2u[zindx,:,:]
  e1v = dsmsk.variables['e1v'][:]
  e1v = e1v[zindx,:,:]
  e3u_0 = dsmsk.variables['e3u_0'][:].squeeze()
  e3v_0 = dsmsk.variables['e3v_0'][:].squeeze()
  e1t = dsmsk.variables['e1t'][:]
  e1t = e1t[zindx,:,:]
  e2t = dsmsk.variables['e2t'][:]
  e2t = e2t[zindx,:,:]
  e1e2t = e1t*e2t

  dsu.close()
  dsv.close()
  dsw.close()
  dsmsk.close()
  
  u = uocetr/e2u/e3u_0
  v = vocetr/e1v/e3v_0
  w = wocetr/e1e2t

  ttl = 'itime=' + str(itime).zfill(3) + '; idepth=' + str(idepth).zfill(3)  

  plt.close('all')

  plotVerticalVelocity(lon, lat, w[idepth], title, **kwargs)
  
  


def plotConstituentMap(lon, lat, U, V, constituent, title, quiverVelocityModule=False, quiverSkip=7, zoomArea=None, maxval=None, minval=0, nlevs=51,
       cmap='rainbow', cbticks=None, units='$mmol\ m^{-3}$'):
  fig = plt.figure(figsize=(7.5, 6))
  gs = gridspec.GridSpec(1, 2, width_ratios=[1,.03])
  ax = plt.subplot(gs[0], projection=ccrs.PlateCarree())
  uh = np.sqrt((U**2 + V**2))
  if maxval is None:
    maxval = np.nanpercentile(constituent[constituent != 0], 99.5)
    maxval = .01 if maxval==0 else maxval
  lvl = np.linspace(minval, maxval, nlevs)
  constituent[constituent >= maxval] = maxval*(1-1e-7)
  plt.contourf(lon, lat, constituent, cmap=cmap, levels=lvl)
  cax = plt.subplot(gs[1])
  cbar = plt.colorbar(cax=cax)
  cbar.set_label(f"Concentration ({units})")
  if not cbticks is None:
    cbar.set_ticks(cbticks)
  plt.axes(ax)
  skip=(slice(None,None,quiverSkip),slice(None,None,quiverSkip))
  if quiverVelocityModule:
    uqvr, vqvr = U, V
  else:
    uqvr, vqvr = U/uh, V/uh
  plt.quiver(lon[skip], lat[skip], uqvr[skip], vqvr[skip], scale=60, width=.0015)
  ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor='w'))
  ax.coastlines()
  plt.title(title)
  if not zoomArea is None:
    ax.set_extent(zoomArea)
  ax.set_aspect('auto')
  cax.set_aspect('auto')
  plt.tight_layout()
  
  


def plotConstituentPcolor(lon, lat, constituent, title, quiverVelocityModule=False, zoomArea=None):
  fig = plt.figure(figsize=(8, 6))
  ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
  plt.pcolor(lon, lat, constituent, cmap='rainbow')
  cbar = plt.colorbar()
  cbar.set_label("Concentration ($mmol\ m^{-3}$)")
  ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor='w'))
  ax.coastlines()
  plt.title(title)
  if not zoomArea is None:
    ax.set_extent(zoomArea)
  plt.tight_layout()




def plotConstituentAtSsnAndDepth(itime, idepth, constVar, title,
      uncflpth='BFM_1d_2019_grid_U_seasavg.nc',
      vncflpth='BFM_1d_2019_grid_V_seasavg.nc',
      cncflpth='BFM_1d_2019_grid_bfm_seasavg.nc',
      **kwargs):
  dsu = netCDF4.Dataset(uncflpth)
  dsv = netCDF4.Dataset(vncflpth)
  dsc = netCDF4.Dataset(cncflpth)
  dsmsk = netCDF4.Dataset('mask.nc')
  
  uocetr = dsu.variables['uocetr_eff'][itime, :]
  vocetr = dsv.variables['vocetr_eff'][itime, :]
  const = dsc.variables[constVar][itime, :]
  const[const > 1e19] = np.nan
  
  lon = dsmsk.variables['nav_lon'][:]
  lat = dsmsk.variables['nav_lat'][:]
  
  nz = uocetr.shape[0]
  zindx = np.zeros((nz)).astype(int)
  e2u = dsmsk.variables['e2u'][:]
  e2u = e2u[zindx,:,:]
  e1v = dsmsk.variables['e1v'][:]
  e1v = e1v[zindx,:,:]
  e3u_0 = dsmsk.variables['e3u_0'][:].squeeze()
  e3v_0 = dsmsk.variables['e3v_0'][:].squeeze()
  e1t = dsmsk.variables['e1t'][:]
  e1t = e1t[zindx,:,:]
  e2t = dsmsk.variables['e2t'][:]
  e2t = e2t[zindx,:,:]
  e1e2t = e1t*e2t

  dsu.close()
  dsv.close()
  dsc.close()
  dsmsk.close()
  
  u = uocetr/e2u/e3u_0
  v = vocetr/e1v/e3v_0

  plotConstituentMap(lon, lat, u[idepth], v[idepth], const[idepth], title, **kwargs)

 #plt.savefig(('uhorz_abs_' + ttl + '.png').replace(' ', '_'), dpi=300)



def plotConstituentAtTimeAndDepth(itime, idepth, constVar, title, 
    uncflpth='BFM_1d_20190101_20190105_grid_U.nc', 
    vncflpth='BFM_1d_20190101_20190105_grid_V.nc', 
    cncflpth='BFM_1d_20190101_20190105_grid_bfm.nc',
    **kwargs):
  dsu = netCDF4.Dataset(uncflpth)
  dsv = netCDF4.Dataset(vncflpth)
  dsc = netCDF4.Dataset(cncflpth)
  dsmsk = netCDF4.Dataset('mask.nc')
  
  uocetr = dsu.variables['uocetr_eff'][itime, :]
  vocetr = dsv.variables['vocetr_eff'][itime, :]
  const = dsc.variables[constVar][itime, :]
  
  lon = dsc.variables['nav_lon'][:]
  lat = dsc.variables['nav_lat'][:]
  
  nz = uocetr.shape[0]
  zindx = np.zeros((nz)).astype(int)
  e2u = dsmsk.variables['e2u'][:]
  e2u = e2u[zindx,:,:]
  e1v = dsmsk.variables['e1v'][:]
  e1v = e1v[zindx,:,:]
  e3u_0 = dsmsk.variables['e3u_0'][:].squeeze()
  e3v_0 = dsmsk.variables['e3v_0'][:].squeeze()
  e1t = dsmsk.variables['e1t'][:]
  e1t = e1t[zindx,:,:]
  e2t = dsmsk.variables['e2t'][:]
  e2t = e2t[zindx,:,:]
  e1e2t = e1t*e2t

  dsu.close()
  dsv.close()
  dsc.close()
  dsmsk.close()
  
  u = uocetr/e2u/e3u_0
  v = vocetr/e1v/e3v_0

  plotConstituentMap(lon, lat, u[idepth], v[idepth], const[idepth], title, **kwargs)



def plotConstituentPcolorAtTimeAndDepth(itime, idepth, constVar, title, cncflpth='BFM_1d_20190101_20190105_grid_bfm.nc', **kwargs):
  dsc = netCDF4.Dataset(cncflpth)
  
  const = dsc.variables[constVar][itime, :]
  
  lon = dsc.variables['nav_lon'][:]
  lat = dsc.variables['nav_lat'][:]

  dsc.close()

  plotConstituentPcolor(lon, lat, const[idepth], title, **kwargs)
  


def plotSeasonsAtDepths():
  seasonTimeIndexes = np.arange(2)
  seasonNames = ['Winter', 'Spring', 'Summer', 'Autumn']
  seasonNames = ['Winter', 'Summer']
  depthMeters = np.array([0, 10, 20, 40, 100, 200, 500, 1000])
  prototypeFl = 'BFM_1d_2019_grid_W_seasavg.nc'
  ds = netCDF4.Dataset(prototypeFl)
  dpth = ds.variables['depthw'][:]
  ds.close()

  knn = NearestNeighbors(n_neighbors=1)
  knn.fit(np.array([dpth]).transpose())
  dist, indxs = knn.kneighbors(np.array([depthMeters]).transpose())
  indxs = indxs.squeeze()

  for iseason in seasonTimeIndexes:
    ssnm = seasonNames[iseason]
    for idepthOut in range(len(depthMeters)):
      dpt = depthMeters[idepthOut]
      idepth = indxs[idepthOut]
      ttl = ssnm + ', ' + str(dpt) + ' m depth'
      print('  plotting ' + ttl)
      plt.close('all')
      plotHorzVelocitiesFromNc(iseason, idepth, 'Currents: ' + ttl)
      plt.savefig('currents_' + ssnm + '_depth=' + str(dpt).zfill(4) + '.png')
      plotConstituentAtSsnAndDepth(iseason, idepth, 'N1p', 'PO4: ' + ttl)
      plt.savefig('N1p_' + ssnm + '_depth=' + str(dpt).zfill(4) + '.png')
      plotConstituentAtSsnAndDepth(iseason, idepth, 'N3n', 'NO3: ' + ttl)
      plt.savefig('N3n_' + ssnm + '_depth=' + str(dpt).zfill(4) + '.png')
      plotConstituentAtSsnAndDepth(iseason, idepth, 'Chla', 'Chlorophille: ' + ttl)
      plt.savefig('Chla_' + ssnm + '_depth=' + str(dpt).zfill(4) + '.png')
  
  
if __name__ == '__main__':
  plotSeasonsAtDepths()

