from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from article import views




urlpatterns = [
    path('', views.index,name="index"),
    path('aboutMe/', views.aboutMe, name='aboutMe'),
    path('mobileProjects/', views.mobileProjectsViews, name = "mobileProjects"),
    path('notFound/', views.notFound, name = "notFound"),
    path('resume/', views.resume,name="resume"),
    path('comingSoon/', views.comingSoon, name = "comingSoon"),
    path('sourceCode/', views.sourceCode, name="sourceCode"),
    path('contact/', views.contact, name = "contact"),


    path('resume/plansImages', views.plansImagesViews, name = "plansImages"),
    path('resume/facetimeImages', views.facetimeImagesViews, name = "facetimeImages"),
    path('resume/flutterWeatherAppImages', views.flutterWeatherAppImagesViews, name = "flutterWeatherAppImages"),
    path('resume/notebookImages/', views.notebookImagesViews, name="notebookImages"),
    path('resume/wordGuessGameImages', views.wordGuessGameImagesViews, name = "wordGuessGameImages"),
    path('resume/twitterImages', views.twitterImagesViews, name = "twitterImages"),
    path('resume/threadsImages', views.threadsImagesViews, name = "threadsImages"),
    path('resume/weatherImages', views.weatherImagesViews, name = "weatherImages"),
    path('resume/recipeImages', views.recipeImagesViews, name = "recipeImages"),
    path('resume/voiceRecorderImages', views.voiceRecorderImagesViews, name = "voiceRecorderImages"), 
    path('resume/walletImages', views.walletImagesViews, name = "walletImages"),
    path('resume/reactRickAndMortyImages', views.rickAndMortyImagesViews, name="rickAndMortyImages"),
    path('resume/qrScannerImages', views.qrScannerImagesViews, name = "qrScannerImages"),
    path('resume/crmImages', views.crmImagesViews, name='crmWebImages'),
    path('resume/sentinelImages', views.sentinelImagesViews, name='sentinelImages'),
    path('resume/macchangerImages', views.macChangerImagesViews, name='macChangerImages'),
    path('resume/networkScannerImages', views.networkScannerImagesViews, name='networkScannerImages'),


    path('desktopProjects', views.desktopProjects, name = "desktopProjects"),
    path('desktopProjects/crmDesktop', views.crmDesktopView, name="crmDesktop"),
    path('desktopProjects/crmDesktop/crmDesktopImages', views.crmDesktopImagesViews, name = "crmDesktopImages"),


    path('webProjects', views.webProjects, name = "webProjects"),
    path('webProjects/crmWeb', views.crmWebView, name = "crmWeb"),
    path('webProjects/crmWeb/crmWebImages', views.crmImagesViews, name = "crmWebImages"),


    path('mobileProjects/plans', views.plansIOSViews, name = "plans"),
    path('mobileProjects/plans/plansImages', views.plansImagesViews, name = "plansImages"),
    path('mobileProjects/faceTime', views.facetimeViews, name = "faceTime"),
    path('mobileProjects/faceTime/facetimeImages', views.facetimeImagesViews, name = "facetime_images"),
    path('mobileProjects/flutterWeatherApp', views.flutterWeatherAppViews, name = "flutterWeatherApp"),
    path('mobileProjects/flutterWeatherApp/flutterWeatherAppImages', views.flutterWeatherAppImagesViews, name = "flutterWeatherAppImages"),
    path('mobileProjects/notebook', views.notebookViews, name = "notebook"),
    path('mobileProjects/notebook/notebookImages', views.notebookImagesViews, name = "notebookImages"),
    path('mobileProjects/wordGuess', views.wordGuessGameViews, name = "wordGuess"),
    path('mobileProjects/wordGuess/wordGuessGameImages', views.wordGuessGameImagesViews, name = "wordGuessGameImages"),
    path('mobileProjects/twitterClone', views.twitterViews, name = "twitterClone"),
    path('mobileProjects/twitterClone/twitterImages', views.twitterImagesViews, name = "twitterImages"),
    path('mobileProjects/threadsClone', views.threadsCloneViews, name = "threadsClone"),
    path('mobileProjects/threadsClone/threadsImages', views.threadsImagesViews, name = "threadsImages"),
    path('mobileProjects/weatherApp', views.weatherAppViews, name = "weatherApp"),
    path('mobileProjects/weatherApp/weatherImages', views.weatherImagesViews, name = "weatherImages"),
    path('mobileProjects/recipe', views.recipeViews, name = "recipe"),
    path('mobileProjects/recipe/recipeImages', views.recipeImagesViews, name = "recipeImages"),
    path('mobileProjects/voiceRecorder', views.voiceRecorderViews, name = "voiceRecorder"),
    path('mobileProjects/voiceRecorder/voiceRecorderImages', views.voiceRecorderImagesViews, name = "voiceRecorderImages"),
    path('mobileProjects/walletUi', views.walletUiViews, name = "walletUi"),
    path('mobileProjects/walletUi/walletImages', views.walletImagesViews, name = "walletImages"),
    path('mobileProjects/rickAndMorty', views.rikcAndMortyViews, name = "rickAndMorty"),
    path('mobileProjects/rickAndMorty/reactRickAndMortyImages', views.rickAndMortyImagesViews, name = "rickAndMortyImages"),
    path('mobileProjects/qrScanner', views.qrCodeScannerViews, name = "qrScanner"),
    path('mobileProjects/qrScanner/qrScannerImages', views.qrScannerImagesViews, name = "qrScannerImages"),


    path('cyberSecurityProjects', views.cyberSecurityProjects, name = "cyberSecurityProjects"),
    path('cybersecurity/sentinel', views.sentinelViews, name = "sentinel"),
    path('cybersecurity/sentinel/sentinelImages', views.sentinelImagesViews, name = "sentinelImages"),
    path('cybersecurity/macchanger', views.macChangerView, name = "macchanger"),
    path('cybersecurity/macchanger/macchangerImages', views.macChangerImagesViews, name = "macChangerImages"),
    path('cybersecurity/networkScanner', views.networkScannerView, name = "networkScanner"),
    path('cybersecurity/networkScanner/networkScannerImages', views.networkScannerImagesViews, name = "networkScannerImages")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'article.views.notFound'