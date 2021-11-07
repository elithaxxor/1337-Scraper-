import os
import sys
import time
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"
    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"
    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"
    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"


###########
color = Colors()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset




    # @staticmeth od


# previous class class TorrentParser(): (( LOOK FOR IT TO CHANGE IN CODE))
# 1 getn_download_len - keeps getting lenght of download to compare to max len
# 2 list_iterator -- iterate .txt and update counter
# 3 torrent download navigator - on torrent download page, this will navigate the dropdown. change accordingly.

class Navigator(webdriver.Chrome):
    chrome_options = Options()
    Keys = Keys
    options = webdriver.ChromeOptions
    driver = ChromeDriverManager().install()
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
    _args = []


        ######
    # executiable_path = ChromeDriverManager().install()
    # driver = webdriver.Chrome(executable_path=executiable_path, chrome_options=chrome_options)
    #


    def __init__(self, counter00=0):
        super(Navigator, self).__init__()
         #super(Navigator, self).__init__()

        self.chrome_options = Options()
        self.driver = ChromeDriverManager().install()
        self.implicitly_wait(20)
        self.torrent_list00 = []
        self.self = self
        self.cwd = os.getcwd()
        self.count = self.count
        self.list_len = list_len
        self.iterations_left = self.iterations_left
        self.counter00 = self.counter00
        self.options = self.chrome_options()
        self.torrent_downloads = self.torrent_downloads
        self.current_iterations = self.list_len - self.counter00
        self.chrome_options = ChromeOptions()
        self.chrome_options.add_extension("/Users/a-robot/PycharmProjects/pythonProject/gpu_venv/ad_blocker.crx")
        self.counter00 = counter00



        #self.executable_path = r"/Users/a-robot/PycharmProjects/pythonProject/gpu_venv"
        #self.executable_path = ChromeDriverManager().install()

       # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                  #chrome_options=chrome_options)

    def __str__(self):
        return '{}({})'.format(type(self).__name__, ', '.join(repr(getattr(self, a)) for a in self._args)) ## guidelines for repr
       # return self.__stringify(str)

    @staticmethod
    def period_wait():
        period = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        # multi = [2,2,2,2,2,2,2,2,2,2]
        period_len = len(period)
        for z, x in enumerate(period):
            print(x * z)
            time.sleep(.2)
            if z <= period_len:
                z += 1
                print(f"{yellow}{x * z}{reset}")
                continue
            elif z == period_len:
                break

    def start(self, first_run=True):
        self.counter00 = 0
        first_run = True
        try:
            while first_run:
                parser = Navigator()
                self.list_len = Navigator.get_download_len(self)
                print(f'{yellow}The List Len {reset}[{self.list_len}]')
                self.iterations_left = self.list_len - self.counter00
                if self.iterations_left == 0:
                    print(f'Parsed {self.counter00} items\n system-exiting.')
                    sys.exit(1)

                elif self.counter00 == 0: ## SET COUNTER VARIABLE TO 1 TO SKIP TEST
                    chrome_options = ChromeOptions()
                    chrome_options = Options()
                    chrome_options.add_extension("/Users/a-robot/PycharmProjects/pythonProject/gpu_venv/ad_blocker.crx")
                    executable_path = r"/Users/a-robot/PycharmProjects/pythonProject/gpu_venv"
                    self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                              chrome_options=chrome_options)
                    #  driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
                    if self.driver:
                        print('Driver Succesfully Installed')
                        time.sleep(2)
                        self.driver.get('https://1337x.to/')
                        self.driver.implicitly_wait(25)  ### no need to call more than once
                        print(self.driver)
                        #  print(OS)
                        print(f'**Total List Len [{list_len}]')
                        time.sleep(4)
                    try:
                        print(f'{yellow}**[starting test before real fun.]{reset}')
                        print(f'{yellow}**[loading dummy file..]{reset}')
                        print(f'{red}**[CURRENT ITERATIONS..]{reset}\n[{self.counter00}]')
                        print(f'{red}**[LIST ITEMS IN ITERATION..]{reset}\n[{self.current_iterations}]')
                        time.sleep(1)
                        search_box = self.driver.find_element_by_id('autocomplete')
                        print(search_box.text)
                        search_box.click()

                        search_box.send_keys('chopper')
                        click_search_box = self.driver.find_element_by_class_name('flaticon-search')
                        search_box.send_keys(Keys.ENTER)
                        self.counter00 += 1
                        print(f'{yellow}**[completed dummy run..]{reset}')
                        print(f'{red}**[CURRENT ITERATIONS..]{reset}\n[{self.current_iterations}]')
                        print(f'{red}**[CURRENT ITERATIONS..]{reset}\n[{self.current_iterations}]')
                        Navigator.period_wait()

                        time.sleep(3)
                        first_run = False



                        Navigator.counter00 = 1
                    except Exception as e:
                        traceback.print_exc()
                        print(f'{red}**Error in First Run.. Ssomething to do with torrent/page and dropdown. {reset}\n {str(e)}]')
                        first_run = False

                if self.counter00 >= int(1):
                    print(f'\t\t{yellow}[---CHECK-- ]{yellow}:: FIRST_RUN = [{first_run}] [{self.counter00}]::{reset}\n**...[---PARSING-- ]')

                    print(f'\t\t{yellow}[---PARSING-- ]{yellow}::[{self.counter00}]::{reset}[---PARSING-- ]')
                    # first_run = False
                    print('X' * 50)
                    print(f'**Total List Len [{self.list_len}]')
                    print(f'**Completed Iterations [{self.counter00}]')
                    print(f'**Iterations Left [{self.iterations_left}]')
                    print('X' * 50)
                    self.counter00 += 1
                    time.sleep(7)
                    Navigator.period_wait()

                    self.driver.implicitly_wait(25)
                    search_box01 = self.driver.find_element_by_id('autocomplete')
                    print(search_box01.text)
                    search_box01.click()
                    search_box01.send_keys(Keys.CONTROL, "a")
                    search_box01.clear()
                    print(
                        f'starting list feed sequence\nThe List is [{self.list_len} long\n Passing the LIST PARSER #[{self.counter00}] of {self.iterations_left}')


                    if self.counter00 <= list_len: ### initiate snex tsequence after test
                        print('X' * 50)
                        counter, torrent_downloads = Navigator.list_iterator(self.counter00)
                        print(f'**Parsing [{torrent_downloads}]')
                        print(f'{yellow}[{self.counter00}] of {self.iterations_left} {reset}')
                        print('**Counter is less than list len')
                        search_box01.send_keys(torrent_downloads)
                    # search_box01.send_keys(Keys.ENTER)
                        time.sleep(.5)
                        print('X' * 50)

                    try:  ######
                        body = WebDriverWait(self.driver, 15).until(
                            EC.presence_of_element_located((By.CLASS_NAME, 'table-list-wrap'))
                            # EC.presence_of_all_elements_located((by.CLASS, 'table-list table table-responsive table-striped'))  ##
                        )
                        print(body.text)
                        print(), print()
                        href_link = body.find_element_by_xpath(
                            "/html/body/main/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]")
                        print(href_link.text)
                        self.counter00+= 1
                        print(f'{red} Reseting Iterator {reset} \n::[Current Iteration] [{self.counter00}]\n --[ITERATIONS LEFT]-- [{self.iterations_left}]')
                        print('X' * 50)


                    except Exception as e:
                        print('X' * 50)
                        time.sleep(.5)
                        print('X' * 50)
                        print(f'{red}--[ERROR IN FINDING ELEMENTS in TABLE XPATH]{reset}\n {str(e)}')
                        traceback.print_exc()
                        print(f'{red}e.message, e.args{reset}')
                        traceback.print_exc()
                        print('X' * 50)

                        continue

        except Exception as e:
            print('X' * 50)
            traceback.print_exc()
            print(f'{red} [ERROR IN START SEQUENCE]  \n{str(e)}')
            print(f'\n::[Current Iteration][{self.counter00}]\n - -[ITERATIONS LEFT] - - [{self.iterations_left}]')
            print(f'{red} [ERROR IN START SEQUENCE]  \n{str(e)}')

            print(f'{red}e.message, e.args{reset}')
            print('X' * 50)


    def get_download_len(self): # 1 getn_download_len - keeps getting lenght of download to compare to max len
        self.torrent_list_len = len(open('hrefdata.txt').readlines())
        global list_len
        self.list_len = self.torrent_list_len
        print(f'**Calculating List Len in \n[{self.cwd}]')
        time.sleep(1)
        print(f'{yellow}[List Length]-----  [{self.torrent_list_len}] ----{reset}')
        return self.list_len

    def list_iterator(self): # 2 list_iterator -- iterate .txt and update counter
        try:
            hrefdata = 'hrefdata.txt'
            cwd = os.getcwd()
           # self.count = self.counter00 ## too lazy to change all. may have to fix later.
            print(f'{yellow} **[Starting List Iterator]** {reset} [{self.counter00}]')
            if self.counter00 != 0:  ## cannot append empty list, the recursion below
                self.href_loc = str(cwd) + f'/{hrefdata}'
                self.href_str = f'** Data Read From Text Data From: [{self.href_loc}]--{self.counter00} ** [SYSTEM]'
                print(self.href_str)
                with open(self.href_loc, 'r') as f:
                    for href in f:
                        print('X' * 50)
                        print('PASS ONE')
                        print(f'**{yellow}Parsing item #[{self.counter00}]  in {self.href_loc} \n{href} ')
                        self.torrent_list = f.readlines(self.counter00)
                        self.torrent = f.readline(self.counter00)
                        self.website_list = [x.strip() for x in href]
                        href01 = self.torrent_list[-1]
                        print('X' * 50)

                        print('website list', self.website_list)
                        print('torrent list ', self.torrent_list)
                        print('href ', href)
                        print('href -1 ', href01)
                        print(f'[SYS]** TORRENT [{self.counter00}] \n {self.torrent}')
                        self.counter00 += 1
                        self.total_count = self.list_len - self.counter00
                        print('X' * 50)

                        print('X' * 50)

                        self.torrent_list00.append(self.torrent)
                        print(f'[SYS]** ADDED #[{self.counter00}] \n**Currently Adding{href}')
                        print(f'[SYS]** TOTAL ADDED #[{self.total_count}] \n {self.torrent_list00}')
                        print(f'[SYSTEM] Found {self.counter00} items in {self.href_loc}')
                        print(f'****[{self.counter00}] items remaining in {self.href_loc}')
                        print(f'[SYS]** TORRENTLIST00 -1 [{self.counter00}] \n {self.torrent_list00[-1]}')
                        print('X' * 50)

                        return self.counter00, self.torrent_list00


        except Exception as e:
            traceback.print_exc()
            print(f"{red}**[ERROR IN DICT READER]{reset}\n {str(e)}")
            traceback.print_exc()
            print(f'{red}e.message, e.args{reset}')
            sys.exit(1)

