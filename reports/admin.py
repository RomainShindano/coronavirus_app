from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin  # GeoModelAdmin
from django.contrib.gis.geos import Point
from .models import Report


class ReportAdmin(OSMGeoAdmin):
    # class ReportAdmin(GeoModelAdmin):

    # default_lon = -3.776591392147457
    # default_lat = 23.46700451941655

    lon = -4.871840802112763
    lat = 24.56539753146479
    pnt = Point(lon, lat, srid=4326)
    pnt.transform(900913)
    default_lon, default_lat = pnt.coords

    default_zoom = 5
    # modifiable = True

    list_display = ("first_symptomatic", "location")


admin.site.register(Report, ReportAdmin)