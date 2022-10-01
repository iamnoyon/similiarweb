from tokenize import Double
from traceback import print_tb
from unicodedata import category
import requests
import lxml.html
import json
import math
from numerize import numerize
import datetime

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

cc = {4:{"name":"Afghanistan","code":"AF"},8:{"name":"Albania","code":"AL"},10:{"name":"Antarctica","code":"AQ"},12:{"name":"Algeria","code":"DZ"},16:{"name":"American Samoa","code":"AS"},20:{"name":"Andorra","code":"AD"},24:{"name":"Angola","code":"AO"},28:{"name":"Antigua and Barbuda","code":"AG"},31:{"name":"Azerbaijan","code":"AZ"},32:{"name":"Argentina","code":"AR"},36:{"name":"Australia","code":"AU"},40:{"name":"Austria","code":"AT"},44:{"name":"Bahamas","code":"BS"},48:{"name":"Bahrain","code":"BH"},50:{"name":"Bangladesh","code":"BD"},51:{"name":"Armenia","code":"AM"},52:{"name":"Barbados","code":"BB"},56:{"name":"Belgium","code":"BE"},60:{"name":"Bermuda","code":"BM"},64:{"name":"Bhutan","code":"BT"},68:{"name":"Bolivia","code":"BO"},70:{"name":"Bosnia and Herzegovina","code":"BA"},72:{"name":"Botswana","code":"BW"},74:{"name":"Bouvet Island","code":"BV"},76:{"name":"Brazil","code":"BR"},84:{"name":"Belize","code":"BZ"},86:{"name":"British Indian Ocean Territory","code":"IO"},90:{"name":"Solomon Islands","code":"SB"},92:{"name":"Virgin Islands, British","code":"VG"},96:{"name":"Brunei Darussalam","code":"BN"},100:{"name":"Bulgaria","code":"BG"},104:{"name":"Myanmar","code":"MM"},108:{"name":"Burundi","code":"BI"},112:{"name":"Belarus","code":"BY"},116:{"name":"Cambodia","code":"KH"},120:{"name":"Cameroon","code":"CM"},124:{"name":"Canada","code":"CA"},132:{"name":"Cape Verde","code":"CV"},136:{"name":"Cayman Islands","code":"KY"},140:{"name":"Central African Republic","code":"CF"},144:{"name":"Sri Lanka","code":"LK"},148:{"name":"Chad","code":"TD"},152:{"name":"Chile","code":"CL"},156:{"name":"China","code":"CN"},158:{"name":"Taiwan, Province of China","code":"TW"},162:{"name":"Christmas Island","code":"CX"},166:{"name":"Cocos (Keeling) Islands","code":"CC"},170:{"name":"Colombia","code":"CO"},174:{"name":"Comoros","code":"KM"},175:{"name":"Mayotte","code":"YT"},178:{"name":"Congo","code":"CG"},180:{"name":"Congo, The Democratic Republic of the","code":"CD"},184:{"name":"Cook Islands","code":"CK"},188:{"name":"Costa Rica","code":"CR"},191:{"name":"Croatia","code":"HR"},192:{"name":"Cuba","code":"CU"},196:{"name":"Cyprus","code":"CY"},203:{"name":"Czech Republic","code":"CZ"},204:{"name":"Benin","code":"BJ"},208:{"name":"Denmark","code":"DK"},212:{"name":"Dominica","code":"DM"},214:{"name":"Dominican Republic","code":"DO"},218:{"name":"Ecuador","code":"EC"},222:{"name":"El Salvador","code":"SV"},226:{"name":"Equatorial Guinea","code":"GQ"},231:{"name":"Ethiopia","code":"ET"},232:{"name":"Eritrea","code":"ER"},233:{"name":"Estonia","code":"EE"},234:{"name":"Faroe Islands","code":"FO"},238:{"name":"Falkland Islands (Malvinas)","code":"FK"},239:{"name":"South Georgia and the South Sandwich Islands","code":"GS"},242:{"name":"Fiji","code":"FJ"},246:{"name":"Finland","code":"FI"},248:{"name":"land Islands","code":"AX"},250:{"name":"France","code":"FR"},254:{"name":"French Guiana","code":"GF"},258:{"name":"French Polynesia","code":"PF"},260:{"name":"French Southern Territories","code":"TF"},262:{"name":"Djibouti","code":"DJ"},266:{"name":"Gabon","code":"GA"},268:{"name":"Georgia","code":"GE"},270:{"name":"Gambia","code":"GM"},275:{"name":"Palestinian Territory, Occupied","code":"PS"},276:{"name":"Germany","code":"DE"},288:{"name":"Ghana","code":"GH"},292:{"name":"Gibraltar","code":"GI"},296:{"name":"Kiribati","code":"KI"},300:{"name":"Greece","code":"GR"},304:{"name":"Greenland","code":"GL"},308:{"name":"Grenada","code":"GD"},312:{"name":"Guadeloupe","code":"GP"},316:{"name":"Guam","code":"GU"},320:{"name":"Guatemala","code":"GT"},324:{"name":"Guinea","code":"GN"},328:{"name":"Guyana","code":"GY"},332:{"name":"Haiti","code":"HT"},334:{"name":"Heard Island and Mcdonald Islands","code":"HM"},336:{"name":"Holy See (Vatican City State)","code":"VA"},340:{"name":"Honduras","code":"HN"},344:{"name":"Hong Kong","code":"HK"},348:{"name":"Hungary","code":"HU"},352:{"name":"Iceland","code":"IS"},356:{"name":"India","code":"IN"},360:{"name":"Indonesia","code":"ID"},364:{"name":"Iran, Islamic Republic Of","code":"IR"},368:{"name":"Iraq","code":"IQ"},372:{"name":"Ireland","code":"IE"},376:{"name":"Israel","code":"IL"},380:{"name":"Italy","code":"IT"},384:{"name":"Cote D'Ivoire","code":"CI"},388:{"name":"Jamaica","code":"JM"},392:{"name":"Japan","code":"JP"},398:{"name":"Kazakhstan","code":"KZ"},400:{"name":"Jordan","code":"JO"},404:{"name":"Kenya","code":"KE"},408:{"name":"Korea, Democratic People'S Republic of","code":"KP"},410:{"name":"Korea, Republic of","code":"KR"},414:{"name":"Kuwait","code":"KW"},417:{"name":"Kyrgyzstan","code":"KG"},418:{"name":"Lao People'S Democratic Republic","code":"LA"},422:{"name":"Lebanon","code":"LB"},426:{"name":"Lesotho","code":"LS"},428:{"name":"Latvia","code":"LV"},430:{"name":"Liberia","code":"LR"},434:{"name":"Libyan Arab Jamahiriya","code":"LY"},438:{"name":"Liechtenstein","code":"LI"},440:{"name":"Lithuania","code":"LT"},442:{"name":"Luxembourg","code":"LU"},446:{"name":"Macao","code":"MO"},450:{"name":"Madagascar","code":"MG"},454:{"name":"Malawi","code":"MW"},458:{"name":"Malaysia","code":"MY"},462:{"name":"Maldives","code":"MV"},466:{"name":"Mali","code":"ML"},470:{"name":"Malta","code":"MT"},474:{"name":"Martinique","code":"MQ"},478:{"name":"Mauritania","code":"MR"},480:{"name":"Mauritius","code":"MU"},484:{"name":"Mexico","code":"MX"},492:{"name":"Monaco","code":"MC"},496:{"name":"Mongolia","code":"MN"},498:{"name":"Moldova, Republic of","code":"MD"},499:{"name":"Montenegro","code":"ME"},500:{"name":"Montserrat","code":"MS"},504:{"name":"Morocco","code":"MA"},508:{"name":"Mozambique","code":"MZ"},512:{"name":"Oman","code":"OM"},516:{"name":"Namibia","code":"NA"},520:{"name":"Nauru","code":"NR"},524:{"name":"Nepal","code":"NP"},528:{"name":"Netherlands","code":"NL"},533:{"name":"Aruba","code":"AW"},540:{"name":"New Caledonia","code":"NC"},548:{"name":"Vanuatu","code":"VU"},554:{"name":"New Zealand","code":"NZ"},558:{"name":"Nicaragua","code":"NI"},562:{"name":"Niger","code":"NE"},566:{"name":"Nigeria","code":"NG"},570:{"name":"Niue","code":"NU"},574:{"name":"Norfolk Island","code":"NF"},578:{"name":"Norway","code":"NO"},580:{"name":"Northern Mariana Islands","code":"MP"},581:{"name":"United States Minor Outlying Islands","code":"UM"},583:{"name":"Micronesia, Federated States of","code":"FM"},584:{"name":"Marshall Islands","code":"MH"},585:{"name":"Palau","code":"PW"},586:{"name":"Pakistan","code":"PK"},591:{"name":"Panama","code":"PA"},598:{"name":"Papua New Guinea","code":"PG"},600:{"name":"Paraguay","code":"PY"},604:{"name":"Peru","code":"PE"},608:{"name":"Philippines","code":"PH"},612:{"name":"Pitcairn","code":"PN"},616:{"name":"Poland","code":"PL"},620:{"name":"Portugal","code":"PT"},624:{"name":"Guinea-Bissau","code":"GW"},626:{"name":"Timor-Leste","code":"TL"},630:{"name":"Puerto Rico","code":"PR"},634:{"name":"Qatar","code":"QA"},638:{"name":"Reunion","code":"RE"},642:{"name":"Romania","code":"RO"},643:{"name":"Russian Federation","code":"RU"},646:{"name":"RWANDA","code":"RW"},654:{"name":"Saint Helena","code":"SH"},659:{"name":"Saint Kitts and Nevis","code":"KN"},660:{"name":"Anguilla","code":"AI"},662:{"name":"Saint Lucia","code":"LC"},666:{"name":"Saint Pierre and Miquelon","code":"PM"},670:{"name":"Saint Vincent and the Grenadines","code":"VC"},674:{"name":"San Marino","code":"SM"},678:{"name":"Sao Tome and Principe","code":"ST"},682:{"name":"Saudi Arabia","code":"SA"},686:{"name":"Senegal","code":"SN"},688:{"name":"Serbia","code":"RS"},690:{"name":"Seychelles","code":"SC"},694:{"name":"Sierra Leone","code":"SL"},702:{"name":"Singapore","code":"SG"},703:{"name":"Slovakia","code":"SK"},704:{"name":"Vietnam","code":"VN"},705:{"name":"Slovenia","code":"SI"},706:{"name":"Somalia","code":"SO"},710:{"name":"South Africa","code":"ZA"},716:{"name":"Zimbabwe","code":"ZW"},724:{"name":"Spain","code":"ES"},729:{"name":"Sudan","code":"SD"},732:{"name":"Western Sahara","code":"EH"},740:{"name":"Suri","code":"SR"},744:{"name":"Svalbard and Jan Mayen","code":"SJ"},748:{"name":"Swaziland","code":"SZ"},752:{"name":"Sweden","code":"SE"},756:{"name":"Switzerland","code":"CH"},760:{"name":"Syrian Arab Republic","code":"SY"},762:{"name":"Tajikistan","code":"TJ"},764:{"name":"Thailand","code":"TH"},768:{"name":"Togo","code":"TG"},772:{"name":"Tokelau","code":"TK"},776:{"name":"Tonga","code":"TO"},780:{"name":"Trinidad and Tobago","code":"TT"},784:{"name":"United Arab Emirates","code":"AE"},788:{"name":"Tunisia","code":"TN"},792:{"name":"Turkey","code":"TR"},795:{"name":"Turkmenistan","code":"TM"},796:{"name":"Turks and Caicos Islands","code":"TC"},798:{"name":"Tuvalu","code":"TV"},800:{"name":"Uganda","code":"UG"},804:{"name":"Ukraine","code":"UA"},807:{"name":"Macedonia, The Former Yugoslav Republic of","code":"MK"},818:{"name":"Egypt","code":"EG"},826:{"name":"United Kingdom","code":"GB"},831:{"name":"Guernsey","code":"GG"},832:{"name":"Jersey","code":"JE"},833:{"name":"Isle of Man","code":"IM"},834:{"name":"Tanzania, United Republic of","code":"TZ"},840:{"name":"United States","code":"US"},850:{"name":"Virgin Islands, U.S.","code":"VI"},854:{"name":"Burkina Faso","code":"BF"},858:{"name":"Uruguay","code":"UY"},860:{"name":"Uzbekistan","code":"UZ"},862:{"name":"Venezuela","code":"VE"},876:{"name":"Wallis and Futuna","code":"WF"},882:{"name":"Samoa","code":"WS"},887:{"name":"Yemen","code":"YE"},894:{"name":"Zambia","code":"ZM"}}

