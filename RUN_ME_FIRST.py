import os

# Install pytubefix
pytube_install = ('py -m pip install \
--trusted-host pypi.org \
--trusted-host pypi.python.org \
--trusted-host files.pythonhosted.org \
--user --upgrade pytubefix')

os.system(pytube_install)