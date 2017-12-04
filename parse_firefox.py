#!/usr/bin/python

import sqlite3
import os
import sys
import struct
import hashlib
import shutil
import subprocess as s



chunkSize = 256 * 1024

mozilla_directory = "/.mozilla/firefox/"
cache_directory = "/.cache/mozilla/firefox/"
mozilla_profile_directory = ""
cache_profile_directory = ""

def main():
    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + " [domain]")
        return
    domain = sys.argv[1]
    ClearFirefox(domain)
    s.call(['notify-send','Nevercookie','Persistent cookies deleted for:'+domain])
#     Scan(domain, "/tmp/database.txt")

# def Scan(domain, database):
#     with open(database, "r") as ins:
#         for line in ins:
#             if domain in line:
#                 ClearFirefox(domain)
#                 break

def ClearFirefox(domain):
    home_directory = os.path.expanduser("~")
    for folderName in os.listdir(home_directory + mozilla_directory):
        if folderName.endswith(".default"):
            cache_profile_directory = home_directory + cache_directory + folderName + "/cache2/entries"
            mozilla_profile_directory = home_directory + mozilla_directory + folderName
            break

    if len(mozilla_profile_directory) == 0 or len(cache_profile_directory) == 0:
        print("Error finding profile directory\n")
        return


    for folderName in os.listdir(mozilla_profile_directory + "/storage/default/"):
        if domain in folderName:
            shutil.rmtree(mozilla_profile_directory + "/storage/default/" + folderName)
            print("Found matching IDB: " + folderName)


    for filePath in os.listdir(cache_profile_directory):
        file = open(cache_profile_directory + '/' + filePath, 'r')
        url = ParseCacheFile(file)
        file.close()
        if domain in url:
            os.remove(cache_profile_directory + '/' + filePath)
            print("Found matching cache: " + url)


    conn = sqlite3.connect(mozilla_profile_directory + "/cookies.sqlite")
    c = conn.cursor()

    c.execute("SELECT host, value FROM moz_cookies")
    cookie_list = []
    for row in c:
        if domain in row[0]:
            cookie_list.append(row[0])
            print("Found matching cookie: " + str(row))
    for host in cookie_list:
        c.execute("DELETE FROM moz_cookies WHERE host = '" + host + "'")
    conn.commit()
    conn.close()

    conn_webstore = sqlite3.connect(mozilla_profile_directory + "/webappsstore.sqlite")
    c_store = conn_webstore.cursor()

    c_store.execute("SELECT originKey FROM webappsstore2")

    cookie_list = []
    for row in c_store:
        rev = row[0][::-1]
        if domain in rev:
            cookie_list.append(row[0])
            print("Found matching cookie: " + str(row))

        for host in cookie_list:
            c_store.execute("DELETE FROM webappsstore2 WHERE originKey = '" + host + "'")
    conn_webstore.commit()
    conn_webstore.close()

def ParseCacheFile (parseFile):
    fileSize = os.path.getsize(parseFile.name)
    parseFile.seek(-4, os.SEEK_END)
    metaStart = struct.unpack('>I', parseFile.read(4))[0]
    numHashChunks = metaStart / chunkSize
    if metaStart % chunkSize :
        numHashChunks += 1
    parseFile.seek(metaStart + 4 + numHashChunks * 2, os.SEEK_SET)
    version = struct.unpack('>I', parseFile.read(4))[0]
    fetchCount = struct.unpack('>I', parseFile.read(4))[0]
    lastFetchInt = struct.unpack('>I', parseFile.read(4))[0]
    lastModInt = struct.unpack('>I', parseFile.read(4))[0]
    frecency = struct.unpack('>I', parseFile.read(4))[0]
    expireInt = struct.unpack('>I', parseFile.read(4))[0]
    keySize = struct.unpack('>I', parseFile.read(4))[0]
    flags = struct.unpack('>I', parseFile.read(4))[0] if version >= 2 else 0
    key = parseFile.read(keySize)
    key_hash = hashlib.sha1(key).hexdigest().upper()
    return key

if __name__ == '__main__':
    main()


