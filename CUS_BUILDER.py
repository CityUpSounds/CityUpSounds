from CUSsourceFile import data
import shutil

print(chr(27) + "[2J")


def clr_existing_file(x):    
    with open(x,'w') as clrfile:
        clrfile.write('')
        print('Built: '+ x)


def append_head_tags_page_index(x):   
    with open(x,'a') as a:        
        a.write('<!DOCTYPE html>\n')
        a.write('<html lang="en">\n')
        a.write('<head>\n')
        a.write('<meta charset="UTF-8">\n')
        a.write('<meta name="viewport"    content="width=device-width, initial-scale=1.0">\n')
        a.write('<title>CityUp Sounds | A collection of ambient sound recordings and sound effects.</title>\n') 
        a.write('<meta name="robots"      content="index, follow">\n')
        a.write('<meta name="description" content="A collection of ambient sound recordings and sound effects. Sharing my passion of sounds and recordings with whom share a similar interest.">\n')
        a.write('<meta name="googlebot"   content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">\n')
        a.write('<meta name="bingbot"     content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">\n')
        a.write('<link rel="canonical"  href="'+ websiteURL +'">\n')        
        a.write('<link rel="stylesheet" href="'+ cssCloudflare +'">\n')
        a.write('<link rel="stylesheet" href="'+ cssStylePath +'">\n')
        a.write('<meta property="og:locale"      content="en_US">\n')
        a.write('<meta property="og:type"        content="website">\n')
        a.write('<meta property="og:title"       content="CityUp Sounds | A collection of ambient sound recordings and sound effects.">\n')
        a.write('<meta property="og:description" content="A collection of ambient sound recordings and sound effects. Sharing my passion of sounds and recordings with whom share a similar interest.">\n')
        a.write('<meta property="og:url"         content="'+ websiteURL +'">\n')
        a.write('<meta property="og:site_name"   content="'+ websiteName +'">\n')
        a.write('<meta property="og:see_also" content="https://cityupsounds.github.io/pages/Footstep_Tram_Tracks.html">\n')
        a.write('<meta property="og:see_also" content="https://cityupsounds.github.io/pages/Footstep_Bush_Tracks.html">\n')

        a.write('<meta property="og:image"            content="https://.......jpg" />\n')
        a.write('<meta property="og:image:secure_url" content="https://.......jpg">\n')
        a.write('<meta property="og:image:type"       content="image/jpeg">\n')
        a.write('<meta property="og:image:width"      content="">\n')
        a.write('<meta property="og:image:height"     content="">\n')
        a.write('<meta property="og:video"            content="https://.......mp4">\n')
        a.write('<meta property="og:video:secure_url" content="https://.......mp4">\n')
        a.write('<meta property="og:video:type"       content="video/mp4.">\n')
        a.write('<meta property="og:video:width"      content="">\n')
        a.write('<meta property="og:video:height"     content="">\n')
        a.write('<meta name="twitter:card" content="summary_large_image">\n')
        a.write('<meta name="twitter:creator" content="'+ metaTwitterHandle +'">\n')
        a.write('<meta name="twitter:site" content="'+ metaTwitterHandle +'">\n')
        a.write('<meta name="twitter:title" content="CityUp Sounds | A collection of ambient sound recordings and sound effects.">\n')
        a.write('<meta name="twitter:url" content="'+ websiteURL +'">\n')
        a.write('<meta name="twitter:description" content="A collection of ambient sound recordings and sound effects. Sharing my passion of sounds and recordings with whom share a similar interest.">\n')
        a.write('<meta name="twitter:image:src" content="https://.......jpg">\n')

        a.write('<link rel="manifest" href="manifest.json">\n')
        a.write('<link rel="shortcut icon" type="image/x-icon"   href="fav/favicon.png">\n')
        a.write('<link rel="apple-touch-icon"                    href="fav/favicon.png" />\n')
        a.write('<link rel="apple-touch-icon-precomposed" sizes="192x192" href="fav/favicon_192x192.png">\n')
        a.write('<link rel="apple-touch-icon" sizes="57x57"      href="fav/favicon_57x57.png">\n')
        a.write('<link rel="apple-touch-icon" sizes="60x60"      href="fav/favicon_60x60.png">\n')
        a.write('<link rel="apple-touch-icon" sizes="72x72"      href="fav/favicon_72x72.png">\n')
        a.write('<link rel="apple-touch-icon" sizes="76x76"      href="fav/favicon_76x76.png">\n')
        a.write('<link rel="apple-touch-icon" sizes="114x114"    href="fav/favicon_114x114.png">\n')
        a.write('<link rel="apple-touch-icon" sizes="120x120"    href="fav/favicon_120x120.png">\n')
        a.write('<link rel="apple-touch-icon" sizes="144x144"    href="fav/favicon_144x144.png">\n')
        a.write('<link rel="apple-touch-icon" sizes="152x152"    href="fav/favicon_152x152.png">\n')
        a.write('<link rel="apple-touch-icon" sizes="180x180"    href="fav/favicon_180x180.png">\n')   
        a.write('<link rel="icon" type="image/png" sizes="16x16" href="fav/favicon_16x16.png">\n')
        a.write('<link rel="icon" type="image/png" sizes="32x32" href="fav/favicon_32x32.png">\n')
        a.write('<link rel="icon" type="image/png" sizes="96x96" href="fav/favicon_96x96.png">\n')
        a.write('<link rel="icon" type="image/png" sizes="192x192" href="fav/favicon_192x192.png">\n')
        a.write('<meta name="msapplication-TileColor" content="#ff4500">\n')
        a.write('<meta name="msapplication-TileImage" content="fav/favicon_144x144.png">\n')
        a.write('<meta name="theme-color" content="#ff4500"> \n')
        a.write('</head>\n')  



