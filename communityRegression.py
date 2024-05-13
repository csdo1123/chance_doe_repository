from calendar import c
from distutils.log import error
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#URL = input('test Server >> ')
# print('Test Server : https://' + URL + '.wanted.co.kr/')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('./webDriver/chromedriver_103.exe', options=options)
#driver.get(url = 'https://' + URL + '.wanted.co.kr/')
driver.get(url = 'https://dev.wanted.co.kr/')
driver.maximize_window()

ac = ActionChains(driver)
jobGroup = {
'devTags':'#커리어고민#취업/이직#개발#데이터#IT/기술', 
'businessTags':'#커리어고민#취업/이직#데이터#서비스기획#경영/전략#리더십', 
'designTags':'#커리어고민#취업/이직#서비스기획#디자인#브랜딩#UX/UI',
'marcketingTags':'#커리어고민#취업/이직#데이터#마케팅#브랜딩', 
'HRTags':'#커리어고민#취업/이직#HR#노무#리더십#조직문화', 
'defaultsTags':'#커리어고민#취업/이직#회사생활#인간관계#IT/기술#라이프스타일#리더십#조직문화',
'userTags':'#인간관계#경영/전략#브랜딩#노무#조직문화'}


def backgroundClick():
    ac.reset_actions()
    ac.move_by_offset(500, 500)
    ac.click()
    ac.perform()

#############################################################################################
#GNB > 커뮤니티 메뉴로 이동 시 "추천" 피드로 이동한다.
print('\nGNB > 커뮤니티 클릭 시 추천 피드로 이동 > ')
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/nav/ul/li[6]/a').click()

driver.implicitly_wait(10)
if(driver.find_element(By.CLASS_NAME, 'RecommendedPostsView_tag_list__Yaqnj').is_displayed):
    print('[PASS]')
else:
    print('[FAIL]')

#미로그인 상태로 특정 객체 클릭 시 로그인 팝업 노출.
print('\n미로그인 상태로 글쓰기 영역 클릭 > ')
driver.find_element(By.CLASS_NAME, 'PostWriteButton_writeButton__pWbNC').click()

driver.implicitly_wait(10)
if(driver.find_element(By.ID, 'email').is_displayed):
    print('[PASS]')
    backgroundClick()
else:
    print('[FAIL]')

print('\n미로그인 상태로 커뮤니티 프로필 클릭 > ')
driver.find_element(By.CLASS_NAME, 'MyCommunityProfile_MyCommunityProfile__link__GUqqM').click()

driver.implicitly_wait(10)
if(driver.find_element(By.ID, 'email').is_displayed):
    print('[PASS]')
    backgroundClick()
else:
    print('[FAIL]')

print('\n미로그인 상태로 관심태그 노출 영역 클릭 > ')
driver.find_element(By.CLASS_NAME, 'RecommendedPostsView_tag_list__Yaqnj').click()

driver.implicitly_wait(10)
if(driver.find_element(By.ID, 'email').is_displayed):
    print('[PASS]')
    backgroundClick()
else:
    print('[FAIL]')

print('\n미로그인 상태로 관심태그 설정 유도 팝업 클릭 > ')
driver.find_element(By.CLASS_NAME, 'InterestTagBanner_InterestTagBanner__r3IQu').click()

driver.implicitly_wait(10)
if(driver.find_element(By.ID, 'email').is_displayed):
    print('[PASS]')
    backgroundClick()
else:
    print('[FAIL]')

print('\n미로그인 상태로 프로필 영역의 댓글 아이콘 클릭 > ')
driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/main/div[2]/section[3]/a[1]').click()

driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="__next"]/main/aside/div/div[2]/div[1]/button').click()

driver.implicitly_wait(10)
if(driver.find_element(By.ID, 'email').is_displayed):
    print('[PASS]')
    backgroundClick()
else:
    print('[FAIL]')

print('\n미로그인 상태로 프로필 영역의 좋아요 아이콘 클릭 > ')
driver.find_element(By.XPATH, '//*[@id="__next"]/main/aside/div/div[2]/div[2]/button').click()

