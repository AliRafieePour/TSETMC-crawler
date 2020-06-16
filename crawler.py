from Dependecies import *


def init(Filter):
    print('crawler called!')
    
    S18 = ""
    scripts = {
    'S11': "mw.Settings.LoadInstHistory=1-mw.Settings.LoadInstHistory;mw.SaveParams();HideAllWindow();mw.LoadInstHistory();mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();mw.Settings.Filters.push({FilterCode: '(pe)<0 0 < (pe) && (pe) < 5'});mw.SelectFilter(0);mw.ShowSettings();mw.SaveParams();mw.QueryWindowFilterNames();", 
    'S12': "mw.Settings.LoadInstHistory=1-mw.Settings.LoadInstHistory;mw.SaveParams();HideAllWindow();mw.LoadInstHistory();mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();mw.Settings.Filters.push({FilterCode: '((pmax)-(pmin))/(pmin)>=0.06;((pmax)-(pmin))/(pmin)>=0.06 && (tmax)<= (1.05*(py));((pmax)-(pmin))/(pmin)>=0.06 && (bvol)!=1;'}); mw.SelectFilter(0);mw.ShowSettings();mw.SaveParams();mw.QueryWindowFilterNames();", 
    'S13': "mw.Settings.LoadInstHistory=1-mw.Settings.LoadInstHistory;mw.SaveParams();HideAllWindow();mw.LoadInstHistory();mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();mw.Settings.Filters.push({FilterCode: '(plp)-(pcp) > 4;(plp)-(pcp)> 4 && (tmax)<= (1.05*(py));(plp)-(pcp)> 4 && (bvol)!=1;(pcp)-(plp) > 4;(pcp)-(plp)> 4 && (tmax)<= (1.05*(py));(pcp)-(plp)> 4 && (bvol)!=1;'}); mw.SelectFilter(0);mw.ShowSettings();mw.SaveParams();mw.QueryWindowFilterNames();", 
    'S14': "mw.Settings.LoadInstHistory=1-mw.Settings.LoadInstHistory;mw.SaveParams();HideAllWindow();mw.LoadInstHistory();mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();mw.Settings.Filters.push({FilterCode: '(pd1)==(tmax) && (qd1)!=0;(pd1)==(tmax) && (qd1) < (bvol);(pd1)==(tmax) && (qd1) < 1000000;(po1)==(tmin) && (qo1)!=0;(po1)==(tmin) && (qo1) < (bvol);(po1)==(tmin) && (qo1) < 1000000;'}); mw.SelectFilter(0); mw.ShowSettings();mw.SaveParams();mw.QueryWindowFilterNames();", 
    'S15': "mw.Settings.LoadInstHistory=1-mw.Settings.LoadInstHistory;mw.SaveParams();HideAllWindow();mw.LoadInstHistory();mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();mw.Settings.Filters.push({FilterCode: '((qd1)+(qd2)+(qd3)) > (10 * ((qo1)+(qo2)+(qo3)));((qd1)+(qd2)+(qd3)) > (10 * ((qo1)+(qo2)+(qo3)))   &&  (pd1)!=(tmax);'}); mw.SelectFilter(0); mw.ShowSettings(); mw.SaveParams(); mw.QueryWindowFilterNames();", 
    'S16': "mw.Settings.LoadInstHistory=1-mw.Settings.LoadInstHistory;mw.SaveParams();HideAllWindow();mw.LoadInstHistory();mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();mw.Settings.Filters.push({FilterCode: '(ct).Buy_N_Volume > ( 0.5 * (tvol));(ct).Buy_N_Volume > ( 5 * (ct).Sell_N_Volume);'}); mw.SelectFilter(0); mw.ShowSettings(); mw.SaveParams(); mw.QueryWindowFilterNames();", 
    'S17': "mw.Settings.LoadInstHistory=1-mw.Settings.LoadInstHistory;mw.SaveParams();HideAllWindow();mw.LoadInstHistory();mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();mw.Settings.Filters.push({FilterCode: '(tvol)  >  5 * [is5];(tvol) > 5 * [is5]  &&  (ct).Sell_CountI  >   2 *  (ct).Buy_CountI;'}); mw.SelectFilter(0); mw.ShowSettings();mw.SaveParams(); mw.QueryWindowFilterNames();", 
    'S18': "mw.Settings.LoadInstHistory=1-mw.Settings.LoadInstHistory;mw.SaveParams();HideAllWindow();mw.LoadInstHistory();mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();mw.Settings.Filters.push({FilterCode: 'true==function ()  {var Max=function ()  { var m=0;  var n; for(n=0; n<30; n ++){if(m<[ih][n].PriceMax)  m=[ih][n].PriceMax; };  return m;};  {if( ( (Max() - (pl)) / (Max())) >  0.5)  return true ;};} (); true==function () {var Min=function ()  { var m=1000000;var n; for(n=0; n<30; n ++)       {if(m > [ih][n].PriceMin)          m = [ih][n].PriceMin; }; return m;};  {if ( (pl) > 1.5 * Min() ) return true ;};} ()'}); mw.SelectFilter(0); mw.ShowSettings();mw.SaveParams(); mw.QueryWindowFilterNames();", 
    'S19': "mw.Settings.LoadInstHistory=1-mw.Settings.LoadInstHistory;mw.SaveParams();HideAllWindow();mw.LoadInstHistory();mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();mw.Settings.Filters.push({FilterCode: '[ih][1].PClosing <  [ih][2].PClosing && [ih][2].PClosing <  [ih][3].PClosing && [ih][3].PClosing <  [ih][4].PClosing && [ih][4].PClosing <  [ih][5].PClosing &&[ih][5].PClosing <  [ih][6].PClosing && (tvol) > (bvol)  &&  (ct).Buy_CountI < (ct).Sell_CountI'}); mw.SelectFilter(0); mw.ShowSettings();mw.SaveParams(); mw.QueryWindowFilterNames();", 
    'S20': "mw.Settings.LoadInstHistory=1-mw.Settings.LoadInstHistory;mw.SaveParams();HideAllWindow();mw.LoadInstHistory();mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();mw.Settings.Filters.push({FilterCode: '( (ct).Sell_CountI + (ct).Sell_CountN ) > 4 *( ((ct).Buy_CountI) + ((ct).Buy_CountN) ); (((ct).Buy_I_Volume)/((ct).Buy_CountI))  >  2 * (((ct).Sell_I_Volume)/((ct).Sell_CountI))'}); mw.SelectFilter(0); mw.ShowSettings();mw.SaveParams(); mw.QueryWindowFilterNames();", 
        

    }
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "normal"  

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    #options.add_argument("--incognito")

    pref = {}
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    #options.add_argument("download.default_directory = C:/Users/A/Desktop")
    driver = webdriver.Chrome(desired_capabilities=caps, options=options, executable_path="C:/Users/Administrator/Desktop/chromedriver.exe")

    driver.get("http://www.tsetmc.com/Loader.aspx?ParTree=15131F")
    time.sleep(5)
    driver.execute_script(scripts[Filter])
    time.sleep(25)
    """
    driver.execute_script("mw.ExportClick('yourmwexcel');")
    time.sleep(5)"""

    output = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(output, 'html.parser')
    print('im making a soup')
    schema = ['div.t0c:nth-of-type(1) a.inst', 'div.t0c5:nth-of-type(3)', 'div.t0c5 span', 'div.t0c5:nth-of-type(5) div.ltr', 'div.t0c:nth-of-type(10)', 'div.t0c5:nth-of-type(16)', 'div.t0c:nth-of-type(17)']
    header = ['Nemad', 'Tedad', 'Hajm', 'Arzesh', 'Darsad', 'EPS', 'P/E']
    data = dict()
    for num, i in enumerate(header, start=0):
        data[i] = [j.get_text() for j in soup.select(schema[num])]
    
    print([len(i) for i in data.values()])

    df = pd.DataFrame.from_dict(data, orient='columns')
    df.to_excel("C:/Users/Administrator/Desktop/Output_{}.xlsx".format(Filter))    
    
    driver.close()
    del driver