def append_head_tags_page(x):   
    with open(x,'a') as a:        
        a.write('<!DOCTYPE html>\n')
        a.write('<html lang="en">\n')
        a.write('<head>\n')
        a.write('<meta charset="UTF-8">\n')
        a.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        a.write('<title>'+ valuePageTitle +' | '+ websiteName +'</title>\n')
        a.write('<link rel="shortcut icon" href="favicon.png" type="image/x-icon">\n')
        a.write('<link rel="stylesheet" href="'+ cssCloudflare +'">\n')
        a.write('<link rel="stylesheet" href="../'+ cssStylePath +'">\n')
        a.write('</head>\n')     


def append_NavBar(x):
    with open(x,'a') as a: 
        a.write('<header id="navigateToTop" class="navBarContainer">\n')
        a.write('<a class="navBarLogo" href="'+ websiteURL +'">\n')
        a.write('<h1>'+ websiteName +'</h1>\n')
        a.write('</a>\n')
        a.write('<nav class="navBarSocial">\n')
        a.write('<a href="'+ linkTwitter +'"><i class="fa fa-twitter" aria-hidden="true"></i></a>\n')
        a.write('<a href="'+ linkInstagram +'"><i class="fa fa-instagram" aria-hidden="true"></i></a>\n')
        a.write('<a href="'+ linkYoutube +'"><i class="fa fa-youtube" aria-hidden="true"></i></a>\n')
        a.write('<a href="'+ linkBandcamp +'"><i class="fa fa-bandcamp" aria-hidden="true"></i></a>\n')
        a.write('</nav>\n')
        a.write('</header>\n')
        

def append_open_body_tag(x):
    with open(x,'a') as a:       
        a.write('\n') 
        a.write('<body class="mainContainer">\n') 


def append_close_body_tag(x):
    with open(x,'a') as a:     
        a.write('\n')   
        a.write('</body>\n')


def append_footer_tags_index(x):
    with open(x,'a') as a: 
        a.write('<footer class="footerContainer">\n')
        a.write('<a class="footerLogo" href="'+ websiteURL +'">\n')
        a.write('<h1>'+ websiteName +'</h1>\n')
        a.write('</a>\n')
        a.write('<nav class="footerMenu">\n')
        a.write('<a href="./pages/'+ linkAbout +'">About</a>\n')
        a.write('<a href="./pages/'+ linkCookie +'">CookiePolicy</a>\n')
        a.write('<a href="./pages/'+ linkPrivacy +'">Privacy Policy</a>\n')
        a.write('<a href="./pages/'+ linkSiteMap +'">Site Map</a>\n')
        a.write('</nav>\n')
        a.write('<nav class="footerSocial">\n')
        a.write('<a href="'+ linkTwitter +'"><i class="fa footerfa fa-twitter" aria-hidden="true"></i></a>\n')
        a.write('<a href="'+ linkInstagram +'"><i class="fa footerfa fa-instagram" aria-hidden="true"></i></a>\n')
        a.write('<a href="'+ linkYoutube +'"><i class="fa footerfa fa-youtube" aria-hidden="true"></i></a>\n')
        a.write('<a href="'+ linkBandcamp +'"><i class="fa footerfa fa-bandcamp" aria-hidden="true"></i></a>\n')
        a.write('</nav>\n')
        a.write('<div class="footerCopyright">\n')
        a.write('<a href="./pages/'+ linkCopyright +'">Copyright &copy;2020</a>\n')
        a.write('</div>\n')
        a.write('</footer>\n')


def append_footer_tags(x):
    with open(x,'a') as a: 
        a.write('<footer class="footerContainer">\n')
        a.write('<a class="footerLogo" href="'+ websiteURL +'">\n')
        a.write('<h1>'+ websiteName +'</h1>\n')
        a.write('</a>\n')
        a.write('<nav class="footerMenu">\n')
        a.write('<a href="'+ linkAbout +'">About</a>\n')
        a.write('<a href="'+ linkCookie +'">CookiePolicy</a>\n')
        a.write('<a href="'+ linkPrivacy +'">Privacy Policy</a>\n')
        a.write('<a href="'+ linkSiteMap +'">Site Map</a>\n')
        a.write('</nav>\n')
        a.write('<nav class="footerSocial">\n')
        a.write('<a href="'+ linkTwitter +'"><i class="fa footerfa fa-twitter" aria-hidden="true"></i></a>\n')
        a.write('<a href="'+ linkInstagram +'"><i class="fa footerfa fa-instagram" aria-hidden="true"></i></a>\n')
        a.write('<a href="'+ linkYoutube +'"><i class="fa footerfa fa-youtube" aria-hidden="true"></i></a>\n')
        a.write('<a href="'+ linkBandcamp +'"><i class="fa footerfa fa-bandcamp" aria-hidden="true"></i></a>\n')
        a.write('</nav>\n')
        a.write('<div class="footerCopyright">\n')
        a.write('<a href="'+ linkCopyright +'">Copyright &copy;2020</a>\n')
        a.write('</div>\n')
        a.write('</footer>\n')
        

def append_close_html_tag(x):
    with open(x,'a') as a:       
        a.write('\n') 
        a.write('</html>\n')       


def move_file(source,target):  
    target = github_repo + target
    shutil.move(source, target)    


#=======================================================
#       GLOBAL CONSTANTS - Consistant 
#=======================================================
cssCloudflare = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
cssStylePath = 'css/style.css'
websiteURL = 'https://cityupsounds.github.io/'
websiteName = 'CityUp Sounds'
linkExternalDownload = 'Link To Bandcamp'
linkAbout = 'about.html'
linkCookie = 'cookie.html'
linkPrivacy = 'privacy.html'
linkSiteMap = 'sitemap.html'
linkCopyright = linkSiteMap
linkTwitter = 'https://twitter.com/CityupSounds'
linkYoutube = 'YouTube'
linkInstagram = 'https://www.instagram.com/cityupsounds/'
linkBandcamp = 'https://cityupsounds.bandcamp.com/'