#base_url = 'https://www.similarweb.com/website/'
base_url = 'https://data.similarweb.com/api/v1/data?domain='
url = base_url + domain
#html = requests.get(url, cookies=cookies, headers=headers)
jsonresponse = requests.get(url, cookies=cookies, headers=headers)
content = json.loads(jsonresponse.content)
print(content)
SiteName = content['SiteName']
#Description = (content['Description'])
GlobalRank = (content['GlobalRank']['Rank'])
CC4CCrank = content['CountryRank']['Country'] #CC == country code
CN4CCrank = cc[CC4CCrank]["name"] #CN == country name
CountryRank = content['CountryRank']['Rank']
SiteCategory = content['CategoryRank']['Category']
CategoryRank = content['CategoryRank']['Rank']
BounceRate = round(float(content['Engagments']['BounceRate']) * 100, 2)
PagePerVisit = round(float(content['Engagments']['PagePerVisit']), 2)
MonthlyVisits = numerize.numerize(round(float(content['Engagments']['Visits'])))
TimesInSec = round(float(content['Engagments']['TimeOnSite']))
TimeOnSite = datetime.timedelta(seconds=TimesInSec)
TCSlist = content['TopCountryShares']
TopCountryShares = []
for dict in TCSlist:
    tCountryName = cc[dict['Country']]['name']
    tShareValue = round(float(dict['Value'])*100,2)
    tCountryShare = str(tCountryName)+ " : " + str(tShareValue)+ "%"
    TopCountryShares.append(tCountryShare)
TraSou = content['TrafficSources']
TrafficSources = []
for key in TraSou:
    #print(key)
    tTraSouValue = round(float(TraSou[key])*100,2)
    tTrafficSource = str(key)+ " : " + str(tTraSouValue) + "%"
    TrafficSources.append(tTrafficSource)

print(TopCountryShares)