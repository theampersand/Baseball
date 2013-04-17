__author__ = 'Administrator'

import requests
from lxml.html import document_fromstring, tostring

url = 'http://games.espn.go.com/flb/leaguesetup/ownerinfo?leagueId=54692'

cookies = dict([('SWID','{9B885E8D-3D84-49B9-885E-8D3D8429B989}'),('broadbandAccess','espn3-false%2Cnetworks-false'),('DE2','dXNhO2luO2luZGlhbmFwb2xpczticm9hZGJhbmQ7NTs0OzQ7NTI3OzAzOS43ODM7LTA4Ni4wNDU7ODQwOzE1OzE0MDs2O3VzOw=='),('id','c5a7bdc4e0000e2||t=1366235691|et=730|cs=002213fd48655c040886872e2b'),('DS','Pzs7MDs7YXR0IHNlcnZpY2VzIGluYy47A'),('BLUE','G9watzgXQpofPLGwUNyH19T5bGATMQzup902DtWcPI#2YNiib#8DC6m#lJ0OwNHfSs#ECuaWnFJKDqnvKVNAyMGKQ5OdTvlsSWVgf7nc0233rLW313dPnPRMK6m44tQkFXHJ7dXbMc$yA#UXsKfH3PhkZ0OK$aq9Zv5OsZvhU8CqBFtC#PYGlZlflTNiv0PXGW0va9sUIC#ttrxbxf4W5EgL9x$X6DZIwo1bd4S2QnzkAUx31P0#XxMoN0p#Xw6ELtSq$RjeJZyDy3DYtNv2Jg'),('CRBLM','CBLM-001:'),('RED','AAAAAAAAEVavAAJUNm7xWUMuGBoIYTlQTu5LSgGU6dVhA/uprOS0lcbTMDqqyJlZJNDO4Q2mY3UKCzxvUlDSH5AXxOnY9uvBuM6TRwPVO5bXplikzVT3K4KCSidqyfKq4Pt2GwxZhoS6l04egIx47ATRxYEgiuvWRvRSdyR//0Vx0TZwcMUnxMbDieRmXljZlKEVaqRlrAhOSIi5Tg6D5hfiJTmxho4WEmndbvQISFGBiFXILS18QENuMmhxdg=='),('userAB','9'),('CRBLM_LAST_UPDATE','1366235692:{9B885E8D-3D84-49B9-885E-8D3D8429B989}')])
r = requests.get(url, cookies=cookies)

root = document_fromstring(r.text)
owner_rows = root.get_element_by_id('1-0')
print(tostring(owner_rows))