github_repo = 'cityupsounds/'

metaTwitterHandle = '@CityupSounds'

productOneName = 'Zoom H6 Recorder'
productOneImagePath = '../img/zoom_h6.jpg'
productOneURL = 'Product 1'

productTwoName = 'Zoom Shotgun Microphone'
productTwoImagePath = '../img/zoom_shotgun_microphone.jpg'
productTwoURL = 'Product 2'

productThreeName = 'Zoom Accessories Pack'
productThreeImagePath = '../img/zoom_accessories.jpg'
productThreeURL = 'Product 3'


# ==========================================================
#                 Build INDEX.HTML Page
# ==========================================================
dictionary = data
articleNumber = 0
valuePageTitle = 'Home Page'
page = 'index.html'

clr_existing_file(page)
append_head_tags_page_index(page)
append_NavBar(page)
append_open_body_tag(page)

for d in dictionary:        
    try: 
        valuePageName = dictionary[d]['pageName'] + '.html'
        articlePath = './pages/'+ valuePageName
    except: 
        print('CRITICAL FAIL = Article '+ articleNumber +' needs a Name..... script TERMINATED')
        exit()
    # ================
    try: 
        valuePageTitle = dictionary[d]['pageTitle']
    except: 
        valuePageTitle = ""
        print('Article '+ articleNumber +' Page Title has ZERO value')
    # ================
    try: 
        valuePageImagePath = './img/'+ dictionary[d]['pageImage']
    except: 
        valuePageImagePath = ""
        print('Article '+ articleNumber +' Page Image has ZERO value')
    # ================   
    try: 
        valueDescription = dictionary[d]['description']
        valueDescription = valueDescription.replace('\n', '</p><p>')
        valueDescription = valueDescription[:120]+'....'
    except: 
        valueDescription = ""
        print('Article '+ articleNumber +' Description has ZERO value')
   
    articleNumber = articleNumber + 1
    articleNumberstr = str(articleNumber)
    with open(page,'a') as a:  
        a.write('<article>\n')
        a.write('<a href="'+ articlePath +'" class="cardContainer" title="'+ valuePageTitle +'">\n')
        a.write('<img class="cardThumbnail" src="'+ valuePageImagePath +'" alt="">\n')
        a.write('<div class="cardDescriptionContainer">\n')
        a.write('<div class="cardNumberBox">\n')
        a.write('<p>{:03}</p>\n'.format(articleNumber))
        a.write('</div>\n')
        a.write('<div class="cardTextBox">\n')
        a.write('<h2>'+ valuePageTitle +'</h2>\n')
        a.write('<p>'+ valueDescription +'</p>\n')
        a.write('</div>\n')
        a.write('</div>\n')
        a.write('</a>\n')
        a.write('</article>\n')

append_close_body_tag(page)
append_footer_tags_index(page)
append_close_html_tag(page)

source = page
target = source
move_file(source,target)


# ==========================================================
#                 BUILD ARTICLE Page
# ==========================================================
dictionary = data

