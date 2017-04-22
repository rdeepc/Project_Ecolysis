from selenium import webdriver

url="https://mynasadata.larc.nasa.gov/las/UI.vm#panelHeaderHidden=false;differences=false;autoContour=false;globalMin=-0.339;globalMax=32.767;xCATID=E1FDD4E311E8690B16343A398E1B9E92;xDSID=ocean_data;varid=sea_level-id-cd469260cd;imageSize=auto;over=xy;compute=Nonetoken;tlo=04-Oct-1992%2000:00;thi=04-Oct-1992%2000:00;catid=E1FDD4E311E8690B16343A398E1B9E92;dsid=ocean_data;varid=sea_level-id-cd469260cd;avarcount=0;xlo=0.5;xhi=359.5;ylo=-89.5;yhi=89.5;operation_id=Plot_2D_XY_zoom;view=xy"
browser = webdriver.Firefox(executable_path=r'H:\soft\anacondapython\New folder\geckodriver.exe')
browser.get(url)
html_source = browser.page_source

def save(filename, contents):
    fh = open(filename, 'w')
    fh.write(contents)
    fh.close()

save('t.txt', str(html_source))