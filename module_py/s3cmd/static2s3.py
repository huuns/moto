# -*- coding: utf-8 -*-

# ==========================================================================================
# write : moto
#
# init          : 16.07.25.
# latest update : 16.10.19.
#
# usage : python static2bucket.py  (push)
#
# work  : static files ------- s3cmd -------> s3 bucket
# ==========================================================================================

import subprocess

PAR_DIR = "/home/ubuntu/dev_project"

staticDL = [
    PAR_DIR + "/g_publish",
    #"-m application/javascript " + PAR_DIR + "/PROJECT/static/djs",
    #"-m text/css " + PAR_DIR + "/PROJECT/static/dcss",

    #PAR_DIR + "/PROJECT/static/admin",
    #PAR_DIR + "/PROJECT/static/facebook",
    #PAR_DIR + "/PROJECT/static/rest_framework",
    #PAR_DIR + "/PROJECT/static/rest_framework_swagger"
]

for directoryAndOption in staticDL:
    static2s3 = 's3cmd sync --guess-mime-type --add-header="Cache-Control:max-age=31536000" --acl-public --delete-removed -P -r %s s3://thefitshoes/' % (directoryAndOption)
    #static2s3 = 's3cmd sync --cf-invalidate --cf-invalidate-default-index --guess-mime-type --acl-public --delete-removed -P -r %s s3://thefitshoes/' % (directoryAndOption)

    print static2s3

    p = subprocess.Popen(static2s3, shell=True, stdout=subprocess.PIPE)
    p.wait()

    print "end"
