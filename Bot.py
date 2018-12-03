 #!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import smtplib
from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol
#Ask User Login VARs
print("Please Login, This Bot Requires Your Login Info, So Instagram Can't Detect its a Bot.")
UserPreDefined = input('Enter Your Username: ')
PassPreDefined = input('Enter Your Password: ')
print("\n")

###Dont Touch the Code Above Or it Can Break the Whole Bot.

################################ User Settings ####################################
#Here Are the Bot Settings
#I`d Suggest Not to Touch Any other Setting, Unless, You know What Your Doing

bot = InstaBot(
    login=UserPreDefined,
    password=PassPreDefined,
    like_per_day=1000,
    comments_per_day=250,
    tag_list=['follow4follow', 'f4f', 'followforfollowback', 'follow4followback', 'followbackinstantly', 'follow4follow', 'likeforfollowers', 'f4follow', 'f4followback', 'f4fback'],
    tag_blacklist=[],
    user_blacklist={},
    max_like_for_one_tag=100,
    follow_per_day=110,
    follow_time=1 * 60,
    unfollow_per_day=10,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[["Awesome!", "Cool!", "Nice!", "Damn.", "Great!", "Hey.", "Hi.", "Lol.", "Best!"],
                  ["Photo", "Picture", "Pic", "Shot", "Snapshot"],
                  ["is", "looks", "feels", "is really"],
                  ["Great", "Super", "Good", "Very Good", "Good", "Wow",
                   "WOW", "Cool", "GREAT","Magnificent", "Magical",
                   "Very Cool", "Stylish", "Beautiful", "So Beautiful",
                   "So Stylish", "So Professional", "Lovely",
                   "So Lovely", "Very Lovely", "Glorious","So Glorious",
                   "Very Glorious", "Adorable", "Excellent", "Amazing"],
                  [".", "..", "...", "!", "!!", "!!!"]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[],
    unfollow_whitelist=[])
######################################## User Setting END ##########################################

###Dont Touch the Code Below Or it Can Break the Whole Bot.

while True:

    #Ask for mode
    print("\n")
    print("Please Choose Your MODE\n")
    print("MODE 0 = ORIGINAL MODE")
    print("MODE 1 = MODIFIED MODE ")
    print("MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    print("MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    print("MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    print("MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT\n")

    print("DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED")
    print("USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD\n")

    mode = int(input('Mode: '))
    ################################################################################
    #Print Mode Info, And Parse Mode
    print("\n")
    print("\n")
    print("Bot Is Now Starting")
    print("CTRL+C or VolDown+C to cancel this Bot or wait 7 seconds to start")
    time.sleep(7)
    ####################################################################################
    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")
