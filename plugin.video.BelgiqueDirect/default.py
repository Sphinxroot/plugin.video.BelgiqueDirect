########################################

import os, sys, xbmc, xbmcgui, xbmcplugin, xbmcaddon
	
#Suisse Direct By Sphinxroot QC

# Various constants used throughout the script
HANDLE = int(sys.argv[1])
ADDON = xbmcaddon.Addon(id='plugin.video.BelgiqueDirect')
LANGUAGE  = ADDON.getLocalizedString
THUMBNAIL_PATH = os.path.join( ADDON.getAddonInfo( 'path' ), 'resources', 'media')

def start() :

	li = xbmcgui.ListItem(label=LANGUAGE(30000), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'belgique.gif'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="plugin://plugin.video.youtube/play/?video_id=F109TZt3nRc", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30001), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Centre.png'))		
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://tvl-live.fl.freecaster.net/live/actv/actv.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30002), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'belrtl.jpg'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="http://bel-lh.akamaihd.net/i/BEL_1@321282/master.m3u8?fluxustv.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30003), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'bx1.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://59959724487e3.streamlock.net/stream/live/chunklist_w1820098040.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30004), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'canalalpha.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://edge4.vedge.infomaniak.com/livecast/ik:canalalpha/chunklist_w1090298739_b2500000.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30005), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'canalzoom.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="http://streamer.canalc.be:1935/canalzoom/smil:SMIL-canalzoom-multi/chunklist_w857378252_b2096000_slfra_t64NzIwcA==.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30006), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'CanalC.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://594a365b4a1b2.streamlock.net/canalc/_definst_/live/chunklist_w1160503303.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30007), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'matele.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://594a365b4a1b2.streamlock.net/matele/live/chunklist_w1148376481.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30008), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'NRJ.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://5be019f0d8c6e.streamlock.net/ngroup/ngrp:NRJHitsTV_all/playlist.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30009), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'ln24.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://live.cdn.ln24.be/out/v1/b191621c8b9a436cad37bb36a82d2e1c/index_1.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30010), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'notele.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://streaming01.divercom.be/notele_live/_definst_/direct.stream/chunklist_w1567084165.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30011), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'RTC.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://media01.webtvlive.eu/rtc-edge/_definst_/smil:live.smil/chunklist_w1270237425_b8256000_DVR_tkdG9rZW5lbmR0aW1lPTE1ODc5NTQxMzAmdG9rZW5zdGFydHRpbWU9MTU4Nzk0MzMzMCZ0b2tlbmhhc2g9UkM2bXlYM1lRV1M4cUN5YzZ4YThVekFxZXNSR2hrbkl0ZjZKYU9lLUZwUT0=.m3u8", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30012), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'trltvi.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="http://rtltvi-lh.akamaihd.net/i/TVI_1@319659/master.m3u8", listitem=li, isFolder=False)	
   	li = xbmcgui.ListItem(label=LANGUAGE(30013), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'tvcom.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://5a0b00d270652.streamlock.net/live/tvcom-live/chunklist_w396605632.m3u8", listitem=li, isFolder=False)
   	li = xbmcgui.ListItem(label=LANGUAGE(30014), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'TVLux.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://5a0b00d270652.streamlock.net/live/tvlux-live/chunklist_w1425646824.m3u8", listitem=li, isFolder=False)
   	li = xbmcgui.ListItem(label=LANGUAGE(30015), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'telemb.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://tvl-live.fl.freecaster.net/live/telemb/telemb.m3u8", listitem=li, isFolder=False)
   	li = xbmcgui.ListItem(label=LANGUAGE(30016), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'tls.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://tvl-live.fl.freecaster.net/live/telesambre/telesambre.m3u8", listitem=li, isFolder=False)
   	li = xbmcgui.ListItem(label=LANGUAGE(30017), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Vedia.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://5a0b00d270652.streamlock.net/live/vedia-live/chunklist_w426448595.m3u8", listitem=li, isFolder=False)    
	setViewMode("500")		
	xbmcplugin.endOfDirectory( HANDLE )		
	
def setViewMode(id):
	if xbmc.getSkinDir() == "skin.confluence":
		xbmc.executebuiltin("Container.SetViewMode(" + id + ")")
			
start()