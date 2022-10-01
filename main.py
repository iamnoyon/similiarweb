import requests
import lxml.html

domain = input('Enter Your Domain Name: ')
#domain = 'quora.com'
cookies = {
    'cookietime': '1664554128770',
    'sgID': '8cffb4bc-b6c8-6951-f8c5-706435dec035',
    'sw_extension_installed': '1664554128826',
    '_ga': 'GA1.2.96362229.1664554129',
    '_gid': 'GA1.2.1237485234.1664554129',
    '_gcl_au': '1.1.1059721303.1664554129',
    '_wingify_pc_uuid': 'f9356febc39b451e9f50161d814b7f92',
    'qcSxc': '1664554129757',
    'nh01NAS': 'd2826211-ffa9-4156-8ec1-58c6262bbb02',
    'nQ_cookieId': '1cfa59b8-604f-d991-78f6-4a10e809c13c',
    '_gd_visitor': 'e6f2f35f-ff3e-4e76-84ed-0a4782452c69',
    '__qca': 'P0-1936664025-1664554129752',
    '_pxvid': '2b235dd1-40da-11ed-bb4b-544254734749',
    '_an_uid': '4362873523387340183',
    'wingify_donot_track_actions': '0',
    'intercom-id-e74067abd037cecbecb0662854f02aee12139f95': 'e544ab0c-8e98-45d5-b104-8e88cadd3867',
    'intercom-session-e74067abd037cecbecb0662854f02aee12139f95': '',
    'locale': 'en-us',
    '_vwo_uuid': 'JA5CF7D7B32C4CBDA14620B5B089E1CA9',
    '_vwo_ds': '3%241664554165%3A66.82481478%3A%3A',
    '_vwo_uuid_v2': 'DFDEA2841578FB36632EFC18A7D8ADEEF|ccace9216fbfe3a07866362280b4ca4d',
    'loyal-user': '{%22date%22:%222022-09-30T16:09:31.780Z%22%2C%22isLoyal%22:false}',
    'sw-cookies-consent': '1',
    '_vis_opt_s': '2%7C',
    '_vis_opt_test_cookie': '1',
    'ak_bmsc': '765512D944012D9EA92BF4C385FCEE73~000000000000000000000000000000~YAAQJaTUF6yPEX2DAQAAkhPbkREfYBCO8v/xRJdLBPNPNvktvvqJyfjDxsxwB8jL7wbwN6B0w7xeYzOZsvgJoUc7V7K1Hntu/V26+c7sLv4SWH6FZIHYMa8EYKevm91dtVnvjBX48+2JPRHnSRMHRb2u8UYYMdyBtXmm1edrcu3kwaqQQReCO398aJmGh8f9LYMpQPl2Eq00F0Ox0CEVo5U2gPQ+Fic+EHFpC2WmjNGd8ZjKi/tcxkkauRHL7alY2+0x7FAUDs2rG5bOAj7CoUm2KQWKSAMd1AbyMlgDqrSNBaDTzOjgrVy22+QruMkqYLacRXCgpJ/MEWfyZDKeveMWE/Vu2/qVt1wkxlJe2zOW9qBqSVRNA9K/3VF9pafDURardps39VJLNLSslIIdaoOAZnmtJWqIQYWu26cwnNkEiTPOwLoXuAr/2xag0mqIv/hgJRC/XlwhrfJQ+zEPaE0lUyvsaGYjQW3lgHmcGjLz+LpfWHuPEtpiLTZb4n8=',
    'pxcts': '91adec5f-4143-11ed-a11b-4c41546c486d',
    '_clck': 'avw6v8|1|f5c|0',
    'sw_utm': 'utm_source%3Daddon%26utm_medium%3Dchrome%26utm_content%3Dheader%26utm_campaign%3Dcta-button',
    'fsrndid': 'false',
    '_gat_UA-42469261-1': '1',
    '_uetsid': '2b7de7d040da11ed94c61b43497ec95a',
    '_uetvid': '2b7e451040da11eda396390d7b95a805',
    '_pxff_cc': 'U2FtZVNpdGU9TGF4Ow==',
    '_pk_id.1.fd33': '3d30c0d680365c24.1664554130.',
    '_pk_ses.1.fd33': '1',
    'mp_7ccb86f5c2939026a4b5de83b5971ed9_mixpanel': '%7B%22distinct_id%22%3A%20%221838f285c5775c-0c3c99c6c16d1f-26021c51-100200-1838f285c58b11%22%2C%22%24device_id%22%3A%20%221838f285c5775c-0c3c99c6c16d1f-26021c51-100200-1838f285c58b11%22%2C%22sgId%22%3A%20%228cffb4bc-b6c8-6951-f8c5-706435dec035%22%2C%22site_type%22%3A%20%22lite%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22session_id%22%3A%20%22fc8b9f72-8f92-4e15-8948-d528538be0fa%22%2C%22session_first_event_time%22%3A%20%222022-10-01T04%3A43%3A19.121Z%22%2C%22url%22%3A%20%22https%3A%2F%2Fwww.similarweb.com%2Fwebsite%2Fquora.com%2F%23overview%22%2C%22language%22%3A%20%22en-us%22%2C%22section%22%3A%20%22website%22%2C%22sub_section%22%3A%20%22%22%2C%22sub_sub_section%22%3A%20%22%22%2C%22last_event_time%22%3A%201664604973365%2C%22utm_source%22%3A%20%22addon%22%2C%22utm_medium%22%3A%20%22chrome%22%2C%22utm_campaign%22%3A%20%22cta-button%22%2C%22utm_content%22%3A%20%22header%22%2C%22sw_extention%22%3A%20true%2C%22%24search_engine%22%3A%20%22google%22%2C%22is_sw_user%22%3A%20false%2C%22entity_id%22%3A%20%22quora.com%22%2C%22entity_name%22%3A%20%22quora.com%22%2C%22main_category%22%3A%20%22Reference%20Materials%22%2C%22sub_category%22%3A%20%22Dictionaries%20and%20Encyclopedias%22%2C%22mode%22%3A%20%22single%22%2C%22domain%22%3A%20%22quora.com%22%2C%22is_small_site%22%3A%20false%2C%22is_ga_connected%22%3A%20false%2C%22first_time_visitor%22%3A%20false%7D',
    '_px3': '8829c687dee922fccd732f94219dd25c52234546c554e3e7fa10a230d8bfa098:Uf/vUCWxE+dajzh9TuDdHpZA34X30oqXn+YLjJ/bpcAwdi8ZFY3Wh77QcWIVTxdoRPYcTxJKBS31/cvd94GFSA==:1000:2X/6SfKRQNrkS7CWA82ha+KIrFNbLSLA2KYG/nfrPrqy/EM+PijSK700b/qQ8/IDah1kIBXr7zPjomuN/qEZyrZQidrhNTME2IVZYNtxP6F+5XxD+Z0y80Z99GcH4HVKelXV4HTieird48yLrnjFrupcmBdfq04BIdwRRTs/jRuoKbDORuorkblJ4klgxGMY3MndkgnsKoLeBup/JrVL6w==',
    '_clsk': '1otfxjl|1664604976890|21|1|e.clarity.ms/collect',
    'bm_sv': 'E5A8DDCD273D64D44BE1BCC5261C8535~YAAQBKTUF8iLqEODAQAAtjswkhHJ6TO+QFcLNm5gttZcsGBK9/49VtcxkNe8EPvYAqT9jaKl0DgiJSLcKvCz4rEkTHyPI2U7icdIp7ySXRX/GF5rVvDmzoN7WR5UXl/kx4V+9Tbtwx+AjwjWSgtPPT8e3RcdeheN+8/KHkkU0OdyVLroBuQInmRNF6ed3J3rPAaANCTkJXH+TsRAOuAMBgOIcvMxSHeaqFRDTdxBnasp3kQ7e1S486jVvP/D1FnAeae+H7o=~1',
    '_vwo_sn': '48424%3A22',
    'RT': '"z=1&dm=www.similarweb.com&si=a0e2b670-26ca-4458-9747-31e5ab24ff11&ss=l8pitgbg&sl=1&tt=aa7&rl=1&ld=aac&ul=y0p"',
}

