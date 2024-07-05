from pathlib import Path

source = Path("/sdcard/Apps")

disable = [
    "com.samsung.android.app.omcagent",
    "com.samsung.android.app.updatecenter",
    "com.google.android.partnersetup",
    "com.samsung.android.honeyboard",
    "com.samsung.android.dialer",
    "com.samsung.android.app.contacts",
    "com.google.android.adservices.api",
    "com.google.android.gms.supervision",
]

uninstall = [
    "com.aura.oobe.samsung",
    "com.facebook.appmanager",
    "com.facebook.services",
    "com.facebook.system",
    "com.google.android.projection.gearhead",
    "com.google.android.youtube"
    "com.hiya.star",
    "com.microsoft.skydrive",
    "com.mygalaxy",
    "com.opera.max.oem",
    "com.samsung.android.app.spage",
    "com.samsung.android.app.watchmanagerstub",
    "com.samsung.android.aremoji",
    "com.samsung.android.aremojieditor",
    "com.samsung.android.calendar",
    "com.samsung.android.game.gamehome",
    "com.samsung.android.game.gametools",
    "com.samsung.android.game.gos",
    "com.samsung.android.mapsagent",
    "com.samsung.android.messaging",
    "com.samsung.android.scloud",
    "com.samsung.android.scpm",
    "com.samsung.android.spaymini",
    "com.samsung.android.stickercenter",
    "com.samsung.android.svcagent",
    "com.samsung.android.themecenter",
    "com.samsung.android.themestore",
    "com.samsung.ecomm.global.in",
    "com.sec.android.app.samsungapps",
    "com.sec.android.daemonapp",
    "com.sec.android.easyMover.Agent",
    "com.sec.android.easyMover",
    "com.sec.android.mimage.avatarstickers",
    "com.android.chrome"
]

install = list(source.rglob("*.apk"))