for d in dictionary: 
    
    try: valuePageName = dictionary[d]['pageName'] + '.html'
    except: 
        print('CRITICAL FAIL = Page needs a Name..... script TERMINATED')
        print('CRITICAL FAIL = Page needs a Name..... script TERMINATED')
        print('CRITICAL FAIL = Page needs a Name..... script TERMINATED')
        exit()
    # ================
    try:        
        valuePageTitle = dictionary[d]['pageTitle']
    except: 
        valuePageTitle = ""
        print('Page Title has ZERO value')
    # ================
    try: 
        valuePageImagePath = dictionary[d]['pageImage']
    except: 
        valuePageImagePath = ""
        print('Page Image has ZERO value')
    # ================
    try: 
        valuePageVideoPath = dictionary[d]['pageVideo']
    except: 
        valuePageVideoPath = ""
        print('Page Video has ZERO value')
    # ================    
    try: valueLocation = dictionary[d]['location']
    except: 
        valueLocation  = ""
        print('Location has ZERO value')
    # ================
    try: valueAudioFormat = dictionary[d]['audioFormat']
    except: 
        valueAudioFormat = ""
        print('AudioFormat has ZERO value')
    # ================
    try: valueDuration = dictionary[d]['duration']
    except: 
        valueDuration = ""
        print('Duration has ZERO value')
    # ================
    try: valueRecorder = dictionary[d]['recorder']
    except: 
        valueRecorder = ""
        print('Recorder has ZERO value')
    # ================
    try: valueMicrophone = dictionary[d]['microphone']
    except: 
        valueMicrophone = ""
        print('Microphone has ZERO value')
    # ================
    try: valueAudioEditing = dictionary[d]['audioEditing']
    except: 
        valueAudioEditing = ""
        print('Audio Editing has ZERO value')
    # ================
    try: valueVideoAvailable = dictionary[d]['videoAvailable']
    except: 
        valueVideoAvailable = ""
        print('VideoAvailable has ZERO value')
    # ================
    try: valueDelivery = dictionary[d]['delivery'] 
    except: 
        valueDelivery = ""
        print('Delivery has ZERO value')
    # ================    
    try: 
        valueDescription = dictionary[d]['description']
        valueDescription = valueDescription.replace('\n', '</p><p>')
    except: 
        valueDescription = ""
        print('Description has ZERO value')
        
    
    page = valuePageName
    
    clr_existing_file(page)
    append_head_tags_page(page)
    append_NavBar(page)
    append_open_body_tag(page)
    
    with open(page,'a') as a:  
        a.write('<article class="page">\n')
        a.write('<h1>'+ valuePageTitle +'</h1>\n')
        a.write('<section class="page_detailsIMG">\n')
        a.write('<div class="page_details">\n')
        a.write('<p><span>Location: </span>'+ valueLocation +'</p>\n')
        a.write('<p><span>Format: </span>'+ valueAudioFormat +'</p>\n')
        a.write('<p><span>Duration: </span>'+ valueDuration +'</p>\n')
        a.write('<p><span>Recorder: </span>'+ valueRecorder +'</p>\n')
        a.write('<p><span>Microphone: </span>'+ valueMicrophone +'</p>\n')
        a.write('<p><span>Audio Editing: </span>'+ valueAudioEditing +'</p>\n')
        a.write('<p><span>Video Available: </span>'+ valueVideoAvailable +'</p>\n')
        a.write('<p><span>Delivery: </span>'+ valueDelivery +'</p>\n')
        a.write('</div>\n')
        a.write('<div class="page_image">\n')
        a.write('<img src="../img/'+ valuePageImagePath +'" alt="">\n')
        a.write('</div>\n')
        a.write('</section>\n')
        a.write('<div class="page__article__text">\n')
        a.write('<p>'+ valueDescription +'</p>\n')
        a.write('</div>\n')
        a.write('<section class="page_videoDL">\n')
        a.write('<div class="page_video_container">\n')
        a.write('<div class="page_video">\n')
        a.write('<iframe loading="lazy" width="560" height="315" src="'+ valuePageVideoPath +'" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n')
        a.write('</div>\n')
        a.write('</div>\n')
        a.write('<div class="page_DL">\n')
        a.write('<a class="page_btn" href="DOWNLOAD">Download Audio</a>\n')
        a.write('</div>\n')
        a.write('</section>\n')
        a.write('</article>\n')
        a.write('<section class="page_products_container">\n')
        a.write('<div class="page_products_image_container">\n')
        a.write('<a href="'+ productTwoURL +'" class="page_products_image">\n')
        a.write('<img src="'+ productTwoImagePath +'" alt="'+ productTwoName +'">\n')
        a.write('</a>\n')
        a.write('<a href="'+ productOneURL +'" class="page_products_image">\n')
        a.write('<img src="'+ productOneImagePath +'" alt="'+ productOneName +'">\n')
        a.write('</a>\n')
        a.write('<a href="'+ productThreeURL +'" class="page_products_image">\n')
        a.write('<img src="'+ productThreeImagePath +'" alt="'+ productThreeName +'">\n')
        a.write('</a>\n')
        a.write('</div>\n')
        a.write('<div class="page_products_disclosure_container">\n')
        a.write('<p>DISCLAIMER: This page contains affiliate links, which means that if you follow one of my product links or use a discount code, please be aware that I may recieve a commission.</p>\n')
        a.write('<p>Id also like to say THANKYOU for the support if you do.</p>\n')
        a.write('<p>I really appreciate it. </p>\n')
        a.write('</div>\n')
        a.write('</section>\n')
        a.write('<section class="mainContainer">\n')

        

    articleNumber = 0 
    
    while articleNumber < 3:  
        articleNumber = articleNumber + 1
        d='article'+str(articleNumber)                 
        try: 
            valuePageName = dictionary[d]['pageName'] + '.html'
            articlePath = valuePageName
        except: 
            print('CRITICAL FAIL = Article '+ str(articleNumber) +' needs a Name..... script TERMINATED')
            exit()
        # ================
        try: 
            valuePageTitle = dictionary[d]['pageTitle']
        except: 
            valuePageTitle = ""
            print('Article '+ articleNumber +' Page Title has ZERO value')
        # ================
        try: 
            valuePageImagePath = './img/'+ dictionary[d]['pageImage']
        except: 
            valuePageImagePath = ""
            print('Article '+ articleNumber +' Page Image has ZERO value')
        # ================   
        try: 
            valueDescription = dictionary[d]['description']
            valueDescription = valueDescription.replace('\n', '</p><p>')
            valueDescription = valueDescription[:120]+'....'
        except: 
            valueDescription = ""
            print('Article '+ articleNumber +' Description has ZERO value')
    
        
        with open(page,'a') as a:  
            a.write('<article>\n')
            a.write('<a href="'+ articlePath +'" class="cardContainer" title="'+ valuePageTitle +'">\n')
            a.write('<img class="cardThumbnail" src=".'+ valuePageImagePath +'" alt="">\n')
            a.write('<div class="cardDescriptionContainer">\n')
            a.write('<div class="cardNumberBox">\n')
            a.write('<p>{:03}</p>\n'.format(articleNumber))
            a.write('</div>\n')
            a.write('<div class="cardTextBox">\n')
            a.write('<h2>'+ valuePageTitle +'</h2>\n')
            a.write('<p>'+ valueDescription +'</p>\n')
            a.write('</div>\n')
            a.write('</div>\n')
            a.write('</a>\n')
            a.write('</article>\n')
    
    with open(page,'a') as a: 
        a.write('</section>\n')
   
    append_close_body_tag(page)
    append_footer_tags(page)
    append_close_html_tag(page)

    source = page
    target = './pages/' + source
    move_file(source,target)
    




# ==========================================================
#                 ABOUT Page
# ==========================================================
valuePageTitle = 'About'
page = linkAbout

clr_existing_file(page)
append_head_tags_page(page)
append_NavBar(page)
append_open_body_tag(page)

