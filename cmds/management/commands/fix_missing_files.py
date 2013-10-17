from django.core.management.base import BaseCommand

from crate.web.packages.models import ReleaseFile
from crate.pypi.processor import PyPIPackage


class Command(BaseCommand):

    def handle(self, *args, **options):
        i = 0
        for rf in ReleaseFile.objects.filter(digest="").distinct("release"):
            print rf.release.package.name, rf.release.version
            p = PyPIPackage(rf.release.package.name, version=rf.release.version)
            p.process(skip_modified=False)
            i += 1
        print "Fixed %d releases" % i
