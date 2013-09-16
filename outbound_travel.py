import simplejson, urllib, time

LOCATION_BASE_URL = 'http://maps.googleapis.com/maps/api/distancematrix/json'

def location(origins="2885+Del+Rosa+Ave+92404|6649+Amethyst+Ave+91701|101+S+Azusa+Ave+91702",destinations="5592+San+Fernando+Rd+91201",sensor="false",mode="driving", units="imperial", avoid="tolls", **loc_args):
    loc_args.update({
        'origins': origins,
        'destinations': destinations,
        'sensor': sensor,
        'mode': mode,
        'units': units,
        'avoid': avoid
    })

    url = LOCATION_BASE_URL + '?' + urllib.urlencode(loc_args)
    result = simplejson.dumps(simplejson.load(urllib.urlopen(url)), indent=2)
    return result

if __name__ == '__main__':
    data = location()
    ds = time.strftime('%Y-%m-%b-%H-%M-%S')
    file = 'output/' + ds + '-outbound.json'
    f = open(file, 'w')
    f.writelines(data)
    f.close()