with open(page,'a') as a:              
    a.write('<article class="about">\n') 
    a.write('<h1>About</h1>\n')
    a.write('<p>Thankyou for visiting my site. I have been blown away by the supportive feedback and reactions I have received.</p>\n')
    a.write('<p>This site was started basically to share my passion of sounds and recordings with an entire world of people whom share a similar interest.</p>\n')
    a.write('<p>My interests initially began mid 2016(ish) with my first sound effects recordings. Recorded only with the smartphone I had at the time, you would appreciate the quality was fairly raw, but was exactly enough to spark the passion I share with so many others today. Along the way I have improved my recording equipment so as to capture a more detailed sound quality. Now as my collection of recordings grows, I share them with you.</p>\n')
    a.write('<p>I hope to continue to grow both this site and my collection of recordings, while sharing my passion for sound.</p>\n')
    a.write('<h2>Contact</h2>\n')
    a.write('<p>The best way to get in contact is via the following links:</p>\n')
    a.write('<div class="about_social">\n')
    a.write('<a href="https://twitter.com/CityupSounds"><i class="fa fa-twitter" aria-hidden="true"></i><span>Twitter</span></a>\n')
    a.write('<a href="https://www.instagram.com/cityupsounds/"><i class="fa fa-instagram" aria-hidden="true"></i><span>Instagram</span></a>\n')
    a.write('<a href="https://cityupsounds.bandcamp.com/"><i class="fa fa-bandcamp" aria-hidden="true"></i><span>Bandcamp</span></a>\n')
    a.write('</div>\n')
    a.write('<h2>Images, Video and Audio</h2>\n')
    a.write('<p>I physicially take the photos, capture the video and record the audio myself. Yep. The images used on this website <i>(exceptions noted below), </i>the video embeded and the audio have been taken by me using my camera / recording equipment. I feel the images and video, just like the sound recordings, are an important part of the experience to help reflect that time; that place.</p>\n')
    a.write('<p>I try to capture images which reflect the emotions of the location and in a way, the emotions of the day, whether be dark or joyfull. </p>\n')
    a.write('<p class="about_indent">PNG - Mostly edited using GIMP.</p>\n')
    a.write('<p class="about_indent">SVG - Mostly edited using SVG-Edit.</p>\n')
    a.write('<p class="about_indent">MP4 - Edited using Shotcut.</p>\n')
    a.write('<p class="about_indent">WAV and MP3 - Mostly edited using Audacity</p>\n')
    a.write('<p><i>**<u> Exception</u>: Social Media Icons linking to accounts.</i></p>\n')
    a.write('<p><i>**<u> Exception</u>: Affiliate Link images.</i></p>\n')
    a.write('<p><i>**<u> Exception</u>: Software screen shots of linked software.</i></p>\n')
    a.write('<h2>HTML and CSS</h2>\n')
    a.write('<p>This site has been built by myself. I scripted the site based on HTML, CSS and Python. I specifically chose not to include JavaScript in my coding but JavaScript is used via third party scripts e.g. Google Analytics. Flexbox in the CSS allows the site to be repsonsive / mobile friendly.</p>\n')
    a.write('<p>Scripting software used is Visual Studio Code</p>\n')
    a.write('<p>Building this site myself has allowed me the opportunitity to learn many concepts of HTML, CSS and Python. Influences and guidance has mostly come from YouTube, web searches, trial and error. I am comfortable acknowledging there shall be errors in this site or that the script could have been   written more efficient. Thats part of the learning experience. Maybe one day I may rebuild the site from scratch again with an improved style... Maybe?</p>\n')
    a.write('<p>Colours used in this site:</p>\n')
    a.write('<p class="about_indent">Black: rgb(0, 0, 0)</p>\n')
    a.write('<p class="about_indent">White: rgb(255, 255, 255)</p>\n')
    a.write('<p class="about_indent">Orangered: rgb(255, 69, 0)</p>\n')
    a.write('</article>\n')

append_close_body_tag(page)
append_footer_tags(page)
append_close_html_tag(page)

source = page
target = './pages/' + source
move_file(source,target)


# ==========================================================
#                 COOKIE POLICY Page
# ==========================================================
valuePageTitle = 'Cookie Policy'
page = linkCookie

clr_existing_file(page)
append_head_tags_page(page)
append_NavBar(page)
append_open_body_tag(page)

with open(page,'a') as a:      
    a.write('<article class="cookie">\n')    
    a.write('<h1>Cookie Policy</h1>\n')      
    a.write('<p><b>'+ websiteName +'</b> is committed to providing quality services to you and this policy outlines the sites ongoing obligations to you in respect to cookies via this site.</p>\n')
    a.write('<h2>Cookies</h2>\n')
    a.write('<p>Cookies are files with small amount of data that is commonly used an anonymous unique identifier. These are sent to your browser from a website that you visit and are stored on your computers hard drive. Third party applications such as Google Analytics and Social Media Sites may use cookies or other internet technologies to provide information on the use of this website and certain online products and services. Information in a cookie does not personally identify you. However, it provide details of the areas of the site which you have been browsing and the number of times that you have accessed the website. Cookies from this website are not used by us to collect or store personal information.</p>\n')
    a.write('<p>If you feel uncomfortable about the use of cookies, some browsers such as Chrome and FireFox allow the user to disable cookies all together from the settings / options menu.</p>\n')
    a.write('<h2>Policy Updates</h2>\n')
    a.write('<p>This Policy may change from time to time and is available on this website.</p>\n')
    a.write('<h2>Cookie Policy Complaints and Enquiries</h2>\n')
    a.write('<p>If you have any queries or complaints about our Cookie Policy please contact us at:</p>\n')
    a.write('<a href="'+ linkTwitter +'"><p><b>'+ linkTwitter +'</b></p></a>\n')   
    a.write('</article>\n')

append_close_body_tag(page)
append_footer_tags(page)
append_close_html_tag(page)

source = page
target = './pages/' + source
move_file(source,target)

       
# ==========================================================
#                 PRIVACY POLICY Page
# ==========================================================
valuePageTitle = 'Privacy Policy'
page = linkPrivacy

clr_existing_file(page)
append_head_tags_page(page)
append_NavBar(page)
append_open_body_tag(page)

