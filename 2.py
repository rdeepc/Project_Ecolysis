import http.client as ht

url = "https://mynasadata.larc.nasa.gov/las/UI.vm#panelHeaderHidden=false;differences=false;autoContour=false;xCATID=E1FDD4E311E8690B16343A398E1B9E92;xDSID=ocean_data;varid=l3m_data-id-f964a63f6d;imageSize=auto;over=xy;compute=Nonetoken;tlo=01-Aug-2011%2000:00;thi=01-Aug-2011%2000:00;catid=E1FDD4E311E8690B16343A398E1B9E92;dsid=ocean_data;varid=l3m_data-id-f964a63f6d;avarcount=0;xlo=-179.5;xhi=179.5;ylo=-89.5;yhi=89.5;operation_id=Plot_2D_XY_zoom;view=xy"
def save(filename, contents):
    fh = open(filename, 'w')
    fh.write(contents)
    fh.close()

conn = ht.HTTPConnection(url)
conn.request("HEAD", "/")
res = conn.getresponse()

save('t.txt', str(res))