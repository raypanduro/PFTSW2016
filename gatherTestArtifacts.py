import os, shutil, ftplib
#from zipfile import ZipFile
import zipfile
from datetime import datetime

#Check if script is invoked from command line:
if __name__ == '__main__':

    #Create a folder to copy the artifacts into
    if os.path.isdir('/tmp/testartifacts/'):
        os.system('rm -rf /tmp/testartifacts')
        print 'Cleaning Test Artifacts folder.....'
        os.makedirs('/tmp/testartifacts')
    else:
        os.makedirs('/tmp/testartifacts')
    #Copy the files
    shutil.copy('/opt/PFT/firstLarge', '/tmp/testartifacts/firstLarge')
    shutil.copy('/opt/PFT/secondLarge', '/tmp/testartifacts/secondLarge')

    #Create a filename with the timestamp
    n = datetime.now()
    timestamp = n.strftime('%Y%m%d_%H%M%S')
    testfilename = 'testartifacts_'+ str(timestamp) +'.zip'

    #And extend the path to include your folder
    testfileext = '/tmp/' + testfilename
    #print testfilename

    #Open a zipfile for writing
    zipf = zipfile.ZipFile(testfileext, 'w', zipfile.ZIP_DEFLATED)

    #Write files into it. Dont forget to close
    zipf.write('/tmp/testartifacts/firstLarge')
    zipf.write('/tmp/testartifacts/secondLarge')
    zipf.close()

    #Open an ftp session and upload the file
    session = ftplib.FTP('127.0.0.1', 'tester', 'python')
    session.cwd('upload')
    trfile = open(testfileext, 'rb')
    session.storbinary('STOR ' + testfilename, trfile)