with open(page,'a') as a:  
    a.write('<article class="privacy">\n') 
    a.write('<h1>Privacy Policy</h1>\n') 
    a.write('<p><b>'+ websiteName +'</b> is committed to providing quality services to you and this policy outlines our ongoing obligations to you in respect of how we manage your Personal Information.</p>\n')
    a.write('<p>We have adopted the Australian Privacy Principles (APPs) contained in the Privacy Act 1988 (Cth) (the Privacy Act). The NPPs govern the way in which we collect, use, disclose, store, secure and dispose of your Personal Information.</p>\n')
    a.write('<p>A copy of the Australian Privacy Principles may be obtained from the website of The Office of the Australian Information Commissioner at www.aoic.gov.au</p>\n')
    a.write('<h2>What is Personal Information and why do we collect it?</h2>\n')
    a.write('<p>Personal Information is information or an opinion that identifies an individual. Examples of Personal Information we may collect include: names, addresses, email addresses, phone and facsimile numbers.</p>\n')
    a.write('<p>This Personal Information is obtained in many ways including our website, from other publicly available sources and from third parties. We dont guarantee website links or policy of authorised third parties.</p>\n')
    a.write('<p>We collect your Personal Information for the primary purpose of providing our services to you, providing information to our clients and marketing. We may also use your Personal Information for secondary purposes closely related to the primary purpose, in circumstances where you would reasonably expect such use or disclosure. You may unsubscribe from our mailing/marketing lists at any time by contacting us in writing.</p>\n')
    a.write('<p>When we collect Personal Information we will, where appropriate and where possible, explain to you why we are collecting the information and how we plan to use it.</p>\n')
    a.write('<h2>Sensitive Information</h2>\n')
    a.write('<p>Sensitive information is defined in the Privacy Act to include information or opinion about such things as an individuals racial or ethnic origin, political opinions, membership of a political association, religious or philosophical beliefs, membership of a trade union or other professional body, criminal record or health information.</p>\n')
    a.write('<p>Sensitive information will be used by us only:</p>\n')
    a.write('<ul>\n')
    a.write('<li class="privacy_indent">\n')
    a.write('<p>For the primary purpose for which it was obtained.</p>\n')
    a.write('</li>\n')
    a.write('<li class="privacy_indent">\n')
    a.write('<p>For a secondary purpose that is directly related to the primary purpose.</p>\n')
    a.write('</li>\n')
    a.write('<li class="privacy_indent">\n')
    a.write('<p>With your consent; or where required or authorised by law.</p>\n')
    a.write('</li>\n')
    a.write('</ul>\n')
    a.write('<h2>Third Parties</h2>\n')
    a.write('<p>Where reasonable and practicable to do so, we will collect your Personal Information only from you. However, in some circumstances we may be provided with information by third parties. In such a case we will take reasonable steps to ensure that you are made aware of the information provided to us by the third party.</p>\n')
    a.write('<p>Our Service may contain links to other sites. If you click on a third-party link, you will be directed to that site. Note that these external sites are not operated by us. Therefore, we strongly advise you to review the Privacy Policy of these websites. We have no control over, and assume no responsibility for the content, privacy policies, or practices of any third-party sites or services.</p>\n')
    a.write('<h2>Cookies</h2>\n')
    a.write('<p>Cookies are files with small amount of data that is commonly used an anonymous unique identifier. These are sent to your browser from the website that you visit and are stored on your computers hard drive. We use cookies and other internet technologies to manage our website and certain online products and services. Information in a cookie does not personally identify you. However, it provides us with details of the areas of the site which you have been browsing and the number of times that you have accessed our website. Our website cookies are not used to collect or store personal information.</p>\n')
    a.write('<h2>Disclosure of Personal Information</h2>\n')
    a.write('<p>Your Personal Information may be disclosed in a number of circumstances including the following:</p>\n')
    a.write('<ul>\n')
    a.write('<li class="privacy_indent">\n')
    a.write('<p>Third parties where you consent to the use or disclosure; and</p>\n')
    a.write('</li>\n')
    a.write('<li class="privacy_indent">\n')
    a.write('<p>Where required or authorised by law.</p>\n')
    a.write('</li>\n')
    a.write('</ul>\n')
    a.write('<h2>Security of Personal Information</h2>\n')
    a.write('<p>Your Personal Information is stored in a manner that reasonably protects it from misuse and loss and from unauthorized access, modification or disclosure.</p>\n')
    a.write('<p>When your Personal Information is no longer needed for the purpose for which it was obtained, we will take reasonable steps to destroy or permanently de-identify your Personal Information. However, most of the Personal Information is or will be stored in client files which will be kept by us for a minimum of 7 years.</p>\n')
    a.write('<h2>Access to your Personal Information</h2>\n')
    a.write('<p>You may access the Personal Information we hold about you and to update and/or correct it, subject to certain exceptions. If you wish to access your Personal Information, please contact us in writing.</p>\n')
    a.write('<p><b>'+ websiteName +'</b> will not charge any fee for your access request, but may charge an administrative fee for providing a copy of your Personal Information.</p>\n')
    a.write('<p>In order to protect your Personal Information, we may require identification from you before releasing the requested information.</p>\n')
    a.write('<h2>Maintaining the Quality of your Personal Information</h2>\n')
    a.write('<p>It is an important to us that your Personal Information is up to date. We will take reasonable steps to make sure that your Personal Information is accurate, complete and up-to-date. If you find that the information we have is not up to date or is inaccurate, please advise us as soon as practicable so we can update our records and ensure we can continue to provide quality services to you.</p>\n')
    a.write('<h2>Policy Updates</h2>\n')
    a.write('<p>This Policy may change from time to time and is available on our website.</p>\n')
    a.write('<h2>Privacy Policy Complaints and Enquiries</h2>\n')
    a.write('<p>If you have any queries or complaints about our Privacy Policy please contact us at:</p>\n')
    a.write('<a href="'+ linkTwitter +'" class="privacy_indent"><p><b>'+ linkTwitter +'</b></p></a>\n')
    a.write('<a id="privacy_template_link" href="https://www.business.vic.gov.au/__data/assets/word_doc/0011/1113599/BV-Privacy-Policy-Template-Update-2017.docx">\n')
    a.write('<p>Privacy Template</p>\n')
    a.write('</a>\n')
    a.write('</article>\n')