driver.implicitly_wait(10)
if(driver.find_element(By.ID, 'email').is_displayed):
    print('[PASS]')
    backgroundClick()
else:
    print('[FAIL]')

print('\n미로그인 상태로 댓글 아이콘 클릭 > ')
driver.find_element(By.XPATH, '//*[@id="__next"]/main/section/article/div[4]/div[1]/button').click()

driver.implicitly_wait(10)
if(driver.find_element(By.ID, 'email').is_displayed):
    print('[PASS]')
    backgroundClick()
else:
    print('[FAIL]')

print('\n미로그인 상태로 좋아요 아이콘 클릭 > ')
driver.find_element(By.XPATH, '//*[@id="__next"]/main/section/article/div[4]/div[2]/button').click()

driver.implicitly_wait(10)
if(driver.find_element(By.ID, 'email').is_displayed):
    print('[PASS]')
    backgroundClick()
else:
    print('[FAIL]')
driver.back()

print('\n미로그인 상태로 추천 피드 타이틀 확인 > ')
title = driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/main/div[2]/section[3]/div[1]/h2')
if(title.text == '추천 커뮤니티글 💘'):
    print('[PASS]')
else:
    print('[FAIL] Actual Result : ' + title.text)

print('\n미로그인 상태로 관심태그 노출 영역에 노출되는 태그 확인 > ')
tags = driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/main/div[2]/section[3]/div[1]/div')
if(tags.text == jobGroup['defaultsTags']):
    print('[PASS]')
else:
    print('[FAIL] Actual Result : ' + tags.text)

#홈으로 이동 > 로그인
driver.find_element(By.CLASS_NAME, 'icon-logo_new').click()

print('\n회원가입하기 버튼 클릭 후 로그인 팝업 노출 확인 > ')
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME, 'signUpButton').click()
driver.implicitly_wait(10)
if(driver.find_element(By.ID, 'email').is_displayed):
    print('[PASS]')
else:
    print('[FAIL]')

#계정 미입력 시 오류메시지 확인
print('\n계정 미입력 오류메시지 노출 확인 > ')
driver.find_element(By.XPATH, '//*[@id="MODAL_BODY"]/div[2]/div[2]/button').click()
errorMessage = driver.find_element(By.CLASS_NAME, 'style_error__PioA9')
if(errorMessage.text == '올바른 이메일 형식을 입력해주세요.'):
    print('[PASS]')
else:
    print('[FAIL] Actual Result : ' + errorMessage.text)

#이메일 형식이 아닌 계정 입력 시 오류메시지 확인
print('\n잘못된 형식의 계정 입력 시 오류메시지 노출 확인 > ')
driver.find_element(By.ID, 'email').send_keys('cm00test.com')
driver.find_element(By.XPATH, '//*[@id="MODAL_BODY"]/div[2]/div[2]/button').click()
errorMessage = driver.find_element(By.CLASS_NAME, 'style_error__PioA9')
if(errorMessage.text == '올바른 이메일 형식을 입력해주세요.'):
    print('[PASS]')
else:
    print('[FAIL] Actual Result : ' + errorMessage.text)
# driver.find_element(By.ID, 'email').clear()
backgroundClick()

#개발직군 태그 확인
for j in jobGroup.keys():
    print('\n' + j + ' 태그 노출 상태 확인 > ')

    if j == 'devTags':
        userId = 'cm_dev@test.com'
    elif j == 'businessTags':
        userId = 'cm_business@test.com'
    elif j == 'designTags':
        userId = 'cm_design@test.com'
    elif j == 'marcketingTags':
        userId = 'cm_marcketing@test.com'
    elif j == 'HRTags':
        userId = 'cm_HR@test.com'
    elif j == 'defaultsTags':
        userId = 'cm_default@test.com'
    elif j == 'userTags':
        userId = 'cm_usertags@test.com'

    driver.find_element(By.CLASS_NAME, 'signUpButton').click()
    driver.find_element(By.ID, 'email').send_keys(userId)
    driver.find_element(By.XPATH, '//*[@id="MODAL_BODY"]/div[2]/div[2]/button').click()
    driver.find_element(By.ID, 'password-text-field').send_keys('dkssud1!')
    driver.find_element(By.XPATH, '//*[@id="MODAL_BODY"]/div/button[1]').click()

    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/nav/ul/li[6]/a').click()
    time.sleep(3)
    tags = driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/main/div[2]/section[3]/div[1]/div')
    if(tags.text == jobGroup[j]):
        print('[PASS]')
    else:
        print('[FAIL] Actual Result : ' + tags.text)
    
    print('\n' + j + ' 직군 계정 로그아웃 > ')
    driver.find_element(By.CLASS_NAME, 'avatarBorder').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'is-logout').click()
    time.sleep(3)
    isLogout = driver.find_element(By.CLASS_NAME, 'signUpButton').is_displayed
    if(isLogout):
        print('[PASS]')
    else:
        print('[FAIL]')