headers = {
    'authority': 'www.similarweb.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'cookietime=1664554128770; sgID=8cffb4bc-b6c8-6951-f8c5-706435dec035; sw_extension_installed=1664554128826; _ga=GA1.2.96362229.1664554129; _gid=GA1.2.1237485234.1664554129; _gcl_au=1.1.1059721303.1664554129; _wingify_pc_uuid=f9356febc39b451e9f50161d814b7f92; qcSxc=1664554129757; nh01NAS=d2826211-ffa9-4156-8ec1-58c6262bbb02; nQ_cookieId=1cfa59b8-604f-d991-78f6-4a10e809c13c; _gd_visitor=e6f2f35f-ff3e-4e76-84ed-0a4782452c69; __qca=P0-1936664025-1664554129752; _pxvid=2b235dd1-40da-11ed-bb4b-544254734749; _an_uid=4362873523387340183; wingify_donot_track_actions=0; intercom-id-e74067abd037cecbecb0662854f02aee12139f95=e544ab0c-8e98-45d5-b104-8e88cadd3867; intercom-session-e74067abd037cecbecb0662854f02aee12139f95=; locale=en-us; _vwo_uuid=JA5CF7D7B32C4CBDA14620B5B089E1CA9; _vwo_ds=3%241664554165%3A66.82481478%3A%3A; _vwo_uuid_v2=DFDEA2841578FB36632EFC18A7D8ADEEF|ccace9216fbfe3a07866362280b4ca4d; loyal-user={%22date%22:%222022-09-30T16:09:31.780Z%22%2C%22isLoyal%22:false}; sw-cookies-consent=1; _vis_opt_s=2%7C; _vis_opt_test_cookie=1; ak_bmsc=765512D944012D9EA92BF4C385FCEE73~000000000000000000000000000000~YAAQJaTUF6yPEX2DAQAAkhPbkREfYBCO8v/xRJdLBPNPNvktvvqJyfjDxsxwB8jL7wbwN6B0w7xeYzOZsvgJoUc7V7K1Hntu/V26+c7sLv4SWH6FZIHYMa8EYKevm91dtVnvjBX48+2JPRHnSRMHRb2u8UYYMdyBtXmm1edrcu3kwaqQQReCO398aJmGh8f9LYMpQPl2Eq00F0Ox0CEVo5U2gPQ+Fic+EHFpC2WmjNGd8ZjKi/tcxkkauRHL7alY2+0x7FAUDs2rG5bOAj7CoUm2KQWKSAMd1AbyMlgDqrSNBaDTzOjgrVy22+QruMkqYLacRXCgpJ/MEWfyZDKeveMWE/Vu2/qVt1wkxlJe2zOW9qBqSVRNA9K/3VF9pafDURardps39VJLNLSslIIdaoOAZnmtJWqIQYWu26cwnNkEiTPOwLoXuAr/2xag0mqIv/hgJRC/XlwhrfJQ+zEPaE0lUyvsaGYjQW3lgHmcGjLz+LpfWHuPEtpiLTZb4n8=; pxcts=91adec5f-4143-11ed-a11b-4c41546c486d; _clck=avw6v8|1|f5c|0; sw_utm=utm_source%3Daddon%26utm_medium%3Dchrome%26utm_content%3Dheader%26utm_campaign%3Dcta-button; fsrndid=false; _gat_UA-42469261-1=1; _uetsid=2b7de7d040da11ed94c61b43497ec95a; _uetvid=2b7e451040da11eda396390d7b95a805; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _pk_id.1.fd33=3d30c0d680365c24.1664554130.; _pk_ses.1.fd33=1; mp_7ccb86f5c2939026a4b5de83b5971ed9_mixpanel=%7B%22distinct_id%22%3A%20%221838f285c5775c-0c3c99c6c16d1f-26021c51-100200-1838f285c58b11%22%2C%22%24device_id%22%3A%20%221838f285c5775c-0c3c99c6c16d1f-26021c51-100200-1838f285c58b11%22%2C%22sgId%22%3A%20%228cffb4bc-b6c8-6951-f8c5-706435dec035%22%2C%22site_type%22%3A%20%22lite%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22session_id%22%3A%20%22fc8b9f72-8f92-4e15-8948-d528538be0fa%22%2C%22session_first_event_time%22%3A%20%222022-10-01T04%3A43%3A19.121Z%22%2C%22url%22%3A%20%22https%3A%2F%2Fwww.similarweb.com%2Fwebsite%2Fquora.com%2F%23overview%22%2C%22language%22%3A%20%22en-us%22%2C%22section%22%3A%20%22website%22%2C%22sub_section%22%3A%20%22%22%2C%22sub_sub_section%22%3A%20%22%22%2C%22last_event_time%22%3A%201664604973365%2C%22utm_source%22%3A%20%22addon%22%2C%22utm_medium%22%3A%20%22chrome%22%2C%22utm_campaign%22%3A%20%22cta-button%22%2C%22utm_content%22%3A%20%22header%22%2C%22sw_extention%22%3A%20true%2C%22%24search_engine%22%3A%20%22google%22%2C%22is_sw_user%22%3A%20false%2C%22entity_id%22%3A%20%22quora.com%22%2C%22entity_name%22%3A%20%22quora.com%22%2C%22main_category%22%3A%20%22Reference%20Materials%22%2C%22sub_category%22%3A%20%22Dictionaries%20and%20Encyclopedias%22%2C%22mode%22%3A%20%22single%22%2C%22domain%22%3A%20%22quora.com%22%2C%22is_small_site%22%3A%20false%2C%22is_ga_connected%22%3A%20false%2C%22first_time_visitor%22%3A%20false%7D; _px3=8829c687dee922fccd732f94219dd25c52234546c554e3e7fa10a230d8bfa098:Uf/vUCWxE+dajzh9TuDdHpZA34X30oqXn+YLjJ/bpcAwdi8ZFY3Wh77QcWIVTxdoRPYcTxJKBS31/cvd94GFSA==:1000:2X/6SfKRQNrkS7CWA82ha+KIrFNbLSLA2KYG/nfrPrqy/EM+PijSK700b/qQ8/IDah1kIBXr7zPjomuN/qEZyrZQidrhNTME2IVZYNtxP6F+5XxD+Z0y80Z99GcH4HVKelXV4HTieird48yLrnjFrupcmBdfq04BIdwRRTs/jRuoKbDORuorkblJ4klgxGMY3MndkgnsKoLeBup/JrVL6w==; _clsk=1otfxjl|1664604976890|21|1|e.clarity.ms/collect; bm_sv=E5A8DDCD273D64D44BE1BCC5261C8535~YAAQBKTUF8iLqEODAQAAtjswkhHJ6TO+QFcLNm5gttZcsGBK9/49VtcxkNe8EPvYAqT9jaKl0DgiJSLcKvCz4rEkTHyPI2U7icdIp7ySXRX/GF5rVvDmzoN7WR5UXl/kx4V+9Tbtwx+AjwjWSgtPPT8e3RcdeheN+8/KHkkU0OdyVLroBuQInmRNF6ed3J3rPAaANCTkJXH+TsRAOuAMBgOIcvMxSHeaqFRDTdxBnasp3kQ7e1S486jVvP/D1FnAeae+H7o=~1; _vwo_sn=48424%3A22; RT="z=1&dm=www.similarweb.com&si=a0e2b670-26ca-4458-9747-31e5ab24ff11&ss=l8pitgbg&sl=1&tt=aa7&rl=1&ld=aac&ul=y0p"',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

base_url = 'https://www.similarweb.com/website/'
url = base_url + domain
html = requests.get(url, cookies=cookies, headers=headers)
'''with open('saving.html', 'wb+') as f:
    f.write(html.content)'''
doc = lxml.html.fromstring(html.content)
global_rank = doc.xpath('//*[@id="overview"]/div/div/div/div[3]/div/div[1]/div/p/text()')[0]
#print(url,doc)
print(global_rank)