append_close_body_tag(page)
append_footer_tags(page)
append_close_html_tag(page)

source = page
target = './pages/' + source
move_file(source,target)


# ==========================================================
#                 SITEMAP Page
# ==========================================================
dictionary = data
articleNumber = 0
valuePageTitle = 'Site Map'
page = linkSiteMap

clr_existing_file(page)
append_head_tags_page(page)
append_NavBar(page)
append_open_body_tag(page)

with open(page,'a') as a:  
    a.write('<div class="sitemap">\n') 
    a.write('<h1>Site Map</h1>\n')
    a.write('<a href="'+ websiteURL   +'">Home Page</a>\n')   

dictionary = data
for d in dictionary:   
    try: 
        valuePageName = dictionary[d]['pageName'] + '.html'
        articlePath = valuePageName
    except: 
        print('CRITICAL FAIL = Page needs a Name..... script TERMINATED')
        print('CRITICAL FAIL = Page needs a Name..... script TERMINATED')
        print('CRITICAL FAIL = Page needs a Name..... script TERMINATED')
        exit()
    # ================
    try: 
        valuePageTitle = dictionary[d]['pageTitle']
    except: 
        valuePageTitle = ""
        print('Page Title has ZERO value')
    # ================
    articleNumber = articleNumber + 1
    with open(page,'a') as a:  
        a.write('<a class="sitemap_indent" href="'+ valuePageName +'">{:03}'.format(articleNumber) +' - '+ valuePageTitle +'</a>\n')    

with open(page,'a') as a:  
    a.write('<a href="'+ linkAbout   +'">About</a>\n')    
    a.write('<a href="'+ linkCookie  +'">Cookie Policy</a>\n')    
    a.write('<a href="'+ linkPrivacy +'">Privacy Policy</a>\n')    
    a.write('<a href="'+ linkSiteMap +'">Site Map</a>\n') 
    a.write('<a href="'+ linkTwitter   +'">Twitter</a>\n')    
    a.write('<a href="'+ linkInstagram +'">Instagram</a>\n')    
    a.write('<a href="'+ linkYoutube   +'">YouTube</a>\n')    
    a.write('<a href="'+ linkBandcamp  +'">Bandcamp</a>\n')  
    a.write('</div>\n') 

append_close_body_tag(page)
append_footer_tags(page)
append_close_html_tag(page)

source = page
target = './pages/' + source
move_file(source,target)




# def append_build_error404_page(x):
#     with open(x,'a') as a:      
#         a.write('<article class="compliance__article">\n')
#         a.write('<div class="error-page-404">\n')
#         a.write('<hr>\n')
#         a.write('<h1>An Error Has Occured</h1>\n')
#         a.write('<p>The Link you have selected is either broken or page is missing.</p>\n')
#         a.write('<p>Link below will take you back to the home page.</p>\n')
#         a.write('<a href="'+ websiteURL +'">\n')
#         a.write('<p><b>Return to Homepage</b></p>\n')
#         a.write('</a>\n')
#         a.write('<hr>\n')
#         a.write('</div>\n')
#         a.write('</article>\n')















# ==========================================================
#                 Build EQUIPMENT.HTML Page
# ==========================================================

# equipment = {
#     'item1':{
#         'itemName': 'Sony Headphones',
#         'itemImage': '../img/sony_headphones.jpg',
#         'itemLink': 'ItemLinkSonyHeadphone',     
#         },
#     'item2':{
#         'itemName': 'Zoom H6 Recorder',
#         'itemImage': '../img/zoom_h6.jpg',
#         'itemLink': 'ItemLinkZoomH6',  
#         },
#     'item3':{
#         'itemName': 'Zoom Accessories',
#         'itemImage': '../img/zoom_accessories.jpg',
#         'itemLink': 'ItemLinkZoomAccessories',  
#         },
#     'item4':{
#         'itemName': 'Zoom Shotgun Mic',
#         'itemImage': '../img/zoom_shotgun_microphone.jpg',
#         'itemLink': 'ItemLinkZoomMicrophone',     
#         },
#     'item5':{
#         'itemName': 'Zoom Windsock',
#         'itemImage': '../img/zoom_windsock.jpg',
#         'itemLink': 'ItemLinkZoomWindsock',  
#         }
#     }


# valuePageTitle = 'Equipment'
# page = linkNavMenuItem1

# clr_existing_file(page)
# append_head_page_content(page)
# append_open_body_tag(page)
# append_nav_page_content(page)
# append_hero_section_PAGE(page)
# append_open_main_tag(page)
# append_open_article_wrapper_tag(page)
# x = page
# dictionary = equipment
# with open(x,'a') as a: 
#         a.write('<article class="compliance__article">\n')
#         a.write('<div class="compliance__article__title">\n')
#         a.write('<h1>Equipment</h1>\n')
#         a.write('</div>\n')
#         a.write('<div class="compliance__article__content">\n')
#         a.write('<p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Blanditiis numquam asperiores cum quo aut perspiciatis error dicta tenetur nobis dolor atque impedit possimus aspernatur id officia ducimus excepturi, eum sint.    </p>\n')
#         a.write('</div>\n')
        
#         a.write('<div class="compliance__article__content flex__row">\n')