#  "//a[contains(@href,'" + _studnetID + "')]"
#  "//a[contains(@href,'" + _studnetID + "')]"
# driver.find_elements(By.XPATH("//*[contains(@class, 'coll-1 name')] or //a[contains(@href,'" + torrent_downloads + "')]")
## set up ax
#

    def torrent_download_navigator(self): # 3 torrent download navigator - on torrent download page, this will navigate the dropdown. change accordingly.
        try:
            print(f'{yellow}[Navigating] -- [ALL-LINKS TO CLICK]')
             ### this is code to click through torrent page and pull pull down downlaod link
            all_links = self.driver.find_element_by_xpath("//*[contains(@class, 'coll-1 name')]")

            if not all_links:
                print(f'{red}-[ERROR IN PARSING ALL_LINKS]\n moving on to single_link parse.\n **[{all_links.text}]')
                pass

            if all_links:
                print(f'{red}-[ERROR IN PARSING ALL_LINKS]\n moving on to single_link parse.\n **[{all_links.text}]')
                all_links.click()

        except Exception as e:
            time.sleep(.5)
            print('X' * 50)
            traceback.print_exc()
            print(f'{red}--[CANOT FIND ELEMENT IN DROPDOWN]{reset}\n {str(e)}')
            print('X' * 50)

        try:
            print(f'{yellow}[Navigating] -- [SINGLE-LINKS TO CLICK]')
            single_link = self.driver.find_element_by_xpath("//a[contains(@href,'" + self.torrent_downloads + "')]")
            if single_link:
                print('single all links\n', single_link.text)
                single_link.click()

        except Exception as e:
            time.sleep(.5)
            print('X' * 50)
            traceback.print_exc()
            print(f'{red}--[CANOT FIND ELEMENT IN DROPDOWN]{reset}\n {str(e)}')
            print('X' * 50)

        try:
            torrent_dropdown = self.driver.find_element_by_class_name("dropdown")
            if torrent_dropdown:
                print(f'{yellow}[FOUND TORRENT DROPDOWN BOXT]{reset}')
                print('Torrent Dropdown\n', torrent_dropdown.text)

                self.counter00 += 1
                first_run = True
                if self.counter00 == int(list_len): ## end sequence
                    print('X' * 50)
                    print('--[[FIN]]--')
                    print(f'{yellow} Total Torrents from List: [{self.torrent_list_len}] ')
                    print(f'[SYS]** TOTAL ADDED #[{self.total_count}] \n {self.torrent_list00}')
                    print(f'[SYSTEM] Found {self.count} items in {self.href_loc}')
                    print(f'[END]{yellow}**** System completed [{self.counter00}] passes. \n With [{self.iterations_left}] iterations left {reset}')

                    print(f'**{yellow} Parsed a total of : #[{self.counter00}] items\n from {self.href_loc} \n {self.torrent_list} ')
                    self.website_list_final = [x.strip() for x in self.href]
                    print(self.website_list_final)
                    print(self.href_str)
                    print('X' * 50)
                    time.sleep(10)
                    sys.exit(1)

                else:
                    self.counter00 += 1
                    pass

        except Exception as e:
            traceback.print_exc()
            print(f'{red}e.message, e.args{reset}')

            print('Exception in --[chained-action]-- cannot download link')
            print(e)
            self.counter00 += 1
            sys.exit(1)



    #     # for link in torrent_list00:
    #     print('PASS TWO')
    #     print(f'[SYS]** ADDED #[{count}] \n {link}')
    #     print(f'[SYS]** TOTAL ADDED #[{total_count}] \n {torrent_list}')
    #     print(f'[SYS]** TORRENT [{count}] \n {link}')
    #     print(f'[SYS]** TORRENT -1 [{count}] \n {link[-1]}')
    #     print(f'[SYS]** TORRENTLIST00 -1 [{count}] \n {torrent_list00[-1]}')
    #     torrent_list_1 = torrent_list00[-1]
    #     count +=1
    #     return count, link
    #
    # else:
    #     print(f'[SYSTEM] Found {count} items in .txt \moving on to test')
    #     href = r"https://1337x.to/"
    #     return href, count
    # # def list_iterator(**args, count=counter00):
    # def list_iterator(counter00):
    #     try:
    #         count = 0
    #         if count == counter00:
    #             href = r'1338x.to'
    #             print('Count is none')
    #             return count, href
    #         count +=1
    #
    #         if count > 0:
    #             torrent_list = []
    #             torrent_list00 = []
    #             hrefdata = 'hrefdata.txt'
    #             cwd = os.getcwd()
    #             href_loc = str(cwd) + f'/{hrefdata}'
    #             href_str = f'[SYSTEM]** Dump The Text Data To: [{href_loc}] ** [SYSTEM]'
    #             print(href_str)
    #
    #             try:
    #                 with open(hrefdata) as f:
    #                     f.readlines()
    #                     print(href_loc)
    #                     for href in f:
    #                         print('1111111')
    #                         torrent_list = f.readline(count)
    #                         website_list = [x.strip() for x in href]
    #                         print('website list', website_list)
    #                         print(type(website_list))
    #                         print('href link', href)
    #                         print(type(href))
    #                         print('torrent list ', torrent_list)
    #                         print(type(torrent_list))
    #                         index = 0
    #                         count = count + 1
    #                         for iterate in torrent_list:
    #                             total_count = count + 1
    #                             torrent_list.append(href)
    #                             print('2222222')
    #                             print(f'[SYS]** ADDED #[{count}] \n {iterate}')
    #                             print(f'[SYS]** TOTAL ADDED #[{total_count}] \n {torrent_list}')
    #                             print(f'[SYSTEM] Found {count} items in {href_loc}')
    #                             print(f'****[{count}] items remaining in {href_loc}')
    #
    #                             if iterate is None:
    #                                 count += 1
    #                                 print('did not find href in list:: arsing 1337x.to')
    #                                 print(f'the count is {count}')
    #                                 iterate = r'https://1337x.to/'
    #                                 return count, iterate
    #                             else:
    #                                 print(f'**parsing{count}\n{href}')
    #                                 return count, href
    #             except Exception as e:
    #                 print(str(e))
    #
    #         elif count is None:
    #             href = r'1338x.to'
    #             print('Count is none')
    #             return count, href
    #
    #         elif count == 0:
    #             href = r'1338x.to'
    #             print('Count is none')
    #             return count, href
    #
    #     except AttributeError:
    #         traceback.print_exc()
    #         href = r'1338x.to'
    #         print('atribute error')
    #         return count, href
    #
    #     except Exception as e:
    #         traceback.print_exc()
    #         traceback.print_exc()
    #         print(f"{red}**[ERROR IN DICT READER]{reset}\n {str(e)}")
    #         sys.exit(1)
    #




    #  sys.exit(1)

            # try:
            #     download_href = driver.find_element_by_link_text('http://itorrents.org/')
            #     # download_href = WebDriverWait(driver, 15).until( EC.presence_of_element_located((By.CLASS_NAME, "l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l8680f3a1872d2d50e0908459a4bfa4dc04f0e610"))
            #     if download_href:
            #         print('**Commencing Download Chain')
            #         action = ActionChains(driver)
            #         action.click(on_element=download_href)  # click on key
            #         action.send_keys(Keys.COMMAND + 't')  # send keys
            #         action.perform()  # execute action
            #         print('download_href \n', download_href.txt)
            #         # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
            #         download_href_click = driver.find_element_by_link_text('http://itorrents.org/').send_keys(
            #             Keys.COMMAND + 't')
            #
            #         counter00 += 1
            #         while True:
            #             if counter00 == int(list_len):
            #                 print('EOL--> SYS.EXIT')
            #                 Parsing = False
            #                 sys.exit(0)
            #             else:
            #                 break
            #


    # x = '30'
    #
    # elif int(ticker) is range(x):
    #
    #     pass

    #
    # try:
    #     #  magnet = driver.find_element
    #     magnet_pull = WebDriverWait(driver, 15).until(
    #         EC.presence_of_element_located((By.CLASS_NAME,
    #                                         "l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l8680f3a1872d2d50e0908459a4bfa4dc04f0e610"))
    #
    #     )
    #     print('magnetpull info')
    #     print(magnet_pull.text)
    #
    #     print(magnet_link.text)
    #     magnet_link.click()
    #
    # except Exception as e:
    #     traceback.print_exc()
    #
    #     print('MAGNET PULL ERROR', str(e))
    #

