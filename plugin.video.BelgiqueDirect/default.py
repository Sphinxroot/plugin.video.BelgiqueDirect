########################################

import os, sys, xbmc, xbmcgui, xbmcplugin, xbmcaddon
	
#Belgique Direct By Sphinxroot QC

# Various constants used throughout the script
HANDLE = int(sys.argv[1])
ADDON = xbmcaddon.Addon(id='plugin.video.BelgiqueDirect')
LANGUAGE  = ADDON.getLocalizedString
THUMBNAIL_PATH = os.path.join( ADDON.getAddonInfo( 'path' ), 'resources', 'media')

def start() :

	li = xbmcgui.ListItem(label=LANGUAGE(30000), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'belgique.gif'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://raw.githubusercontent.com/Sphinxroot/M3U-URL/master/Belgique.fr.m3u", listitem=li, isFolder=False)    
	setViewMode("500")		
	xbmcplugin.endOfDirectory( HANDLE )		
	
def setViewMode(id):
	if xbmc.getSkinDir() == "skin.confluence":
		xbmc.executebuiltin("Container.SetViewMode(" + id + ")")
			
start()