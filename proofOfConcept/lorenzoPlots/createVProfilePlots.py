import numpy as np
import netCDF4
from shapely import geometry as g

from matplotlib import pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


def getAreas():
  # area1: north of the transect Senigallia-Lussino
  area1 = np.array([[13.214988194242391,43.71488987433399],
                    [14.472922764554891,44.52720675241598],
                    [14.378407729515418,45.98693995393536],
                    [11.510976088890418,45.99075659534529],
                    [11.48172225721503,44.012314751811424],
                    [13.214988194242391,43.71488987433399]])

  # area2: Giulianova-Kornati -> Senigallia-Lussino
  area2 = np.array([[13.978415260701151,42.74561800372274],
                    [15.300300608938056,43.796390392938676],
                    [15.226470896737583,46.284360605719726],
                    [14.36230694984787,46.03446597734454],
                    [14.474358346654807,44.53066046303087],
                    [13.215888663605107,43.71507179602531],
                    [13.78276761561759,42.773901970730925],
                    [13.978415260701151,42.74561800372274]])

  # area3: Vieste-Neum -> Giulianova-Kornati
  area3 = np.array([[16.17807359575388,41.880358739201576],
                    [17.622680495725003,42.918716250594116],
                    [17.08438249336298,44.08602279417732],
                    [15.29722405799489,43.797961450004905],
                    [13.977772485879703,42.74430555763478],
                    [14.776525693945553,41.740222562981394],
                    [16.17807359575388,41.880358739201576]])

  # area4: Otranto-Orikum -> Vieste-Neum
  area4 = np.array([[18.49042842979291,40.14196974120509],
                    [19.47370479698041,40.3264852221989],
                    [21.28644893760541,42.52154758734668],
                    [17.61683571717548,42.9225482844081],
                    [16.172264424962798,41.88432209047661],
                    [15.425342679184721,41.61178441460781],
                    [18.49042842979291,40.14196974120509]])

  areas = [area1, area2, area3, area4]
  areaNames = ['A', 'B', 'C', 'D']
  maxZ = [50, 100, 200, 1000]

  return areas, maxZ, areaNames



def plotAreas():
  areas, _, areaNames = getAreas()
  
  dsmsk = netCDF4.Dataset('adriaclimMask4Plot.nc')
  lon = dsmsk.variables['nav_lon'][:]
  lat = dsmsk.variables['nav_lat'][:]
  dsmsk.close()
  
  mp = np.zeros([2, lon.shape[0], lon.shape[1]])
  narea = len(areas)
  areaBaricenters = []
  for ia in range(narea):
    fld = np.ones(mp.shape)*(ia + 1)
    fld = crop3DMapOnPolygon(lon, lat, fld, areas[ia])
    fld[np.isnan(fld)] = 0
    mp += fld
    areaBaricenters.append(g.Polygon(areas[ia]).centroid.coords.xy)

  mp[mp==0] = np.nan
  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
  plt.pcolor(lon, lat, mp[0, :, :], cmap='Pastel1')
  for bc, areaName in zip(areaBaricenters, areaNames):
    plt.text(bc[0][0], bc[1][0], areaName, fontsize=14)

  ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor='w'))
  ax.coastlines()

  plt.title('Areas')
  



def crop3DMapOnPolygon(lon, lat, map3D, polygon):
  # polygon is given in form of [xcoordinates, ycoordinates]
  # assuming that map3D is (z, y, x)
  lonflatten = lon.flatten()
  latflatten = lat.flatten()
  pts = np.array([lonflatten, latflatten]).transpose()

  ply = g.Polygon(polygon)
  ncnt = np.vectorize(lambda p: ply.contains(g.Point(p)), signature='(n)->()')
  maskFlatten = ncnt(pts)
  mask = maskFlatten.reshape(lon.shape)

  nz = map3D.shape[0]
  mask_ = np.expand_dims(mask, 0)
  mask3D = mask_[np.zeros([nz]).astype(int), :, :]

  croppedMap3D = map3D.copy()
  croppedMap3D[~mask3D] = np.nan

  return croppedMap3D


def plotVerticalProfileFromNcFile(map3DNcFile, constName, itimes, area, maxZ, title, xlabel, legendlabels):
  dsmsk = netCDF4.Dataset('adriaclimMask4Plot.nc')
  lon = dsmsk.variables['nav_lon'][:]
  lat = dsmsk.variables['nav_lat'][:]
  z = dsmsk.variables['gdept_1d'][0,:]
  dsmsk.close()

  for itime in itimes:
    ds = netCDF4.Dataset(map3DNcFile)
    map3D = ds.variables[constName][itime,:]
    ds.close()
    map3D[map3D == 0] = np.nan
    map3D = crop3DMapOnPolygon(lon, lat, map3D, area)
    vprof = np.nanmean(map3D, axis=(1,2))
    vprof[z > maxZ] = 0
    cnd = vprof > 0
    plt.plot(vprof[cnd], -z[cnd], label=legendlabels[itime])

  plt.ylabel('depth (m)')
  plt.xlabel(xlabel)
  plt.title(title)
  plt.legend()
  plt.tight_layout()
  
  
def plotAllProfiles(map3DNcFile):
  plotAreas()
  plt.savefig('vprof_aaa_areas.png')
  plt.close('all')

  areas, maxZs, areaNames = getAreas()
  narea = len(areaNames)
  times = [0, 1]
  timedescrs = ['Winter 2019', 'Summer 2019']
  timeshortdescrs = ['winter', 'summer']
  ntm = len(times)
  constNames = ['Chla', 'O2o', 'N1p', 'N3n', 'R1c']
  constDescrs = ['Chlorophyll a', '$O_2$', '$PO_4$', '$NO_3$', 'Labile Dissolved Organic Matter']
  constUnits = ['$mg\ m^{{-3}}$', '$mmol\ m^{{-3}}$', '$mmol\ m^{{-3}}$', '$mmol\ m^{{-3}}$', '$mmol\ m^{{-3}}$']
  nconst = len(constNames)
  for ia in range(narea):
    for icnst in range(nconst):
      area = areas[ia]
      maxZ = maxZs[ia]
      areaName = areaNames[ia]
      constName = constNames[icnst]
      constDescr = constDescrs[icnst]
      constUnit = constUnits[icnst]
      xlabel = f"{constDescr} ({constUnit})" 
      title = f"area {areaName}, {constDescr}"
      fname = f"vprof_area={areaName}_{constName}.png"
      print("generating file " + fname)

      plotVerticalProfileFromNcFile(map3DNcFile, constName, times, area, maxZ, title, xlabel, timeshortdescrs)
      
      plt.savefig(fname)
      plt.close('all')
  

