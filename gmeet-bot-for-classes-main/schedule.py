
# TODO Starts@poweron Deploys@time-match  Notifies@10minsbefore Ends@time-match 



from bot import botinstance
bot=botinstance()

Schedule = {
    "Monday": {
        1: {
            "Name": "Linux",
            "Time": "9:30",
            "Link": "https://meet.google.com/vha-vraf-kea"
        },
        2: {
            "Name": "ML",
            "Time": "11:30",
            "Link": "https://meet.google.com/dek-gxmb-pes"
        },
        3: {
            "Name": "ML",
            "Time": "11:30",
            "Link": "https://meet.google.com/vha-vraf-kea"
        },

    },

    "Tuesday": {
        1: {
            "Name": "Linux",
            "Time": "9:30",
            "Link": "https://meet.google.com/vha-vraf-kea"
        },
        2: {
            "Name": "ML",
            "Time": "11:30",
            "Link": "https://meet.google.com/dek-gxmb-pes"
        },
        3: {
            "Name": "ML",
            "Time": "11:30",
            "Link": "https://meet.google.com/vha-vraf-kea"
        },

    },

}


link = 'https://meet.google.com/vha-vraf-kea'
driver = bot.runInstance(link)


# day = fetch every days "Day" from time module

# while(True):
    # main loop running till shutdown
    
    # * checks every 10 mins, if time is matching and run an instance
    # link=Schedule[Day][Number][Link]
    # driver = bot.runInstance(link)


    # TODO: instance reminds me after 50 mins of supposed-to-be start time, whereas the meeting is ended by the teacher and if exception-raised, then handled by me

    # * If all meetings over, then loop breaks, when counter has reached max, say 3
    # * Make it headless if possible and then errors are displayed as popups