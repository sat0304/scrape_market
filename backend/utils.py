import random

user_agent_list = [
    # Chrome
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2762.73 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
    # Firefox
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (X11; Linux ppc64le; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Mozilla/5.0 (X11; Linux; rv:74.0) Gecko/20100101 Firefox/74.0'
]


def get_random_agent():
    return random.choice(user_agent_list)


cookies = [
    {
        "name": "ADDRESSBOOKBAR_WEB_CLARIFICATION",
        "value": "1710237857",
        "domain": 'www.ozon.ru',
    },
    {
        "name": "__Secure-ETC",
        "value": "614b2fe049703cd4dd30cf4204f1741f",
        "domain": 'www.ozon.ru',
    },
    {
        "name": "__Secure-ab-group",
        "value": "49",
        "domain": '.ozon.ru',
    },
    {
        "name": "__Secure-access-token",
        "value": "4.8406781.u2L9rb6gTI68Zo7eFDx6rg.49.AcmMnm6jGm_XbhAtS6kufJqbN5l_7ofRa0e7aCZMEng1OSif0EOSQ5Tm9c44C8AC_nQaY7fhMUphjv-XptV8zbc.20180917083516.20240314100910.fTeUs1jxrRvkMrU6XACoixoxHhiWG8YxPdolTsH_wJY",
        "domain": '.ozon.ru',
    },
    {
        "name": "__Secure-ext_xcid",
        "value": "a6c974503d808dfdc6307870676cf8e3",
        "domain": '.ozon.ru',
    },
    {
        "name": "__Secure-refresh-token",
        "value": "4.8406781.u2L9rb6gTI68Zo7eFDx6rg.49.AcmMnm6jGm_XbhAtS6kufJqbN5l_7ofRa0e7aCZMEng1OSif0EOSQ5Tm9c44C8AC_nQaY7fhMUphjv-XptV8zbc.20180917083516.20240314100910.M7dJV7-nLaea-3-GWxVvItWPEczhApT5mCPTtaN6dgw",
        "domain": '.ozon.ru',
    },
    {
        "name": "__Secure-user-id",
        "value": "8406781",
        "domain": '.ozon.ru',
    },
    {
        "name": "__cf_bm",
        "value": "eZVOnZYuUTpZMNjC_SJM91Sd0038.eGrvavRgJABYvI-1710403750-1.0.1.1-0Wg4eUzXwivbDwaze3jGFSxRPeKKynjKfltw6xlr7_f.CV9.LnjwWzMWUVwD_NT8p4wV.3BGl3RseBbX8Pkx7Q",
        "domain": '.ozon.ru',
    },
    {
        "name": "abt_data",
        "value":"b44fa3b92e0ce43c13b4215dadcd1cfb:a75d1c216f65be0a982b80973270f8ecba36451d52890e4971affb4b063211621d2c2ce80fe1d9831c39f658e49935b6ec2ae6658d99f0312c59db997e8e5d8216b41d54adbc53029b0a82aa0add0af555b9c3493d8c78cdac3659339e18132c4a0621ac7724c977e532e658cbc40a9ad45d374a658764d2203e92ac9107e0340e3b17ba0ccb22c517f27cadd02edc0f7ef63058566c088b6489263be02765810369d04a4422aa6bd8fe2c8411b141bf334b3daeb9494ffa41fd0da840094da37e4e00ed8db50a03a47945d661e9a05279c3a02c8a4a5960159c4fce1d9a45212f6ef90fa0150d4e43f8d4b4d0445935b2636115a0846ef17982cbce63f7851fba34846d2301989e8bbbe28e6bf8e172308b19ba02488366f1382a4f3b4c2264",
        "domain": '.ozon.ru',
    },
    {
        "name": "cf_clearance",
        "value": "n9i7MquvH2uMACaMsfit8vU7qy1wRVctDl8qxtMluIw-1710403751-1.0.1.1-_Mj_oPZcEQFJi5k0oNIMWBGIYvt6iU5RNkDfv3SXnXDteKfEEh_0Lh8a3U_v6MhNjkkbbbsEVXyLEN.vbUP.sg",
        "domain": 'www.ozon.ru',
    },
    {
        "name": "is_cookies_accepted",
        "value": "1",
        "domain": 'www.ozon.ru',
    },
    {
        "name": "ob_theme",
        "value": "DEFAULT",
        "domain": '.ozon.ru',
    },
    {
        "name": "rfuid",
        "value": "NjkyNDcyNDUyLDEyNC4wNDM0NzUyNzUxNjA3NCwxMzQ3MDc1MTIzLC0xLDM2NjM4MTI3NyxXM3NpYm1GdFpTSTZJbEJFUmlCV2FXVjNaWElpTENKa1pYTmpjbWx3ZEdsdmJpSTZJbEJ2Y25SaFlteGxJRVJ2WTNWdFpXNTBJRVp2Y20xaGRDSXNJbTFwYldWVWVYQmxjeUk2VzNzaWRIbHdaU0k2SW1Gd2NHeHBZMkYwYVc5dUwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjBzZXlKMGVYQmxJam9pZEdWNGRDOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5WFgwc2V5SnVZVzFsSWpvaVEyaHliMjFsSUZCRVJpQldhV1YzWlhJaUxDSmtaWE5qY21sd2RHbHZiaUk2SWxCdmNuUmhZbXhsSUVSdlkzVnRaVzUwSUVadmNtMWhkQ0lzSW0xcGJXVlVlWEJsY3lJNlczc2lkSGx3WlNJNkltRndjR3hwWTJGMGFXOXVMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4wc2V5SjBlWEJsSWpvaWRHVjRkQzl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOVhYMHNleUp1WVcxbElqb2lRMmh5YjIxcGRXMGdVRVJHSUZacFpYZGxjaUlzSW1SbGMyTnlhWEIwYVc5dUlqb2lVRzl5ZEdGaWJHVWdSRzlqZFcxbGJuUWdSbTl5YldGMElpd2liV2x0WlZSNWNHVnpJanBiZXlKMGVYQmxJam9pWVhCd2JHbGpZWFJwYjI0dmNHUm1JaXdpYzNWbVptbDRaWE1pT2lKd1pHWWlmU3g3SW5SNWNHVWlPaUowWlhoMEwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjFkZlN4N0ltNWhiV1VpT2lKTmFXTnliM052Wm5RZ1JXUm5aU0JRUkVZZ1ZtbGxkMlZ5SWl3aVpHVnpZM0pwY0hScGIyNGlPaUpRYjNKMFlXSnNaU0JFYjJOMWJXVnVkQ0JHYjNKdFlYUWlMQ0p0YVcxbFZIbHdaWE1pT2x0N0luUjVjR1VpT2lKaGNIQnNhV05oZEdsdmJpOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5TEhzaWRIbHdaU0k2SW5SbGVIUXZjR1JtSWl3aWMzVm1abWw0WlhNaU9pSndaR1lpZlYxOUxIc2libUZ0WlNJNklsZGxZa3RwZENCaWRXbHNkQzFwYmlCUVJFWWlMQ0prWlhOamNtbHdkR2x2YmlJNklsQnZjblJoWW14bElFUnZZM1Z0Wlc1MElFWnZjbTFoZENJc0ltMXBiV1ZVZVhCbGN5STZXM3NpZEhsd1pTSTZJbUZ3Y0d4cFkyRjBhVzl1TDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMHNleUowZVhCbElqb2lkR1Y0ZEM5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlYWDFkLFd5SnlkUzFTVlNKZCwwLDEsMCwyNCwyMzc0MTU5MzAsOCwyMjcxMjY1MjAsMCwxLDAsLTQ5MTI3NTUyMyxSMjl2WjJ4bElFbHVZeTRnVG1WMGMyTmhjR1VnUjJWamEyOGdUR2x1ZFhnZ2VEZzJYelkwSURVdU1DQW9XREV4T3lCTWFXNTFlQ0I0T0RaZk5qUXBJRUZ3Y0d4bFYyVmlTMmwwTHpVek55NHpOaUFvUzBoVVRVd3NJR3hwYTJVZ1IyVmphMjhwSUVOb2NtOXRaUzh4TWpJdU1DNHdMakFnVTJGbVlYSnBMelV6Tnk0ek5pQXlNREF6TURFd055Qk5iM3BwYkd4aCxleUpqYUhKdmJXVWlPbnNpWVhCd0lqcDdJbWx6U1c1emRHRnNiR1ZrSWpwbVlXeHpaU3dpU1c1emRHRnNiRk4wWVhSbElqcDdJa1JKVTBGQ1RFVkVJam9pWkdsellXSnNaV1FpTENKSlRsTlVRVXhNUlVRaU9pSnBibk4wWVd4c1pXUWlMQ0pPVDFSZlNVNVRWRUZNVEVWRUlqb2libTkwWDJsdWMzUmhiR3hsWkNKOUxDSlNkVzV1YVc1blUzUmhkR1VpT25zaVEwRk9UazlVWDFKVlRpSTZJbU5oYm01dmRGOXlkVzRpTENKU1JVRkVXVjlVVDE5U1ZVNGlPaUp5WldGa2VWOTBiMTl5ZFc0aUxDSlNWVTVPU1U1SElqb2ljblZ1Ym1sdVp5SjlmWDE5LDY1LDEyODk0ODU0MzgsMSwxLC0xLDE2OTk5NTQ4ODcsMTY5OTk1NDg4NywzMzYwMDc5MzMsNA==",
        "domain": '.ozon.ru',
    },
    {
        "name": "xcid",
        "value": "0f52ad4fb7cba850b4f3df39f82bfa68",
        "domain": 'www.ozon.ru',
    },

]