# driver.quit()


# my_element00 = driver.find_element_by_class_name('') ## <--- pass in class value  #-> class styling method
# print(my_element00)

#
#  #### DROP DOWN CLASSES FOR MAGNET / TORRENT DOWNLOAD ##
# <ul class="lfa750b508ad7d04e3fc96bae2ea94a5d121e6607 lcafae12a818cf41a5873ad374b98e79512c946c6">
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l8680f3a1872d2d50e0908459a4bfa4dc04f0e610" href="magnet:?xt=urn:btih:F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2&amp;dn=The+Titanic+Secret+by+Clive+Cussler%2C+Jack+Du+Brul+EPUB&amp;tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&amp;tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.uw0.xyz%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fopen.demonii.si%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.nibba.trade%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Fopentracker.sktorrent.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fbt.xxx-tracker.com%3A2710%2Fannounce&amp;tr=udp%3A%2F%2Fzephir.monocul.us%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Famigacity.xyz%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce" onclick="javascript: count(this);"><span class="icon"><i class="flaticon-ld08a4206c278863eddc1bf813faa024ef55ce0ef"></i></span>Magnet Download</a> </li>
# <li class="dropdown">
# <a data-toggle="dropdown" class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c le41399670fcf7cac9ad72cbf1af20d76a1fa16ad" onclick="javascript: count(this);" href="#"><span class="icon"><i class="flaticon-le9f40194aef2ed76d8d0f7f1be7fe5aad6fce5e6"></i></span>Torrent Download</a>
# <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l13bf8e2d22d06c362f67b795686b16d022e80098" target="_blank" href="http://itorrents.org/torrent/F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2.torrent"><span class="icon"><i class="flaticon-lbebff891414215bfc65d51afbd7677e45be19fad"></i></span>ITORRENTS MIRROR</a> </li>
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l13bf8e2d22d06c362f67b795686b16d022e80098" target="_blank" href="http://torrage.info/torrent.php?h=F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2"><span class="icon"><i class="flaticon-lbebff891414215bfc65d51afbd7677e45be19fad"></i></span>TORRAGE MIRROR</a></li>
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l13bf8e2d22d06c362f67b795686b16d022e80098" target="_blank" href="http://btcache.me/torrent/F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2"><span class="icon"><i class="flaticon-lbebff891414215bfc65d51afbd7677e45be19fad"></i></span>BTCACHE MIRROR</a></li>
# <li><a class="l4702248fa49fbaf25efd33c5904b4b3175b29571 l0e850ee5d16878d261dd01e2486970eda4fb2b0c l8680f3a1872d2d50e0908459a4bfa4dc04f0e610" href="magnet:?xt=urn:btih:F5BC20E9AA709CFC32BE63B2F6BEE56882EB7BD2&amp;dn=The+Titanic+Secret+by+Clive+Cussler%2C+Jack+Du+Brul+EPUB&amp;tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&amp;tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.uw0.xyz%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fopen.demonii.si%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.nibba.trade%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Fopentracker.sktorrent.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fbt.xxx-tracker.com%3A2710%2Fannounce&amp;tr=udp%3A%2F%2Fzephir.monocul.us%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Famigacity.xyz%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&amp;tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&amp;tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce"><span class="icon"><i class="flaticon-ld08a4206c278863eddc1bf813faa024ef55ce0ef"></i></span>None Working? Use Magnet</a></li>
#
