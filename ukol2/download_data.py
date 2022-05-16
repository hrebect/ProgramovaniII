import io
import sys
import zipfile
import requests

try:
    r = requests.get("http://data.piid.cz/PID_GTFS.zip")
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('PID_GTFS')

except requests.exceptions.ConnectionError:
    print('No internet connection or invalid URL')
    sys.exit()
except requests.exceptions.Timeout:
    print ("Timeout Error:")
    sys.exit()
except requests.exceptions.RequestException as err:
    print('Somethong else...', err)
    sys.exit()
except zipfile.BadZipfile:
    print('file is not a ZIP')
    sys.exit()
except PermissionError as perer:
    print('Permission derail', perer)
    sys.exit()