# for d in dictionary:     
#     itemName = dictionary[d]['itemName']
#     itemImage = dictionary[d]['itemImage']
#     itemLink = dictionary[d]['itemLink']    
#     with open(x,'a') as a: 
#         a.write('<a href="'+ itemLink +'" class="short__article radius">\n')
#         a.write('<div class="short__article__numimg flex__column">\n')
#         a.write('<div class="box page__article__product__plain">\n')
#         a.write('<img loading="lazy" src="'+ itemImage +'" alt="">\n')
#         a.write('</div>\n')
#         a.write('<div>\n')
#         a.write('<h2>'+ itemName +'</h2>\n')
#         a.write('</div>\n')
#         a.write('</div>\n')
#         a.write('</a>\n')        
       
# with open(x,'a') as a: 
#     a.write('</div>\n')
#     a.write('</article>\n')

# append_close_main_tag(page)
# append_footer_page_content(page)
# append_close_body_tag(page)
# append_close_html_tag(page)

# source = page
# target = 'pages/' + source
# move_file(source,target)






# # ===========================
# # special page: error404.html
# # ===========================
# valuePageTitle = 'Error 404'
# page = 'error404.html'
# execute_build_compliance_page_ABOVE(page)
# append_build_error404_page(page)
# execute_build_compliance_page_BELOW(page)
# source = page
# target = 'pages/' + source
# move_file(source,target)


# def append_article_content(x):
#     with open(x,'a') as a:        
#         a.write('<article class="page__article__container page__article__background">\n')
#         a.write('<h1 class="page__article__title">'+ valuePageTitle  +'</h1>\n')
#         a.write('<div class="page__article__details__container">\n')
#         a.write('<p><span>Location: </span>'+ valueLocation +'</p>\n')
#         a.write('<p><span>Format: </span>'+ valueAudioFormat +'</p>\n')
#         a.write('<p><span>Duration: </span>'+ valueDuration +'</p>\n')
#         a.write('<p><span>Recorder: </span>'+ valueRecorder +'</p>\n')
#         a.write('<p><span>Microphone: </span>'+ valueMicrophone +'</p>\n')
#         a.write('<p><span>Audio Editing: </span>'+ valueAudioEditing +'</p>\n')
#         a.write('<p><span>Video Available: </span>'+ valueVideoAvailable +'</p>\n')
#         a.write('<p><span>Delivery: </span>'+ valueDelivery +'</p>\n')
#         a.write('</div>\n')
#         a.write('<div class="page__article__image">\n')
#         a.write('<img src="../img/'+ valuePageImagePath +'" alt="">\n')
#         a.write('</div>\n')
#         a.write('<div class="page__article__text">\n')
#         a.write('<p>'+ valueDescription +'</p>\n')
#         a.write('</div>\n')
#         a.write('<div class="container__video__and__download">\n')
#         a.write('<div class=" responsive__article__video__container">\n')
#         a.write('<div class="responsive__article__video">\n')
#         a.write('<iframe loading="lazy" width="560" height="315" src="https://www.youtube.com/embed/5bsqGX3Inpw" frameborder="0"allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n')
#         a.write('</div>\n')
#         a.write('</div>\n')
#         a.write('<section class="page__article__external__link__container">\n')
#         a.write('<a href="Link To Bandcamp">Download Audio</a>\n')
#         a.write('</section>\n')
#         a.write('</div>\n')
#         a.write('</article>\n')
#         a.write('<div class="transparent__divider divider-20"></div>\n')


# def append_external_link(x):
#     with open(x,'a') as a:
#         a.write('<section class="page__article__external__link__container">\n')
#         a.write('<a href="'+ linkExternalDownload +'">Download Audio</a>\n')
#         a.write('</section>\n')
#         a.write('<div class="transparent__divider divider-20"></div>\n')


# def append_library_link(x):
#     with open(x,'a') as a:
#         a.write('<h2>You May Also Like....</h2>\n')
#         a.write('<section class="box__wrapper">\n')
#         a.write('<a class="box" href="./pages/0001.html"><img loading="lazy" src="../img/0001.jpg" alt="">\n')
#         a.write('<h2>Footsteps Tram Tracks</h2>\n')
#         a.write('</a>\n')
#         a.write('<a class="box" href=""><img loading="lazy" src="../img/0002.jpg" alt="">\n')
#         a.write('<h2>Footsteps Bush Track</h2>\n')
#         a.write('</a>\n')
#         a.write('<a class="box" href=""><img loading="lazy" src="../img/0002.jpg" alt="">\n')
#         a.write('<h2>title</h2>\n')
#         a.write('</a>\n')
#         a.write('</section>\n')
#         a.write('<div class="transparent__divider divider-20"></div>\n')


# def append_disclosure_content(x):
#     with open(x,'a') as a:
#         a.write('<section class="page__article__product__disclosure__container">\n')
#         a.write('<h2>Field Recording Equipment....</h2>\n')
#         a.write('<section class="box__wrapper">\n')
#         a.write('<a class="box page__article__product__plain" href=""><img loading="lazy" src="../img/sony_headphones.jpg" alt="">\n')
#         a.write('</a>\n')
#         a.write('<a class="box page__article__product__plain" href=""><img loading="lazy" src="../img/zoom_h6.jpg" alt="">\n')
#         a.write('</a>\n')
#         a.write('<a class="box page__article__product__plain" href=""><img loading="lazy" src="../img/zoom_accessories.jpg" alt="">\n')
#         a.write('</a>\n')
#         a.write('</section>\n')
#         a.write('<div class="page__article__product__disclosure">\n')
#         a.write('<p>DISCLAIMER: This page contains affiliate links, which means that if you follow one of my product links or use a discount code, please be aware that I may recieve a commission.</p>\n')
#         a.write("<p>I'd also like to say THANKYOU for the support if you do.</p>\n")
#         a.write('<p>I really appreciate it. </p>\n')
#         a.write('</div>\n')
#         a.write('</section>\n')