#테스트 계정 로그인 후 커뮤니티 이동하여 추천 원티드 PICK 타이틀 확인.
print('\n로그인 상태로 추천 원티드 PICK 타이틀 확인 > ')
driver.find_element(By.CLASS_NAME, 'signUpButton').click()
driver.find_element(By.ID, 'email').send_keys('cm02@test.com')
driver.find_element(By.XPATH, '//*[@id="MODAL_BODY"]/div[2]/div[2]/button').click()
driver.find_element(By.ID, 'password-text-field').send_keys('dkssud1!')
driver.find_element(By.XPATH, '//*[@id="MODAL_BODY"]/div/button[1]').click()

time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/nav/ul/li[6]/a').click()
time.sleep(5)
wantedPickTitle = driver.find_element(By.CLASS_NAME, 'TopPickPostView_wantedPickTitle__LP_JP')
if(wantedPickTitle.text == '추천 원티드 PICK 🌈'):
    print('[PASS]')
else:
    print('[FAIL] Actual Result :' + wantedPickTitle.text)

#글쓰기 영역 텍스트 확인.
print('글쓰기 영역 텍스트 확인 > ')
writeTitle = driver.find_element(By.CLASS_NAME, 'PostWriteButton_writeButton__pWbNC')
if writeTitle.text == '커리어와 라이프스타일에 대해 자유롭게 이야기 해주세요!':
    print('[PASS]')
else:
    print('[FAIL] Actual Result : ' + writeTitle.text)

#관심태그 미선택 유저의 추천 타이틀 확인.
print('\n관심태그 미선택 유저의 추천피드 타이틀 확인 > ')
recommendedTitle = driver.find_element(By.XPATH, '//*[@id="__next"]/div[4]/main/div[2]/section[3]/div[1]/h2')
if recommendedTitle.text == '추천 커뮤니티글 💘':
    print('[PASS]')
else:
    print('[FAIL]')

#관심태그 미설정 유저에게 관심태그 설정 유도 팝업 노출.
print('\n관심태그 미설정 유저에게 관심태그 설정 유도 팝업 노출 확인 > ')
if driver.find_element(By.CLASS_NAME, 'InterestTagBanner_InterestTagBanner__r3IQu').is_displayed:
    print('[PASS]')
else:
    print('[FAIL]')

#관심태그 설정 유저에게 관심태그 설정 유도 팝업 미노출.
print('\n관심태그 설정 유저에게 관심태그 설정 유도 팝업 미노출 확인 > ')
driver.find_element(By.CLASS_NAME, 'avatarBorder').click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'is-logout').click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'signUpButton').click()
driver.find_element(By.ID, 'email').send_keys('cm03@test.com')
driver.find_element(By.XPATH, '//*[@id="MODAL_BODY"]/div[2]/div[2]/button').click()
driver.find_element(By.ID, 'password-text-field').send_keys('dkssud1!')
driver.find_element(By.XPATH, '//*[@id="MODAL_BODY"]/div/button[1]').click()

time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/nav/ul/li[6]/a').click()
time.sleep(5)
try:
        if driver.find_element(By.CLASS_NAME, 'InterestTagBanner_InterestTagBanner__r3IQu').is_displayed:
            print('[FAIL]')
except selenium.common.exceptions.NoSuchElementException as e:
    print('[PASS]')

time.sleep(3)