import requests
import json


# curlconverter.com
def get_data():

  cookies = {
      'ADRUM': 's=1645346310898&r=https%3A%2F%2Fwww.mvideo.ru%2Fnaushniki-54%2Fnaushniki-3967%3F-1514563257',
      'cfidsgib-w-mvideo': '01oanCrHWNFSO4MCNWPq9KHuwJpy8K3r3/2h9av5Ujg4whwQMj+bnFMowlk7HgW/V3r2zOTEVOOFhU/Myzw5aMKhhzDFBkUOzo1GdFWTFesfKdq+5YFpfLHEfiW7sY9cgEpeQ+qcJi/0KxrvcJ9kAhBsbCabN2CWraF0Eg==',
      '__lhash_': '4951edc324cfa080f9c75af34268468a',
      'CACHE_INDICATOR': 'false',
      'COMPARISON_INDICATOR': 'false',
      'HINTS_FIO_COOKIE_NAME': '1',
      'MVID_AB_SERVICES_DESCRIPTION': 'var4',
      'MVID_ADDRESS_COMMENT_AB_TEST': '2',
      'MVID_BLACK_FRIDAY_ENABLED': 'true',
      'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
      'MVID_CART_MULTI_DELETE': 'true',
      'MVID_CATALOG_STATE': '1',
      'MVID_CITY_ID': 'CityCZ_1780',
      'MVID_FILTER_CODES': 'true',
      'MVID_FILTER_TOOLTIP': '1',
      'MVID_FLOCKTORY_ON': 'true',
      'MVID_GEOLOCATION_NEEDED': 'true',
      'MVID_GET_LOCATION_BY_DADATA': 'DaData',
      'MVID_GIFT_KIT': 'true',
      'MVID_GTM_DELAY': 'true',
      'MVID_GUEST_ID': '21165813336',
      'MVID_HANDOVER_SUMMARY': 'true',
      'MVID_IS_NEW_BR_WIDGET': 'true',
      'MVID_KLADR_ID': '6300000100000',
      'MVID_LAYOUT_TYPE': '1',
      'MVID_LP_HANDOVER': '2',
      'MVID_LP_SOLD_VARIANTS': '3',
      'MVID_MCLICK': 'true',
      'MVID_MINI_PDP': 'true',
      'MVID_NEW_ACCESSORY': 'true',
      'MVID_NEW_DESKTOP_FILTERS': 'true',
      'MVID_NEW_LK': 'true',
      'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
      'MVID_NEW_LK_LOGIN': 'true',
      'MVID_NEW_LK_OTP_TIMER': 'true',
      'MVID_NEW_MBONUS_BLOCK': 'true',
      'MVID_PROMO_CATALOG_ON': 'true',
      'MVID_REGION_ID': '4',
      'MVID_REGION_SHOP': 'S972',
      'MVID_SERVICES': '111',
      'MVID_SERVICES_MINI_BLOCK': 'var2',
      'MVID_SMART_BANNER_BOTTOM': 'true',
      'MVID_SUPER_FILTERS': 'true',
      'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
      'MVID_TIMEZONE_OFFSET': '4',
      'MVID_WEBP_ENABLED': 'true',
      'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
      'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
      'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
      'flacktory': 'no',
      'searchType2': '3',
      'MVID_ENVCLOUD': 'canary',
      '_ga': 'GA1.1.1949130276.1659289651',
      'SMSError': '',
      'authError': '',
      'tmr_lvid': 'd7e7467ecfb0cba88138cc8bb8c79cd2',
      'tmr_lvidTS': '1659289653815',
      'tmr_detect': '1%7C1659289653904',
      'uxs_uid': 'db884c70-10f8-11ed-8668-597e775d7f7b',
      'st_uid': '208579af15b245d6a9282eec843a4e40',
      'tmr_reqNum': '18',
      'JSESSIONID': '7x2dvmQTLswT8n3jhJhdHwjyyTPjJjZMLnPjRLRWh1GKnLfQGxSk!655083687',
      'bIPs': '-1341531712',
      '_ga_CFMZTSS5FM': 'GS1.1.1659289650.1.1.1659289728.0',
      '_ga_BNX5WPP3YK': 'GS1.1.1659289650.1.1.1659289728.60',
  }

  headers = {
      'authority': 'www.mvideo.ru',
      'accept': 'application/json',
      'accept-language': 'en-US,en;q=0.9',
      'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=1ec0c5485cde44df819cc44dda213827,sentry-sample_rate=1',
      # Requests sorts cookies= alphabetically
      # 'cookie': 'ADRUM=s=1645346310898&r=https%3A%2F%2Fwww.mvideo.ru%2Fnaushniki-54%2Fnaushniki-3967%3F-1514563257; cfidsgib-w-mvideo=01oanCrHWNFSO4MCNWPq9KHuwJpy8K3r3/2h9av5Ujg4whwQMj+bnFMowlk7HgW/V3r2zOTEVOOFhU/Myzw5aMKhhzDFBkUOzo1GdFWTFesfKdq+5YFpfLHEfiW7sY9cgEpeQ+qcJi/0KxrvcJ9kAhBsbCabN2CWraF0Eg==; __lhash_=4951edc324cfa080f9c75af34268468a; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_1780; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GTM_DELAY=true; MVID_GUEST_ID=21165813336; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=6300000100000; MVID_LAYOUT_TYPE=1; MVID_LP_HANDOVER=2; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=4; MVID_REGION_SHOP=S972; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_SMART_BANNER_BOTTOM=true; MVID_SUPER_FILTERS=true; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=4; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=3; MVID_ENVCLOUD=canary; _ga=GA1.1.1949130276.1659289651; SMSError=; authError=; tmr_lvid=d7e7467ecfb0cba88138cc8bb8c79cd2; tmr_lvidTS=1659289653815; tmr_detect=1%7C1659289653904; uxs_uid=db884c70-10f8-11ed-8668-597e775d7f7b; st_uid=208579af15b245d6a9282eec843a4e40; tmr_reqNum=18; JSESSIONID=7x2dvmQTLswT8n3jhJhdHwjyyTPjJjZMLnPjRLRWh1GKnLfQGxSk!655083687; bIPs=-1341531712; _ga_CFMZTSS5FM=GS1.1.1659289650.1.1.1659289728.0; _ga_BNX5WPP3YK=GS1.1.1659289650.1.1.1659289728.60',
      'dnt': '1',
      'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da',
      'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'sentry-trace': '1ec0c5485cde44df819cc44dda213827-94660ca31d4b742a-1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
      'x-set-application-id': 'b903fe2e-f8fe-48d7-aa55-26e49bf351e7',
  }

  params = {
      'categoryId': '195',
      'offset': '0',
      'limit': '24',
      'filterParams': [
          'WyJza2lka2EiLCIiLCJkYSJd',
          'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
      ],
      'doTranslit': 'true',
  }

  response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
  # print(response)

  products_ids = response.get('body').get('products')

  with open('1_products_ids,json', 'w') as file:
    json.dump(products_ids, file, indent=4, ensure_ascii=False)

  # print(products_ids)

  json_data = {
    'productIds': products_ids,
    'mediaTypes': [
      'images',
    ],
    'category': True,
    'status': True,
    'brand': True,
    'propertyTypes': [
      'KEY',
    ],
    'propertiesConfig': {
      'propertiesPortionSize': 5,
    },
    'multioffer': False,
  }

  response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

  with open('2_items.json', 'w') as file:
    json.dump(response, file, indent=4, ensure_ascii=False)


  products = response.get('body').get('products')
  # print(len(products))


  products_ids_str = ','.join(products_ids)

  params = {
    'productIds': products_ids_str,
    'addBonusRubles': 'true',
    'isPromoApplied': 'true',
  }
  
  response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

  with open('3_prices.json', 'w') as file:
    json.dump(response, file, indent=4, ensure_ascii=False)

  items_prices = {

  }

  material_prices = response.get('body').get('materialPrices')

  for item in material_prices:
    item_id = item.get('price').get('productId')
    item_base_price = item.get('price').get('basePrice')
    item_sale_price = item.get('price').get('salePrice')
    item_bonus = item.get('bonusRubles').get('total')

    items_prices[item_id] = {
      'item_basePrice': item_base_price,
      'item_salePrice': item_sale_price,
      'item_bonus': item_bonus
    }

  with open('4_items_prices.json', 'w') as file:
    json.dump(items_prices, file, indent=4, ensure_ascii=False)



def get_result():
  with open('2_items.json') as file:
    products_data = json.load(file)

  with open('4_items_prices.json') as file:
    products_prices = json.load(file)

  products_data = products_data.get('body').get('products')

  for item in products_data:
    product_id = item.get('productId')

    if product_id in products_prices:
      prices = products_prices[product_id]

    item['item_basePrice'] = prices.get('item_basePrice')
    item['item_salePrice'] = prices.get('item_salePrice')
    item['item_bonus'] = prices.get('item_bonus')

  with open('5_result.json', 'w') as file:
    json.dump(products_data, file, indent=4, ensure_ascii=False)






def main():
  get_data()
  get_result()


if __name__ == '__main__':
  main()