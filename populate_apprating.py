# coding: utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT_Project.settings')

import django
django.setup()

from AppRating.models import Category, App


def populate():
             user1 = add_user('leifos', 'leifos')
             user2 = add_user('laura', 'laura')
             user3 = add_user('david', 'david')
             user4 = add_user('louis', 'louis')
             
             app_cat1 = add_cat('Games')
             app_cat2 = add_cat('Social')
             app_cat3 = add_cat('Music')

             appid = "1053012308"
             app1 =  add_app(appid = appid,
                     appname = "Clash Royal",
                     category = app_cat1,
                     description = "<p>Enter the Arena! From the creators of Clash of Clans comes a real-time multiplayer game starring the Royales, your favorite Clash characters and much, much more.<br><br>Collect and upgrade dozens of cards featuring the Clash of Clans troops, spells and defenses you know and love, as well as the Royales: Princes, Knights, Baby Dragons and more. Knock the enemy King and Princesses from their towers to defeat your opponents and win Trophies, Crowns and glory in the Arena. Form a Clan to share cards and build your very own battle community.<br> <br>Lead the Clash Royale Family to victory!<br><br>PLEASE NOTE! Clash Royale is free to download and play, however, some game items can also be purchased for real money. If you don't want to use this feature, please disable in-app purchases in your device's settings. Also, under our Terms of Service and Privacy Policy, you must be at least 13 years of age to play or download Clash Royale.<br> <br>A network connection is also required.<br> <br>FEATURES<br>● Duel players from around the world in real-time and take their Trophies<br>● Earn chests to unlock rewards, collect powerful new cards and upgrade existing ones<br>● Destroy opponent’s towers and win Crowns to earn epic Crown chests<br>● Build and upgrade your card collection with the Clash Royale Family along with dozens of your favorite Clash troops, spells and defenses<br>● Construct your ultimate Battle Deck to defeat your opponents<br>● Progress through multiple Arenas all the way to the top<br>● Form a Clan to share cards and build your very own battle community<br>● Challenge your Clanmates and friends to a private duel<br>● Learn different battle tactics by watching the best duels on TV Royale<br><br><br>Support<br>Are you having problems? Visit http://supercell.helpshift.com/a/clash-royale/ or http://supr.cl/ClashRoyaleForum or contact us in game by going to Settings &gt; Help and Support.<br><br>Privacy Policy: <br>http://supercell.com/en/privacy-policy/<br><br>Terms of Service:<br>http://supercell.com/en/terms-of-service/<br><br>Parent’s Guide:<br>http://supercell.com/en/parents/</p>",
                     developer = "Supercell Oy",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg",
                     likecount = 22,
                     dislikecount = 10)

             appid = "1055704405"
             add_app(appid = appid,
                     appname = "Barista Blitz",
                     category = app_cat1,
                     description = "<p>Move tiles and combine yummy ingredients in this addictive puzzle game with a caffeinated twist! Create hundreds of tasty drinks and snacks on your journey from trainee barista to culinary master. Show tile matching ability on the game board as you travel to wonderful restaurants around the world, using strategy and even luck to make every customer smile!<br><br>Key Features<br>An awesome new way to Match 3! <br>Hundreds of sumptuous levels to conquer with locations including the Coffee Shop, Sushi Bar, Ice Cream Stand and Pizza Parlor.<br>Craft over 100 treats including iced coffees, velvet cupcakes, sushi rolls, cheeseburgers, chocolate sundaes, and even pepperoni pizza!<br>Multiple game modes with a variety of objectives each level offers a new challenge and great new ways to succeed!<br>Grab special bonus tiles including Magic Coins, and avoid pesky hazards like Onion Volcanoes and Broken Steamers.<br>Use invaluable special boosters for an extra advantage such as Diamonds and Lucky Cats!<br>Explore a wonderful action packed world with beautiful graphics to make you smile.<br>Move tiles around the board in a swirl to create multiple matches at once, just like a real Barista swirls steamed milk into a Cappuccino to make designs!<br>Challenging but rewarding gameplay.<br>Only on iOS  looks great on all iPhone and iPad devices!</p>",
                     developer = "King",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg",
                     likecount = 84,
                     dislikecount = 80)

             appid = "1041808803"
             add_app(appid = appid,
                     appname = "Beat Stomper",
                     category = app_cat1,
                     description = "<p>Music, Neon light, Geometry. <br>Jump, Hold , Stomp.<br>The perfect combination of pure joy.<br>It is born for you, and you are born for it.<br><br>What are you waiting for?</p>",
                     developer = "Rocky Hong",
                     price = "1.49",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")

             appid = "553834731"
             app2 =  add_app(appid = appid,
                     appname = "Candy Crush Saga",
                     category = app_cat1,
                     description = "<p>Candy Crush Saga, from the makers of Candy Crush Soda Saga &amp; Farm Heroes Saga!<br><br>The sweetest game around!<br><br>Join Tiffi and Mr. Toffee on their sweet adventure through the Candy Kingdom. Travel through magical lands, visiting wondrous places and meeting deliciously kookie characters! Switch and match your way through hundreds of levels in this delicious puzzle adventure.  The sweetest game just keeps getting sweeter!<br><br>Take on this deliciously sweet Saga alone or play with friends to see who can get the highest score!&nbsp;<br><br>Candy Crush Saga is completely free to play but some in game items such as extra moves or lives will require payment.<br><br>You can turn off the payment feature by disabling in app purchases in your device’s settings.<br><br>Candy Crush Saga features:<br><br>Collect sugar drops to advance along the sugar track for special suprises!<br><br>Tasty candy graphics that will leave you hungry for more<br><br>Unwrap delicious environments and meet the sweetest characters<br><br>Helpful magical boosters to help with challenging levels&nbsp;<br><br>Complete adventurous levels and unlock treats<br><br>Easy and fun to play, challenging to master&nbsp;<br><br>Hundreds of sweet levels&nbsp;in the Candy Kingdom more added every 2 weeks!<br><br>Leaderboards to watch your friends and competitors!<br><br>Easily sync the game between devices and unlock full game features when connected to the Internet<br><br>Already a fan of Candy Crush Saga?&nbsp;Like us on Facebook or follow us on Twitter for the latest news:<br><br>facebook.com/CandyCrushSaga<br><br>twitter.com/CandyCrushSaga<br><br>Last but not least, a big THANK YOU goes out to everyone who has played Candy Crush Saga!<br><br>Minimum iOS version recommended: 5.1.1</p>",
                     developer = "King",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")

             appid = "529479190"
             add_app(appid = appid,
                     appname = "Clash of Clans",
                     category = app_cat1,
                     description = "<p>From rage-­filled Barbarians with glorious mustaches to pyromaniac wizards, raise your own army and lead your clan to victory! Build your village to fend off raiders, battle against millions of players worldwide, and forge a powerful clan with others to destroy enemy clans.<br> <br>PLEASE NOTE!  Clash of Clans is free to download and play, however, some game items can also be purchased for real money. If you don't want to use this feature, please disable in-app purchases in your device's settings.  Also, under our Terms of Service and Privacy Policy, you must be at least 13 years of age to play or download Clash of Clans. <br><br>A network connection is also required.<br><br>FEATURES<br>●	Build your village into an unbeatable fortress <br>●	Raise your own army of Barbarians, Archers, Hog Riders, Wizards, Dragons and other mighty fighters<br>●	Battle with players worldwide and take their Trophies<br>●	Join together with other players to form the ultimate Clan<br>●	Fight against rival Clans in epic Clan Wars <br>●	Build 18 unique units with multiple levels of upgrades<br>●	Discover your favorite attacking army from countless combinations of troops, spells, Heroes and Clan reinforcements <br>●	Defend your village with a multitude of Cannons, Towers, Mortars, Bombs, Traps  and Walls<br>●	Fight against the Goblin King in a campaign through the realm<br><br>PLAYER REVIEWS <br>Clash of Clans proudly announces over one million five star reviews on the App Store.<br><br>SUPPORT<br>Chief, are you having problems?  Visit http://supercell.helpshift.com/a/clash-of-clans/ or http://supr.cl/ClashForum or contact us in game by going to Settings &gt; Help and Support.<br><br>Privacy Policy:<br>http://www.supercell.net/privacy-policy/<br><br>Terms of Service:<br>http://www.supercell.net/terms-of-service/<br><br>Parent’s Guide:<br>http://www.supercell.net/parents</p>",
                     developer = "Supercell",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")

             appid = "1053533457"
             app3 =  add_app(appid = appid,
                     appname = "Color Switch",
                     category = app_cat1,
                     description= "<p>Tap the ball carefully through each obstacle and your ball will switch color with some powerups.<br>You must follow the color pattern on each obstacle to cross it ! <br><br>Be careful not to pass through the wrong color, or you’ll have to start again.</p>",
                     developer = "Marc Lejeune",
                     price  = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg",
                     likecount = 23,
                     dislikecount = 8)

             appid = "1060017016"
             add_app(appid = appid,
                     appname = "Dirac",
                     category = app_cat1,
                     description="<p>FROM: MEDIOCRE, Apple design award winning lab behind mind altering experiments SMASH HIT and DOES NOT COMMUTE.<br><br>SUBJECT: Explore the microverse with top scientists from across the world using the revolutionary DIRAC engine.<br><br>MESSAGE: Congratulations!<br><br>Thanks to the Mediated intern opportunity colocation research (MEDIOCRE) laboratory, you have<br>been given the exclusive opportunity to work with DIRAC, the latest in computerized quantum<br>disentanglement technology. You have been granted unlimited and unsupervised access to the DIRAC<br>mkII Quasi-Fibonacci de-unfocusing vectorscope terminal. Through phase-distorted intermodulation<br>inference you will be able to manually disentangle and sort through the macroscopic existence<br>of the microverse.<br><br>Press the appropriately labeled button below to claim your shot at the understated glamour of<br>life as a lab technician (intern).</p>",
                     developer = "Mediocre AB",
                     price = "1.49",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg",
                     likecount = 12)

             appid = "940452319"
             app4 =  add_app(appid = appid,
                     appname = "Dragon Land",
                     category = app_cat1,
                     description = "<p>Welcome to the land of dragons! Dragon Land is a groundbreaking 3D platform game like you’ve never seen on mobile: stunning levels, evil bosses, challenging skill features and a multiplayer mode!<br><br>Fun is guaranteed: jump, dash, climb and glide your way through every episode. Unlock new dragons and master different skills!<br><br>Enjoy a jaw-dropping experience in colorful landscapes. Start with one dragon and use it to rescue his friends from tough bosses! As your dragon and skill collection grows, so will the difficulty of the challenges.<br><br>FEATURES:<br>- Campaign mode: play over 100 levels full of rewards and items to find!<br>- Dozens of unique dragons: they all have their own special skills. Collect them all!<br>- Enhance your dragons by leveling them up and customizing them with cool skins.<br>- Secret levels: find keys to unlock these extra-tough, extra-rewarding areas.<br>- Multiplayer: play against other players in real time races and climb the rankings!<br>- Quick play: one hit, infinite levels. How far you can get? Beat your friend scores in this challenging mode!<br><br>Dragon Land is a multiplatform game: You can play on lots of devices. Please note that the game currently requires iPhone 4S, iPad 2, iPad mini or iPod Touch 5th Generation or newer.<br><br>Are you enjoying the game? We’d like to know! Leave us a nice review sharing your thoughts!<br><br>Having an issue? Go to Settings &gt; Help &gt; Support, we’ll try to help you the best way we can!<br>Dragon Land is FREE to download and FREE to play. However, you can purchase in-app items with real money. If you wish to disable this feature, please turn off the in-app purchases in your phone or tablet’s Settings.</p>",
                     developer = "Social Point",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")

             appid = "606080169"
             add_app(appid = appid,
                     appname = "Hardest Game Ever 2",
                     category = app_cat1,
                     description = "<p>Ranked #1 (Overall) in US, UK, Canada, Germany, Australia, ... for HARDEST GAME EVER 1, HARDEST GAME EVER 2 is definitely a game you don't want to miss out!<br><br>From the developers that brought you the world #1 ranking games you won't want to miss its sequel 'Hardest Game Ever 2'!<br><br>Hardest Game Ever 2 is a series of fun and exciting mini-game that measures your reaction time to the milliseconds and pixels! See how fast you can slap and how sharp is your reaction to catch the eggs before they touch the floor in milliseconds! Hardest Game Ever 2 promises to bring you hours of adrenaline drain! Challenge your family and friends and find out who's got the fastest reaction on iPhone/iPod/iPad!<br><br>Featuring:<br>+ Simple 3 Button Game Play<br>+ 24 Stages with 4 Challenging Levels<br>+ Ranking with Facebook Pals<br>+ Simple yet addictive gameplay<br>+ Multi-language Instructions<br><br><br><br><br>Read a few testimonial from our gamers for 0.03 seconds, testimonials don't lie:<br><br>Amazing! - 5/5 Stars<br>by Lainie24 - 10 February 2011<br>",
                     developer="Orangenouse Studios",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")

             appid = "996583546"
             add_app(appid = appid,
                     appname = "Speed Guess",
                     category = app_cat1,
                     description = "<p>Draw, doodle, sketch and guess words with friends and make new friends. Speed Guess Something is a sequel toDraw Something, the most popular social drawing and guessing game, with many new fun features added.<br> <br>While you can continue to draw and guess with friends and other players in a turn based game, we now introduce a brand new PvP challenge mode - ‘Speed Guess’. Play a real time PvP challenge with friends, to guess drawings and sketches correctly in the shortest time possible. Win a game and challenge other players to beat your best time. Challenge friends directly to a duel for the highest score in a guessing match.<br><br>Highlights: <br>Challenge friends in a real time PvP game on Speed Guess mode.<br>Enjoy the addictive turn based drawing game in Draw &amp; Guess mode.<br>Sketch and show your creativity with paint brushes to your friends.<br>Make new friends with other gamers via chat.<br>Get featured on our Facebook page if your artwork is awesome.<br>Earn badges and unlock achievements.<br>Showcase your achievements, game stats and recent activity to your friends via profiles.<br>Fully backward compatible - retain all your progress from Draw Something.<br> <br>No Drawing Skills Required! Stick figures, doodles and a sense of humor are welcome! Just wiggle your finger to sketch a doodle masterpiece! Get in on the fun! Download now and experience for yourself the laugh-out-loud game.<br><br>ADDITIONAL DISCLOSURES<br>Use of this application is governed by the Zynga Terms of Service. These Terms are available athttp://m.zynga.com/legal/terms-of-service.<br>For specific information about how Zynga collects and uses personal or other data, please read our privacy policy at http://m.zynga.com/privacy/policy. Zynga’s Privacy Policy is also available through the Privacy Policy field in the Developer section below.<br>The game is free to play, however in-app purchases are available for additional content and premium currency. In-app purchases range from $0.99 to $24.99.<br>This game does permit a user to connect to social networks, such as Facebook, and as such players may come into contact with other people when playing this game.<br>Terms of Service for Social Networks you connect to in this game may also apply to you. You will be given the opportunity to participate in special offers, events, and programs from Zynga Inc and its partners.</p>",
                     developer = "Zynga Inc.",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg",
                     likecount = 44,
                     dislikecount = 8)





             appid = "389801252"
             add_app(appid = appid,
                     appname = "Instagram",
                     category = app_cat2,
                     description = "<p>Instagram is a simple way to capture and share the world's moments. Transform your everyday  photos and videos into works of art and share them with your family and friends. <br><br>See the world through somebody else's eyes by following not only the people you know, but inspirational Instagrammers, photographers, athletes, celebrities and fashion icons. Every time you open Instagram, you'll see new photos and videos from your closest friends, plus breathtaking moments shared by creative people across the globe.<br><br>Over 400 million people use Instagram to: <br><br>* Edit photos and videos with free, custom-designed filters. <br>* Improve photos with 10 advanced creative tools to change brightness, contrast and saturation as well as shadows, highlights and perspective.<br>* Find  people to follow based on the accounts and photos they already love.<br>* Make videos look cinematic with Instagram's custom-built stabilization.<br>* Instantly share photos and videos on Facebook, Twitter, Tumblr and other social networks. <br>* Connect with Instagrammers all over the world and keep up with their photos and videos. <br>* Send private photo and video messages directly to friends.<br>* Use Handoff to switch between your Apple Watch and your iPhone</p>",
                     developer = "Instagram Inc.",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")

             appid = "447188370"
             add_app(appid = appid,
                     appname = "Snapchat",
                     category = app_cat2,
                     description = "<p>Life's more fun when you live in the moment :) Happy Snapping!<br><br>* * *<br><br>Please note: Snapchatters can always capture or save your messages, such as by taking a screenshot or using a camera. Be mindful of what you Snap!</p>",
                     developer = "Snapchat Inc.",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg",
                     likecount = 6,
                     dislikecount = 2)

             appid = "284882215"
             app5 =  add_app(appid = appid,
                     appname = "Facebook",
                     category = app_cat2,
                     description = "<p>Keeping up with friends is faster than ever.<br>See what friends are up to<br>Share updates, photos and videos<br>Get notified when friends like and comment on your posts<br>Text, chat and have group conversations<br>Play games and use your favorite apps<br><br>Read our Data Use Policy, Terms and other important info in the legal section of our App Store description.<br><br>Continued use of GPS running in the background can dramatically decrease battery life. Facebook doesn’t run GPS in the background unless you give us permission by turning on optional features that require this.</p>",
                     developer = "Facebook Inc.",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")

             appid = "304878510"
             add_app(appid = appid,
                     appname = "Skype",
                     category = app_cat2,
                     description = "<p>Skype keeps the world talking. Free messaging, voice and video calls with anyone for free.<br><br>- Talk face to face with a video call.<br>- New group video calls with up to 25 people.<br>- Free voice calls to anyone else on Skype. Add up to 25 people on a group call.<br>- Message your friends in an instant and add up to 300 people to a group chat.<br>- Call mobiles and landlines at low rates (Skype to Skype calls are always free). <br>- Share photos, video messages, your location and add emoticons and Mojis to your chat.<br>- Skype’s available on smartphones, tablets, PCs, Macs, and even some TVs. Now it’s even easier to stay connected to friends and family – no matter the device they’re on.<br>- Available for Apple Watch – your notifications and chats available on your wrist.<br><br>Learn more at skype.com<br><br><br>System requirements:<br>iOS 7.0 or above (If you are using iOS 6 or earlier, you can download the last compatible version by tapping install/update and following the prompt to download.) The Apple Watch features require iOS 8.2 and of course, an Apple Watch.</p>",
                     developer="Skype Communications S.a.r.l",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")

             appid = "333903271"
             app6 =  add_app(appid = appid,
                     appname = "Twitter",
                     category = app_cat2,
                     description = "<p>Twitter is now available for Apple Watch. <br><br>Tweet, Retweet, reply and favorite in a flash. Quickly see recent Tweets and top trends. Share your location, a song, or your thoughts with a flick on the wrist. It's Twitter, but littler.<br>_<br><br>Twitter is a free app that lets you connect with people, express yourself, and discover more about all the things you love.<br><br>See what your favorite celebs and athletes are chatting about. Be the first to hear breaking news. Catch a glimpse behind the scenes at concerts, sporting events, and more.<br><br>Then join the conversation: Tweet your own text, photos, and video to your followers — and maybe make a few fans along the way.<br><br>Get inspired. Be social. Even send private messages to friends. All in real time, as big (and little) things happen, from anywhere you happen to be.</p>",
                     developer = "Twitter Inc.",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg",
                     likecount = 9)

             appid = "512727332"
             add_app(appid = appid,
                     appname = "Flipagram",
                     category = app_cat2,
                     description = "<p>Tens of millions of monthly users worldwide and growing!<br><br>Flipagram is the easiest way to create, share and discover amazing musical video stories! <br><br>Tell your story, your way: Shoot video to music or use your existing photos and videos, then pick the perfect soundtrack from millions of popular free choices.<br><br>Share your stories privately, or with the Flipagram community and beyond. Get featured, go viral, become a Flipastar! Our editors are always looking for fun, inspiring, or creative Flipagrams to feature to our fast-growing community.<br><br>Then explore a world of amazing stories by browsing channels, trending tags, or following all kinds of musicians, celebrities, and interesting Flipagrammers from around the globe! <br><br>Flipagram in 3 easy steps:<br>1. Capture - Shoot music videos or select photos &amp; video clips from camera roll, albums, or Facebook.<br>2. Create - add your favorite music, set timing, cool filters, and text to tell your story.<br>3. Share - on Flipagram or to Instagram, Facebook, Twitter, WhatsApp, or beyond.<br><br>NEW FEATURES<br> Create Full Screen Flips<br> Get Immersed in Full Screen Viewing<br> Add up to 60 seconds of Free Music<br> Share privately with Direct Messaging<br><br>FEATURES<br> Shoot music videos and lip sync dubs to your favorite songs<br> Add photos and video clips<br> Voice Narration<br> Auto-time for Instagram or Vine<br> Style with awesome filters<br> Pause and tap through Flipagrams one moment at a time<br> Get likes and comments<br> Reflip public Flipagrams and collect more likes when you get reflipped<br> Channels to help discover popular Flipagram content<br> Add your Instagram and Snapchat links to your profile<br> Top artists and songs on Flipagram charts<br> Beautiful fonts<br> Find friends to follow<br> Notifications of interesting activity<br> Explore users, #hashtags, and editor’s picks<br> Control the privacy of your profile and each Flipagram that you create<br> Easy sharing to all your favorite apps: Instagram, Facebook, Twitter, YouTube, Vine, Tumblr, Email, Text, Pinterest, FB Messenger, WhatsApp, KIK, or LINE.<br> Sharing to Sina Weibo &amp; WeChat for Chinese users</p>",
                     developer = "Flipagram Inc.",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")

             appid = "310633997"
             add_app(appid = appid,
                     appname = "WhatsApp Messenger",
                     category = app_cat2,
                     description = "<p>WhatsApp Messenger is a FREE messaging app available for iPhone and other smartphones. WhatsApp uses your phone's Internet connection (4G/3G/2G/EDGE or Wi-Fi, as available) to let you message and call friends and family. Switch from SMS to WhatsApp to send and receive messages, calls, photos, videos, and Voice Messages. <br><br>WHY USE WHATSAPP:  <br><br>NO FEES: WhatsApp uses your phone's Internet connection (4G/3G/2G/EDGE or Wi-Fi, as available) to let you message and call friends and family, so you don't have to pay for every message or call.* There are no subscription fees to use WhatsApp.<br><br>MULTIMEDIA: Send and receive photos, videos, and Voice Messages. <br><br>FREE CALLS: Call your friends and family for free with WhatsApp Calling, even if they're in another country.* WhatsApp calls use your phone's Internet connection rather than your cellular plan's voice minutes. (Note: Data charges may apply. Contact your provider for details. Also, you can't access 911 and other emergency service numbers through WhatsApp). <br><br>GROUP CHAT: Enjoy group chats with your contacts so you can easily stay in touch with your friends or family.<br><br>WHATSAPP WEB: You can also send and receive WhatsApp messages right from your computer's browser.<br><br>NO INTERNATIONAL CHARGES: There's no extra charge to send WhatsApp messages internationally. Chat with your friends around the world and avoid international SMS charges.* <br><br>SAY NO TO USERNAMES AND PINS: Why bother having to remember yet another username or PIN? WhatsApp works with your phone number, just like SMS, and integrates seamlessly with your phone's existing address book. <br><br>ALWAYS LOGGED IN: With WhatsApp, you're always logged in so you don't miss messages. No more confusion about whether you're logged in or logged out. <br><br>QUICKLY CONNECT WITH YOUR CONTACTS: Your address book is used to quickly and easily connect you with your contacts who have WhatsApp so there's no need to add hard-to-remember usernames.<br><br>OFFLINE MESSAGES: Even if you miss your notifications or turn off your phone, WhatsApp will save your recent messages until the next time you use the app.<br><br>AND MUCH MORE: Share your location, exchange contacts, set custom wallpapers and notification sounds, email chat history, broadcast messages to multiple contacts at once, and more!<br><br>*Data charges may apply. Contact your provider for details. <br>We're always excited to hear from you! If you have feedback, questions, or concerns, please email us at: <br>iphone-support@whatsapp.com <br><br>or follow us on twitter: <br><br>http://twitter.com/WhatsApp<br>@WhatsApp<br>---------------------------------------------------------<br><br>Note: WhatsApp is a telephony app, so iPod and iPad are not supported devices.</p>",
                     developer = "WhatsApp Inc.",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")

             appid = "429047995"
             add_app(appid = appid,
                     appname = "Pinterest",
                     category = app_cat2,
                     description = "<p>Pinterest is a visual bookmarking tool that helps you discover and save creative ideas. Use Pinterest to make meals, plan travel, carry out DIY projects and much more.<br><br>With Pinterest you can:<br><br>Pin from your mobile browser: save good things you find from around the web<br><br>Plan a project: home refurbs, garden redesigns and other DIY stuff<br><br>Get creative ideas: recipes to cook, articles to read, gifts to buy and creative ways to save money<br><br>Explore a hobby: from comic art and camping, to woodworking and weaving<br><br>Save travel inspiration: outdoor adventures, family fun, road trips and much more<br><br>Find your style: fashion, home décor, grooming tips and beauty inspiration</p>",
                     developer = "Pinterest Inc.",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg",
                     likecount = 21,
                     dislikecount = 12)

             appid = "319881193"
             add_app(appid = appid,
                     appname = "Grindr Xtra",
                     category = app_cat2,
                     description = "<p>More men, photos, and options for the guy on the go. Enjoy advanced features that only the world’s largest mobile gay dating and social network can offer.<br><br>Over 2 million guys in 196 countries use Grindr every day.  Grindr finds guys close to you for chatting and meeting anywhere in the world. Find your perfect guy right now.<br><br>Enjoy the premium features of Grindr Xtra: <br>Never see banner ads<br>Never miss a message with push notification alerts<br>Attract more attention by adding multiple Grindr Tribes to your profile, perfect for the man who’s not just a Bear or a Jock<br>View up to 300 guys<br>Swipe quickly through profiles and views<br>Use advanced filters like body type, ethnicity and relationship status to find exactly your type of guy<br>Keep your sexy selections in touch and avoid those who aren’t a match with unlimited favorites and blocks<br>And much more<br><br>Gay chatting, dating and playing are only a few taps away.<br><br>Grindr has multiple subscription options to choose from starting as low as $5.00 per month.<br>Payment will be charged to your iTunes Account at confirmation of purchase.<br>Your account will be charged for renewal within 24 hours prior to the end of the current 30, 90, 180, or 365 day subscription period. <br>Auto-renew may be turned off by going to your iTunes Account Settings and must be turned off at least 24 hours before the end of the current subscription period to take effect.<br>No cancellation of the current subscription is allowed during the active subscription period.<br><br>Note: Only adults 18 years or older are allowed to use Grindr and Grindr Xtra.<br><br>Check out : <br>Grindr’s privacy policy at: grindr.com/privacy-policy.<br>Grindr’s terms of service at: grindr.com/terms-of-service</p>",
                     developer = "Grindr LLC",
                     price = "0.79",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")
                 
                appid = "454638411"
                app7 =  add_app(appid = appid,
                        appname = "Messenger",
                        category = app_cat2,
                        description = "<p>Instantly reach the people in your life—for free. Messenger is just like texting, but you don't have to pay for every message (it works with your data plan). <br><br>Not just for Facebook friends: Message people in your phone book and just enter a phone number to add a new contact.<br><br>Group chats: Create groups for the people you message most. Name them, set group photos and keep them all in one place.<br><br>Photos and videos: Shoot videos and snap selfies or other photos right from the app and send them with one tap.<br><br>Free calls: Talk as long as you want, even with people in other countries. (Calls are free over Wi-Fi. Otherwise, standard data charges apply.)<br><br>Even more ways to message: <br>Bring your conversations to life with stickers. <br>Preview your camera roll photos and videos without leaving the conversation--then choose the perfect ones to send.<br>Record voice messages when you have more to say.<br><br>Extra features:<br>Know when people have seen your messages.<br>Forward messages or photos to people who weren't in the conversation.<br>Search for people and groups to quickly get back to them.<br>Turn on location to let people know when you're nearby.<br>See who's available on Messenger and who's active on Facebook. <br>Turn off notifications when you're working, sleeping or just need a break.<br>Stay logged in so you never miss a message.</p>",
                        developer = "Facebook Inc.",
                        price = "Free",
                        iconpath = "images/App/Games/" + appid + "/icon.jpeg",
                        imagepath1 = "images/App/Games/" + appid + "/screen1.jpeg",
                        imagepath2 = "images/App/Games/" + appid + "/screen2.jpeg",
                        imagepath3 = "images/App/Games/" + appid + "/screen3.jpeg")
        
             appid = "324684580"
             app8 =  add_app(appid = appid,
                     appname = "Spotify Music",
                     category = app_cat3,
                     description = "<p>Spotify is the best way to listen to music on mobile or tablet. <br><br>Search for any track, artist or album and listen for free. Make and share playlists. Build your biggest, best ever music collection. <br><br>Get inspired with personal recommendations, and readymade playlists for just about everything.<br><br>Listen absolutely free with ads, or get Spotify Premium.<br><br>Free on mobile<br>Play any artist, album, or playlist in shuffle mode.<br><br>Free on tablet<br>Play any song, any time.<br><br>Premium features<br>Play any song, any time on any device: mobile, tablet or computer.<br>Enjoy ad-free music. <br>Listen offline. <br>Get better sound quality.<br><br>Get your monthly Spotify Premium subscription through the app. If you choose to subscribe, you will be charged a price according to your country. The price will be shown in the app before you complete the payment. The subscription renews every month unless auto-renew is turned off at least 24 hours before end of the current subscription period. Your iTunes account will automatically be charged within 24 hours prior to the end of the current period and you will be charged for one month at a time.  You can turn off auto-renew at any time from your iTunes account settings. <br><br>Monthly prices:<br>AD 12.99 EUR / AR 7.99 USD / AU 14.99 AUD / AT 12.99 EUR / BE 12.99 EUR / BO 7.99 USD / BR 7.99 USD / BG 6.99 EUR / CA 12.99 CAD / CL 7.99 USD / CO 7.99 USD / CR 7.99 USD / CY 8.99 EUR / CZ 7.99 EUR / DK 129.00 DKK / DO 7.99 USD / EC 7.99 USD / SV 7.99 USD / EE 8.99 EUR / FI 12.99 EUR / FR 12.99 EUR / GB 12.99 GBP / DE 12.99 EUR / GR 8.99 EUR / GT 7.99 USD / HN 7.99 USD / HK 68.00 HKD / HU 6.99 EUR / IS 12.99 EUR / IE 12.99 EUR / IT 12.99 EUR / LV 8.99 EUR / LI 16.00 CHF / LT 8.99 EUR / LU 12.99 EUR / MY 6.99 USD / MT 8.99 EUR / MX 119.00 MXN / MC 12.99 EUR / NZ 16.99 NZD / NI 7.99 USD / NO 129.00 NOK / PA 7.99 USD / PY 7.99 USD / PE 7.99 USD / PH 3.99 USD / PL 6.99 EUR / PT 8.99 EUR / SG 9.99 USD / SK 7.99 EUR / ES 12.99 EUR / SE 129.00 SEK / CH 16.00 CHF / TW 210.00 TWD / NL 12.99 EUR / TR 12.99 TRY / UY 7.99 USD / US 12.99 USD<br><br>Privacy policy: http://www.spotify.com/legal/privacy-policy/<br>Terms of use: https://www.spotify.com/legal/end-user-agreement/<br><br>Love Spotify?&nbsp;<br>Like us on Facebook: http://www.facebook.com/spotify&nbsp;<br>Follow us on Twitter: http://twitter.com/spotify</p>",
                     developer = "Spotify Ltd.",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg",
                     likecount = 70)


             appid = "336353151"
             add_app(appid = appid,
                     appname = "SoundCloud",
                     category = app_cat3,
                     description = "<p>Millions of people use SoundCloud to listen to music and audio for free.<br><br>Wherever you are, whatever you’re doing. The SoundCloud app lets you hear more.<br> <br>More hip hop. More rock. More electronic. More classical. More house, jazz, audiobooks, sports…<br><br><br>KEY FEATURES<br> <br>- Discover new and trending music you won’t find anywhere else<br>- Listen to your favorite tracks and artists from a vast selection of music and audio<br>- Connect with friends and artists to hear what they share<br>- Create &amp; listen to playlists that fit your mood<br>- Shuffle your likes and playlists<br>- Browse tracks by genre<br>- Listen to your stream wherever you are using WiFi or data<br>- Play, pause and skip tracks from the lockscreen<br>- Sign in or register with Facebook, Google+, or your email<br><br>GET STARTED<br> <br>It’s easy to dive straight in and start discovering music &amp; audio. <br><br>Use Search to find your favorite tracks and artists. Tap the heart to 'like' a track – this will put it in your Collection and make it easy to listen again later.  You can also add tracks to personalized playlists. <br>Looking for a more relaxing listening and discovery experience? As you listen, you can easily start a Station from any of your favorite tracks to discover similar music. <br><br><br>Find out more on http://help.soundcloud.com/customer/portal/topics/110297-mobile-apps/articles<br><br>PRAISE FOR SOUNDCLOUD<br> <br>“SoundCloud is focused on building out a massive trove of content, weaving it all into the Web and making it easier to share. The “YouTube for audio” analogy looks increasingly apt, especially if its metrics continue to shoot skyward.” - ReadWrite<br> <br>“SoundCloud is a sharing machine. Remember the early days of audio online — when you had to download the Real Player or Windows Media Player to listen? The days of downloading before listening are over.” - USA Today<br> <br>“It's an evolution of audio's most vital self-service creation and discovery platform, music's best analogue to Twitter, YouTube, and Kindle Direct Publishing. It's not just finding or sharing songs or podcasts or spoken-word readings your friends may be listening to — it's finding and sharing the people who make those recordings, too.” - The Verge<br><br>COMMUNITY<br> <br>Like what you hear? Let us know, and share your discoveries with the world. <br> <br>SoundCloud Blog: http://blog.soundcloud.com<br>Facebook: http://www.facebook.com/soundcloud<br>Twitter: https://www.twitter.com/soundcloud<br>Tumblr: http://soundcloud.tumblr.com<br>Instagram: http://instagram.com/soundcloud<br><br>PROBLEMS? FEEDBACK?<br><br>The more you tell us, the better SoundCloud gets. <br><br>http://help.soundcloud.com/<br>https://twitter.com/SCsupport<br><br>PERMISSIONS<br><br>Your privacy is really important to us. We only ask for the permissions we need for the app to be at its best. <br><br>For more information, read http://help.soundcloud.com/customer/portal/articles/1575188-what-permissions-are-required-to-download-the-app<br><br>If you have any more questions get in touch with us - see the help section. <br><br>This app is available in English, Spanish &amp; Portuguese.</p>",
                     developer = "SoundCloud Ltd.",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")

             appid = "898358948"
             add_app(appid = appid,
                     appname = "DICE",
                     category = app_cat3,
                     description = "<p>Buy tickets to the best gigs in town with no booking or transaction fees on DICE. Find shows from Adele, Disclosure, Tame Impala, Years and Years, Taylor Swift, George Ezra, Wolf Alice, Four Tet, Jamie XX, Miguel, Skepta and Bring Me The Horizon amongst others hand-picked by our devoted music team.<br><br>-- MORE ABOUT US --<br><br>DICE is the only place where fans can buy face value tickets to the best gigs, club nights and festivals with no booking fees. When we say no booking fees, we don’t mean ‘no hidden fees’, we mean the price the artist and promoter intended you to pay. <br><br>We all have a world of music at our fingertips and in our headphones, but nothing can beat experiencing your favourite band, DJ, or artist live. We want to help you discover more live music. <br><br>Each show featured on DICE is hand-picked by a devoted music team with new acts added daily. Over 600 artists have sold tickets through DICE since launch, including Adele, Disclosure, Tame Impala, Years and Years, Taylor Swift, George Ezra, Wolf Alice, Four Tet, Jamie XX, Miguel, Skepta and Bring Me The Horizon among others.<br><br>Tickets are linked to the device they’re purchased on making them completely tout proof and, as it’s 100% mobile, you’ll never need to print a ticket again. <br><br>Can’t make a gig you’ve purchased tickets for? No problem, you can return unwanted tickets back to DICE for a full refund. Our unique “Waiting List” feature also means those who missed out are kept up-to-date as new tickets become available for sold out shows. <br><br>Featured in the App Store Best Apps of 2015 and The Guardian's Best Apps of 2014.<br><br>Live in London, Manchester, Bristol, Glasgow and Cardiff.<br><br>Apple Pay enabled.</p>",
                     developer = "DICE",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg",
                     likecount = 13)

             appid = "1036437162"
             add_app(appid = appid,
                     appname = "Music Memos",
                     category = app_cat3,
                     description = "<p>Music Memos is the easiest way for songwriters to capture and organise new musical ideas. Use your iPhone, iPad or iPod touch to record acoustic guitar, piano, voice or any musical instrument as high-quality, uncompressed audio. Then name, tag and rate your ideas to start building a library of all your favourite new song parts and riffs. Music Memos automatically detects your tempo, rhythmic feel and chords and lets you instantly hear your musical idea accompanied by a rhythm section with realistic drums and bass. View the chords you’ve played, add comments and lyrics, or share your recordings with friends or directly to Apple Music Connect.* And it’s easy to take your favourite ideas into GarageBand to add more instruments and continue building your song.<br><br>Quickly capture musical ideas<br>Easily record any musical idea using a simple interface<br>Instantly listen to your recorded song ideas with a virtual drummer and bass player, who follow along like a live band in the room<br>Adjust the groove and sound of the drum or bass using simple and intuitive controls to hear your song idea in different ways<br>Tune your guitar with a built-in instrument tuner<br><br>Build a library of song ideas<br>•&nbsp;Name any song idea, or delete unwanted recordings<br>•&nbsp;Tag your song ideas to help you find them later using keywords like verse, chorus, mellow, energetic, or add your own custom tags<br>•&nbsp;Rate your song idea 1–5 stars to help you identify your favourites<br>Supports iCloud Drive so your library of song ideas is always safe and available across all your iOS devices&nbsp;<br><br>View, edit and document your song ideas<br>Automatically analyses the music you played and displays musical measures and suggested chord names<br>Rename or provide further detail for any chord names throughout your song<br>The drum and bass performances adapt immediately to match any chord and rhythm edits<br>•&nbsp;Trim away any unwanted parts from the beginning and end of your recording<br>•&nbsp;Keep track of comments, lyric ideas, alternative guitar tunings or capo position<br><br>Share your new song<br>Use iCloud Drive to make your song ideas available across all your iOS devices<br>•&nbsp;Email any song idea to a friend to share your music, or to collaborate with other musicians<br>•&nbsp;Quickly open your idea in GarageBand for iOS to add more instruments and keep building your song<br>•&nbsp;Export a song idea to the Mac so you can work in GarageBand or Logic Pro X as a full multi-track production<br>Share to SoundCloud, YouTube and Apple Music Connect*&nbsp;<br><br>*Requires Apple Music Connect account</p>",
                     developer = "Apple",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg",
                     likecount = 36)

             appid = "1057125583"
             add_app(appid = appid,
                     appname = "Free Music Pro",
                     category = app_cat3,
                     description = "<p>Fully featured music discovery application!<br>Browse, Search, Listen and Enjoy free music on your iPhone, iPod and iPad. <br> <br>√ Millions of tracks available!<br>√ Single tap music streaming<br>√ Search for DJ, song, remix or cover<br> <br>Music player:<br>√ Full featured media player<br>√ Equalizer with BassBooster<br>√ Over 20 realistic EQ presets<br>√ Stylish audio Visualizer<br>√ Lock screen playback controls<br>√ Fine scrubbing<br>√ Background music playback<br> <br>Manager:<br>√ Sort by track name, date, duration<br>√ Create unlimited music playlists<br>√ Album covers<br>√ History of recently listened tracks</p>",
                     developer = "Dominic Renilla",
                     price = "1.49",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")

             appid = "475820434"
             add_app(appid = appid,
                     appname = "Notion",
                     category = app_cat3,
                     description = "<p>AS FEATURED IN APPLE ADS<br><br>Notion is a notation editor and playback tool for your iPad, iPhone and iPod Touch, (any iOS8 compatible device) giving you the convenience of an easy-to-use music creation tool right at your fingertips. An incredible composition app for any music lover, Notion gives you the ability to compose, edit, and playback scores using real audio samples performed by The London Symphony Orchestra recorded at Abbey Road Studios. You can capture your musical ideas anytime, and take this helpful application anywhere.<br><br>With a user-friendly interface and simple interactive piano keyboard, fretboard, and drum pad; Notion makes it easy to get started composing your music. And, with Notion's abundance of advanced functions you can take your most basic ideas to an entirely new level right on your iOS device.<br><br>In addition to the notation editor you can also hear your music performed with real audio samples, giving you the most realistic playback possible. Notion comes bundled with piano and orchestral samples recorded by The London Symphony Orchestra at Abbey Road Studios as well as popular instruments such as guitar, bass, and much more. The initial app download contains piano - you can then manage which of the bundled sounds to have on your device, or keep in the cloud, just tap on Sounds.<br><br>Begin your project by using the simple score setup tool or choose a template. You can also open MusicXML, Guitar Pro, and MIDI files. You can continue to alter your score and playback using a palette full of articulations, expressions, and dynamics. Or create the perfect balance using the full-featured multi-track mixer with effects.<br><br>Once you are happy with your creation you can share your work by emailing the Notion file. Or you can send MIDI or MusicXML files, or send an audio or PDF file. You can sync your scores across devices, and with Notion for Windows and Mac, by using iCloud and Dropbox. <br><br>Notion Features:<br>- Handwriting in-app purchase for iPad now available<br>- Enter, edit, and playback notation, tab, or both<br>- Orchestral samples by The London Symphony Orchestra recorded at Abbey Road Studios. <br>- Piano, keyboards, electric guitar, acoustic guitar, electric bass<br>- MIDI step-time entry with your favorite MIDI device or MIDI Bluetooth device<br>- Record real-time MIDI input into your score.<br>- Audition Mode: Use the on-screen virtual instruments to hear sounds before entering them into your score.<br>- Clean and intuitive user interface <br>- Support for retina display<br>- Native 64-bit support<br>- Option to tap in notes with finger or stylus<br>- Interactive piano keyboard, 24-fret guitar fretboard and drumpad for step, and realtime, entry<br>- Quick and simple selection palette <br>- Distortion and reverb effects<br>- Full audio mixer<br>- Full range of orchestral functions and articulations including: Staccato, Flutter tongues, Trills, Vibrato, and much more…<br>- Full range of guitar functions and articulations including: bends, vibrato, slides, hammer on, pull off, mutes, whammy bar techniques, bass slap, harmonics, and more…<br>- Drag score items such as dynamics<br>- Switch Instruments<br>- Transposition<br>- Insert text<br>- Rehearsal Marks<br>- Lyrics<br>- Chord Symbols and Diagrams<br>- Rhythm Slashes<br>- Cross staff beaming for grand staff instruments<br>- Swing<br>- Continuous and Page View<br>- Quick “Undo” and “Redo” functions<br>- Chord and melody modes<br>- Easy delete and erase capabilities <br>- Enter and edit title and composer information<br>- Save as an audio file<br>- Import .notion, MIDI, MusicXML, GuitarPro 3-5 files<br>- Export/email .notion, PDF, MusicXML, .WAV, AAC or MIDI files<br>- Sync with iCloud, Dropbox or iTunes File Sharing<br>- Print to AirPrint enabled printers<br>- Expand your bundled sound library with in-app purchases<br>- Help Files<br>- And much more…</p>",
                     developer = "NOTION Music Inc",
                     price = "10.99",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")

             appid = "459313476"
             add_app(appid = appid,
                     appname = "Tenuto",
                     category = app_cat3,
                     description = "<p>Tenuto is a collection of fifteen customizable exercises designed to enhance your musicality. From recognizing chords on a keyboard to identifying intervals by ear, it has an exercise for you. Tenuto also includes five musical calculators for accidentals, intervals, chords, analysis symbols, and twelve-tone matrices.<br><br>The musictheory.net exercises and calculators used by thousands are now available in your pocket.<br><br>Complete module list:<br><br>Staff-based Exercises<br>Note Identification<br>&nbsp;&nbsp;&nbsp;Identify the displayed note.<br>Key Signature Identification<br>&nbsp;&nbsp;&nbsp;Identify the displayed key signature.<br>Interval Identification<br>&nbsp;&nbsp;&nbsp;Identify the displayed interval.<br>Chord Identification<br>&nbsp;&nbsp;&nbsp;Identify the displayed chord.<br><br>Keyboard-based Exercises<br>Keyboard Identification<br>&nbsp;&nbsp;&nbsp;Identify the note name of the piano key.<br>Keyboard Reverse Identification<br>&nbsp;&nbsp;&nbsp;Identify the note by pressing a piano key.<br>Keyboard Interval Identification<br>&nbsp;&nbsp;&nbsp;Identify the interval of the highlighted piano keys.<br>Keyboard Chord Identification<br>&nbsp;&nbsp;&nbsp;Identify the chord of the highlighted piano keys.<br><br>Fretboard-based Exercises<br>Fretboard Identification<br>&nbsp;&nbsp;&nbsp;Identify the note of the highlighted fret.<br>Fretboard Interval Identification<br>&nbsp; &nbsp;Identify the interval of the highlighted frets.<br>Fretboard Chord Identification<br>&nbsp; &nbsp;Identify the chord of the highlighted frets.<br><br>Ear Training Exercises<br>Note Ear Training<br>&nbsp;&nbsp;&nbsp;Listen and identify the played note.<br>Interval Ear Training<br>&nbsp;&nbsp;&nbsp;Listen and identify the played interval.<br>Scale Ear Training<br>&nbsp;&nbsp;&nbsp;Listen and identify the played scale.<br>Chord Ear Training<br>&nbsp;&nbsp;&nbsp;Listen and identify the played chord.<br><br>Calculators<br>Accidental Calculator<br>&nbsp;&nbsp;&nbsp;Display the accidental for a note and key.<br>Interval Calculator<br>&nbsp;&nbsp;&nbsp;Display the interval for a note, type, and key.<br>Chord Calculator<br>&nbsp;&nbsp;&nbsp;Display the chord for a note, type, and key.<br>Analysis Calculator<br>&nbsp;&nbsp;&nbsp;Display the chord for a symbol and key.<br>Matrix Calculator<br>&nbsp;&nbsp;&nbsp;Display the twelve-tone matrix for a specified tone row.</p>",
                     developer = "musictheory.net",
                     price = "2.99",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg",
                     likecount = 120)

             appid = "554616591"
             add_app(appid = appid,
                     appname = "Digital Concert Hall",
                     category = app_cat3,
                     description = "<p>Watch and listen to classical music's finest conductors and soloists performing with the Berliner Philharmoniker– live as it happens or on-demand as it suits you.<br><br>“Classical music’s most advanced response to the digital revolution.” – FINANCIAL TIMES<br><br>Acclaimed directors take the helm of the Digital Concert Hall (DCH) productions inside the video studio in the Berlin Philharmonie. Seven remote-controlled HD cameras have been installed in the Philharmonie in Berlin which, along with excellent audio technology, ensure that the experience is as authentic as it is thrilling.<br><br>Download the app now and watch Sir Simon Rattle conducting Beethoven’s 4th and Mahler’s 1st symphonies FOR FREE!<br><br>- Over 40 live-streams every year in HD video*<br>- Hundreds of concert recordings on-demand*<br>- Historic concerts with Herbert von Karajan and Claudio Abbado*<br>- Hundreds of free exclusive interviews with the conductors and soloists<br>- Feature-length documentaries, incl. Rhythm is it! and Trip to Asia<br>- Free children's concerts for the whole family<br><br>*requires paid access<br><br>Featured conductors: Sir Simon Rattle, Claudio Abbado, Daniel Barenboim, Gustavo Dudamel, Alan Gilbert, Nikolaus Harnoncourt, Mariss Jansons, Zubin Mehta, Andris Nelsons, Yannick Nézet-Séguin, Seiji Ozawa, Kirill Petrenko, Christian Thielemann and many more.<br><br>Featured soloists: Yefim Bronfman, Renée Fleming, Christian Gerhaher, Matthias Goerne, Barbara Hannigan, Janine Jansen, Jonas Kaufmann, Leonidas Kavakos, Magdalena Kožená, Katia and Marielle Labèque, Yo-Yo Ma, Anne-Sophie Mutter, Murray Perahia, Maurizio Pollini, Thomas Quasthoff, Kate Royal, András Schiff, Mitsuko Uchida and many more.</p>",
                     developer = "Berliner Philharmoniker",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg",
                     likecount = 80)

             appid = "524299475"
             add_app(appid = appid,
                     appname = "AutoRap by Smule",
                     category = app_cat3,
                     description = "<p>Say something. AutoRap turns your speech into rap. Choose from 100+ beats from artists like Drake, Eminem, Nicki Minaj, Snoop Dogg and let AutoRap transform your words into a lyrical masterpiece! You may share your rap song and even go viral!<br><br>“You simply speak into your phone, and the app chops your voice and buries it in a whole mess of autotuney goodness —Engadget <br>I tried it…and this is just pure fun —Queen Latifah<br><br>Features: <br>- Talk mode: instantly turn your words in to a rap song<br>- Rap mode: Auto-tune your freestyle verses (corrects bad rapping) <br>- Remix - recreate the rap in different beats<br>- Rap Battles - show off your rapping. <br>- Discover Top rappers.  Get followers<br><br>The current catalog includes songs and beats by:  <br>- Drake<br>- Lil Wayne<br>- Nicki Minaj <br>- Eminem feat. Rihanna <br>- BOB <br>- T-Pain<br>- Snoop Dogg <br>- Ludacris <br>- Tupac feat. Dr. Dre <br>- Outkast <br>- Nelly <br>- Beastie Boys <br>- Kelis <br>- Chamillionaire <br>...and many more.   <br><br>NEW BEATS AND SONGS ADDED EVERY WEEK. <br><br>TALK MODE: <br>Talk into the app, and AutoRap magically morphs your speech into a legit rap. Create your own original rap songs with Freestyle Beats and Premium Songs from artists like Snoop Dogg and Nicki Minaj to AutoRap. The Rappification™ feature will turn you into a rap star! <br><br>RAP MODE: <br>It's all you! Dish a fresh rhyme in your own time and style. AutoRap autotunes your verses to match the tempo of the beat you chose. (Headphones recommended for Rap Mode)<br><br>REMIX - FUN, FUN, FUN:<br>Change the beat for the rap you've just created.  Try different beats and watch how your rap gets recreated in different styles.  Pick the one that works best for you.<br><br>SHARE, GO VIRAL: CONNECTING THE WORLD THROUGH MUSIC™<br>Rap about something that matters to you and go viral. Share your rap recordings with your friends via text message, email, Facebook or Twitter. Sing them a happy birthday they’ll never forget, or give ‘em the lowdown on the sandwich you ate for lunch.<br><br>RAP BATTLE: <br>You don't have to rap alone. Challenge your friends to an epic three-round, turn-by-turn rap-off and let AutoRap seamlessly weave verses from you and your opponent into a single track of rapperly rapport. <br><br><br>We add new beats to the songbook 3 times per week. Check back to see what's new! <br><br><br>ALWAYS FREE: <br>We offer one song that is ALWAYS FREE: “Turkey Burgers” - so you can use the app anytime you want completely free, without spending any money, ever. <br><br>UNLIMITED VIP SUBSCRIPTION: <br>- You can subscribe for $2.99*<br>- Subscribers have unlimited access to ALL songs and beats, the remix table, and much more! <br>- Payment will be charged to iTunes Account at confirmation of purchase <br>- Subscription automatically renews unless auto-renew is turned off at least 24-hours before the end of the current period <br>- Account will be charged for renewal within 24-hours prior to the end of the current period at the cost of the chosen package <br>- Subscriptions may be managed by the user and auto-renewal may be turned off by going to the user's Account Settings after purchase <br>- No cancellation of the current subscription is allowed during active subscription period <br>- You can read our privacy policy at http://www.smule.com/privacy <br>- Any unused portion of a free trial period, if offered, will be forfeited when the user purchases a subscription to that publication <br><br>*All subscription prices are equal to the value Apple's App Store Matrix determines to be the equivalent of $2.99 USD</p>",
                     developer = "Smule",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")

             appid = "292738169"
             add_app(appid = appid,
                     appname = "Deezer Music",
                     category = app_cat3,
                     description = "<p>With Deezer you can listen to as much music as you want for FREE.<br><br>Just search for the artists, albums and tracks you love and listen without limits.<br><br>Create your own playlists using our recommendations and 100% customised mixes!<br><br>It's all free thanks to advertising. If you don't want ads, switch to Premium+.<br><br>In free mode on your phone:<br>- Listen to mixes inspired by a track, artist, playlist or album.<br>***Want more freedom? Try Premium+ for 15 days, free!***<br><br>In free mode on your tablet:<br>- Listen to the tracks you want at any time, with ads.<br><br>In Premium+ mode, you get all the music you want, anytime, anywhere:<br>- All the tracks you want<br>- No ads, no interruptions<br>- Download your music to listen even without a connection<br>- Enjoy high quality sound<br>- Deezer and CarPlay: From your mobile to your car stereo<br><br>NEW: Deezer is now available on Apple Watch<br>Have the time of your life thanks to Deezer on Apple Watch. Listen to your favourite tracks, discover your future favourites with Flow, and enjoy all the latest music releases at the flick of a wrist.<br><br><br>Follow Deezer!<br>Facebook: http://www.facebook.com/deezer <br>Twitter: https://twitter.com/deezeruk<br><br><br>-----------------------------------<br><br>Download and use the Deezer app for free. Subscribe to Deezer Premium+ to benefit from additional features (as described above).<br><br>Deezer Premium+ is a subscription service with a monthly charge of:&nbsp;<br>AL 6.99 EUR / AR 9.99 USD / AT 9.99 EUR / AU 12.99 AUD / BE 9.99 EUR / BH 9.99 USD / BO 8.99 USD / BR 9.99 USD / BW 4.99 USD / CA 9.99 CAD / CH 13.00 CHF / CL 9.99 USD / CO 9.99 USD / CR 6.99 USD / CZ 6.99 EUR / DE 9.99 EUR / DK 99 DKK / EC 6.99 USD / ES 9.99 EUR / FI 9.99 EUR / FR 9.99 EUR / GB 9.99 GBP / GR 6.99 EUR / GT 6.99 USD / HN 6.99 USD / HR 6.99 EUR / HU 6.99 EUR / ID 5.99 USD / IE 9.99 EUR / IT 9.99 EUR / LT 6.99 EUR / LU 9.99 EUR / MU 4.99 USD / MX 99 MXN / MY 4.99 USD / NL 9.99 EUR / NO 98 NOK / NZ 12.99 NZD / PE 8.99 USD / PH 5.99 USD / PL 6.99 EUR / PT 9.99 EUR / PY 8.99 USD / RO 6.99 EUR / RU 199 RUB / SE 99 SEK / SG 9.98 SGD / SI 6.99 EUR / SK 6.99 EUR / SN 4.99 USD / SV 6.99 USD / TH 5.99 USD / TN 4.99 EUR / TR 12.99 TRY / UY 8.99 USD / ZA 64.99 ZAR&nbsp;<br><br>Payment will be charged to iTunes Account at confirmation of purchase.<br>Account will be charged for renewal within 24-hours prior to the end of the current period, at the same price.<br>No cancellation of the current subscription is allowed during active subscription period<br><br>*** Manage your subscription directly from your iPhone ***<br>Subscriptions may be managed by the user and auto-renewal may be turned off by going to the user's Account Settings after purchase.<br>1. Tap the Settings icon on your mobile, then tap the Store icon.<br>2. Sign in with your iTunes ID.<br>3. Tap View Apple ID then Manage App Subscriptions.<br>4. You will be able to see when your next payment is due, or cancel your automatic renewal.<br><br>*** You may cancel your subscription at any time ***<br>Renewal of your monthly Deezer Premium+ subscription is automatic.&nbsp;<br>You can cancel this automatic renewal at any time, at least 24 hours before the end of the current subscription period.<br><br>Privacy policy: http://www.deezer.com/legal/personal-datas.php<br>Terms of use: http://www.deezer.com/legal/cgu.php</p>",
                     developer = "Deezer",
                     price = "Free",
                     iconpath = "images/App/" + appid + "/icon.jpeg",
                     imagepath1 = "images/App/" + appid + "/screen1.jpeg",
                     imagepath2 = "images/App/" + appid + "/screen2.jpeg",
                     imagepath3 = "images/App/" + appid + "/screen3.jpeg")
                     
                     
             # Print out apps.
             for c in Category.objects.all():
                  for a in App.objects.filter(category=c):
                      print "- {0} - {1}".format(str(c), str(a))

            add_comment(user1, app1, 5, 'wow')
            add_comment(user1, app2, 4, 'nice')
            add_comment(user1, app3, 5, 'well done')
            add_comment(user2, app4, 5, 'Perfect')
            add_comment(user2, app5, 5, 'Perfect')
            add_comment(user3, app6, 3, 'not good')
            add_comment(user4, app7, 5, 'wow')
            add_comment(user4, app8, 4, 'wow...')


def add_app(appid, appname, category, description, developer, price, iconpath, imagepath1, imagepath2, imagepath3, averscore=0, viewcount=0, likecount=0, dislikecount=0):
    a = App.objects.get_or_create(appid=appid)[0]
    a.appname = appname
    a.description = description
    a.category = category
    a.averscore = averscore
    a.developer = developer
    a.price = price
    a.iconpath = iconpath
    a.imagepath1 = imagepath1
    a.imagepath2 = imagepath2
    a.imagepath3 = imagepath3
    a.viewcount = viewcount
    a.likecount = likecount
    a.dislikecount = dislikecount
    a.save()
    return a

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

def add_user(username, password):
    c = User.objects.get_or_create(username=username, password=password)[0]

def add_comment(user, app, score, content):
    app.averscore = (app.averscore * app.commentcount + score) / (app.commentcount + 1)
    app.commentcount = app.commentcount + 1
    app.save()

    c = Comment.objects.get_or_create(user=user, app=app, score=score, content=content)[0]
    c.save
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting AppRating population script..."
    populate()