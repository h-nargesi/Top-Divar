> نمونه‌های خام Captured از DevTools (مرجع؛ ساختار پاسخ‌ها دستکاری نشود).
> **اسکراب ۲۰۲۶-۰۹-۱۸:** اطلاعات تماس (نام مشاور/آژانس) با نشان `REDACTED` جایگزین شده‌اند — کلیدها و ساختار JSON دست‌نخورده و فیکسچرها قابل‌استفاده‌اند؛ الگوی «REDACTED در ⟨محله⟩» همان الگوی «⟨مشاور/آژانس⟩ در ⟨محله⟩» است (heuristic آیندهٔ `is_dealer` — `divar-api.md` بخش ۵).
> تحلیل کامل ساختار درخواست/پاسخ و نگاشت فیلدها: [`divar-api.md`](divar-api.md) — طرح کانفیگ متناظر: [`configuration.md`](configuration.md)
> جزئیات آگهی: بخش `## post detail (posts-v2/web)` (JSON عملیاتی) و بخش `## fetch` (HTML fallback).

## search page 1

```js
fetch("https://api.divar.ir/v8/postlist/w/search", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:144.0) Gecko/20100101 Firefox/144.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json",
        "X-Web-Serving-Mode": "desktop",
        "X-Screen-Size": "1762x1322",
        "X-Standard-Divar-Error": "true",
        "X-Render-Type": "CSR",
        "traceparent": "00-3436b85b288bf157d4813d7bfc5fd7ae-4a37b2416bfa4bbb-00",
        "tracestate": "sentry.sampled_not_recording=1,sentry.sample_rand=0.21846375820322972,sentry.sample_rate=0.01,sentry.url=https://api.divar.ir/v8/postlist/w/search",
        "sentry-trace": "3436b85b288bf157d4813d7bfc5fd7ae-4a37b2416bfa4bbb-0",
        "baggage": "sentry-environment=client,sentry-release=the-wall-v14-124-1,sentry-public_key=7e7d19d51ebe4bd5955fda8ab50107b1,sentry-trace_id=3436b85b288bf157d4813d7bfc5fd7ae,sentry-sampled=false,sentry-sample_rand=0.21846375820322972,sentry-sample_rate=0.01",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    },
    "referrer": "https://divar.ir/",
    "body": "{\"source_view\":\"FILTER\",\"disable_recommendation\":false,\"map_state\":{\"camera_info\":{\"bbox\":{\"min_latitude\":35.656063,\"min_longitude\":51.234558,\"max_latitude\":35.820652,\"max_longitude\":51.495358},\"place_hash\":\"1||apartment-sell||\",\"zoom\":12.090831685211496},\"page_state\":\"HALF_STATE\"},\"search_data\":{\"form_data\":{\"data\":{\"bbox\":{\"repeated_float\":{\"value\":[{\"value\":51.2345581},{\"value\":35.6560631},{\"value\":51.4953575},{\"value\":35.820652}]}},\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\"}},\"map_free_roaming\":{\"boolean\":{\"value\":true}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\"}},\"warehouse\":{\"boolean\":{\"value\":true}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}}}},\"server_payload\":{\"@type\":\"type.googleapis.com/widgets.SearchData.ServerPayload\",\"additional_form_data\":{\"data\":{\"sort\":{\"str\":{\"value\":\"sort_date\"}}}}}},\"city_ids\":[\"1\"],\"previous_place_ids\":[],\"user_selected_location\":{\"places\":[{\"place_id\":\"1\"}]},\"previous_user_selected_location\":{\"places\":[]}}",
    "method": "POST",
    "mode": "cors"
});
```
response:
```json
{
 "list_top_widgets": [
  {
   "widget_type": "POST_LIST_HEADLINE",
   "data": {
    "@type": "type.googleapis.com/widgets.PostListHeadline",
    "text": "خرید و فروش آپارتمان، پنت هاوس و برج در آذری و ۵ محلهٔ دیگر تهران"
   }
  },
  {
   "widget_type": "SEARCH_ALERT_TOGGLE_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.SearchAlertToggleRowData",
    "title": "آگهی جدید اومد خبرم کن",
    "icon": {
     "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bell.png",
     "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bell.png",
     "icon_name": "BELL",
     "icon_color": "ICON_SECONDARY"
    },
    "search_hash": "5793aa1755524ef9cf5a79b74a4fe85f",
    "has_divider": true,
    "push_notification_info_box": {
     "title": "دیوار برای خبردادن انتشار آگهی\u200cهای جدید به دسترسی ارسال نوتیفیکیشن نیاز دارد.",
     "button_text": "دادن دسترسی ارسال نوتیفیکیشن",
     "dismiss_time_seconds": "604800"
    }
   },
   "action_log": {
    "server_side_info": {
     "item_type": {
      "type": "SEARCH_ALERT_TOGGLE"
     }
    },
    "enabled": true
   },
   "uid": "search_alert_toggle_row"
  },
  {
   "widget_type": "MAP_POST_COUNT_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.MapPostCountRowData"
   },
   "uid": "map_post_count_row"
  }
 ],
 "list_widgets": [
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "۸۰ متر/۲ خواب/بازسازی شده/صرافهای شمالی",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gapa1FMk",
      "web_info": {
       "title": "۸۰ متر/۲ خواب/بازسازی شده/صرافهای شمالی",
       "district_persian": "سعادت\u200cآباد",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapa1FMk_N"
     }
    },
    "image_url": "https://s100.divarcdn.com/static/photo/neda/webp_thumbnail/KvdepfALl2w67HJkWSfWig/452d4fdc-e5ac-4d9d-85fd-c5c594664ee5.webp",
    "bottom_description_text": "مشاور املاک در سعادت\u200cآباد",
    "middle_description_text": "۳۵,۰۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 8,
    "image_top_left_tag": {
     "text": "۸",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gapa1FMk"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gapa1FMk",
           "web_info": {
            "title": "۸۰ متر/۲ خواب/بازسازی شده/صرافهای شمالی",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gapa1FMk",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapa1FMk_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gapa1FMk",
      "index": 0,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "recent_ads": {
         "value": "1d"
        },
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "floor": {
         "min": -1,
         "max": 6
        },
        "parking": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "elevator": true,
        "sort": {
         "value": "sort_date"
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "min": 40,
         "max": 140
        },
        "rebuilt": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "category": {
         "value": "apartment-sell"
        },
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "cities": [
         "1"
        ]
       },
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "server_payload_json": "{\"@type\":\"type.googleapis.com/widgets.SearchData.ServerPayload\",\"additional_form_data\":{\"data\":{\"sort\":{\"str\":{\"value\":\"sort_date\"}}}}}",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       }
      },
      "sort_date": "2026-09-15T14:29:17.323148Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "129متر.بالای کاج. فرعی دنج",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gapCVkTW",
      "web_info": {
       "title": "129متر.بالای کاج. فرعی دنج",
       "district_persian": "سعادت\u200cآباد",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapCVkTW_N"
     }
    },
    "image_url": "https://s100.divarcdn.com/static/photo/neda/webp_thumbnail/eMD6NTvRQ4vBjodG6FA-fg/14ac5720-6d0b-48a5-a17e-9eaaf44be506.webp",
    "bottom_description_text": "REDACTED در سعادت\u200cآباد",
    "middle_description_text": "۵۲,۰۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 5,
    "image_top_left_tag": {
     "text": "۵",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gapCVkTW"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gapCVkTW",
           "web_info": {
            "title": "129متر.بالای کاج. فرعی دنج",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gapCVkTW",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapCVkTW_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gapCVkTW",
      "index": 1,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "parking": true,
        "building-age": {
         "max": 15,
         "min": 0
        },
        "elevator": true,
        "sort": {
         "value": "sort_date"
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "min": 40,
         "max": 140
        },
        "rebuilt": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "category": {
         "value": "apartment-sell"
        },
        "price_per_square": {
         "max": 900000000,
         "min": 256000000
        },
        "warehouse": true,
        "cities": [
         "1"
        ],
        "recent_ads": {
         "value": "1d"
        },
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "floor": {
         "min": -1,
         "max": 6
        }
       },
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "server_payload_json": "{\"@type\":\"type.googleapis.com/widgets.SearchData.ServerPayload\",\"additional_form_data\":{\"data\":{\"sort\":{\"str\":{\"value\":\"sort_date\"}}}}}",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       }
      },
      "sort_date": "2026-09-15T14:05:19.199979Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "آپارتمان ۱۱۷ متری علامه شمالی",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gapST84s",
      "web_info": {
       "title": "آپارتمان ۱۱۷ متری علامه شمالی",
       "district_persian": "سعادت\u200cآباد",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapST84s_N"
     }
    },
    "image_url": "https://s100.divarcdn.com/static/photo/neda/webp_thumbnail/pWdbhFA6aTCPtRtcqV3mug/11b0d23d-20f6-498d-9730-d3fad45dd9d7.webp",
    "bottom_description_text": "REDACTED در سعادت\u200cآباد",
    "middle_description_text": "۵۵,۰۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 8,
    "image_top_left_tag": {
     "text": "۸",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gapST84s"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gapST84s",
           "web_info": {
            "title": "آپارتمان ۱۱۷ متری علامه شمالی",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gapST84s",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapST84s_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gapST84s",
      "index": 2,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "floor": {
         "max": 6,
         "min": -1
        },
        "parking": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "elevator": true,
        "sort": {
         "value": "sort_date"
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "min": 40,
         "max": 140
        },
        "rebuilt": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "category": {
         "value": "apartment-sell"
        },
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "cities": [
         "1"
        ],
        "recent_ads": {
         "value": "1d"
        },
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "price": {
         "min": 11000000000,
         "max": 60000000000
        }
       },
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "server_payload_json": "{\"@type\":\"type.googleapis.com/widgets.SearchData.ServerPayload\",\"additional_form_data\":{\"data\":{\"sort\":{\"str\":{\"value\":\"sort_date\"}}}}}",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       }
      },
      "sort_date": "2026-09-15T12:10:18.010474Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "۹۵متر علامه شمالی",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gapCTkSq",
      "web_info": {
       "title": "۹۵متر علامه شمالی",
       "district_persian": "سعادت\u200cآباد",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapCTkSq_N"
     }
    },
    "image_url": "https://s100.divarcdn.com/static/photo/neda/webp_thumbnail/tBGZCB3y-YPSpNr3wACcog/c65c4fb2-2280-4b22-a404-176751180a26.webp",
    "bottom_description_text": "REDACTED در سعادت\u200cآباد",
    "middle_description_text": "۴۱,۰۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 1,
    "image_top_left_tag": {
     "text": "۱",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gapCTkSq"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gapCTkSq",
           "web_info": {
            "title": "۹۵متر علامه شمالی",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gapCTkSq",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapCTkSq_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gapCTkSq",
      "index": 3,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "elevator": true,
        "sort": {
         "value": "sort_date"
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "min": 40,
         "max": 140
        },
        "rebuilt": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "category": {
         "value": "apartment-sell"
        },
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "cities": [
         "1"
        ],
        "recent_ads": {
         "value": "1d"
        },
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "floor": {
         "min": -1,
         "max": 6
        },
        "parking": true,
        "building-age": {
         "min": 0,
         "max": 15
        }
       },
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "server_payload_json": "{\"@type\":\"type.googleapis.com/widgets.SearchData.ServerPayload\",\"additional_form_data\":{\"data\":{\"sort\":{\"str\":{\"value\":\"sort_date\"}}}}}",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       }
      },
      "sort_date": "2026-09-15T11:48:43.809806Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "اپارتمان ۷۹ متری",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gapWiPux",
      "web_info": {
       "title": "اپارتمان ۷۹ متری",
       "district_persian": "آبشار تهران (دریاچه)",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapWiPux_N"
     }
    },
    "image_url": "https://s100.divarcdn.com/static/photo/neda/webp_thumbnail/LeguZ4DMnroIS12UXOF-MQ/2ee7b46d-8ac8-416d-9c93-a53dcf21ade4.webp",
    "bottom_description_text": "۹ ساعت پیش در آبشار تهران (دریاچه)",
    "middle_description_text": "۲۲,۱۲۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 1,
    "image_top_left_tag": {
     "text": "۱",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gapWiPux"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gapWiPux",
           "web_info": {
            "title": "اپارتمان ۷۹ متری",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gapWiPux",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapWiPux_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gapWiPux",
      "index": 4,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "cities": [
         "1"
        ],
        "recent_ads": {
         "value": "1d"
        },
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "floor": {
         "min": -1,
         "max": 6
        },
        "parking": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "elevator": true,
        "sort": {
         "value": "sort_date"
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "min": 40,
         "max": 140
        },
        "rebuilt": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "category": {
         "value": "apartment-sell"
        }
       },
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "server_payload_json": "{\"@type\":\"type.googleapis.com/widgets.SearchData.ServerPayload\",\"additional_form_data\":{\"data\":{\"sort\":{\"str\":{\"value\":\"sort_date\"}}}}}",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       }
      },
      "sort_date": "2026-09-15T11:05:44.501011Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "۸۳متر۲خواب سعادت آباد علامه شمالی",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "ganKwkiP",
      "web_info": {
       "title": "۸۳متر۲خواب سعادت آباد علامه شمالی",
       "district_persian": "سعادت\u200cآباد",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_ganKwkiP_N"
     }
    },
    "image_url": "https://s100.divarcdn.com/static/photo/neda/webp_thumbnail/La4CNKVndRnR4aWfcfLQsA/b1b7b5d3-16dd-48af-b0f0-44826fe3feac.webp",
    "bottom_description_text": "REDACTED در سعادت\u200cآباد",
    "middle_description_text": "۴۴,۰۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 15,
    "image_top_left_tag": {
     "text": "۱۵",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "ganKwkiP"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "ganKwkiP",
           "web_info": {
            "title": "۸۳متر۲خواب سعادت آباد علامه شمالی",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "ganKwkiP",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_ganKwkiP_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "ganKwkiP",
      "index": 5,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "parking": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "elevator": true,
        "sort": {
         "value": "sort_date"
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "min": 40,
         "max": 140
        },
        "rebuilt": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "category": {
         "value": "apartment-sell"
        },
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "cities": [
         "1"
        ],
        "recent_ads": {
         "value": "1d"
        },
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "floor": {
         "min": -1,
         "max": 6
        }
       },
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "server_payload_json": "{\"@type\":\"type.googleapis.com/widgets.SearchData.ServerPayload\",\"additional_form_data\":{\"data\":{\"sort\":{\"str\":{\"value\":\"sort_date\"}}}}}",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       }
      },
      "sort_date": "2026-09-15T10:21:36.819344Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "بلوار فرهنگ ۸۵متر",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gafebEer",
      "web_info": {
       "title": "بلوار فرهنگ ۸۵متر",
       "district_persian": "دریا",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gafebEer_N"
     }
    },
    "image_url": "https://s100.divarcdn.com/static/photo/neda/webp_thumbnail/fGzEPHgjUjq_X4pkPicqDA/2f2b1ef4-3ac4-46fa-b371-de3661edce93.webp",
    "bottom_description_text": "REDACTED در دریا",
    "red_text": "نردبان شده",
    "middle_description_text": "۳۳,۰۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 17,
    "image_top_left_tag": {
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/videocam.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/videocam.png",
      "icon_name": "VIDEOCAM",
      "icon_color": "WHITE_PRIMARY"
     }
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gafebEer"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gafebEer",
           "web_info": {
            "title": "بلوار فرهنگ ۸۵متر",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gafebEer",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gafebEer_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gafebEer",
      "index": 6,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "cities": [
         "1"
        ],
        "recent_ads": {
         "value": "1d"
        },
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "floor": {
         "min": -1,
         "max": 6
        },
        "parking": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "elevator": true,
        "sort": {
         "value": "sort_date"
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "min": 40,
         "max": 140
        },
        "rebuilt": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "category": {
         "value": "apartment-sell"
        }
       },
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "server_payload_json": "{\"@type\":\"type.googleapis.com/widgets.SearchData.ServerPayload\",\"additional_form_data\":{\"data\":{\"sort\":{\"str\":{\"value\":\"sort_date\"}}}}}",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       }
      },
      "sort_date": "2026-09-15T10:05:42.698806Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "آپارتمان ۷۸ متری سعادت آباد کتاب",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gapCQxrL",
      "web_info": {
       "title": "آپارتمان ۷۸ متری سعادت آباد کتاب",
       "district_persian": "سعادت\u200cآباد",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapCQxrL_N"
     }
    },
    "image_url": "https://s100.divarcdn.com/static/photo/neda/webp_thumbnail/EtrgTIoHah6tC9OEDna84A/c88dae79-9751-436f-b0f8-413933375964.webp",
    "bottom_description_text": "REDACTED در سعادت\u200cآباد",
    "middle_description_text": "۳۲,۰۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 18,
    "image_top_left_tag": {
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/videocam.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/videocam.png",
      "icon_name": "VIDEOCAM",
      "icon_color": "WHITE_PRIMARY"
     }
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gapCQxrL"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gapCQxrL",
           "web_info": {
            "title": "آپارتمان ۷۸ متری سعادت آباد کتاب",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gapCQxrL",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapCQxrL_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gapCQxrL",
      "index": 7,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "cities": [
         "1"
        ],
        "recent_ads": {
         "value": "1d"
        },
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "floor": {
         "min": -1,
         "max": 6
        },
        "parking": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "elevator": true,
        "sort": {
         "value": "sort_date"
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "min": 40,
         "max": 140
        },
        "rebuilt": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "category": {
         "value": "apartment-sell"
        }
       },
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "server_payload_json": "{\"@type\":\"type.googleapis.com/widgets.SearchData.ServerPayload\",\"additional_form_data\":{\"data\":{\"sort\":{\"str\":{\"value\":\"sort_date\"}}}}}",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       }
      },
      "sort_date": "2026-09-15T08:25:33.266302Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  }
 ],
 "search_data": {
  "form_data": {
   "data": {
    "rebuilt": {
     "boolean": {
      "value": true
     }
    },
    "price_per_square": {
     "number_range": {
      "minimum": "256000000",
      "maximum": "900000000",
      "value": {
       "minimum": "256000000",
       "maximum": "900000000"
      }
     }
    },
    "elevator": {
     "boolean": {
      "value": true
     }
    },
    "category": {
     "str": {
      "value": "apartment-sell"
     }
    },
    "rooms": {
     "repeated_string": {
      "value": [
       "یک",
       "دو",
       "سه",
       "چهار"
      ]
     }
    },
    "warehouse": {
     "boolean": {
      "value": true
     }
    },
    "building-age": {
     "number_range": {
      "minimum": "0",
      "maximum": "15",
      "value": {
       "minimum": "0",
       "maximum": "15"
      }
     }
    },
    "size": {
     "number_range": {
      "minimum": "40",
      "maximum": "140",
      "value": {
       "minimum": "40",
       "maximum": "140"
      }
     }
    },
    "floor": {
     "number_range": {
      "minimum": "-1",
      "maximum": "6",
      "value": {
       "minimum": "-1",
       "maximum": "6"
      }
     }
    },
    "price": {
     "number_range": {
      "minimum": "11000000000",
      "maximum": "60000000000",
      "value": {
       "minimum": "11000000000",
       "maximum": "60000000000"
      }
     }
    },
    "districts": {
     "repeated_string": {
      "value": [
       "198",
       "399",
       "654",
       "75",
       "907",
       "929"
      ]
     }
    },
    "parking": {
     "boolean": {
      "value": true
     }
    },
    "recent_ads": {
     "str": {
      "value": "1d"
     }
    }
   }
  },
  "server_payload": {
   "@type": "type.googleapis.com/widgets.SearchData.ServerPayload",
   "additional_form_data": {
    "data": {
     "sort": {
      "str": {
       "value": "sort_date"
      }
     }
    }
   }
  }
 },
 "action_log": {
  "server_side_info": {
   "info": {
    "@type": "type.googleapis.com/action_log.PostListLoadPageInfo",
    "cities": [
     "1"
    ],
    "current_tab": "default",
    "search_data": {
     "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
     "server_payload_json": "{\"@type\":\"type.googleapis.com/widgets.SearchData.ServerPayload\",\"additional_form_data\":{\"data\":{\"sort\":{\"str\":{\"value\":\"sort_date\"}}}}}",
     "cities": [
      "1"
     ],
     "query_input_type": "TEXT",
     "user_selected_location": {
      "@type": "type.googleapis.com/widgets.UserSelectedLocation",
      "places": [
       {
        "place_id": "1"
       }
      ]
     }
    },
    "tokens": [
     "gapa1FMk",
     "gapCVkTW",
     "gapST84s",
     "gapCTkSq",
     "gapWiPux",
     "ganKwkiP",
     "gafebEer",
     "gapCQxrL"
    ],
    "has_next_page": true,
    "pelle": {
     "elastic": {}
    },
    "last_post_date_epoch": "1789460733266302",
    "search_id": "5793aa1755524ef9cf5a79b74a4fe85f",
    "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
    "source_view": "MAP_DISCOVERY_MAP",
    "posts_metadata": [
     {
      "token": "gapa1FMk",
      "sort_date": "1789482557323148",
      "source": "f",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":21469}"
     },
     {
      "token": "gapCVkTW",
      "sort_date": "1789481119199979",
      "source": "f",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":22907}"
     },
     {
      "token": "gapST84s",
      "sort_date": "1789474218010474",
      "source": "f",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":29808}"
     },
     {
      "token": "gapCTkSq",
      "sort_date": "1789472923809806",
      "source": "f",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":31102}"
     },
     {
      "token": "gapWiPux",
      "sort_date": "1789470344501011",
      "source": "f",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":33682}"
     },
     {
      "token": "ganKwkiP",
      "sort_date": "1789467696819344",
      "source": "f",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":36329}"
     },
     {
      "token": "gafebEer",
      "sort_date": "1789466742698806",
      "source": "f",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":37283}"
     },
     {
      "token": "gapCQxrL",
      "sort_date": "1789460733266302",
      "source": "f",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":43293}"
     }
    ],
    "jli": {
     "price": {
      "min": 11000000000,
      "max": 60000000000
     },
     "floor": {
      "min": -1,
      "max": 6
     },
     "parking": true,
     "building-age": {
      "min": 0,
      "max": 15
     },
     "elevator": true,
     "sort": {
      "value": "sort_date"
     },
     "places": {
      "value": [
       "1"
      ]
     },
     "size": {
      "min": 40,
      "max": 140
     },
     "rebuilt": true,
     "districts": {
      "vacancies": [
       "198",
       "399",
       "654",
       "75",
       "907",
       "929"
      ]
     },
     "category": {
      "value": "apartment-sell"
     },
     "price_per_square": {
      "min": 256000000,
      "max": 900000000
     },
     "warehouse": true,
     "cities": [
      "1"
     ],
     "recent_ads": {
      "value": "1d"
     },
     "rooms": {
      "value": [
       "یک",
       "دو",
       "سه",
       "چهار"
      ]
     }
    },
    "search_layer": "fulltext_t1",
    "bookmark_info": {
     "search_hash": "5793aa1755524ef9cf5a79b74a4fe85f",
     "bookmark_state": {},
     "alert_state": {}
    },
    "widget_order": [
     {
      "type": "SEARCH_RESULT",
      "track_id": "gapa1FMk"
     },
     {
      "index": 1,
      "type": "SEARCH_RESULT",
      "track_id": "gapCVkTW"
     },
     {
      "index": 2,
      "type": "SEARCH_RESULT",
      "track_id": "gapST84s"
     },
     {
      "index": 3,
      "type": "SEARCH_RESULT",
      "track_id": "gapCTkSq"
     },
     {
      "index": 4,
      "type": "SEARCH_RESULT",
      "track_id": "gapWiPux"
     },
     {
      "index": 5,
      "type": "SEARCH_RESULT",
      "track_id": "ganKwkiP"
     },
     {
      "index": 6,
      "type": "SEARCH_RESULT",
      "track_id": "gafebEer"
     },
     {
      "index": 7,
      "type": "SEARCH_RESULT",
      "track_id": "gapCQxrL"
     }
    ],
    "list_level_extra_info": "{}",
    "user_selected_location": {
     "@type": "type.googleapis.com/widgets.UserSelectedLocation",
     "places": [
      {
       "place_id": "1"
      }
     ]
    }
   },
   "item_type": {
    "type": "POST_LIST_LOAD_PAGE"
   }
  },
  "enabled": true
 },
 "search_bar": {
  "bookmark": {
   "toggle_action_log": {
    "server_side_info": {
     "item_type": {
      "type": "SEARCH_BAR_BOOKMARKED_STATE_CHANGE_STATE"
     }
    },
    "enabled": true
   },
   "enabled": true,
   "bookmark_info": {
    "search_hash": "5793aa1755524ef9cf5a79b74a4fe85f",
    "bookmark_state": {},
    "alert_state": {}
   }
  }
 },
 "pagination": {
  "has_next_page": true,
  "data": {
   "@type": "type.googleapis.com/post_list.PaginationData",
   "last_post_date": "2026-09-15T08:25:33.266302Z",
   "page": 1,
   "layer_id": 1,
   "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
   "cumulative_widgets_count": 8,
   "viewed_tokens": "H4sIAAAAAAAE/wTAsQqAIBAG4Be6JWhol1oqMJSc/8B+5CAuI/Lx+whDN60qhLldYxLCQhz6RwhzUcMthKXi3ybENX9avBBnPsZchTC3tbr8AQAA//9EZfSqRwAAAA==",
   "search_bookmark_info": {
    "search_hash": "5793aa1755524ef9cf5a79b74a4fe85f",
    "bookmark_state": {},
    "alert_state": {}
   },
   "first_page_viewed_at": "2026-09-15T20:27:06.543881332Z",
   "filters_hash": "V5OqF1VSTvnPWnm3Sk/oXw=="
  },
  "is_first_page": true
 },
 "search_id": "5793aa1755524ef9cf5a79b74a4fe85f",
 "seo_details": {
  "title": "خرید و فروش آپارتمان، پنت هاوس و برج در آذری و ۵ محلهٔ دیگر تهران با بهترین قیمت | دیوار",
  "description": "بهترین گزینه\u200cها برای خرید و فروش آپارتمان، پنت\u200cهاوس و برج در آذری و ۵ محلهٔ دیگر تهران را در دیوار پیدا کنید. قیمت\u200cهای مناسب و تنوع بالا!",
  "headline": "خرید و فروش آپارتمان، پنت هاوس و برج در آذری و ۵ محلهٔ دیگر تهران",
  "robots_metadata": {
   "follow": true
  },
  "bread_crumb": [
   {
    "name": "آپارتمان",
    "search_data": {
     "form_data": {
      "data": {
       "category": {
        "str": {
         "value": "apartment-sell"
        }
       },
       "districts": {
        "repeated_string": {
         "value": [
          "198"
         ]
        }
       }
      }
     }
    }
   },
   {
    "name": "فروش مسکونی",
    "search_data": {
     "form_data": {
      "data": {
       "districts": {
        "repeated_string": {
         "value": [
          "198"
         ]
        }
       },
       "category": {
        "str": {
         "value": "residential-sell"
        }
       }
      }
     }
    }
   },
   {
    "name": "املاک",
    "search_data": {
     "form_data": {
      "data": {
       "category": {
        "str": {
         "value": "real-estate"
        }
       },
       "districts": {
        "repeated_string": {
         "value": [
          "198"
         ]
        }
       }
      }
     }
    }
   },
   {
    "name": "آذری",
    "search_data": {
     "form_data": {
      "data": {
       "districts": {
        "repeated_string": {
         "value": [
          "198"
         ]
        }
       }
      }
     }
    }
   },
   {
    "name": "تهران",
    "search_data": {
     "form_data": {}
    }
   },
   {
    "name": "دیوار"
   }
  ]
 },
 "map_data": {
  "encoded_polygon_list": [
   "yfuxEyhkxHKU_@y@QoCk@aBwAmDmEwLiHyP@w@Do@`EcPdF[xEa@dRyAd@tEL|@Tz@f@fA{Ib_AeAMsAYqA]}@[a@s@",
   "oicyEm~hyHnCca@|AkVbB}VbBcWbB_W`AcN~TtMi@~HmJ~uA{Dxl@iAbQOfBCR_@hBSlCs@jIoAaAcBsBmM_P~Bg]",
   "k|zxE}mtxHdCelAjBPlFj@dTvBlTrBwDnn@y@xLwAHkCVqHh@aBHgKp@aQhA",
   "qfmyE}eqxH_B_Ew@kDa@}DqA{OcA}G_DwN]cBWuBM}BKqC?qAB_ANoBPiB\\eBf@gBpAmCdA{A~A_BfCyAbCo@bC|@`BLrA?lHq@rVgDrDc@hD?bEXfEbBtFvC~FhDeDrF{BxEqArFQfG?jJnCbQ~Dp\\tAzGdC`XxA~RjCf[uh@xIcQ`CkAqHeB{Gu@oBwCgGyA{CuCiIi@sCm@qC{@cFACuByHaGsO",
   "magyEi}uwHrBlT|Cpa@xAjY?rDQlHsF~}@yLaAiBi@}CmCk@e@{BeD}A]u@Co@TuDUr@mLjBd@Vi\\zCmpAsFoUqDkOzI`A`AaErI}BjIe@pCxX",
   "_oiyEkssxH?lQ@~c@\\GdQKl@Bj@HrAVLliAqNtI{DdAmZnFkCg[yA_SeCaXuA{G_Eq\\oCcQ?kJPgGpAsFzByEdDsFfC~AbB|@xCdBhGlDnFlCpCx@rB\\"
  ],
  "state": {
   "camera_info": {
    "bbox": {
     "min_longitude": 51.209896087646484,
     "min_latitude": 35.663768768310547,
     "max_longitude": 51.52001953125,
     "max_latitude": 35.792888641357422
    },
    "place_hash": "1|198,399,654,75,907,929|apartment-sell||",
    "zoom": 12.090831685211496
   },
   "page_state": "HALF_STATE",
   "state_hash": "list"
  },
  "post_count_text": "۸ آگهی در این محدوده",
  "post_count": 8,
  "config": {
   "style_url": "https://map.divar.ir/back/style/prod/style-light-view-port-v1.0.0-abef6830-neshan.json",
   "dark_style_url": "https://map.divar.ir/back/style/prod/style-dark-view-port-v1.0.0-abef6830-neshan.json",
   "source_id": "divar-map-discovery-posts-source-v0.1.1",
   "layer_ids": [
    "divar-map-discovery-posts-layer-mini-pins-view-port",
    "divar-map-discovery-posts-layer-long-text-pins-view-port",
    "divar-map-discovery-new-posts-layer-long-text-pins-view-port",
    "divar-map-discovery-posts-history-layer-mini-pins",
    "divar-map-discovery-posts-history-layer-long-text-pins",
    "divar-map-discovery-posts-layer-mini-pins-view-port-problematic",
    "divar-map-discovery-posts-layer-mini-pins-view-port-llm-verified",
    "divar-map-discovery-posts-history-layer-long-text-pins-problematic",
    "divar-map-discovery-posts-layer-long-text-pins-view-port-llm-verified",
    "divar-map-discovery-new-posts-layer-long-text-pins-view-port-llm-verified",
    "divar-map-discovery-posts-layer-long-text-pins-view-port-verified",
    "divar-map-discovery-posts-history-layer-long-text-pins-verified"
   ],
   "marker_source_id": "divar-map-discovery-active-marker-source",
   "history_source_id": "divar-map-discovery-posts-history-source",
   "satellite_style_url": "https://map.divar.ir/back/style/style-android-v0.2.0.json",
   "clustering_layer_ids": [
    "divar-map-discovery-clustered-posts-layer-view-port"
   ],
   "click_padding": {
    "top": 12,
    "bottom": 24,
    "left": 12,
    "right": 12
   },
   "clustering_click_padding": {
    "top": 12,
    "bottom": 24,
    "left": 12,
    "right": 12
   },
   "view_port_post_source_id": "divar-map-discovery-view-port-posts-source",
   "view_port_cluster_source_id": "divar-map-discovery-view-port-clusters-source"
  },
  "map_switch_mode": "BOTTOM_SHEET"
 },
 "suggestion_cache_data": [
  {
   "input_data": {
    "number_range": {
     "minimum": "11000000000",
     "maximum": "60000000000",
     "value": {
      "minimum": "11000000000",
      "maximum": "60000000000"
     }
    }
   },
   "display": "از ۱۱ میلیارد تا ۶۰ میلیارد",
   "cache_key": "apartment-sell:price"
  },
  {
   "input_data": {
    "number_range": {
     "minimum": "0",
     "maximum": "15",
     "value": {
      "minimum": "0",
      "maximum": "15"
     }
    }
   },
   "display": "از نوساز تا ۱۵ سال",
   "cache_key": "apartment-sell:building-age"
  },
  {
   "input_data": {
    "number_range": {
     "minimum": "40",
     "maximum": "140",
     "value": {
      "minimum": "40",
      "maximum": "140"
     }
    }
   },
   "display": "از ۴۰ متر تا ۱۴۰ متر",
   "cache_key": "apartment-sell:size"
  },
  {
   "input_data": {
    "number_range": {
     "minimum": "-1",
     "maximum": "6",
     "value": {
      "minimum": "-1",
      "maximum": "6"
     }
    }
   },
   "display": "از زیر همکف تا ۶",
   "cache_key": "apartment-sell:floor"
  },
  {
   "input_data": {
    "number_range": {
     "minimum": "256000000",
     "maximum": "900000000",
     "value": {
      "minimum": "256000000",
      "maximum": "900000000"
     }
    }
   },
   "display": "از ۲۵۶ میلیون تا ۹۰۰ میلیون",
   "cache_key": "apartment-sell:price_per_square"
  },
  {
   "input_data": {
    "repeated_string": {
     "value": [
      "198"
     ]
    }
   },
   "display": "آذری",
   "cache_key": "districts"
  },
  {
   "input_data": {
    "repeated_string": {
     "value": [
      "399"
     ]
    }
   },
   "display": "نارمک",
   "cache_key": "districts"
  },
  {
   "input_data": {
    "repeated_string": {
     "value": [
      "654"
     ]
    }
   },
   "display": "آذربایجان",
   "cache_key": "districts"
  },
  {
   "input_data": {
    "repeated_string": {
     "value": [
      "75"
     ]
    }
   },
   "display": "سعادت\u200cآباد",
   "cache_key": "districts"
  },
  {
   "input_data": {
    "repeated_string": {
     "value": [
      "907"
     ]
    }
   },
   "display": "آبشار تهران (دریاچه)",
   "cache_key": "districts"
  },
  {
   "input_data": {
    "repeated_string": {
     "value": [
      "929"
     ]
    }
   },
   "display": "دریا",
   "cache_key": "districts"
  }
 ],
 "show_no_search_result_notice": true
}
```

## search page 2

```js
fetch("https://api.divar.ir/v8/postlist/w/search", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:144.0) Gecko/20100101 Firefox/144.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json",
        "X-Web-Serving-Mode": "desktop",
        "X-Screen-Size": "1762x1322",
        "X-Standard-Divar-Error": "true",
        "X-Render-Type": "CSR",
        "traceparent": "00-182297dc47b6cd346d6a35857d107d20-c3d4d9be254efc96-00",
        "tracestate": "sentry.sampled_not_recording=1,sentry.sample_rand=0.08485441732917909,sentry.sample_rate=0.01,sentry.url=https://api.divar.ir/v8/postlist/w/search",
        "sentry-trace": "182297dc47b6cd346d6a35857d107d20-c3d4d9be254efc96-0",
        "baggage": "sentry-environment=client,sentry-release=the-wall-v14-124-1,sentry-public_key=7e7d19d51ebe4bd5955fda8ab50107b1,sentry-trace_id=182297dc47b6cd346d6a35857d107d20,sentry-sampled=false,sentry-sample_rand=0.08485441732917909,sentry-sample_rate=0.01",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    },
    "referrer": "https://divar.ir/",
    "body": "{\"source_view\":\"FILTER\",\"pagination_data\":{\"@type\":\"type.googleapis.com/post_list.PaginationData\",\"last_post_date\":\"2026-09-15T08:25:33.266302Z\",\"page\":1,\"layer_id\":1,\"search_uid\":\"a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8\",\"cumulative_widgets_count\":8,\"viewed_tokens\":\"H4sIAAAAAAAE/wTAsQqAIBAG4Be6JWhol1oqMJSc/8B+5CAuI/Lx+whDN60qhLldYxLCQhz6RwhzUcMthKXi3ybENX9avBBnPsZchTC3tbr8AQAA//9EZfSqRwAAAA==\",\"search_bookmark_info\":{\"search_hash\":\"5793aa1755524ef9cf5a79b74a4fe85f\",\"bookmark_state\":{},\"alert_state\":{}},\"first_page_viewed_at\":\"2026-09-15T20:27:06.543881332Z\",\"filters_hash\":\"V5OqF1VSTvnPWnm3Sk/oXw==\"},\"disable_recommendation\":false,\"map_state\":{\"camera_info\":{\"bbox\":{}}},\"search_data\":{\"form_data\":{\"data\":{\"rebuilt\":{\"boolean\":{\"value\":true}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"elevator\":{\"boolean\":{\"value\":true}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"warehouse\":{\"boolean\":{\"value\":true}},\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"parking\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}}}},\"server_payload\":{\"@type\":\"type.googleapis.com/widgets.SearchData.ServerPayload\",\"additional_form_data\":{\"data\":{\"sort\":{\"str\":{\"value\":\"sort_date\"}}}}}},\"city_ids\":[\"1\"],\"user_selected_location\":{\"places\":[{\"place_id\":\"1\"}]},\"previous_user_selected_location\":{\"places\":[]}}",
    "method": "POST",
    "mode": "cors"
});
```
response:
```json
{
 "list_widgets": [
  {
   "widget_type": "DIVIDER_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.DividerRowData",
    "fullwidth": true,
    "padded": true
   }
  },
  {
   "widget_type": "SELECTOR_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.SelectorRowData",
    "title": "آگهی\u200cهای مشابه",
    "icon": {},
    "description": "آگهی\u200cهای زیر، نتیجه\u200cهای نزدیک به جستجوی شماست.",
    "last_notification_date": "0001-01-01T00:00:00Z",
    "fullwidth": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "۷۴متر دو خواب فول امکانات تکواحد تاپ لوکیشن",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gapOqAFe",
      "web_info": {
       "title": "۷۴متر دو خواب فول امکانات تکواحد تاپ لوکیشن",
       "district_persian": "مدائن",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapOqAFe_N"
     }
    },
    "image_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/xk063r5G3uoAY60RcpgqFA/ec5b49bc-0d35-4126-b9ad-15266c8b5571.webp",
    "bottom_description_text": "REDACTED در مدائن",
    "middle_description_text": "۲۱,۵۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 1,
    "image_top_left_tag": {
     "text": "۱",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gapOqAFe"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gapOqAFe",
           "web_info": {
            "title": "۷۴متر دو خواب فول امکانات تکواحد تاپ لوکیشن",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gapOqAFe",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapOqAFe_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gapOqAFe",
      "index": 0,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "recent_ads": {
         "value": "1d"
        },
        "cities": [
         "1"
        ],
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "max": 140,
         "min": 40
        },
        "floor": {
         "min": -1,
         "max": 6
        },
        "category": {
         "value": "apartment-sell"
        },
        "parking": true,
        "sort": {
         "value": "sort_date"
        },
        "rebuilt": true,
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "elevator": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "building-age": {
         "min": 0,
         "max": 15
        }
       },
       "last_post_sort_date": "1789460733266302",
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "sort": "sort_date",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       },
       "page": 1
      },
      "sort_date": "2026-09-15T20:03:28.795195Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "سامان شمالی ۹۰متری شیک تکواحدی دوکله فول ۷سال ساخت",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gap6V9xd",
      "web_info": {
       "title": "سامان شمالی ۹۰متری شیک تکواحدی دوکله فول ۷سال ساخت",
       "district_persian": "هفت حوض",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gap6V9xd_N"
     }
    },
    "image_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/5_Q_fsi2M27QTsyx6xSp8Q/d44ae7a0-c85e-4aa7-b633-2138a514684f.webp",
    "bottom_description_text": "REDACTED در هفت حوض",
    "middle_description_text": "۲۵,۲۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 17,
    "image_top_left_tag": {
     "text": "۱۷",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gap6V9xd"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gap6V9xd",
           "web_info": {
            "title": "سامان شمالی ۹۰متری شیک تکواحدی دوکله فول ۷سال ساخت",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gap6V9xd",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gap6V9xd_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gap6V9xd",
      "index": 1,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "category": {
         "value": "apartment-sell"
        },
        "parking": true,
        "sort": {
         "value": "sort_date"
        },
        "rebuilt": true,
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "elevator": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "price_per_square": {
         "max": 900000000,
         "min": 256000000
        },
        "warehouse": true,
        "building-age": {
         "max": 15,
         "min": 0
        },
        "recent_ads": {
         "value": "1d"
        },
        "cities": [
         "1"
        ],
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "max": 140,
         "min": 40
        },
        "floor": {
         "min": -1,
         "max": 6
        }
       },
       "last_post_sort_date": "1789460733266302",
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "sort": "sort_date",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       },
       "page": 1
      },
      "sort_date": "2026-09-15T15:06:55.745259Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "100متر   سالن پرده خور     فول    دردشت",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gapKlv_g",
      "web_info": {
       "title": "100متر   سالن پرده خور     فول    دردشت",
       "district_persian": "دردشت",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapKlv_g_N"
     }
    },
    "image_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/PP8qcdCUElG7NkHEFPJ98A/cf4f3613-9f38-49fc-84b9-7e49bdfa8ce3.webp",
    "bottom_description_text": "REDACTED در دردشت",
    "middle_description_text": "۲۸,۴۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 2,
    "image_top_left_tag": {
     "text": "۲",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gapKlv_g"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gapKlv_g",
           "web_info": {
            "title": "100متر   سالن پرده خور     فول    دردشت",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gapKlv_g",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapKlv_g_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gapKlv_g",
      "index": 2,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "min": 40,
         "max": 140
        },
        "floor": {
         "min": -1,
         "max": 6
        },
        "category": {
         "value": "apartment-sell"
        },
        "parking": true,
        "sort": {
         "value": "sort_date"
        },
        "rebuilt": true,
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "elevator": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "recent_ads": {
         "value": "1d"
        },
        "cities": [
         "1"
        ],
        "price": {
         "min": 11000000000,
         "max": 60000000000
        }
       },
       "last_post_sort_date": "1789460733266302",
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "sort": "sort_date",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       },
       "page": 1
      },
      "sort_date": "2026-09-15T14:23:52.612875Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "۱۱۳متر۲خ فول/سالن بزرگ/دسترسی ویژه/هلال احمر نارمک",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gaKu5_tB",
      "web_info": {
       "title": "۱۱۳متر۲خ فول/سالن بزرگ/دسترسی ویژه/هلال احمر نارمک",
       "district_persian": "هفت حوض",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gaKu5_tB_N"
     }
    },
    "image_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/jH2gDF0kyZ2GAwcNL48EKw/3d8ed800-d16d-4cb4-98e4-c67b38cf96dd.webp",
    "bottom_description_text": "REDACTED در هفت حوض",
    "red_text": "نردبان شده",
    "middle_description_text": "۳۱,۸۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 18,
    "image_top_left_tag": {
     "text": "۱۸",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gaKu5_tB"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gaKu5_tB",
           "web_info": {
            "title": "۱۱۳متر۲خ فول/سالن بزرگ/دسترسی ویژه/هلال احمر نارمک",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gaKu5_tB",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gaKu5_tB_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gaKu5_tB",
      "index": 3,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "category": {
         "value": "apartment-sell"
        },
        "parking": true,
        "sort": {
         "value": "sort_date"
        },
        "rebuilt": true,
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "elevator": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "recent_ads": {
         "value": "1d"
        },
        "cities": [
         "1"
        ],
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "max": 140,
         "min": 40
        },
        "floor": {
         "min": -1,
         "max": 6
        }
       },
       "last_post_sort_date": "1789460733266302",
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "sort": "sort_date",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       },
       "page": 1
      },
      "sort_date": "2026-09-15T14:13:12.232121Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "۱۱۸ متر ۲ خواب ، نبش میدان",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gala1vuI",
      "web_info": {
       "title": "۱۱۸ متر ۲ خواب ، نبش میدان",
       "district_persian": "هفت حوض",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gala1vuI_N"
     }
    },
    "image_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/fLOj-vDf9CBcbpNySOzgxA/0c6fa2b2-1e71-483c-8553-7087c971b324.webp",
    "bottom_description_text": "REDACTED در هفت حوض",
    "red_text": "نردبان شده",
    "middle_description_text": "۴۱,۰۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 1,
    "image_top_left_tag": {
     "text": "۱",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gala1vuI"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gala1vuI",
           "web_info": {
            "title": "۱۱۸ متر ۲ خواب ، نبش میدان",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gala1vuI",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gala1vuI_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gala1vuI",
      "index": 4,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "recent_ads": {
         "value": "1d"
        },
        "cities": [
         "1"
        ],
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "max": 140,
         "min": 40
        },
        "floor": {
         "min": -1,
         "max": 6
        },
        "category": {
         "value": "apartment-sell"
        },
        "parking": true,
        "sort": {
         "value": "sort_date"
        },
        "rebuilt": true,
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "elevator": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        }
       },
       "last_post_sort_date": "1789460733266302",
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "sort": "sort_date",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       },
       "page": 1
      },
      "sort_date": "2026-09-15T14:09:56.688075Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "فروش اپارتمان تک خوابه ، ۶۵ متری ، ثقفی",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gagmw_S-",
      "web_info": {
       "title": "فروش اپارتمان تک خوابه ، ۶۵ متری ، ثقفی",
       "district_persian": "درختی",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gagmw_S-_N"
     }
    },
    "image_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/kFyk7Rb8CY2niwYHqdnsQQ/24c57749-586d-4709-914a-b4d7327c8a33.webp",
    "bottom_description_text": "REDACTED در درختی",
    "red_text": "نردبان شده",
    "middle_description_text": "۳۰,۵۵۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 9,
    "image_top_left_tag": {
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/videocam.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/videocam.png",
      "icon_name": "VIDEOCAM",
      "icon_color": "WHITE_PRIMARY"
     }
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gagmw_S-"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gagmw_S-",
           "web_info": {
            "title": "فروش اپارتمان تک خوابه ، ۶۵ متری ، ثقفی",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gagmw_S-",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gagmw_S-_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gagmw_S-",
      "index": 5,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "min": 40,
         "max": 140
        },
        "floor": {
         "min": -1,
         "max": 6
        },
        "category": {
         "value": "apartment-sell"
        },
        "parking": true,
        "sort": {
         "value": "sort_date"
        },
        "rebuilt": true,
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "elevator": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "recent_ads": {
         "value": "1d"
        },
        "cities": [
         "1"
        ],
        "price": {
         "min": 11000000000,
         "max": 60000000000
        }
       },
       "last_post_sort_date": "1789460733266302",
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "sort": "sort_date",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       },
       "page": 1
      },
      "sort_date": "2026-09-15T13:45:36.312194Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "آپارتمان 48 متری  یک خوابه فول تک واحدی",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "galCSjaC",
      "web_info": {
       "title": "آپارتمان 48 متری  یک خوابه فول تک واحدی",
       "district_persian": "دردشت",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_galCSjaC_N"
     }
    },
    "image_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/WFMb4cR0sC2yNyOfzePd3w/2d2b513c-b247-4e0b-b30e-acb4101dee25.webp",
    "bottom_description_text": "REDACTED در دردشت",
    "red_text": "نردبان شده",
    "middle_description_text": "۱۲,۷۹۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 1,
    "image_top_left_tag": {
     "text": "۱",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "galCSjaC"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "galCSjaC",
           "web_info": {
            "title": "آپارتمان 48 متری  یک خوابه فول تک واحدی",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "galCSjaC",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_galCSjaC_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "galCSjaC",
      "index": 6,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "price_per_square": {
         "max": 900000000,
         "min": 256000000
        },
        "warehouse": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "recent_ads": {
         "value": "1d"
        },
        "cities": [
         "1"
        ],
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "max": 140,
         "min": 40
        },
        "floor": {
         "min": -1,
         "max": 6
        },
        "category": {
         "value": "apartment-sell"
        },
        "parking": true,
        "sort": {
         "value": "sort_date"
        },
        "rebuilt": true,
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "elevator": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        }
       },
       "last_post_sort_date": "1789460733266302",
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "sort": "sort_date",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       },
       "page": 1
      },
      "sort_date": "2026-09-15T09:18:16.012936Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "۸۳ متر ۲خواب شخصی ساز سال ساخت ۱۳۹۹ فروشنده تک برگ",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gapOQBF3",
      "web_info": {
       "title": "۸۳ متر ۲خواب شخصی ساز سال ساخت ۱۳۹۹ فروشنده تک برگ",
       "district_persian": "گلستان (شهرک راه آهن)",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapOQBF3_N"
     }
    },
    "image_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/mw0bYvoPH3j9mEZLStFduA/7267a354-e97c-47b0-a6c7-068bb24ee0e7.webp",
    "bottom_description_text": "REDACTED در گلستان (شهرک راه آهن)",
    "middle_description_text": "۲۵,۵۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 2,
    "image_top_left_tag": {
     "text": "۲",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gapOQBF3"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gapOQBF3",
           "web_info": {
            "title": "۸۳ متر ۲خواب شخصی ساز سال ساخت ۱۳۹۹ فروشنده تک برگ",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gapOQBF3",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapOQBF3_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gapOQBF3",
      "index": 7,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "recent_ads": {
         "value": "1d"
        },
        "cities": [
         "1"
        ],
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "min": 40,
         "max": 140
        },
        "floor": {
         "min": -1,
         "max": 6
        },
        "category": {
         "value": "apartment-sell"
        },
        "parking": true,
        "sort": {
         "value": "sort_date"
        },
        "rebuilt": true,
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "elevator": true
       },
       "last_post_sort_date": "1789460733266302",
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "sort": "sort_date",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       },
       "page": 1
      },
      "sort_date": "2026-09-15T08:34:26.721035Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "آپارتمان ۱۰۴متر بلوار اقاقیا سند تک برگ چیتگر",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gapGwthB",
      "web_info": {
       "title": "آپارتمان ۱۰۴متر بلوار اقاقیا سند تک برگ چیتگر",
       "district_persian": "گلستان (شهرک راه آهن)",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapGwthB_N"
     }
    },
    "image_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/m6xoLuxvwTcIOVDyfQJ-TA/df457caa-4361-413b-9202-d36a2fc9bc39.webp",
    "bottom_description_text": "REDACTED در گلستان (شهرک راه آهن)",
    "middle_description_text": "۲۸,۷۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 6,
    "image_top_left_tag": {
     "text": "۶",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gapGwthB"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gapGwthB",
           "web_info": {
            "title": "آپارتمان ۱۰۴متر بلوار اقاقیا سند تک برگ چیتگر",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gapGwthB",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gapGwthB_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gapGwthB",
      "index": 8,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "category": {
         "value": "apartment-sell"
        },
        "parking": true,
        "sort": {
         "value": "sort_date"
        },
        "rebuilt": true,
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "elevator": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "recent_ads": {
         "value": "1d"
        },
        "cities": [
         "1"
        ],
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "min": 40,
         "max": 140
        },
        "floor": {
         "min": -1,
         "max": 6
        }
       },
       "last_post_sort_date": "1789460733266302",
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "sort": "sort_date",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       },
       "page": 1
      },
      "sort_date": "2026-09-15T08:33:18.306226Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "۸۰ متر سند تک برگ",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gaYCIV74",
      "web_info": {
       "title": "۸۰ متر سند تک برگ",
       "district_persian": "گلستان (شهرک راه آهن)",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gaYCIV74_N"
     }
    },
    "image_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/eoT82rNCkQFhYshu-rQaPQ/7e6c55c2-7b9e-4817-8993-2de3f656cc0c.webp",
    "bottom_description_text": "REDACTED در گلستان (شهرک راه آهن)",
    "red_text": "نردبان شده",
    "middle_description_text": "۲۲,۰۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 3,
    "image_top_left_tag": {
     "text": "۳",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gaYCIV74"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gaYCIV74",
           "web_info": {
            "title": "۸۰ متر سند تک برگ",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gaYCIV74",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gaYCIV74_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gaYCIV74",
      "index": 9,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "category": {
         "value": "apartment-sell"
        },
        "parking": true,
        "sort": {
         "value": "sort_date"
        },
        "rebuilt": true,
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "elevator": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "recent_ads": {
         "value": "1d"
        },
        "cities": [
         "1"
        ],
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "max": 140,
         "min": 40
        },
        "floor": {
         "max": 6,
         "min": -1
        }
       },
       "last_post_sort_date": "1789460733266302",
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "sort": "sort_date",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       },
       "page": 1
      },
      "sort_date": "2026-09-15T07:45:20.089850Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "۱۲۰متر تکواحدی فول امکانات/تک برگ شهرک راه آهن",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gaoy-XDp",
      "web_info": {
       "title": "۱۲۰متر تکواحدی فول امکانات/تک برگ شهرک راه آهن",
       "district_persian": "گلستان (شهرک راه آهن)",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gaoy-XDp_N"
     }
    },
    "image_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/4ZgpyK_967CsM27ZxBfc6Q/ddf32f50-2968-4d03-b0d4-1457cd847838.webp",
    "bottom_description_text": "REDACTED در گلستان (شهرک راه آهن)",
    "middle_description_text": "۳۳,۰۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 2,
    "image_top_left_tag": {
     "text": "۲",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gaoy-XDp"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gaoy-XDp",
           "web_info": {
            "title": "۱۲۰متر تکواحدی فول امکانات/تک برگ شهرک راه آهن",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gaoy-XDp",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gaoy-XDp_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gaoy-XDp",
      "index": 10,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "rebuilt": true,
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "elevator": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "building-age": {
         "max": 15,
         "min": 0
        },
        "recent_ads": {
         "value": "1d"
        },
        "cities": [
         "1"
        ],
        "price": {
         "max": 60000000000,
         "min": 11000000000
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "max": 140,
         "min": 40
        },
        "floor": {
         "max": 6,
         "min": -1
        },
        "category": {
         "value": "apartment-sell"
        },
        "parking": true,
        "sort": {
         "value": "sort_date"
        }
       },
       "last_post_sort_date": "1789460733266302",
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "sort": "sort_date",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       },
       "page": 1
      },
      "sort_date": "2026-09-15T06:57:47.172788Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "۱۰۵ متر شمال کاج روبه افتاب ۸ سال ساخت",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gaZayYsS",
      "web_info": {
       "title": "۱۰۵ متر شمال کاج روبه افتاب ۸ سال ساخت",
       "district_persian": "سعادت\u200cآباد",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gaZayYsS_N"
     }
    },
    "image_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/ji9Pf3NpK_DY2z-Ac1wppg/e3fa3204-dd6d-4ed0-aae4-1d20d0ffa036.webp",
    "bottom_description_text": "REDACTED در سعادت\u200cآباد",
    "red_text": "نردبان شده",
    "middle_description_text": "۶۳,۰۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 1,
    "image_top_left_tag": {
     "text": "۱",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gaZayYsS"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gaZayYsS",
           "web_info": {
            "title": "۱۰۵ متر شمال کاج روبه افتاب ۸ سال ساخت",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gaZayYsS",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gaZayYsS_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gaZayYsS",
      "index": 11,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "elevator": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "price_per_square": {
         "min": 256000000,
         "max": 900000000
        },
        "warehouse": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "recent_ads": {
         "value": "1d"
        },
        "cities": [
         "1"
        ],
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "max": 140,
         "min": 40
        },
        "floor": {
         "min": -1,
         "max": 6
        },
        "category": {
         "value": "apartment-sell"
        },
        "parking": true,
        "sort": {
         "value": "sort_date"
        },
        "rebuilt": true
       },
       "last_post_sort_date": "1789460733266302",
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "sort": "sort_date",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       },
       "page": 1
      },
      "sort_date": "2026-09-15T06:11:36.764532Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "۴۸متر ۱خ فول امکانات ۹ساله/سوپر لاکچری/کرمان جنوبی",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gamaEAGF",
      "web_info": {
       "title": "۴۸متر ۱خ فول امکانات ۹ساله/سوپر لاکچری/کرمان جنوبی",
       "district_persian": "هفت حوض",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gamaEAGF_N"
     }
    },
    "image_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/XXpimQmGLmI9NJuRrSrlVQ/7343148d-432f-417f-b93a-f103e2d0072b.webp",
    "bottom_description_text": "REDACTED در هفت حوض",
    "middle_description_text": "۱۲,۵۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 12,
    "image_top_left_tag": {
     "text": "۱۲",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gamaEAGF"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gamaEAGF",
           "web_info": {
            "title": "۴۸متر ۱خ فول امکانات ۹ساله/سوپر لاکچری/کرمان جنوبی",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gamaEAGF",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gamaEAGF_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gamaEAGF",
      "index": 12,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "parking": true,
        "sort": {
         "value": "sort_date"
        },
        "rebuilt": true,
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "elevator": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "price_per_square": {
         "max": 900000000,
         "min": 256000000
        },
        "warehouse": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "recent_ads": {
         "value": "1d"
        },
        "cities": [
         "1"
        ],
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "max": 140,
         "min": 40
        },
        "floor": {
         "min": -1,
         "max": 6
        },
        "category": {
         "value": "apartment-sell"
        }
       },
       "last_post_sort_date": "1789460733266302",
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "sort": "sort_date",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       },
       "page": 1
      },
      "sort_date": "2026-09-15T05:17:19.998244Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  },
  {
   "widget_type": "POST_ROW",
   "data": {
    "@type": "type.googleapis.com/widgets.PostRowData",
    "title": "۱۲۰متر ۳خواب نوساز/ ۲واحدی/ ۲پارکینگ/ نورگیر جنوبی",
    "action": {
     "type": "VIEW_POST",
     "payload": {
      "@type": "type.googleapis.com/widgets.ViewPostPayload",
      "token": "gajKAphW",
      "web_info": {
       "title": "۱۲۰متر ۳خواب نوساز/ ۲واحدی/ ۲پارکینگ/ نورگیر جنوبی",
       "district_persian": "آسمان",
       "city_persian": "تهران"
      },
      "ad_instance_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gajKAphW_N"
     }
    },
    "image_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/wjB1Z82NV7udLJ1jS0yk2A/a4787a22-e6d3-4189-992b-194d9c3014e1.webp",
    "bottom_description_text": "REDACTED در آسمان",
    "red_text": "نردبان شده",
    "middle_description_text": "۶۳,۰۰۰,۰۰۰,۰۰۰ تومان",
    "has_divider": true,
    "image_count": 9,
    "image_top_left_tag": {
     "text": "۹",
     "icon": {
      "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/camera.png",
      "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/camera.png",
      "icon_name": "CAMERA",
      "icon_color": "WHITE_PRIMARY"
     },
     "is_icon_left": true
    },
    "long_press_action": {
     "type": "LOAD_MENU",
     "payload": {
      "@type": "type.googleapis.com/widgets.LoadMenuPayload",
      "menu": {
       "items": [
        {
         "text": "نشان کردن",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/bookmark_border.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/bookmark_border.png",
          "icon_name": "BOOKMARK_BORDER",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "MAKE_NETWORK_CALL",
          "payload": {
           "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
           "grpc_request_path": "/yaad_v2.YaadV2/SetBookmarkV2",
           "rest_request_path": "/yaad/bookmark-v2",
           "request_data": {
            "@type": "type.googleapis.com/yaad_v2.SetBookmarkV2Request.RequestData",
            "token": "gajKAphW"
           },
           "needs_auth": true
          }
         },
         "alignment": "RIGHT"
        },
        {
         "text": "باز کردن در صفحه جدید",
         "icon": {
          "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/add_circle_outline.png",
          "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/add_circle_outline.png",
          "icon_name": "ADD_CIRCLE_OUTLINE",
          "icon_color": "ICON_SECONDARY"
         },
         "action": {
          "type": "VIEW_POST",
          "payload": {
           "@type": "type.googleapis.com/widgets.ViewPostPayload",
           "token": "gajKAphW",
           "web_info": {
            "title": "۱۲۰متر ۳خواب نوساز/ ۲واحدی/ ۲پارکینگ/ نورگیر جنوبی",
            "open_new_tab": true
           }
          }
         },
         "alignment": "RIGHT"
        }
       ],
       "banner": {}
      },
      "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
     }
    },
    "token": "gajKAphW",
    "should_indicate_seen_status": true,
    "tracker_session_id": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8_gajKAphW_N",
    "layout_type": "GRID_ITEM"
   },
   "action_log": {
    "server_side_info": {
     "info": {
      "@type": "type.googleapis.com/action_log.PostItemInfo",
      "post_token": "gajKAphW",
      "index": 13,
      "post_type": "SEARCH",
      "list_type": "PAGE",
      "source_page": "POST_LIST_PAGE",
      "extra_data": {
       "@type": "type.googleapis.com/action_log.PostItemInfo.SearchExtraData",
       "jli": {
        "sort": {
         "value": "sort_date"
        },
        "rebuilt": true,
        "rooms": {
         "value": [
          "یک",
          "دو",
          "سه",
          "چهار"
         ]
        },
        "elevator": true,
        "districts": {
         "vacancies": [
          "198",
          "399",
          "654",
          "75",
          "907",
          "929"
         ]
        },
        "price_per_square": {
         "max": 900000000,
         "min": 256000000
        },
        "warehouse": true,
        "building-age": {
         "min": 0,
         "max": 15
        },
        "recent_ads": {
         "value": "1d"
        },
        "cities": [
         "1"
        ],
        "price": {
         "min": 11000000000,
         "max": 60000000000
        },
        "places": {
         "value": [
          "1"
         ]
        },
        "size": {
         "max": 140,
         "min": 40
        },
        "floor": {
         "min": -1,
         "max": 6
        },
        "category": {
         "value": "apartment-sell"
        },
        "parking": true
       },
       "last_post_sort_date": "1789460733266302",
       "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
       "search_data": {
        "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
        "sort": "sort_date",
        "cities": [
         "1"
        ],
        "query_input_type": "TEXT",
        "user_selected_location": {
         "@type": "type.googleapis.com/widgets.UserSelectedLocation",
         "places": [
          {
           "place_id": "1"
          }
         ]
        }
       },
       "page": 1
      },
      "sort_date": "2026-09-14T20:49:10.418023Z"
     },
     "item_type": {
      "type": "POST_ITEM"
     }
    },
    "enabled": true
   }
  }
 ],
 "action_log": {
  "server_side_info": {
   "info": {
    "@type": "type.googleapis.com/action_log.PostListLoadPageInfo",
    "cities": [
     "1"
    ],
    "current_tab": "default",
    "search_data": {
     "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"654\",\"75\",\"907\",\"929\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"11000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
     "sort": "sort_date",
     "cities": [
      "1"
     ],
     "query_input_type": "TEXT",
     "user_selected_location": {
      "@type": "type.googleapis.com/widgets.UserSelectedLocation",
      "places": [
       {
        "place_id": "1"
       }
      ]
     }
    },
    "tokens": [
     "gapOqAFe",
     "gap6V9xd",
     "gapKlv_g",
     "gaKu5_tB",
     "gala1vuI",
     "gagmw_S-",
     "galCSjaC",
     "gapOQBF3",
     "gapGwthB",
     "gaYCIV74",
     "gaoy-XDp",
     "gaZayYsS",
     "gamaEAGF",
     "gajKAphW"
    ],
    "page": 1,
    "pelle": {
     "elastic": {}
    },
    "last_post_date_epoch": "-62135596800000000",
    "search_id": "2e7fcf54c0dd6555f96559e5454afc49",
    "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
    "source_view": "MAP_DISCOVERY_MAP",
    "posts_metadata": [
     {
      "token": "gapOqAFe",
      "sort_date": "1789502608795195",
      "source": "f_relax",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":1418}"
     },
     {
      "token": "gap6V9xd",
      "sort_date": "1789484815745259",
      "source": "f_relax",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":19211}"
     },
     {
      "token": "gapKlv_g",
      "sort_date": "1789482232612875",
      "source": "f_relax",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":21794}"
     },
     {
      "token": "gaKu5_tB",
      "sort_date": "1789481592232121",
      "source": "f_relax",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":22434}"
     },
     {
      "token": "gala1vuI",
      "sort_date": "1789481396688075",
      "source": "f_relax",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":22630}"
     },
     {
      "token": "gagmw_S-",
      "sort_date": "1789479936312194",
      "source": "f_relax",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":24090}"
     },
     {
      "token": "galCSjaC",
      "sort_date": "1789463896012936",
      "source": "f_relax",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":40130}"
     },
     {
      "token": "gapOQBF3",
      "sort_date": "1789461266721035",
      "source": "f_relax",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":42760}"
     },
     {
      "token": "gapGwthB",
      "sort_date": "1789461198306226",
      "source": "f_relax",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":42828}"
     },
     {
      "token": "gaYCIV74",
      "sort_date": "1789458320089850",
      "source": "f_relax",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":45706}"
     },
     {
      "token": "gaoy-XDp",
      "sort_date": "1789455467172788",
      "source": "f_relax",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":48559}"
     },
     {
      "token": "gaZayYsS",
      "sort_date": "1789452696764532",
      "source": "f_relax",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":51330}"
     },
     {
      "token": "gamaEAGF",
      "sort_date": "1789449439998244",
      "source": "f_relax",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":54586}"
     },
     {
      "token": "gajKAphW",
      "sort_date": "1789418950418023",
      "source": "f_relax",
      "extra_info": "{\"category\":\"apartment-sell\",\"highlight\":null,\"matched_rules\":[],\"is_enriched_pipeline_consumed\":true,\"enriched_pipeline_name\":\"-\",\"freshness\":85076}"
     }
    ],
    "jli": {
     "recent_ads": {
      "value": "1d"
     },
     "cities": [
      "1"
     ],
     "price": {
      "min": 11000000000,
      "max": 60000000000
     },
     "places": {
      "value": [
       "1"
      ]
     },
     "size": {
      "max": 140,
      "min": 40
     },
     "floor": {
      "min": -1,
      "max": 6
     },
     "category": {
      "value": "apartment-sell"
     },
     "parking": true,
     "sort": {
      "value": "sort_date"
     },
     "rebuilt": true,
     "rooms": {
      "value": [
       "یک",
       "دو",
       "سه",
       "چهار"
      ]
     },
     "elevator": true,
     "districts": {
      "vacancies": [
       "198",
       "399",
       "654",
       "75",
       "907",
       "929"
      ]
     },
     "price_per_square": {
      "min": 256000000,
      "max": 900000000
     },
     "warehouse": true,
     "building-age": {
      "min": 0,
      "max": 15
     }
    },
    "search_layer": "fuzzy_filter",
    "widget_order": [
     {
      "type": "SEARCH_RESULT",
      "track_id": "gapOqAFe"
     },
     {
      "index": 1,
      "type": "SEARCH_RESULT",
      "track_id": "gap6V9xd"
     },
     {
      "index": 2,
      "type": "SEARCH_RESULT",
      "track_id": "gapKlv_g"
     },
     {
      "index": 3,
      "type": "SEARCH_RESULT",
      "track_id": "gaKu5_tB"
     },
     {
      "index": 4,
      "type": "SEARCH_RESULT",
      "track_id": "gala1vuI"
     },
     {
      "index": 5,
      "type": "SEARCH_RESULT",
      "track_id": "gagmw_S-"
     },
     {
      "index": 6,
      "type": "SEARCH_RESULT",
      "track_id": "galCSjaC"
     },
     {
      "index": 7,
      "type": "SEARCH_RESULT",
      "track_id": "gapOQBF3"
     },
     {
      "index": 8,
      "type": "SEARCH_RESULT",
      "track_id": "gapGwthB"
     },
     {
      "index": 9,
      "type": "SEARCH_RESULT",
      "track_id": "gaYCIV74"
     },
     {
      "index": 10,
      "type": "SEARCH_RESULT",
      "track_id": "gaoy-XDp"
     },
     {
      "index": 11,
      "type": "SEARCH_RESULT",
      "track_id": "gaZayYsS"
     },
     {
      "index": 12,
      "type": "SEARCH_RESULT",
      "track_id": "gamaEAGF"
     },
     {
      "index": 13,
      "type": "SEARCH_RESULT",
      "track_id": "gajKAphW"
     }
    ],
    "list_level_extra_info": "{}",
    "user_selected_location": {
     "@type": "type.googleapis.com/widgets.UserSelectedLocation",
     "places": [
      {
       "place_id": "1"
      }
     ]
    }
   },
   "item_type": {
    "type": "POST_LIST_LOAD_PAGE"
   }
  },
  "enabled": true
 },
 "search_bar": {},
 "pagination": {
  "data": {
   "@type": "type.googleapis.com/post_list.PaginationData",
   "last_post_date": "0001-01-01T00:00:00Z",
   "page": 2,
   "layer_page": 1,
   "layer_id": 36,
   "search_uid": "a1c8dea0-1fc1-472d-81b2-7da8d5ac0dc8",
   "cumulative_widgets_count": 22,
   "viewed_tokens": "H4sIAAAAAAAE/xTKy26DMBCF4ReaLKKmtyVx4yhyK0BGULpBpyodwNCaO7x9NLtP5/wMj6P+cMTwKnVJJrDJy2kUqMTZXpDV0bwR48+sro6I8Vt+X8pBLhVvw7sg7ANdCp7S1+1HYNqlYGKY+bGYzsRocVzmGzG4Wwt7kEXZBkriMD7rB8F1nSqJc3VLn0/E+N8Pn2+eGF/Y89ESo8MluGpiNCbwVXYPAAD//5xebh3FAAAA",
   "search_bookmark_info": {
    "search_hash": "5793aa1755524ef9cf5a79b74a4fe85f",
    "bookmark_state": {},
    "alert_state": {}
   },
   "first_page_viewed_at": "2026-09-15T20:27:06.543881332Z",
   "viewed_rows": [
    {
     "type": "VIEWED_ROW_SIMILAR_RESULTS_DIVIDER"
    }
   ],
   "filters_hash": "Ln/PVMDdZVX5ZVnlRUr8SQ=="
  }
 },
 "search_id": "2e7fcf54c0dd6555f96559e5454afc49",
 "show_no_search_result_notice": true
}
```

## post detail (posts-v2/web)

> منبع عملیاتی جزئیات آگهی — `GET /v8/posts-v2/web/{token}`. token نمونه: `gap5-Twe` (همان آگهی بخش `## fetch`).
> بدون کوکی؛ هدرهای sentry لازم نیست. تحلیل و نگاشت: [`divar-api.md`](divar-api.md) بخش ۷.۴ و ۱۲.

```js
fetch("https://api.divar.ir/v8/posts-v2/web/gap5-Twe", {
    "headers": {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "X-Web-Serving-Mode": "desktop"
    },
    "referrer": "https://divar.ir/",
    "method": "GET"
});
```
response:
```json
{
 "sections": [
  {
   "section_name": "BREADCRUMB",
   "widgets": [
    {
     "widget_type": "BREADCRUMB",
     "data": {
      "@type": "type.googleapis.com/widgets.BreadcrumbData",
      "parent_items": [
       {
        "title": "املاک",
        "action": {
         "type": "OPEN_POSTLIST_PAGE_GRPC",
         "payload": {
          "@type": "type.googleapis.com/widgets.OpenPostListPageGRPCPayload",
          "search_data": {
           "form_data": {
            "data": {
             "category": {
              "str": {
               "value": "real-estate"
              }
             }
            }
           }
          },
          "source_view": "CATEGORY_BREAD_CRUMB",
          "source_view_str": "CATEGORY_BREAD_CRUMB"
         }
        }
       },
       {
        "title": "فروش مسکونی",
        "action": {
         "type": "OPEN_POSTLIST_PAGE_GRPC",
         "payload": {
          "@type": "type.googleapis.com/widgets.OpenPostListPageGRPCPayload",
          "search_data": {
           "form_data": {
            "data": {
             "category": {
              "str": {
               "value": "residential-sell"
              }
             }
            }
           }
          },
          "source_view": "CATEGORY_BREAD_CRUMB",
          "source_view_str": "CATEGORY_BREAD_CRUMB"
         }
        }
       },
       {
        "title": "فروش آپارتمان",
        "action": {
         "type": "OPEN_POSTLIST_PAGE_GRPC",
         "payload": {
          "@type": "type.googleapis.com/widgets.OpenPostListPageGRPCPayload",
          "search_data": {
           "form_data": {
            "data": {
             "category": {
              "str": {
               "value": "apartment-sell"
              }
             }
            }
           }
          },
          "source_view": "CATEGORY_BREAD_CRUMB",
          "source_view_str": "CATEGORY_BREAD_CRUMB"
         }
        }
       }
      ],
      "current_page_title": "۹۷ متر ۲ خواب دونبش // دید ابدی",
      "padded": true
     }
    }
   ]
  },
  {
   "section_name": "TITLE",
   "widgets": [
    {
     "widget_type": "LEGEND_TITLE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.LegendTitleRowData",
      "title": "۹۷ متر ۲ خواب دونبش // دید ابدی",
      "high_level_heading": true,
      "padding": "NO_PADDING"
     }
    },
    {
     "widget_type": "EXPANDABLE_SECTION",
     "data": {
      "@type": "type.googleapis.com/widgets.ExpandableSectionData",
      "widget_list": [
       {
        "widget_type": "DESCRIPTION_ROW",
        "data": {
         "@type": "type.googleapis.com/widgets.DescriptionRowData",
         "text": "انتشار آگهی: ۷ مرداد ۱۴۰۵، ۱۵:۴۳\nآخرین نردبان: ۲۱ شهریور ۱۴۰۵، ۱۰:۲۷\nآخرین به‌روز‌رسانی: ۲۵ شهریور ۱۴۰۵، ۱۱:۰۷",
         "is_primary": true,
         "small": true,
         "text_alignment": "RIGHT"
        }
       }
      ],
      "title": "ماه پیش در تهران، یوسف‌آباد، خ سی و هشتم فضل‌الهی",
      "icon": {}
     }
    },
    {
     "widget_type": "SELECTOR_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.SelectorRowData",
      "title": "زنگ خطرهای قبل از معامله",
      "action": {
       "type": "OPEN_PAGE",
       "payload": {
        "@type": "type.googleapis.com/widgets.OpenPagePayload",
        "request_http_method": "POST",
        "request_data": {
         "@type": "type.googleapis.com/post_api_v2.GetFraudAlertPageRequest.Data",
         "category": "apartment-sell"
        },
        "specification": {
         "@type": "type.googleapis.com/widgets.OpenPagePayload.SimplePageSpecification",
         "navigation_button": "BACK"
        },
        "is_modal": true,
        "rest_request_path": "/v8/postview/fraud-alert",
        "grpc_request_path": "/post_api_v2.PostApi/GetFraudAlertPage"
       }
      },
      "has_divider": true,
      "icon": {
       "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/warning.png",
       "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/warning.png",
       "icon_name": "WARNING",
       "icon_color": "ICON_SECONDARY"
      },
      "has_arrow": true,
      "last_notification_date": "0001-01-01T00:00:00Z"
     },
     "action_log": {
      "server_side_info": {
       "info": {
        "@type": "type.googleapis.com/action_log.PostWarningInfo",
        "post_token": "gap5-Twe"
       },
       "item_type": {
        "type": "POST_WARNING"
       }
      },
      "enabled": true
     }
    }
   ]
  },
  {
   "section_name": "DESCRIPTION",
   "widgets": [
    {
     "widget_type": "TITLE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.TitleRowData",
      "text": "توضیحات",
      "text_color": "TEXT_PRIMARY",
      "text_type": "SECONDARY"
     }
    },
    {
     "widget_type": "DESCRIPTION_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.DescriptionRowData",
      "text": "بهترین واحد در منطقه رو از دست نده! \n\n⚜️ ۲ خواب، دونبش، غرق نور، با دید ابدی و بدون مشرف\n⚜️ نقشه عالی و سالن مربع شکل که هر جور بچینی قشنگه\n⚜️ خواب‌ها استاندارد و بزرگ هستن.\n⚜️ دو ساله، کلید نخورده و آماده تحویل!\n⚜️ ورودی از لابی شیک و سرایدار مقیم برای امنیت بیشتر.\n\nکارشناس فروش منطقه، REDACTED\n برای هماهنگی و بازدید، پیام بدین یا تماس بگیرین.",
      "is_primary": true,
      "text_alignment": "RIGHT"
     }
    }
   ]
  },
  {
   "section_name": "IMAGE",
   "widgets": [
    {
     "widget_type": "IMAGE_CAROUSEL",
     "data": {
      "@type": "type.googleapis.com/widgets.ImageCarouselData",
      "items": [
       {
        "image": {
         "url": "https://postimage01.divarcdn.com/static/photo/neda/webp_post/ctqDuy-S76vGZAxvffrTCg/43cff8b2-eb49-4012-8e90-3f565fc0ef29.webp",
         "alt": "۹۷ متر ۲ خواب دونبش // دید ابدی|فروش آپارتمان|تهران, یوسف‌آباد|دیوار",
         "thumbnail_url": "https://postimage01.divarcdn.com/static/photo/neda/webp_thumbnail/uuK5NfzXt4Aa6ExBzNNOUg/43cff8b2-eb49-4012-8e90-3f565fc0ef29.webp"
        }
       }
      ],
      "image_aspect_ratio": {
       "dynamic_aspect_ratio": {
        "height": 3,
        "width": 4
       }
      },
      "has_preview": true,
      "show_tooltip": true,
      "tooltip_data": {
       "icon": {
        "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/fullscreen.png",
        "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/fullscreen.png",
        "icon_name": "FULLSCREEN",
        "icon_color": "WHITE_PRIMARY"
       },
       "text": "عکس‌ها: تزئینی"
      }
     }
    }
   ]
  },
  {
   "section_name": "LIST_DATA",
   "widgets": [
    {
     "widget_type": "GROUP_INFO_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.GroupInfoRow",
      "items": [
       {
        "title": "متراژ",
        "value": "۹۷"
       },
       {
        "title": "ساخت",
        "value": "۱۴۰۳"
       },
       {
        "title": "اتاق",
        "value": "۲"
       }
      ],
      "has_divider": true
     }
    },
    {
     "widget_type": "UNEXPANDABLE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.UnexpandableRowData",
      "title": "تصویر‌ها برای همین ملک است؟",
      "value": "خیر",
      "has_divider": true
     }
    },
    {
     "widget_type": "UNEXPANDABLE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.UnexpandableRowData",
      "title": "قیمت کل",
      "value": "‏۴۸,۵۰۰,۰۰۰,۰۰۰ تومان",
      "has_divider": true
     }
    },
    {
     "widget_type": "UNEXPANDABLE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.UnexpandableRowData",
      "title": "قیمت هر متر",
      "value": "‏۵۰۰,۰۰۰,۰۰۰ تومان",
      "has_divider": true
     }
    },
    {
     "widget_type": "UNEXPANDABLE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.UnexpandableRowData",
      "title": "طبقه",
      "value": "۵",
      "has_divider": true
     }
    },
    {
     "widget_type": "SECTION_TITLE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.SectionTitleRowData",
      "title": "ویژگی‌ها و امکانات",
      "title_color": "TEXT_PRIMARY",
      "padding": "ALT"
     }
    },
    {
     "widget_type": "GROUP_FEATURE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.GroupFeatureRow",
      "items": [
       {
        "title": "آسانسور",
        "icon": {
         "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/elevator.png",
         "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/elevator.png",
         "icon_name": "ELEVATOR",
         "icon_color": "ICON_SECONDARY"
        },
        "available": true
       },
       {
        "title": "پارکینگ",
        "icon": {
         "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/parking.png",
         "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/parking.png",
         "icon_name": "PARKING",
         "icon_color": "ICON_SECONDARY"
        },
        "available": true
       },
       {
        "title": "انباری",
        "icon": {
         "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/cabinet.png",
         "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/cabinet.png",
         "icon_name": "CABINET",
         "icon_color": "ICON_SECONDARY"
        },
        "available": true
       }
      ],
      "has_divider": true
     }
    },
    {
     "widget_type": "SELECTOR_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.SelectorRowData",
      "title": "سایر ویژگی‌ها و امکانات",
      "action": {
       "type": "LOAD_MODAL_PAGE",
       "payload": {
        "@type": "type.googleapis.com/widgets.LoadModalPagePayload",
        "modal_page": {
         "title": "ویژگی‌ها و امکانات",
         "widget_list": [
          {
           "widget_type": "TITLE_ROW",
           "data": {
            "@type": "type.googleapis.com/widgets.TitleRowData",
            "text": "امکانات",
            "has_divider": true,
            "text_color": "TEXT_PRIMARY"
           }
          },
          {
           "widget_type": "FEATURE_ROW",
           "data": {
            "@type": "type.googleapis.com/widgets.FeatureRowData",
            "title": "آسانسور",
            "has_divider": true,
            "icon": {
             "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/elevator.png",
             "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/elevator.png",
             "icon_name": "ELEVATOR",
             "icon_color": "ICON_SECONDARY"
            }
           }
          },
          {
           "widget_type": "FEATURE_ROW",
           "data": {
            "@type": "type.googleapis.com/widgets.FeatureRowData",
            "title": "پارکینگ",
            "has_divider": true,
            "icon": {
             "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/parking.png",
             "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/parking.png",
             "icon_name": "PARKING",
             "icon_color": "ICON_SECONDARY"
            }
           }
          },
          {
           "widget_type": "FEATURE_ROW",
           "data": {
            "@type": "type.googleapis.com/widgets.FeatureRowData",
            "title": "انباری",
            "icon": {
             "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/cabinet.png",
             "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/cabinet.png",
             "icon_name": "CABINET",
             "icon_color": "ICON_SECONDARY"
            }
           }
          }
         ]
        }
       }
      },
      "has_divider": true,
      "icon": {},
      "has_arrow": true,
      "last_notification_date": "0001-01-01T00:00:00Z",
      "fullwidth": true
     },
     "action_log": {
      "server_side_info": {
       "info": {
        "@type": "type.googleapis.com/action_log.ViewPostFeaturesInfo",
        "post_token": "gap5-Twe"
       },
       "item_type": {
        "type": "VIEW_POST_FEATURES"
       }
      },
      "enabled": true
     }
    },
    {
     "widget_type": "SELECTOR_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.SelectorRowData",
      "title": "بررسی و کارشناسی",
      "action": {
       "type": "OPEN_PAGE",
       "payload": {
        "@type": "type.googleapis.com/widgets.OpenPagePayload",
        "request_http_method": "POST",
        "request_data": {
         "@type": "type.googleapis.com/service_providers.GetServiceProvidersPageRequest.RequestData",
         "source_v2": "DEMAND_POST",
         "filter": {
          "service_types": [
           "REPORT_INSPECTION"
          ],
          "city_id": 1,
          "category": "apartment-sell",
          "post_token": "gap5-Twe",
          "touchpoint": "DEMAND_POST"
         },
         "action_data_builder": {
          "conversation_id": "gap5-Twe",
          "post_token": "gap5-Twe",
          "touchpoint": "DEMAND_POST",
          "source": "DEMAND_POST",
          "lead_source": "DEMAND"
         },
         "display_data": {
          "page_title": "بررسی و کارشناسی"
         },
         "trace_id": "cf05eb41-da02-4d49-a89a-9fbe589bf4de",
         "source": "DEMAND_POST",
         "lead_source": "DEMAND"
        },
        "specification": {
         "@type": "type.googleapis.com/widgets.OpenPagePayload.SimplePageSpecification"
        },
        "is_modal": true,
        "rest_request_path": "/v8/open-platform/service-providers",
        "grpc_request_path": "/service_providers.ServiceProviders/GetServiceProvidersPage"
       }
      },
      "has_divider": true,
      "icon": {
       "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/article-magnifier.png",
       "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/article-magnifier.png",
       "icon_name": "ARTICLE_MAGNIFIER",
       "icon_color": "ICON_SECONDARY"
      },
      "has_arrow": true,
      "last_notification_date": "0001-01-01T00:00:00Z"
     }
    }
   ]
  },
  {
   "section_name": "TAGS",
   "widgets": [
    {
     "widget_type": "WRAPPER_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.WrapperRowData",
      "chip_list": {
       "chips": [
        {
         "text": "فروش آپارتمان",
         "type": "ACTION",
         "action": {
          "type": "OPEN_POSTLIST_PAGE_GRPC",
          "payload": {
           "@type": "type.googleapis.com/widgets.OpenPostListPageGRPCPayload",
           "search_data": {
            "form_data": {
             "data": {
              "category": {
               "str": {
                "value": "apartment-sell"
               }
              }
             }
            }
           },
           "source_view": "CATEGORY_BREAD_CRUMB",
           "source_view_str": "CATEGORY_BREAD_CRUMB"
          }
         }
        },
        {
         "text": "فروش آپارتمان در یوسف‌آباد",
         "type": "ACTION",
         "action": {
          "type": "OPEN_POSTLIST_PAGE_GRPC",
          "payload": {
           "@type": "type.googleapis.com/widgets.OpenPostListPageGRPCPayload",
           "search_data": {
            "form_data": {
             "data": {
              "category": {
               "str": {
                "value": "apartment-sell"
               }
              },
              "districts": {
               "repeated_string": {
                "value": [
                 "90"
                ]
               }
              }
             }
            }
           },
           "source_view": "CATEGORY_BREAD_CRUMB",
           "source_view_str": "CATEGORY_BREAD_CRUMB"
          }
         }
        }
       ]
      }
     }
    }
   ]
  },
  {
   "section_name": "MAP",
   "widgets": [
    {
     "widget_type": "MAP_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.MapRowData",
      "location": {
       "type": "FUZZY",
       "fuzzy_data": {
        "point": {
         "latitude": 35.734610425177365,
         "longitude": 51.40530956635603
        },
        "radius": 500
       }
      },
      "image_url": "https://mapimage.divarcdn.com/v8/mapimage?encrypted_data=MTIzNDU2Nzg5MTIzXL_Y8SdZyazuQp-XOg7PaPpL736MLc2ODD3PkY6uBOaYTw==&is_nearby=true"
     },
     "action_log": {
      "server_side_info": {
       "info": {
        "@type": "type.googleapis.com/action_log.MapInfo",
        "post_token": "gap5-Twe"
       },
       "item_type": {
        "type": "MAP"
       }
      },
      "enabled": true
     }
    }
   ]
  },
  {
   "section_name": "NOTE",
   "widgets": [
    {
     "widget_type": "NOTE",
     "data": {
      "@type": "type.googleapis.com/widgets.NoteData",
      "title": "یادداشت من",
      "button_title": "ویرایش یادداشت",
      "post_token": "gap5-Twe",
      "icon_button": {
       "icon": {
        "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/more_vert.png",
        "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/more_vert.png",
        "icon_name": "MORE_VERT",
        "icon_color": "ICON_SECONDARY"
       },
       "action": {
        "type": "LOAD_MENU",
        "payload": {
         "@type": "type.googleapis.com/widgets.LoadMenuPayload",
         "menu": {
          "items": [
           {
            "text": "ویرایش یادداشت",
            "icon": {
             "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/edit.png",
             "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/edit.png",
             "icon_name": "EDIT",
             "icon_color": "ICON_SECONDARY"
            },
            "action": {
             "type": "NOTE",
             "payload": {
              "@type": "type.googleapis.com/widgets.NotePayload",
              "post_token": "gap5-Twe",
              "max_character_count": 256
             }
            },
            "alignment": "RIGHT"
           },
           {
            "text": "حذف یادداشت",
            "icon": {
             "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_primary/v1/trash_o.png",
             "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_primary/v1/trash_o.png",
             "icon_name": "TRASH_O",
             "icon_color": "ICON_PRIMARY"
            },
            "action": {
             "type": "MAKE_NETWORK_CALL",
             "payload": {
              "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
              "grpc_request_path": "/yaad_v2.YaadV2/DeleteNoteV2",
              "rest_request_path": "/yaad/delete-note-v2",
              "request_data": {
               "@type": "type.googleapis.com/yaad_v2.DeleteNoteV2Request.RequestData",
               "token": "gap5-Twe"
              },
              "needs_auth": true
             }
            },
            "alignment": "RIGHT",
            "state": "STATE_NEGATIVE"
           }
          ],
          "banner": {}
         },
         "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
        }
       }
      }
     }
    }
   ]
  },
  {
   "section_name": "STATIC",
   "widgets": [
    {
     "widget_type": "SELECTOR_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.SelectorRowData",
      "title": "گزارش آگهی",
      "action": {
       "type": "OPEN_FORM_PAGE",
       "payload": {
        "@type": "type.googleapis.com/widgets.OpenFormPagePayload",
        "grpc_servicer": "/post_quality.PostQualityFeedback/GetFeedbackForm",
        "request_data": {
         "@type": "type.googleapis.com/post_quality.GetFeedbackFormRequest.RequestData",
         "post_token": "gap5-Twe"
        },
        "rest_request_path": "/v8/post-quality/feedback-form"
       }
      },
      "has_divider": true,
      "icon": {
       "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/report.png",
       "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/report.png",
       "icon_name": "REPORT",
       "icon_color": "ICON_SECONDARY"
      },
      "last_notification_date": "0001-01-01T00:00:00Z"
     }
    }
   ]
  },
  {
   "section_name": "BUSINESS_SECTION",
   "widgets": [
    {
     "widget_type": "LAZY_SECTION",
     "data": {
      "@type": "type.googleapis.com/widgets.LazySectionData",
      "rest_request_path": "/v8/premium-user/post-page/business-data/gap5-Twe/lazy",
      "grpc_request_path": "/premium_panel.PremiumPanel/GetPostBusinessLazyWidgets",
      "request_data": {
       "@type": "type.googleapis.com/premium_panel.GetPostBusinessLazyWidgetsRequest.RequestData",
       "post_token": "gap5-Twe",
       "hashed_post_owner_user_id": "0a8e25f03c178e8349f4cd5fe9cec49673d2f2f4ab5679fe8bd75d5b11327fae",
       "post_business_type": "premium-panel"
      }
     }
    }
   ]
  }
 ],
 "share": {
  "title": "۹۷ متر ۲ خواب دونبش __ دید ابدی",
  "web_url": "https://divar.ir/v/gap5-Twe"
 },
 "seo": {
  "title": "فروش ۹۷ متر ۲ خواب دونبش __ دید ابدی در تهران - ۲۱ شهریور ۱۴۰۵",
  "description": "آگهی ۹۷ متر ۲ خواب دونبش __ دید ابدی در دیوار تهران",
  "android_package_name": "ir.divar",
  "android_app_url": "android-app://ir.divar/http/v/۹۷ متر ۲ خواب دونبش __ دید ابدی/gap5-Twe/",
  "web_info": {
   "title": "۹۷ متر ۲ خواب دونبش __ دید ابدی",
   "district_persian": "یوسف‌آباد",
   "city_persian": "تهران",
   "category_slug_persian": "فروش آپارتمان"
  },
  "unavailable_after": "2026-09-28T15:43:16.906208",
  "bread_crumb": [
   {
    "name": "فروش آپارتمان",
    "search_data": {
     "form_data": {
      "data": {
       "category": {
        "str": {
         "value": "apartment-sell"
        }
       },
       "districts": {
        "repeated_string": {
         "value": [
          "90"
         ]
        }
       }
      }
     }
    }
   },
   {
    "name": "فروش مسکونی",
    "search_data": {
     "form_data": {
      "data": {
       "category": {
        "str": {
         "value": "residential-sell"
        }
       },
       "districts": {
        "repeated_string": {
         "value": [
          "90"
         ]
        }
       }
      }
     }
    }
   },
   {
    "name": "املاک",
    "search_data": {
     "form_data": {
      "data": {
       "category": {
        "str": {
         "value": "real-estate"
        }
       },
       "districts": {
        "repeated_string": {
         "value": [
          "90"
         ]
        }
       }
      }
     }
    }
   },
   {
    "name": "یوسف‌آباد",
    "search_data": {
     "form_data": {
      "data": {
       "districts": {
        "repeated_string": {
         "value": [
          "90"
         ]
        }
       }
      }
     }
    }
   },
   {
    "name": "1",
    "search_data": {
     "form_data": {}
    }
   },
   {
    "name": "دیوار"
   }
  ],
  "post_seo_schema": {
   "@type": "Apartment",
   "description": "بهترین واحد در منطقه رو از دست نده! \n\n⚜️ ۲ خواب، دونبش، غرق نور، با دید ابدی و بدون مشرف\n⚜️ نقشه عالی و سالن مربع شکل که هر جور بچینی قشنگه\n⚜️ خواب‌ها استاندارد و بزرگ هستن.\n⚜️ دو ساله، کلید نخورده و آماده تحویل!\n⚜️ ورودی از لابی شیک و سرایدار مقیم برای امنیت بیشتر.\n\nکارشناس فروش منطقه، REDACTED\n برای هماهنگی و بازدید، پیام بدین یا تماس بگیرین.",
   "accommodationCategory": "فروش آپارتمان",
   "url": "https://divar.ir/v/۹۷-متر-۲-خواب-دونبش-دید-ابدی/gap5-Twe",
   "name": "۹۷ متر ۲ خواب دونبش // دید ابدی",
   "image": "https://postimage01.divarcdn.com/static/photo/neda/webp_post/ctqDuy-S76vGZAxvffrTCg/43cff8b2-eb49-4012-8e90-3f565fc0ef29.webp",
   "numberOfRooms": "دو",
   "geo": {
    "address": "تهران, یوسف‌آباد",
    "latitude": "35.73463475119",
    "longitude": "51.405345168845",
    "@type": "GeoCoordinates"
   },
   "@context": "https://schema.org",
   "web_info": {
    "title": "۹۷ متر ۲ خواب دونبش // دید ابدی",
    "city_persian": "تهران",
    "district_persian": "یوسف‌آباد",
    "category_slug_persian": "فروش آپارتمان"
   },
   "floorSize": {
    "value": "97",
    "unitCode": "MTK",
    "@type": "QuantitativeValue"
   }
  },
  "image_url": "https://postimage01.divarcdn.com/static/photo/neda/post/xutSkDxwRixlf2on5wYEKA/43cff8b2-eb49-4012-8e90-3f565fc0ef29.jpg"
 },
 "contact": {
  "action_log": {
   "server_side_info": {
    "info": {
     "@type": "type.googleapis.com/action_log.ContactInfoInfo",
     "post_token": "gap5-Twe",
     "method_name": "GetContactWeb",
     "contact_uuid": "38e38c45-0818-43de-911f-aa5e2b711937"
    },
    "item_type": {
     "type": "CONTACT_INFO"
    }
   },
   "enabled": true
  },
  "contact_uuid": "38e38c45-0818-43de-911f-aa5e2b711937"
 },
 "webengage": {
  "token": "gap5-Twe",
  "district": "yousef-abad",
  "brand_model": "",
  "gender": "",
  "category": "apartment-sell",
  "price": 48499998720,
  "cat_3": "apartment-sell",
  "cat_1": "real-estate",
  "business_type": "premium-panel",
  "business_ref": "MXYdIQan_ciZIrYqZ",
  "cat_2": "residential-sell",
  "originality": "",
  "image_count": 1,
  "city": "tehran",
  "status": "",
  "rent": 0,
  "credit": 0,
  "source_view": ""
 },
 "analytics": {
  "cat1": "real-estate",
  "cat2": "residential-sell",
  "cat3": "apartment-sell",
  "city": "tehran"
 },
 "city": {
  "city_id": "1",
  "name": "تهران",
  "parent_id": "904",
  "second_slug": "tehran"
 }
}
```

### gammaxvi — فاقد آسانسور و پارکینگ (نمونهٔ امکانات منفی)

> همان endpoint با token دوم — کالبدسازی قاعدهٔ امکاناتِ غایب (`divar-api.md` بخش ۸.۷): آیتم منفی به شکل عنوان «… ندارد» بدون کلید `available` و با `icon_color: ICON_HINT`.
> نکات دیگر نمونه: سه تاریخ «انتشار / آخرین نردبان / آخرین به‌روزرسانی» در بخش TITLE (فیلدهای `published_at`/`last_bumped_at`/`last_updated_at` — بخش ۷.۴)؛ بذر نگاشت «هروی = 1024» در breadcrumb (بخش ۱۲.۵)؛ آشتی قیمت با اختلاف ۶۶هزار تومانی (بخش ۸.۶).
> Captured: 2026-09-17، بدون کوکی. مقادیر per-request (مثل `contact_uuid` و `trace_id`) در هر فراخوانی فرق می‌کنند.

```js
fetch("https://api.divar.ir/v8/posts-v2/web/gammaxvi", {
    "headers": {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:144.0) Gecko/20100101 Firefox/144.0",
        "X-Web-Serving-Mode": "desktop"
    },
    "referrer": "https://divar.ir/",
    "method": "GET"
});
```
response:
```json
{
 "sections": [
  {
   "section_name": "BREADCRUMB",
   "widgets": [
    {
     "widget_type": "BREADCRUMB",
     "data": {
      "@type": "type.googleapis.com/widgets.BreadcrumbData",
      "parent_items": [
       {
        "title": "املاک",
        "action": {
         "type": "OPEN_POSTLIST_PAGE_GRPC",
         "payload": {
          "@type": "type.googleapis.com/widgets.OpenPostListPageGRPCPayload",
          "search_data": {
           "form_data": {
            "data": {
             "category": {
              "str": {
               "value": "real-estate"
              }
             }
            }
           }
          },
          "source_view": "CATEGORY_BREAD_CRUMB",
          "source_view_str": "CATEGORY_BREAD_CRUMB"
         }
        }
       },
       {
        "title": "فروش مسکونی",
        "action": {
         "type": "OPEN_POSTLIST_PAGE_GRPC",
         "payload": {
          "@type": "type.googleapis.com/widgets.OpenPostListPageGRPCPayload",
          "search_data": {
           "form_data": {
            "data": {
             "category": {
              "str": {
               "value": "residential-sell"
              }
             }
            }
           }
          },
          "source_view": "CATEGORY_BREAD_CRUMB",
          "source_view_str": "CATEGORY_BREAD_CRUMB"
         }
        }
       },
       {
        "title": "فروش آپارتمان",
        "action": {
         "type": "OPEN_POSTLIST_PAGE_GRPC",
         "payload": {
          "@type": "type.googleapis.com/widgets.OpenPostListPageGRPCPayload",
          "search_data": {
           "form_data": {
            "data": {
             "category": {
              "str": {
               "value": "apartment-sell"
              }
             }
            }
           }
          },
          "source_view": "CATEGORY_BREAD_CRUMB",
          "source_view_str": "CATEGORY_BREAD_CRUMB"
         }
        }
       }
      ],
      "current_page_title": "هـروی / ۹۸ متـر / فاقد آسانسور و پارکینگ",
      "padded": true
     }
    }
   ]
  },
  {
   "section_name": "TITLE",
   "widgets": [
    {
     "widget_type": "LEGEND_TITLE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.LegendTitleRowData",
      "title": "هـروی / ۹۸ متـر / فاقد آسانسور و پارکینگ",
      "high_level_heading": true,
      "padding": "NO_PADDING"
     }
    },
    {
     "widget_type": "EXPANDABLE_SECTION",
     "data": {
      "@type": "type.googleapis.com/widgets.ExpandableSectionData",
      "widget_list": [
       {
        "widget_type": "DESCRIPTION_ROW",
        "data": {
         "@type": "type.googleapis.com/widgets.DescriptionRowData",
         "text": "انتشار آگهی: ۲۲ شهریور ۱۴۰۵، ۱۷:۱۹\nآخرین نردبان: ۲۴ شهریور ۱۴۰۵، ۰۶:۰۱\nآخرین به\u200cروز\u200cرسانی: ۲۴ شهریور ۱۴۰۵، ۰۶:۰۲",
         "is_primary": true,
         "small": true,
         "text_alignment": "RIGHT"
        }
       }
      ],
      "title": "۳ روز پیش در تهران، هروی",
      "icon": {}
     }
    },
    {
     "widget_type": "SELECTOR_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.SelectorRowData",
      "title": "زنگ خطرهای قبل از معامله",
      "action": {
       "type": "OPEN_PAGE",
       "payload": {
        "@type": "type.googleapis.com/widgets.OpenPagePayload",
        "request_http_method": "POST",
        "request_data": {
         "@type": "type.googleapis.com/post_api_v2.GetFraudAlertPageRequest.Data",
         "category": "apartment-sell"
        },
        "specification": {
         "@type": "type.googleapis.com/widgets.OpenPagePayload.SimplePageSpecification",
         "navigation_button": "BACK"
        },
        "is_modal": true,
        "rest_request_path": "/v8/postview/fraud-alert",
        "grpc_request_path": "/post_api_v2.PostApi/GetFraudAlertPage"
       }
      },
      "has_divider": true,
      "icon": {
       "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/warning.png",
       "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/warning.png",
       "icon_name": "WARNING",
       "icon_color": "ICON_SECONDARY"
      },
      "has_arrow": true,
      "last_notification_date": "0001-01-01T00:00:00Z"
     },
     "action_log": {
      "server_side_info": {
       "info": {
        "@type": "type.googleapis.com/action_log.PostWarningInfo",
        "post_token": "gammaxvi"
       },
       "item_type": {
        "type": "POST_WARNING"
       }
      },
      "enabled": true
     }
    }
   ]
  },
  {
   "section_name": "DESCRIPTION",
   "widgets": [
    {
     "widget_type": "TITLE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.TitleRowData",
      "text": "توضیحات",
      "text_color": "TEXT_PRIMARY",
      "text_type": "SECONDARY"
     }
    },
    {
     "widget_type": "DESCRIPTION_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.DescriptionRowData",
      "text": "◼️◼️◼️◼️امــلاڪ بــزرگـ\u200cـ مــاکان◼️◼️◼️◼️\n◼️◼️بزرگترین و حرفـه ای ترین در منطقـہ◼️◼️\n   ⚫⚫  به جستجـو پایــان بـده ⚫⚫\n\n⚫ ۹۸ متـر  / ۲ خواب \nتا برج ۴ سال ۱۴۰۶ مستاجر دارد ( مبلغ ۱.۳۰۰ پیش، ۶.۵۰۰ اجاره ) \n⚫ طبقه ۳.۵ ( فاقد آسانسور )\n⚫ به صورت تک واحدی\n⚫ فاقد پارکیـنگ\n⚫ تـراس \n⚫ سالن پرده خـور / رو به آفتاب \n⚫ واحد تمیز \n⚫ دسترسی عالی به مراکز خرید و اتوبانهای مجاور \n\n⚫ جهت اطلاعات بیشتر لطفا تماس حاصل فرمایید. \n\nکارشناس فروش؛ REDACTED",
      "is_primary": true,
      "text_alignment": "RIGHT"
     }
    }
   ]
  },
  {
   "section_name": "IMAGE",
   "widgets": [
    {
     "widget_type": "IMAGE_CAROUSEL",
     "data": {
      "@type": "type.googleapis.com/widgets.ImageCarouselData",
      "items": [
       {
        "image": {
         "url": "https://s100.divarcdn.com/static/photo/neda/webp_post/YvjIgO2QRK2JXCfZUmOe5A/08c25269-07bf-47d7-ac25-f3ecac63425f.webp",
         "alt": "هـروی / ۹۸ متـر / فاقد آسانسور و پارکینگ|فروش آپارتمان|تهران, هروی|دیوار",
         "thumbnail_url": "https://s100.divarcdn.com/static/photo/neda/webp_thumbnail/auM9fvkPskGFGKSRR7d9zA/08c25269-07bf-47d7-ac25-f3ecac63425f.webp"
        }
       }
      ],
      "image_aspect_ratio": {
       "dynamic_aspect_ratio": {
        "height": 3,
        "width": 4
       }
      },
      "has_preview": true,
      "show_tooltip": true,
      "tooltip_data": {
       "icon": {
        "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/white_primary/v1/fullscreen.png",
        "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/white_primary/v1/fullscreen.png",
        "icon_name": "FULLSCREEN",
        "icon_color": "WHITE_PRIMARY"
       },
       "text": "عکس\u200cها: تزئینی"
      }
     }
    }
   ]
  },
  {
   "section_name": "LIST_DATA",
   "widgets": [
    {
     "widget_type": "GROUP_INFO_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.GroupInfoRow",
      "items": [
       {
        "title": "متراژ",
        "value": "۹۸"
       },
       {
        "title": "ساخت",
        "value": "۱۳۸۴"
       },
       {
        "title": "اتاق",
        "value": "۲"
       }
      ],
      "has_divider": true
     }
    },
    {
     "widget_type": "UNEXPANDABLE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.UnexpandableRowData",
      "title": "تصویر\u200cها برای همین ملک است؟",
      "value": "خیر",
      "has_divider": true
     }
    },
    {
     "widget_type": "UNEXPANDABLE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.UnexpandableRowData",
      "title": "قیمت کل",
      "value": "\u200f۲۰,۵۰۰,۰۰۰,۰۰۰ تومان",
      "has_divider": true
     }
    },
    {
     "widget_type": "UNEXPANDABLE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.UnexpandableRowData",
      "title": "قیمت هر متر",
      "value": "\u200f۲۰۹,۱۸۳,۰۰۰ تومان",
      "has_divider": true
     }
    },
    {
     "widget_type": "UNEXPANDABLE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.UnexpandableRowData",
      "title": "طبقه",
      "value": "۳",
      "has_divider": true
     }
    },
    {
     "widget_type": "SECTION_TITLE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.SectionTitleRowData",
      "title": "ویژگی\u200cها و امکانات",
      "title_color": "TEXT_PRIMARY",
      "padding": "ALT"
     }
    },
    {
     "widget_type": "GROUP_FEATURE_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.GroupFeatureRow",
      "items": [
       {
        "title": "آسانسور ندارد",
        "icon": {
         "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_hint/v1/elevator.png",
         "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_hint/v1/elevator.png",
         "icon_name": "ELEVATOR",
         "icon_color": "ICON_HINT"
        }
       },
       {
        "title": "پارکینگ ندارد",
        "icon": {
         "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_hint/v1/parking.png",
         "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_hint/v1/parking.png",
         "icon_name": "PARKING",
         "icon_color": "ICON_HINT"
        }
       },
       {
        "title": "انباری",
        "icon": {
         "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/cabinet.png",
         "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/cabinet.png",
         "icon_name": "CABINET",
         "icon_color": "ICON_SECONDARY"
        },
        "available": true
       }
      ],
      "has_divider": true
     }
    },
    {
     "widget_type": "SELECTOR_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.SelectorRowData",
      "title": "سایر ویژگی\u200cها و امکانات",
      "action": {
       "type": "LOAD_MODAL_PAGE",
       "payload": {
        "@type": "type.googleapis.com/widgets.LoadModalPagePayload",
        "modal_page": {
         "title": "ویژگی\u200cها و امکانات",
         "widget_list": [
          {
           "widget_type": "TITLE_ROW",
           "data": {
            "@type": "type.googleapis.com/widgets.TitleRowData",
            "text": "ویژگی\u200cها",
            "has_divider": true,
            "text_color": "TEXT_PRIMARY"
           }
          },
          {
           "widget_type": "UNEXPANDABLE_ROW",
           "data": {
            "@type": "type.googleapis.com/widgets.UnexpandableRowData",
            "title": "تعداد واحد در طبقه",
            "value": "۱",
            "has_divider": true
           }
          },
          {
           "widget_type": "TITLE_ROW",
           "data": {
            "@type": "type.googleapis.com/widgets.TitleRowData",
            "text": "امکانات",
            "has_divider": true,
            "text_color": "TEXT_PRIMARY"
           }
          },
          {
           "widget_type": "FEATURE_ROW",
           "data": {
            "@type": "type.googleapis.com/widgets.FeatureRowData",
            "title": "آسانسور ندارد",
            "has_divider": true,
            "icon": {
             "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/elevator.png",
             "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/elevator.png",
             "icon_name": "ELEVATOR",
             "icon_color": "ICON_SECONDARY"
            }
           }
          },
          {
           "widget_type": "FEATURE_ROW",
           "data": {
            "@type": "type.googleapis.com/widgets.FeatureRowData",
            "title": "پارکینگ ندارد",
            "has_divider": true,
            "icon": {
             "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/parking.png",
             "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/parking.png",
             "icon_name": "PARKING",
             "icon_color": "ICON_SECONDARY"
            }
           }
          },
          {
           "widget_type": "FEATURE_ROW",
           "data": {
            "@type": "type.googleapis.com/widgets.FeatureRowData",
            "title": "انباری",
            "has_divider": true,
            "icon": {
             "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/cabinet.png",
             "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/cabinet.png",
             "icon_name": "CABINET",
             "icon_color": "ICON_SECONDARY"
            }
           }
          },
          {
           "widget_type": "FEATURE_ROW",
           "data": {
            "@type": "type.googleapis.com/widgets.FeatureRowData",
            "title": "بالکن دارد",
            "icon": {
             "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/balcony.png",
             "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/balcony.png",
             "icon_name": "BALCONY",
             "icon_color": "ICON_SECONDARY"
            }
           }
          }
         ]
        }
       }
      },
      "has_divider": true,
      "icon": {},
      "has_arrow": true,
      "last_notification_date": "0001-01-01T00:00:00Z",
      "fullwidth": true
     },
     "action_log": {
      "server_side_info": {
       "info": {
        "@type": "type.googleapis.com/action_log.ViewPostFeaturesInfo",
        "post_token": "gammaxvi"
       },
       "item_type": {
        "type": "VIEW_POST_FEATURES"
       }
      },
      "enabled": true
     }
    },
    {
     "widget_type": "SELECTOR_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.SelectorRowData",
      "title": "بررسی و کارشناسی",
      "action": {
       "type": "OPEN_PAGE",
       "payload": {
        "@type": "type.googleapis.com/widgets.OpenPagePayload",
        "request_http_method": "POST",
        "request_data": {
         "@type": "type.googleapis.com/service_providers.GetServiceProvidersPageRequest.RequestData",
         "source_v2": "DEMAND_POST",
         "filter": {
          "service_types": [
           "REPORT_INSPECTION"
          ],
          "city_id": 1,
          "category": "apartment-sell",
          "post_token": "gammaxvi",
          "touchpoint": "DEMAND_POST"
         },
         "action_data_builder": {
          "conversation_id": "gammaxvi",
          "post_token": "gammaxvi",
          "touchpoint": "DEMAND_POST",
          "source": "DEMAND_POST",
          "lead_source": "DEMAND"
         },
         "display_data": {
          "page_title": "بررسی و کارشناسی"
         },
         "trace_id": "f8e3e75b-fa5a-41aa-8160-85ffacb7f2b1",
         "source": "DEMAND_POST",
         "lead_source": "DEMAND"
        },
        "specification": {
         "@type": "type.googleapis.com/widgets.OpenPagePayload.SimplePageSpecification"
        },
        "is_modal": true,
        "rest_request_path": "/v8/open-platform/service-providers",
        "grpc_request_path": "/service_providers.ServiceProviders/GetServiceProvidersPage"
       }
      },
      "has_divider": true,
      "icon": {
       "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/article-magnifier.png",
       "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/article-magnifier.png",
       "icon_name": "ARTICLE_MAGNIFIER",
       "icon_color": "ICON_SECONDARY"
      },
      "has_arrow": true,
      "last_notification_date": "0001-01-01T00:00:00Z"
     }
    }
   ]
  },
  {
   "section_name": "TAGS",
   "widgets": [
    {
     "widget_type": "WRAPPER_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.WrapperRowData",
      "chip_list": {
       "chips": [
        {
         "text": "فروش آپارتمان",
         "type": "ACTION",
         "action": {
          "type": "OPEN_POSTLIST_PAGE_GRPC",
          "payload": {
           "@type": "type.googleapis.com/widgets.OpenPostListPageGRPCPayload",
           "search_data": {
            "form_data": {
             "data": {
              "category": {
               "str": {
                "value": "apartment-sell"
               }
              }
             }
            }
           },
           "source_view": "CATEGORY_BREAD_CRUMB",
           "source_view_str": "CATEGORY_BREAD_CRUMB"
          }
         }
        },
        {
         "text": "فروش آپارتمان در هروی",
         "type": "ACTION",
         "action": {
          "type": "OPEN_POSTLIST_PAGE_GRPC",
          "payload": {
           "@type": "type.googleapis.com/widgets.OpenPostListPageGRPCPayload",
           "search_data": {
            "form_data": {
             "data": {
              "category": {
               "str": {
                "value": "apartment-sell"
               }
              },
              "districts": {
               "repeated_string": {
                "value": [
                 "1024"
                ]
               }
              }
             }
            }
           },
           "source_view": "CATEGORY_BREAD_CRUMB",
           "source_view_str": "CATEGORY_BREAD_CRUMB"
          }
         }
        }
       ]
      }
     }
    }
   ]
  },
  {
   "section_name": "MAP",
   "widgets": [
    {
     "widget_type": "MAP_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.MapRowData",
      "location": {
       "type": "FUZZY",
       "fuzzy_data": {
        "point": {
         "latitude": 35.766802300280453,
         "longitude": 51.47618109689914
        },
        "radius": 500
       }
      },
      "image_url": "https://mapimage.divarcdn.com/v8/mapimage?encrypted_data=MTIzNDU2Nzg5MTIzXJ52-wJ49azuQuakp6HdZ_pLjQKhBZCMeTlb2qdty590fw==&is_nearby=true"
     },
     "action_log": {
      "server_side_info": {
       "info": {
        "@type": "type.googleapis.com/action_log.MapInfo",
        "post_token": "gammaxvi"
       },
       "item_type": {
        "type": "MAP"
       }
      },
      "enabled": true
     }
    }
   ]
  },
  {
   "section_name": "NOTE",
   "widgets": [
    {
     "widget_type": "NOTE",
     "data": {
      "@type": "type.googleapis.com/widgets.NoteData",
      "title": "یادداشت من",
      "button_title": "ویرایش یادداشت",
      "post_token": "gammaxvi",
      "icon_button": {
       "icon": {
        "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/more_vert.png",
        "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/more_vert.png",
        "icon_name": "MORE_VERT",
        "icon_color": "ICON_SECONDARY"
       },
       "action": {
        "type": "LOAD_MENU",
        "payload": {
         "@type": "type.googleapis.com/widgets.LoadMenuPayload",
         "menu": {
          "items": [
           {
            "text": "ویرایش یادداشت",
            "icon": {
             "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/edit.png",
             "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/edit.png",
             "icon_name": "EDIT",
             "icon_color": "ICON_SECONDARY"
            },
            "action": {
             "type": "NOTE",
             "payload": {
              "@type": "type.googleapis.com/widgets.NotePayload",
              "post_token": "gammaxvi",
              "max_character_count": 256
             }
            },
            "alignment": "RIGHT"
           },
           {
            "text": "حذف یادداشت",
            "icon": {
             "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_primary/v1/trash_o.png",
             "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_primary/v1/trash_o.png",
             "icon_name": "TRASH_O",
             "icon_color": "ICON_PRIMARY"
            },
            "action": {
             "type": "MAKE_NETWORK_CALL",
             "payload": {
              "@type": "type.googleapis.com/widgets.MakeNetworkCallPayload",
              "grpc_request_path": "/yaad_v2.YaadV2/DeleteNoteV2",
              "rest_request_path": "/yaad/delete-note-v2",
              "request_data": {
               "@type": "type.googleapis.com/yaad_v2.DeleteNoteV2Request.RequestData",
               "token": "gammaxvi"
              },
              "needs_auth": true
             }
            },
            "alignment": "RIGHT",
            "state": "STATE_NEGATIVE"
           }
          ],
          "banner": {}
         },
         "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
        }
       }
      }
     }
    }
   ]
  },
  {
   "section_name": "STATIC",
   "widgets": [
    {
     "widget_type": "SELECTOR_ROW",
     "data": {
      "@type": "type.googleapis.com/widgets.SelectorRowData",
      "title": "گزارش آگهی",
      "action": {
       "type": "OPEN_FORM_PAGE",
       "payload": {
        "@type": "type.googleapis.com/widgets.OpenFormPagePayload",
        "grpc_servicer": "/post_quality.PostQualityFeedback/GetFeedbackForm",
        "request_data": {
         "@type": "type.googleapis.com/post_quality.GetFeedbackFormRequest.RequestData",
         "post_token": "gammaxvi"
        },
        "rest_request_path": "/v8/post-quality/feedback-form"
       }
      },
      "has_divider": true,
      "icon": {
       "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/v1/report.png",
       "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/v1/report.png",
       "icon_name": "REPORT",
       "icon_color": "ICON_SECONDARY"
      },
      "last_notification_date": "0001-01-01T00:00:00Z"
     }
    }
   ]
  },
  {
   "section_name": "BUSINESS_SECTION",
   "widgets": [
    {
     "widget_type": "LAZY_SECTION",
     "data": {
      "@type": "type.googleapis.com/widgets.LazySectionData",
      "rest_request_path": "/v8/premium-user/post-page/business-data/gammaxvi/lazy",
      "grpc_request_path": "/premium_panel.PremiumPanel/GetPostBusinessLazyWidgets",
      "request_data": {
       "@type": "type.googleapis.com/premium_panel.GetPostBusinessLazyWidgetsRequest.RequestData",
       "post_token": "gammaxvi",
       "hashed_post_owner_user_id": "9bbf85358b8b865aca0b9e9a0494cfaeee6b66d3a214470cf144102f6f7f2d1f",
       "post_business_type": "premium-panel"
      }
     }
    }
   ]
  }
 ],
 "share": {
  "title": "هـروی _ ۹۸ متـر _ فاقد آسانسور و پارکینگ",
  "web_url": "https://divar.ir/v/gammaxvi"
 },
 "seo": {
  "title": "فروش هـروی _ ۹۸ متـر _ فاقد آسانسور و پارکینگ در تهران - ۲۴ شهریور ۱۴۰۵",
  "description": "آگهی هـروی _ ۹۸ متـر _ فاقد آسانسور و پارکینگ در دیوار تهران",
  "android_package_name": "ir.divar",
  "android_app_url": "android-app://ir.divar/http/v/هـروی _ ۹۸ متـر _ فاقد آسانسور و پارکینگ/gammaxvi/",
  "web_info": {
   "title": "هـروی _ ۹۸ متـر _ فاقد آسانسور و پارکینگ",
   "district_persian": "هروی",
   "city_persian": "تهران",
   "category_slug_persian": "فروش آپارتمان"
  },
  "unavailable_after": "2026-10-14T17:19:08.441706",
  "bread_crumb": [
   {
    "name": "فروش آپارتمان",
    "search_data": {
     "form_data": {
      "data": {
       "category": {
        "str": {
         "value": "apartment-sell"
        }
       },
       "districts": {
        "repeated_string": {
         "value": [
          "1024"
         ]
        }
       }
      }
     }
    }
   },
   {
    "name": "فروش مسکونی",
    "search_data": {
     "form_data": {
      "data": {
       "districts": {
        "repeated_string": {
         "value": [
          "1024"
         ]
        }
       },
       "category": {
        "str": {
         "value": "residential-sell"
        }
       }
      }
     }
    }
   },
   {
    "name": "املاک",
    "search_data": {
     "form_data": {
      "data": {
       "category": {
        "str": {
         "value": "real-estate"
        }
       },
       "districts": {
        "repeated_string": {
         "value": [
          "1024"
         ]
        }
       }
      }
     }
    }
   },
   {
    "name": "هروی",
    "search_data": {
     "form_data": {
      "data": {
       "districts": {
        "repeated_string": {
         "value": [
          "1024"
         ]
        }
       }
      }
     }
    }
   },
   {
    "name": "1",
    "search_data": {
     "form_data": {}
    }
   },
   {
    "name": "دیوار"
   }
  ],
  "post_seo_schema": {
   "@type": "Apartment",
   "web_info": {
    "district_persian": "هروی",
    "category_slug_persian": "فروش آپارتمان",
    "title": "هـروی / ۹۸ متـر / فاقد آسانسور و پارکینگ",
    "city_persian": "تهران"
   },
   "name": "هـروی / ۹۸ متـر / فاقد آسانسور و پارکینگ",
   "image": "https://s100.divarcdn.com/static/photo/neda/webp_post/YvjIgO2QRK2JXCfZUmOe5A/08c25269-07bf-47d7-ac25-f3ecac63425f.webp",
   "floorSize": {
    "value": "98",
    "unitCode": "MTK",
    "@type": "QuantitativeValue"
   },
   "geo": {
    "address": "تهران, هروی",
    "latitude": "35.767027356443",
    "longitude": "51.47634903593",
    "@type": "GeoCoordinates"
   },
   "@context": "https://schema.org",
   "url": "https://divar.ir/v/هـروی-۹۸-متـر-فاقد-آسانسور-و-پارکینگ/gammaxvi",
   "numberOfRooms": "دو",
   "description": "◼️◼️◼️◼️امــلاڪ بــزرگـ\u200cـ مــاکان◼️◼️◼️◼️\n◼️◼️بزرگترین و حرفـه ای ترین در منطقـہ◼️◼️\n   ⚫⚫  به جستجـو پایــان بـده ⚫⚫\n\n⚫ ۹۸ متـر  / ۲ خواب \nتا برج ۴ سال ۱۴۰۶ مستاجر دارد ( مبلغ ۱.۳۰۰ پیش، ۶.۵۰۰ اجاره ) \n⚫ طبقه ۳.۵ ( فاقد آسانسور )\n⚫ به صورت تک واحدی\n⚫ فاقد پارکیـنگ\n⚫ تـراس \n⚫ سالن پرده خـور / رو به آفتاب \n⚫ واحد تمیز \n⚫ دسترسی عالی به مراکز خرید و اتوبانهای مجاور \n\n⚫ جهت اطلاعات بیشتر لطفا تماس حاصل فرمایید. \n\nکارشناس فروش؛ REDACTED",
   "accommodationCategory": "فروش آپارتمان"
  },
  "image_url": "https://s100.divarcdn.com/static/photo/neda/post/n8VUg3hlfzipfclxRQNd9w/08c25269-07bf-47d7-ac25-f3ecac63425f.jpg"
 },
 "contact": {
  "chat_enabled": true,
  "action_log": {
   "server_side_info": {
    "info": {
     "@type": "type.googleapis.com/action_log.ContactInfoInfo",
     "post_token": "gammaxvi",
     "method_name": "GetContactWeb",
     "contact_uuid": "36431fdc-1b2a-45bd-b622-38a658951ad3"
    },
    "item_type": {
     "type": "CONTACT_INFO"
    }
   },
   "enabled": true
  },
  "contact_uuid": "36431fdc-1b2a-45bd-b622-38a658951ad3"
 },
 "webengage": {
  "city": "tehran",
  "business_type": "premium-panel",
  "image_count": 1,
  "business_ref": "CUVUyVYz_pQRgYEXa",
  "token": "gammaxvi",
  "source_view": "",
  "originality": "",
  "credit": 0,
  "gender": "",
  "cat_2": "residential-sell",
  "price": 20500000768,
  "category": "apartment-sell",
  "brand_model": "",
  "cat_3": "apartment-sell",
  "status": "",
  "district": "heravi",
  "rent": 0,
  "cat_1": "real-estate"
 },
 "analytics": {
  "cat1": "real-estate",
  "cat2": "residential-sell",
  "cat3": "apartment-sell",
  "city": "tehran"
 },
 "city": {
  "city_id": "1",
  "name": "تهران",
  "parent_id": "904",
  "second_slug": "tehran"
 }
}
```

## fetch

> صفحه HTML آگهی `gap5-Twe` (SSR با `__PRELOADED_STATE__`) — **fallback** اگر JSON `posts-v2/web` در دسترس نبود.
> منبع عملیاتی: بخش `## post detail (posts-v2/web)`. تحلیل: [`divar-api.md`](divar-api.md) بخش ۷.۴ و ۱۲.

https://divar.ir/v/%DB%B9%DB%B7-%D9%85%D8%AA%D8%B1-%DB%B2-%D8%AE%D9%88%D8%A7%D8%A8-%D8%AF%D9%88%D9%86%D8%A8%D8%B4-%D8%AF%DB%8C%D8%AF-%D8%A7%D8%A8%D8%AF%DB%8C/gap5-Twe
```html
<!doctype html>
<html lang="fa-IR" dir="rtl" data-theme="light" translate="no">
    <head>
        <meta charset="utf-8">
        <title data-react-helmet="true">فروش ۹۷ متر ۲ خواب دونبش __ دید ابدی در تهران - ۲۱ شهریور ۱۴۰۵</title>
        <meta data-react-helmet="true" name="viewport" content="width=992, initial-scale=1"/>
        <meta data-react-helmet="true" name="description" content="آگهی ۹۷ متر ۲ خواب دونبش __ دید ابدی در دیوار تهران"/>
        <meta data-react-helmet="true" name="twitter:card" content="summary"/>
        <meta data-react-helmet="true" name="twitter:site" content="@divar_official"/>
        <meta data-react-helmet="true" name="twitter:url" content="https://divar.ir/v/%DB%B9%DB%B7-%D9%85%D8%AA%D8%B1-%DB%B2-%D8%AE%D9%88%D8%A7%D8%A8-%D8%AF%D9%88%D9%86%D8%A8%D8%B4-%D8%AF%DB%8C%D8%AF-%D8%A7%D8%A8%D8%AF%DB%8C/gap5-Twe"/>
        <meta data-react-helmet="true" name="twitter:title" content="فروش ۹۷ متر ۲ خواب دونبش __ دید ابدی در تهران - ۲۱ شهریور ۱۴۰۵"/>
        <meta data-react-helmet="true" name="twitter:description" content="آگهی ۹۷ متر ۲ خواب دونبش __ دید ابدی در دیوار تهران"/>
        <meta data-react-helmet="true" name="twitter:image" content="https://s100.divarcdn.com/static/photo/neda/post/xutSkDxwRixlf2on5wYEKA/43cff8b2-eb49-4012-8e90-3f565fc0ef29.jpg"/>
        <meta data-react-helmet="true" name="twitter:creator" content="سایت دیوار"/>
        <meta data-react-helmet="true" property="og:site_name" content="سایت دیوار"/>
        <meta data-react-helmet="true" property="og:type" content="website"/>
        <meta data-react-helmet="true" property="og:url" content="https://divar.ir/v/%DB%B9%DB%B7-%D9%85%D8%AA%D8%B1-%DB%B2-%D8%AE%D9%88%D8%A7%D8%A8-%D8%AF%D9%88%D9%86%D8%A8%D8%B4-%D8%AF%DB%8C%D8%AF-%D8%A7%D8%A8%D8%AF%DB%8C/gap5-Twe"/>
        <meta data-react-helmet="true" property="og:title" content="فروش ۹۷ متر ۲ خواب دونبش __ دید ابدی در تهران - ۲۱ شهریور ۱۴۰۵"/>
        <meta data-react-helmet="true" property="og:description" content="آگهی ۹۷ متر ۲ خواب دونبش __ دید ابدی در دیوار تهران"/>
        <meta data-react-helmet="true" property="og:image" content="https://s100.divarcdn.com/static/photo/neda/post/xutSkDxwRixlf2on5wYEKA/43cff8b2-eb49-4012-8e90-3f565fc0ef29.jpg"/>
        <meta data-react-helmet="true" property="og:locale" content="fa_IR"/>
        <meta data-react-helmet="true" name="robots" content="INDEX,FOLLOW,unavailable_after: 2026-09-28T15:43:16.906208Z,max-image-preview:large"/>
        <meta name="traceparent" content="00-c3c7b26162d55e5ad9686af0126b8753-7a64b79d57a05ca0-00"/>
        <meta name="google" content="notranslate">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="format-detection" content="telephone=no"/>
        <meta name="referrer" content="strict-origin-when-cross-origin"/>
        <script>
            window.env = {
                "SERVING_MODE": "desktop",
                "IS_STAGING": false,
                "PORT": 8080,
                "DISABLE_AXIOS_CACHE_INTERCEPTOR": false,
                "FORCE_SSR_FOR_KNOWN_BOTS": true,
                "RELEASE_VERSION": "the-wall-v14-125-2",
                "ANDROID_PACKAGE_NAME": "io.thewall",
                "ANDROID_PACKAGE_NAME_IRAN": "ir.divar",
                "WEBENGAGE_ENABLE": false,
                "ENABLE_GOOGLE_TAG_MANAGER": true,
                "GOOGLE_TAG_MANAGER_ID": "GTM-NGGBSR3",
                "RESEND_AUTH_CODE_TIMEOUT": 30000,
                "LOCAL_SEARCH_HISTORY_VERSION": 1.1,
                "ENABLE_ENAMAD": true,
                "SHOW_IOS_APP_STORE_LINK": true,
                "IOS_APP_STORE_APP_LINK": "https://deewarmarket.com/download",
                "SHOW_GOOGLE_PLAY_LINK": false,
                "SHOW_APK_FILE_LINK": true,
                "APK_FILE_LINK": "https://divar.ir/downloads/android/release/release_260901010/Divar-release-11.14.20-w-260901010.apk",
                "APK_FILE_FALLBACK_LINK": "https://divar.ir/downloads/android/release/rollback_apk.apk",
                "APK_FILE_LEGACY_LINK": "https://divar.ir/downloads/android/release/release_260609010/Divar-release-11.14.14-260609010.apk",
                "APK_FILE_LEGACY_MAX_ANDROID_VERSION": 6,
                "GOOGLE_PLAY_APP_LINK": "https://play.google.com/store/apps/details?id=io.thewall&utm_campaign=new_app_google_play&utm_source=divar_download_page&utm_medium=web",
                "IS_CANARY": false,
                "BROWSE_LINK_PROCESSOR_DATA_URL": "https://s100.divarcdn.com/static/public/search/filters-config.json?version=1.0",
                "MULTICITY_DATA_URL": "https://map.divarcdn.com/places-web.json",
                "OPEN_TELEMETRY_SERVICE_NAME": "the-wall",
                "OPEN_TELEMETRY_ENDPOINT": "https://opentelemetry.divar.ir",
                "OPEN_TELEMETRY_SERVICE_NAMESPACE": "client",
                "ENABLE_A11Y_FEEDBACK": true,
                "CHECK_COOKIE_SERVER_COLLISION": false,
                "CAPTCHA_SITE_KEY": "fctd38ygaj",
                "IS_Clarity_ENABLED": true,
                "FORCE_RICH_WEB_VIEW_CSR": false,
                "IS_SENTRY_ENABLED": true,
                "TRACES_SAMPLE_RATE_FALLBACK": 0.01,
                "SENTRY_APPLICATION_KEY": "the-wall-sentry-key",
                "IS_CLIENT_IDS_ENABLED": true,
                "IS_RESUBMIT_ENABLED": true,
                "IS_SUBMIT_WEB_NEW_CATEGORY_SELECTION_ENABLED": true,
                "HAS_RECOVERABLE_ERROR_HANDLER": true,
                "CLIENT_EXPORTER_WIDGET_RENDER_SAMPLE_RATE": 0.1,
                "CLIENT_EXPORTER_ACTION_CLICK_SAMPLE_RATE": 0.1,
                "IS_LOGIN_RESTRICTION_MESSAGE_ENABLED": false,
                "IMAGE_UPLOAD_API_TIMEOUT": 600,
                "TOTAL_VALID_FAILED_REQUESTS_FOR_PRICING_CHECKLIST_PAGE": 5,
                "IS_SEARCH_ASSISTANT_QUERY_SUGGESTION_ENABLED": true,
                "IS_INSET_BANNER_LAZY_ENABLED": true,
                "IS_SEARCH_ASSISTANT_TAB_ENABLED": true,
                "IS_GOOGLE_REFERRER_ACTION_LOG_ENABLED": false,
                "IS_PAYMENT_RETRY_ENABLED": false,
                "IS_LIVE_SESSION_ENABLED": true,
                "IS_INJECT_META_TAGS_FOR_CSR_ENABLED": true,
                "CLIENT_EXPORTER_IMAGE_METRICS_SAMPLE_RATE": 0.1,
                "IS_POST_ROW_EVENT_BATCH_ENABLED": true,
                "IS_SUPERTOKENS_AUTH_ENABLED": true,
                "IS_CONTACT_ACTION_LOG_VALIDATION_ENABLED": true,
                "IS_PROACTIVE_REFRESH_TOKEN_ENABLED": true,
                "IS_CITY_MODAL_WITH_TABS_ENABLED": false,
                "IS_DYNAMIC_LOGIN_ENABLED": true,
                "IS_SERVICE_WORKER_CAPTURE_EXCEPTION": false,
                "IS_HTTP_CLIENT_CAPTURE_EXCEPTION": true,
                "IS_VISIBILITY_EVENT_SENDER_WRAPPER_ERROR_BOUNDARY_ENABLED": true,
                "IS_MY_DIVAR_MERGE_TABS_ENABLED": true,
                "NODE_ENV": "production",
                "PUBLIC_PATH": "https://s100.divarcdn.com/web-assets/2026/09/",
                "PREFIX_URL": "https://divar.ir",
                "DOMAIN_NAME": ".divar.ir",
                "AUTH_DOMAIN_NAME": ".divar.ir",
                "SENTRY_DSN": "https://7e7d19d51ebe4bd5955fda8ab50107b1@sentry.divar.cloud/5",
                "API_URL": "https://api.divar.ir/",
                "ACTION_LOG_API_URL": "https://actionlog.divar.ir/log",
                "API_TIMEOUT": 10,
                "SENTRY_ORG": "sentry",
                "SENTRY_PROJECT": "the-wall",
                "SENTRY_URL": "https://sentry.divar.cloud",
                "RENDER_MODE": "ssr"
            };
        </script>
        <script>
            "use strict";
            (function() {
                var a = {
                    UNKNOWN: "UNKNOWN",
                    MODERN: "MODERN",
                    LEGACY: "LEGACY",
                    HEADLESS: "HEADLESS"
                };
                var L = {
                    STATUS_UNSPECIFIED: "STATUS_UNSPECIFIED",
                    READY: "READY",
                    WATCHDOG_TIMEOUT: "WATCHDOG_TIMEOUT",
                    SETUP_ERROR: "SETUP_ERROR"
                }
                  , p = {
                    RESOURCE_TYPE_UNSPECIFIED: "RESOURCE_TYPE_UNSPECIFIED",
                    JAVASCRIPT: "JAVASCRIPT",
                    CSS: "CSS",
                    IMAGE: "IMAGE",
                    FONT: "FONT"
                }
                  , U = {
                    MODULE_TYPE_UNSPECIFIED: "MODULE_TYPE_UNSPECIFIED",
                    NOT_APPLICABLE: "NOT_APPLICABLE",
                    MODULE: "MODULE",
                    NO_MODULE: "NO_MODULE"
                }
                  , D = {
                    LOAD_STATUS_UNSPECIFIED: "LOAD_STATUS_UNSPECIFIED",
                    SUCCESS: "SUCCESS",
                    FAILED: "FAILED"
                };
                var _window = window
                  , M = _window.env
                  , J = M.NODE_ENV === "production";
                var j = M.IS_STAGING === !0;
                var f = "__ce0"
                  , W = "__ce1"
                  , b = "__ce2";
                function A() {
                    return typeof performance != "undefined" && typeof performance.now == "function" ? performance.now() : new Date().getTime();
                }
                function x() {
                    if (typeof Request != "function")
                        return !1;
                    try {
                        return new Request("https://d.ir",{
                            keepalive: !0
                        }).keepalive === !0;
                    } catch (O) {
                        return !1;
                    }
                }
                function B() {
                    var S;
                    if (typeof navigator == "undefined")
                        return !1;
                    var O = ((S = navigator.userAgent) == null ? void 0 : S.toLowerCase()) || "";
                    return O.indexOf("firefox") !== -1 || O.indexOf("fxios") !== -1;
                }
                function X() {
                    return (navigator && navigator.userAgent || "").indexOf("HeadlessChrome") !== -1 ? a.HEADLESS : navigator && navigator.webdriver === !0 ? a.HEADLESS : !("at" in Array.prototype) || !("hasOwn" in Object) ? a.LEGACY : a.MODERN;
                }
                function Y() {
                    return navigator && navigator.standalone === !0 ? !0 : typeof window.matchMedia == "function" ? window.matchMedia("(display-mode: standalone)").matches === !0 : !1;
                }
                function I(O) {
                    return {
                        view_id: O.viewId,
                        page: O.page,
                        app_name: "APP_THE_WALL",
                        is_pwa: Y(),
                        serving_mode: O.servingMode,
                        render_mode: O.renderMode,
                        browser_tier: X(),
                        app_version: O.release
                    };
                }
                function k(O, S, i) {
                    var _ = {
                        timestamp: "".concat(Date.now())
                    };
                    _[O] = S;
                    var R = {
                        reports: [{
                            user_event: _
                        }],
                        device: {
                            os: {
                                name: "web",
                                version: i.browserVersion
                            }
                        }
                    };
                    return JSON.stringify(R);
                }
                function V(O) {
                    var S, i = A();
                    g();
                    var _ = !1
                      , o = !1
                      , R = !1
                      , P = !1
                      , s = {};
                    function y(e) {
                        if (typeof navigator == "undefined" || typeof navigator.sendBeacon != "function")
                            return Promise.resolve(!1);
                        try {
                            var E = typeof Blob == "function" ? new Blob([e],{
                                type: "text/plain;charset=UTF-8"
                            }) : e;
                            return Promise.resolve(navigator.sendBeacon(O.gateway, E));
                        } catch (E) {
                            return Promise.resolve(!1);
                        }
                    }
                    function F(e, E) {
                        if (typeof fetch != "function" || E && !x())
                            return Promise.resolve(!1);
                        var T = typeof AbortController == "function" ? new AbortController : void 0, r;
                        try {
                            r = fetch(O.gateway, {
                                method: "POST",
                                body: e,
                                mode: "no-cors",
                                keepalive: !0,
                                credentials: "omit",
                                headers: {
                                    "Content-Type": "text/plain;charset=UTF-8"
                                },
                                signal: T == null ? void 0 : T.signal
                            });
                        } catch (t) {
                            return Promise.resolve(!1);
                        }
                        return Promise.race([r.then(function(t) {
                            return t.ok || t.type === "opaque"
                        }).catch(function() {
                            return !1
                        }), new Promise(function(t) {
                            setTimeout(function() {
                                t(!1),
                                T == null || T.abort();
                            }, 1e4);
                        }
                        )]);
                    }
                    function H(e) {
                        return typeof XMLHttpRequest != "function" ? Promise.resolve(!1) : new Promise(function(E) {
                            var T = !1
                              , r = function r(t) {
                                T || (T = !0,
                                E(t));
                            };
                            try {
                                var t = new XMLHttpRequest;
                                t.open("POST", O.gateway, !0),
                                t.setRequestHeader("Content-Type", "text/plain;charset=UTF-8"),
                                t.withCredentials = !1,
                                t.timeout = 1e4,
                                t.onload = function() {
                                    return r(!0)
                                }
                                ,
                                t.onerror = function() {
                                    return r(!0)
                                }
                                ,
                                t.ontimeout = function() {
                                    return r(!1)
                                }
                                ,
                                t.onabort = function() {
                                    return r(!1)
                                }
                                ,
                                t.send(e);
                            } catch (t) {
                                r(!1);
                            }
                        }
                        );
                    }
                    function u(e) {
                        if (typeof XMLHttpRequest != "function")
                            return !1;
                        try {
                            var E = new XMLHttpRequest;
                            return E.open("POST", O.gateway, !1),
                            E.setRequestHeader("Content-Type", "text/plain;charset=UTF-8"),
                            E.withCredentials = !1,
                            E.send(e),
                            !0;
                        } catch (E) {
                            return !1;
                        }
                    }
                    function N(e, E, T) {
                        var r;
                        try {
                            r = k(e, E, O);
                        } catch (n) {
                            return;
                        }
                        var t = B();
                        F(r, T).then(function(n) {
                            return n ? !0 : t && T ? u(r) : t ? H(r) : y(r)
                        }).then(function(n) {
                            n || T && !t && u(r);
                        });
                    }
                    function g() {
                        var e = {
                            context: I(O),
                            liveness: {}
                        };
                        N("web_page_load_event", e);
                    }
                    function C(e) {
                        if (R)
                            return;
                        var E = Object.keys(s);
                        if (E.length === 0)
                            return;
                        R = !0;
                        var T = [];
                        for (var t = 0; t < E.length; t++)
                            T.push(s[E[t]]);
                        var r = {
                            context: I(O),
                            resources: T
                        };
                        N("web_resources_event", r, e),
                        window.removeEventListener("pagehide", c),
                        document.removeEventListener("visibilitychange", l),
                        S == null || S.disconnect(),
                        S = void 0;
                    }
                    function d(e) {
                        if (_ || o)
                            return;
                        _ = !0,
                        C();
                        var E = {
                            context: I(O),
                            load_status: {
                                status: e,
                                elapsed: Math.round(A() - i)
                            }
                        };
                        N("web_page_load_event", E);
                    }
                    function m() {
                        if (!o) {
                            if (o = !0,
                            !_) {
                                var e = {
                                    context: I(O),
                                    load_status: {
                                        status: L.READY,
                                        elapsed: Math.round(A() - i)
                                    }
                                };
                                N("web_page_load_event", e);
                            }
                            C();
                        }
                    }
                    function K() {
                        if (!o || P)
                            return;
                        P = !0;
                        var e = {
                            context: I(O),
                            render_error: {}
                        };
                        N("web_page_load_event", e);
                    }
                    function v(e, E, T, r) {
                        if (R)
                            return;
                        var t = "".concat(e, "|").concat(E);
                        if (!Object.prototype.hasOwnProperty.call(s, t)) {
                            var n = {
                                name: e,
                                resource_type: p.JAVASCRIPT,
                                module_type: E,
                                status: T
                            };
                            T === D.SUCCESS && r !== void 0 && (n.duration = r),
                            s[t] = n;
                        }
                    }
                    function h(e) {
                        var E = e.getAttribute("data-name");
                        if (!E)
                            return;
                        var T;
                        if (e.type === "module")
                            T = U.MODULE;
                        else if (e.hasAttribute("nomodule"))
                            T = U.NO_MODULE;
                        else
                            return;
                        var r = A();
                        e.addEventListener("load", function() {
                            v(E, T, D.SUCCESS, Math.round(A() - r));
                        }),
                        e.addEventListener("error", function() {
                            v(E, T, D.FAILED);
                        });
                    }
                    function w(e) {
                        if (!e || e.nodeType !== 1)
                            return;
                        var E = e;
                        E.tagName === "SCRIPT" && E.hasAttribute("data-chunk") && h(E);
                    }
                    function c() {
                        C(!0);
                    }
                    function l() {
                        document.visibilityState === "hidden" && C(!0);
                    }
                    typeof MutationObserver == "function" && (S = new MutationObserver(function(e) {
                        for (var E = 0; E < e.length; E++) {
                            var T = e[E].addedNodes;
                            for (var r = 0; r < T.length; r++)
                                w(T[r]);
                        }
                    }
                    ),
                    S.observe(document.documentElement, {
                        childList: !0,
                        subtree: !0
                    })),
                    setTimeout(function() {
                        o || d(L.WATCHDOG_TIMEOUT);
                    }, O.timeoutMs),
                    window.addEventListener("pagehide", c),
                    document.addEventListener("visibilitychange", l),
                    window[f] = m,
                    window[W] = d,
                    window[b] = K;
                }
                window.probe = V;
                var te = V;
            }
            )();
            probe({
                "viewId": "f53a8f1f-ddac-4f91-9f5e-9343f0ecfd5f",
                "release": "the-wall-v14-125-2",
                "gateway": "https://api.divar.ir/v1/client-exporter/send-report",
                "servingMode": "desktop",
                "renderMode": "ssr",
                "page": "POST_DETAIL",
                "timeoutMs": 15000,
                "browserVersion": "153"
            });
        </script>
        <link rel="preconnect" href="https://s100.divarcdn.com"/>
        <link rel="dns-prefetch" href="https://s100.divarcdn.com">
        <link rel="preload" as="fetch" crossorigin="anonymous" href="https://s100.divarcdn.com/static/public/search/filters-config.json?version=1.0">
        <link rel="preload" as="fetch" crossorigin="anonymous" href="https://map.divarcdn.com/places-web.json">
        <link data-chunk="main" rel="modulepreload" as="script" href="https://s100.divarcdn.com/web-assets/2026/09/runtime.88fc8528.desktop.js">
        <link data-chunk="main" rel="modulepreload" as="script" href="https://s100.divarcdn.com/web-assets/2026/09/polyfills.b041981d.desktop.js">
        <link data-chunk="main" rel="modulepreload" as="script" href="https://s100.divarcdn.com/web-assets/2026/09/vendors-pb.37583302.desktop.js">
        <link data-chunk="main" rel="modulepreload" as="script" href="https://s100.divarcdn.com/web-assets/2026/09/main.a472176b.desktop.js">
        <link data-chunk="bootstrap" rel="modulepreload" as="script" href="https://s100.divarcdn.com/web-assets/2026/09/widget-base-183.c90455ee.desktop.js">
        <link data-chunk="bootstrap" rel="modulepreload" as="script" href="https://s100.divarcdn.com/web-assets/2026/09/framework-pb-535.37f1a3ba.desktop.js">
        <link data-chunk="bootstrap" rel="modulepreload" as="script" href="https://s100.divarcdn.com/web-assets/2026/09/khesht-326.894ba0c9.desktop.js">
        <link data-chunk="bootstrap" rel="modulepreload" as="script" href="https://s100.divarcdn.com/web-assets/2026/09/components-179.d6e1052a.desktop.js">
        <link data-chunk="bootstrap" rel="modulepreload" as="script" href="https://s100.divarcdn.com/web-assets/2026/09/utils-357.29d51d34.desktop.js">
        <link data-chunk="bootstrap" rel="modulepreload" as="script" href="https://s100.divarcdn.com/web-assets/2026/09/services-671.684eee20.desktop.js">
        <link data-chunk="bootstrap" rel="modulepreload" as="script" href="https://s100.divarcdn.com/web-assets/2026/09/store-962.40538bcd.desktop.js">
        <link data-chunk="bootstrap" rel="modulepreload" as="script" href="https://s100.divarcdn.com/web-assets/2026/09/per-localization-94.c8aa1079.desktop.js">
        <link data-chunk="bootstrap" rel="modulepreload" as="script" href="https://s100.divarcdn.com/web-assets/2026/09/bootstrap-547.f4f8925c.desktop.js">
        <link rel="manifest" href="/manifest.json" crossorigin="use-credentials">
        <link rel="search" type="application/opensearchdescription+xml" title="Divar" href="/opensearch.xml"/>
        <link rel="apple-touch-icon" sizes="180x180" href="https://s100.divarcdn.com/web-assets/publics/apple-touch-icon.png">
        <link rel="icon" type="image/png" sizes="32x32" href="https://s100.divarcdn.com/web-assets/publics/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="16x16" href="https://s100.divarcdn.com/web-assets/publics/favicon-16x16.png">
        <link rel="mask-icon" href="https://s100.divarcdn.com/web-assets/publics/safari-pinned-tab.svg" color="#c32e2e">
        <meta name="color-scheme" content="only light">
        <meta name="theme-color" media="(prefers-color-scheme: light)" content="#ffffff"/>
        <meta name="theme-color" media="(prefers-color-scheme: dark)" content="#18181b"/>
        <link data-react-helmet="true" href="https://s100.divarcdn.com/web-assets/2026/09/IRANSansWeb.cdb118d6.woff2" type="font/woff2" as="font" rel="preload" crossOrigin="anonymous"/>
        <link data-react-helmet="true" rel="canonical" href="https://divar.ir/v/%DB%B9%DB%B7-%D9%85%D8%AA%D8%B1-%DB%B2-%D8%AE%D9%88%D8%A7%D8%A8-%D8%AF%D9%88%D9%86%D8%A8%D8%B4-%D8%AF%DB%8C%D8%AF-%D8%A7%D8%A8%D8%AF%DB%8C/gap5-Twe"/>
        <link data-react-helmet="true" rel="alternate" href="android-app://ir.divar/http/v/۹۷ متر ۲ خواب دونبش __ دید ابدی/gap5-Twe/"/>
        <link data-react-helmet="true" rel="apple-touch-icon" href="https://s100.divarcdn.com/web-assets/publics/android-chrome-512x512.png"/>
        <link data-react-helmet="true" rel="android-touch-icon" href="https://s100.divarcdn.com/web-assets/publics/android-chrome-512x512.png"/>
        <style type="text/css">
            /* vendors-pb-159.400a4952.desktop.css */
            html {
                -webkit-text-size-adjust: 100%;
                line-height: 1.15;
            }

            body {
                margin: 0;
            }

            main {
                display: block;
            }

            h1 {
                font-size: 2em;
                margin: .67em 0;
            }

            hr {
                box-sizing: content-box;
                height: 0;
                overflow: visible;
            }

            pre {
                font-family: monospace,monospace;
                font-size: 1em;
            }

            a {
                background-color: transparent;
            }

            abbr[title] {
                border-bottom: none;
                text-decoration: underline;
                text-decoration: underline dotted;
            }

            b,strong {
                font-weight: bolder;
            }

            code,kbd,samp {
                font-family: monospace,monospace;
                font-size: 1em;
            }

            small {
                font-size: 80%;
            }

            sub,sup {
                font-size: 75%;
                line-height: 0;
                position: relative;
                vertical-align: baseline;
            }

            sub {
                bottom: -.25em;
            }

            sup {
                top: -.5em;
            }

            img {
                border-style: none;
            }

            button,input,optgroup,select,textarea {
                font-family: inherit;
                font-size: 100%;
                line-height: 1.15;
                margin: 0;
            }

            button,input {
                overflow: visible;
            }

            button,select {
                text-transform: none;
            }

            [type=button],[type=reset],[type=submit],button {
                -webkit-appearance: button;
            }

            [type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner,button::-moz-focus-inner {
                border-style: none;
                padding: 0;
            }

            [type=button]:-moz-focusring,[type=reset]:-moz-focusring,[type=submit]:-moz-focusring,button:-moz-focusring {
                outline: 1px dotted ButtonText;
            }

            fieldset {
                padding: .35em .75em .625em;
            }

            legend {
                box-sizing: border-box;
                color: inherit;
                display: table;
                max-width: 100%;
                padding: 0;
                white-space: normal;
            }

            progress {
                vertical-align: baseline;
            }

            textarea {
                overflow: auto;
            }

            [type=checkbox],[type=radio] {
                box-sizing: border-box;
                padding: 0;
            }

            [type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button {
                height: auto;
            }

            [type=search] {
                -webkit-appearance: textfield;
                outline-offset: -2px;
            }

            [type=search]::-webkit-search-decoration {
                -webkit-appearance: none;
            }

            ::-webkit-file-upload-button {
                -webkit-appearance: button;
                font: inherit;
            }

            details {
                display: block;
            }

            summary {
                display: list-item;
            }

            [hidden],template {
                display: none;
            }

            /* widget-base-183.17dd2262.desktop.css */
            @-moz-keyframes slide-from-right-putwZd {
                0% {
                    opacity: 0;
                    -moz-transform: translate(20%);
                    transform: translate(20%)
                }

                to {
                    opacity: 1;
                    -moz-transform: translate(0);
                    transform: translate(0)
                }
            }

            @keyframes slide-from-right-putwZd {
                0% {
                    opacity: 0;
                    -moz-transform: translate(20%);
                    transform: translate(20%)
                }

                to {
                    opacity: 1;
                    -moz-transform: translate(0);
                    transform: translate(0)
                }
            }

            @-moz-keyframes slide-from-left-Nx6haW {
                0% {
                    opacity: 0;
                    -moz-transform: translate(-20%);
                    transform: translate(-20%)
                }

                to {
                    opacity: 1;
                    -moz-transform: translate(0);
                    transform: translate(0)
                }
            }

            @keyframes slide-from-left-Nx6haW {
                0% {
                    opacity: 0;
                    -moz-transform: translate(-20%);
                    transform: translate(-20%)
                }

                to {
                    opacity: 1;
                    -moz-transform: translate(0);
                    transform: translate(0)
                }
            }

            @supports(padding-bottom: constant(safe-area-inset-bottom)) {
                .offset-ZRHscq {
                    margin-bottom:calc(56px + constant(safe-area-inset-bottom))
                }
            }

            @supports(padding-bottom: env(safe-area-inset-bottom)) {
                .offset-ZRHscq {
                    margin-bottom:calc(56px + env(safe-area-inset-bottom, 0))
                }
            }

            /* bootstrap-547.0ea3018f.desktop.css */
            body,html {
                -webkit-tap-highlight-color: transparent;
            }

            @page {
                size: auto;
                margin: 0
            }

            /* main-792.20fa726a.desktop.css */
            :root {
                --surface-neutral-weaker: 255,255,255;
                --surface-neutral-weak: 244,244,245;
                --surface-neutral-default: 228,228,231;
                --surface-neutral-strong: 195,195,201;
                --surface-neutral-stronger: 161,161,170;
                --surface-neutral-on-color: 255,255,255;
                --surface-inverted-weaker: 113,113,122;
                --surface-inverted-weak: 82,82,91;
                --surface-inverted-default: 63,63,70;
                --surface-inverted-strong: 42,42,48;
                --surface-inverted-stronger: 24,24,27;
                --surface-inverted-on-color: 0,0,0;
                --surface-brand-weakest: 252,248,248;
                --surface-brand-weaker: 250,231,231;
                --surface-brand-weak: 252,201,201;
                --surface-brand-default: 232,135,135;
                --surface-brand-strong: 216,57,57;
                --surface-brand-stronger: 195,46,46;
                --surface-brand-strongest: 141,49,49;
                --surface-informative-weaker: 237,242,255;
                --surface-informative-weak: 229,238,255;
                --surface-informative-default: 215,228,255;
                --surface-informative-strong: 124,162,245;
                --surface-informative-stronger: 48,98,212;
                --surface-positive-weaker: 230,249,239;
                --surface-positive-weak: 216,248,231;
                --surface-positive-default: 198,241,218;
                --surface-positive-strong: 117,204,158;
                --surface-positive-stronger: 29,124,77;
                --surface-warning-weaker: 255,240,224;
                --surface-warning-weak: 255,232,209;
                --surface-warning-default: 252,222,192;
                --surface-warning-strong: 254,184,114;
                --surface-warning-stronger: 246,163,81;
                --surface-negative-weaker: 255,235,235;
                --surface-negative-weak: 254,230,230;
                --surface-negative-default: 252,217,217;
                --surface-negative-strong: 244,144,144;
                --surface-negative-stronger: 197,52,52;
                --surface-dimmer-neutral-weak: 0,0,0;
                --surface-dimmer-neutral-default: 0,0,0;
                --surface-dimmer-neutral-strong: 0,0,0;
                --surface-dimmer-brand-weak: 195,46,46;
                --surface-dimmer-brand-default: 195,46,46;
                --surface-dimmer-brand-strong: 195,46,46;
                --surface-dimmer-neutral-opacity-dark: 16%;
                --surface-dimmer-neutral-opacity-darker: 32%;
                --surface-dimmer-neutral-opacity-darkest: 64%;
                --surface-dimmer-brand-opacity-dark: 16%;
                --surface-dimmer-brand-opacity-darker: 32%;
                --surface-dimmer-brand-opacity-darkest: 64%;
                --content-neutral-weaker: 195,195,201;
                --content-neutral-weak: 161,161,170;
                --content-neutral-default: 113,113,122;
                --content-neutral-strong: 82,82,91;
                --content-neutral-stronger: 42,42,48;
                --content-neutral-on-color: 255,255,255;
                --content-inverted-weaker: 255,255,255;
                --content-inverted-weak: 244,244,245;
                --content-inverted-default: 195,195,201;
                --content-inverted-strong: 161,161,170;
                --content-inverted-stronger: 113,113,122;
                --content-inverted-on-color: 42,42,48;
                --content-brand-weaker: 252,201,201;
                --content-brand-weak: 232,135,135;
                --content-brand-default: 205,103,103;
                --content-brand-strong: 195,46,46;
                --content-brand-stronger: 141,49,49;
                --content-informative-weaker: 124,162,245;
                --content-informative-weak: 89,135,242;
                --content-informative-default: 48,98,212;
                --content-informative-strong: 39,89,205;
                --content-informative-stronger: 57,90,167;
                --content-positive-weaker: 74,165,120;
                --content-positive-weak: 74,165,120;
                --content-positive-default: 29,124,77;
                --content-positive-strong: 30,113,74;
                --content-positive-stronger: 14,78,48;
                --content-warning-weaker: 231,143,56;
                --content-warning-weak: 215,128,41;
                --content-warning-default: 187,104,26;
                --content-warning-strong: 85,58,31;
                --content-warning-stronger: 62,44,26;
                --content-negative-weaker: 244,144,144;
                --content-negative-weak: 242,100,100;
                --content-negative-default: 197,52,52;
                --content-negative-strong: 161,54,54;
                --content-negative-stronger: 149,45,45;
                --border-neutral-weaker: 228,228,231;
                --border-neutral-weak: 195,195,201;
                --border-neutral-default: 161,161,170;
                --border-neutral-strong: 113,113,122;
                --border-neutral-stronger: 82,82,91;
                --border-brand-weaker: 252,201,201;
                --border-brand-weak: 232,135,135;
                --border-brand-default: 205,103,103;
                --border-brand-strong: 195,46,46;
                --border-brand-stronger: 141,49,49;
                --border-informative-weaker: 215,228,255;
                --border-informative-weak: 205,221,255;
                --border-informative-default: 124,162,245;
                --border-informative-strong: 48,98,212;
                --border-informative-stronger: 57,90,167;
                --border-positive-weaker: 198,241,218;
                --border-positive-weak: 194,235,213;
                --border-positive-default: 117,204,158;
                --border-positive-strong: 29,124,77;
                --border-positive-stronger: 14,78,48;
                --border-warning-weaker: 252,222,192;
                --border-warning-weak: 255,212,168;
                --border-warning-default: 254,184,114;
                --border-warning-strong: 231,143,56;
                --border-warning-stronger: 187,104,26;
                --border-negative-weaker: 252,217,217;
                --border-negative-weak: 252,207,207;
                --border-negative-default: 244,144,144;
                --border-negative-strong: 197,52,52;
                --border-negative-stronger: 149,45,45;
                --purple-assistive: 91,19,247;
                --magenta-assistive: 216,13,182;
            }

            [data-theme=dark] {
                --surface-neutral-weaker: 24,24,27;
                --surface-neutral-weak: 42,42,48;
                --surface-neutral-default: 63,63,70;
                --surface-neutral-strong: 82,82,91;
                --surface-neutral-stronger: 113,113,122;
                --surface-neutral-on-color: 255,255,255;
                --surface-inverted-weaker: 113,113,122;
                --surface-inverted-weak: 228,228,231;
                --surface-inverted-default: 161,161,170;
                --surface-inverted-strong: 249,250,251;
                --surface-inverted-stronger: 252,252,253;
                --surface-inverted-on-color: 0,0,0;
                --surface-brand-weakest: 35,21,21;
                --surface-brand-weaker: 52,29,29;
                --surface-brand-weak: 116,28,28;
                --surface-brand-default: 141,49,49;
                --surface-brand-strong: 195,46,46;
                --surface-brand-stronger: 216,57,57;
                --surface-brand-strongest: 205,103,103;
                --surface-informative-weaker: 24,32,51;
                --surface-informative-weak: 32,47,82;
                --surface-informative-default: 39,61,114;
                --surface-informative-strong: 39,89,205;
                --surface-informative-stronger: 124,162,245;
                --surface-positive-weaker: 6,45,27;
                --surface-positive-weak: 7,52,31;
                --surface-positive-default: 8,59,35;
                --surface-positive-strong: 30,113,74;
                --surface-positive-stronger: 74,165,120;
                --surface-warning-weaker: 39,30,21;
                --surface-warning-weak: 62,44,26;
                --surface-warning-default: 85,58,31;
                --surface-warning-strong: 215,128,41;
                --surface-warning-stronger: 254,184,114;
                --surface-negative-weaker: 89,33,33;
                --surface-negative-weak: 102,36,36;
                --surface-negative-default: 115,39,39;
                --surface-negative-strong: 161,54,54;
                --surface-negative-stronger: 242,100,100;
                --surface-dimmer-neutral-weak: 0,0,0;
                --surface-dimmer-neutral-default: 0,0,0;
                --surface-dimmer-neutral-strong: 0,0,0;
                --surface-dimmer-brand-weak: 195,46,46;
                --surface-dimmer-brand-default: 195,46,46;
                --surface-dimmer-brand-strong: 195,46,46;
                --surface-dimmer-neutral-opacity-dark: 16%;
                --surface-dimmer-neutral-opacity-darker: 32%;
                --surface-dimmer-neutral-opacity-darkest: 64%;
                --surface-dimmer-brand-opacity-dark: 16%;
                --surface-dimmer-brand-opacity-darker: 32%;
                --surface-dimmer-brand-opacity-darkest: 64%;
                --content-neutral-weaker: 63,63,70;
                --content-neutral-weak: 113,113,122;
                --content-neutral-default: 161,161,170;
                --content-neutral-strong: 195,195,201;
                --content-neutral-stronger: 249,250,251;
                --content-neutral-on-color: 255,255,255;
                --content-inverted-weaker: 42,42,48;
                --content-inverted-weak: 63,63,70;
                --content-inverted-default: 113,113,122;
                --content-inverted-strong: 161,161,170;
                --content-inverted-stronger: 195,195,201;
                --content-inverted-on-color: 42,42,48;
                --content-brand-weaker: 52,29,29;
                --content-brand-weak: 116,28,28;
                --content-brand-default: 141,49,49;
                --content-brand-strong: 205,103,103;
                --content-brand-stronger: 232,135,135;
                --content-informative-weaker: 39,89,205;
                --content-informative-weak: 48,98,212;
                --content-informative-default: 89,135,242;
                --content-informative-strong: 124,162,245;
                --content-informative-stronger: 205,221,255;
                --content-positive-weaker: 29,124,77;
                --content-positive-weak: 74,165,120;
                --content-positive-default: 117,204,158;
                --content-positive-strong: 194,235,213;
                --content-positive-stronger: 198,241,218;
                --content-warning-weaker: 187,104,26;
                --content-warning-weak: 215,128,41;
                --content-warning-default: 231,143,56;
                --content-warning-strong: 246,163,81;
                --content-warning-stronger: 254,184,114;
                --content-negative-weaker: 161,54,54;
                --content-negative-weak: 197,52,52;
                --content-negative-default: 242,100,100;
                --content-negative-strong: 244,144,144;
                --content-negative-stronger: 252,207,207;
                --border-neutral-weaker: 42,42,48;
                --border-neutral-weak: 63,63,70;
                --border-neutral-default: 82,82,91;
                --border-neutral-strong: 113,113,122;
                --border-neutral-stronger: 161,161,170;
                --border-brand-weaker: 52,29,29;
                --border-brand-weak: 141,49,49;
                --border-brand-default: 216,57,57;
                --border-brand-strong: 205,103,103;
                --border-brand-stronger: 232,135,135;
                --border-informative-weaker: 24,32,51;
                --border-informative-weak: 32,47,82;
                --border-informative-default: 39,61,114;
                --border-informative-strong: 57,90,167;
                --border-informative-stronger: 48,98,212;
                --border-positive-weaker: 6,45,27;
                --border-positive-weak: 7,52,31;
                --border-positive-default: 8,59,35;
                --border-positive-strong: 14,78,48;
                --border-positive-stronger: 29,124,77;
                --border-warning-weaker: 39,30,21;
                --border-warning-weak: 62,44,26;
                --border-warning-default: 85,58,31;
                --border-warning-strong: 187,104,26;
                --border-warning-stronger: 231,143,56;
                --border-negative-weaker: 89,33,33;
                --border-negative-weak: 102,36,36;
                --border-negative-default: 115,39,39;
                --border-negative-strong: 242,100,100;
                --border-negative-stronger: 244,144,144;
                --purple-assistive: 91,19,247;
                --magenta-assistive: 216,13,182;
            }

            :root {
                --surface-assistive-default: linear-gradient(89.01deg,rgba(91,19,247,8%),rgba(206,0,170,0)),#fff;
                --content-assistive-default: linear-gradient(80deg,#5b13f7,#d80db6);
                --border-assistive-default: linear-gradient(89.01deg,#5b13f7 0.2%,#9810d7 48.86%,#d80db6);
            }

            [data-theme=dark] {
                --surface-assistive-default: linear-gradient(89.01deg,rgba(91,19,247,8%),rgba(206,0,170,0)),#242424;
                --content-assistive-default: linear-gradient(80deg,#5b13f7,#d80db6);
                --border-assistive-default: linear-gradient(89.01deg,#5b13f7 0.2%,#9810d7 48.86%,#d80db6);
            }

            body {
                font-family: IRANSans,tahoma,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;
                font-size: 1rem;
                font-weight: 400;
            }

            a {
                text-decoration: none;
            }

            button,h1,h2,h3,h4,h5,h6,input,p,small,span,textarea {
                font-family: IRANSans,tahoma,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;
            }

            h3,h4,h5,h6 {
                font-size: 1.25rem;
                font-weight: 500;
                line-height: 1.5;
            }

            h3 {
                font-size: 1.5rem;
            }

            h5 {
                font-size: 1.125rem;
            }

            h6 {
                font-size: 1rem;
                line-height: 2;
            }

            h1,h2 {
                font-size: 3rem;
                font-weight: 400;
                line-height: 1.5;
            }

            h2 {
                font-size: 2rem;
            }

            p {
                font-size: 1rem;
                font-weight: 400;
                line-height: 2;
            }

            @media screen and (max-width: 768px) {
                p {
                    font-size: .875rem;
                }

                h3,h4,h5,h6 {
                    font-size: 1.125rem;
                }

                h3 {
                    font-size: 1.25rem;
                }

                h5 {
                    font-size: 1rem;
                }

                h1,h2 {
                    font-size: 2rem;
                }

                h1,h2 {
                    font-weight: 500;
                }

                h2 {
                    font-size: 1.125rem;
                }
            }

            html {
                box-sizing: border-box;
            }

            *,:after,:before {
                box-sizing: inherit;
                outline-color: #7ca2f5;
                outline-color: rgb(var(--border-informative-default));
            }

            body,html {
                background-color: #fff;
                background-color: rgb(var(--surface-neutral-weaker));
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
                height: 100%;
            }

            fieldset {
                border: 0;
                margin: 0;
                min-width: 0;
                padding: 0;
            }

            a {
                color: #c32e2e;
                color: rgb(var(--content-brand-strong));
            }

            body {
                --navbar-height: 64px;
                --browse-location-row-height: 0px;
                overflow-x: visible !important;
            }

            @font-face {
                font-display: swap;
                font-family: IRANSans;
                font-style: normal;
                font-weight: 700;
                src: url(https://s100.divarcdn.com/web-assets/2026/09/IRANSansWeb_Bold.94bdf556.woff2) format("woff2"),url(https://s100.divarcdn.com/web-assets/2026/09/IRANSansWeb_Bold.dd12fb6a.woff) format("woff")
            }

            @font-face {
                font-display: swap;
                font-family: IRANSans;
                font-style: normal;
                font-weight: 500;
                src: url(https://s100.divarcdn.com/web-assets/2026/09/IRANSansWeb_Medium.9f338149.woff2) format("woff2"),url(https://s100.divarcdn.com/web-assets/2026/09/IRANSansWeb_Medium.2d28b58d.woff) format("woff")
            }

            @font-face {
                font-display: swap;
                font-family: IRANSans;
                font-style: normal;
                font-weight: 400;
                src: url(https://s100.divarcdn.com/web-assets/2026/09/IRANSansWeb.cdb118d6.woff2) format("woff2"),url(https://s100.divarcdn.com/web-assets/2026/09/IRANSansWeb.9ffdcda0.woff) format("woff")
            }

            @font-face {
                font-display: swap;
                font-family: IRANSans;
                font-style: normal;
                font-weight: 300;
                src: url(https://s100.divarcdn.com/web-assets/2026/09/IRANSansWeb_Light.b5815f24.woff2) format("woff2"),url(https://s100.divarcdn.com/web-assets/2026/09/IRANSansWeb_Light.b35266cb.woff) format("woff")
            }

            @font-face {
                font-display: block;
                font-family: sonnat;
                font-style: normal;
                font-weight: 400;
                src: url(https://s100.divarcdn.com/web-assets/2026/09/sonnat-icons.4a686f4a.woff2) format("woff2"),url(https://s100.divarcdn.com/web-assets/2026/09/sonnat-icons.0c8d9969.woff) format("woff")
            }

            @keyframes assistive {
                0% {
                    background-position: 100% 100%
                }

                50% {
                    background-position: 0 0
                }

                to {
                    background-position: 100% 100%
                }
            }

            @keyframes rotate {
                to {
                    transform: rotate(1turn)
                }
            }

            @keyframes stroke-dash {
                0% {
                    stroke-dasharray: 1,100;
                    stroke-dashoffset: 0
                }

                50% {
                    stroke-dasharray: 80,100;
                    stroke-dashoffset: 46
                }

                to {
                    stroke-dasharray: 1,100;
                    stroke-dashoffset: 0
                }
            }

            @keyframes wave {
                0%,to {
                    opacity: .2
                }

                50% {
                    opacity: 1;
                    transform: translateY(-4px)
                }
            }

            @supports(-webkit-line-clamp:2) {
                .kt-card__description {
                    -webkit-line-clamp: 2;
                    -webkit-box-orient: vertical;
                    display: -webkit-box
                }
            }

            @supports not (-webkit-line-clamp:2) {
                .kt-card__description {
                    max-height: 3rem
                }
            }

            @keyframes kt-switch-ripple {
                to {
                    background-color: #fae7e7;
                    background-color: rgb(var(--surface-brand-weaker));
                    transform: scale(4)
                }
            }

            @supports(padding-bottom: constant(safe-area-inset-bottom)) {
                .kt-modal--scrollable .kt-modal__actions {
                    padding-bottom:calc(12px + constant(safe-area-inset-bottom))
                }
            }

            @supports(padding-bottom: env(safe-area-inset-bottom)) {
                .kt-modal--scrollable .kt-modal__actions {
                    padding-bottom:calc(12px + env(safe-area-inset-bottom, 0))
                }
            }

            @supports(padding-bottom: constant(safe-area-inset-bottom)) {
                .kt-alert--scrollable .kt-alert__actions {
                    padding-bottom:calc(12px + constant(safe-area-inset-bottom))
                }
            }

            @supports(padding-bottom: env(safe-area-inset-bottom)) {
                .kt-alert--scrollable .kt-alert__actions {
                    padding-bottom:calc(12px + env(safe-area-inset-bottom, 0))
                }
            }

            @supports(-webkit-line-clamp:2) {
                .kt-event-row__text--subtitle {
                    -webkit-line-clamp: 2;
                    -webkit-box-orient: vertical;
                    display: -webkit-box
                }
            }

            @supports(-webkit-line-clamp:2) {
                .kt-post-card__title {
                    -webkit-line-clamp: 2;
                    -webkit-box-orient: vertical;
                    display: -webkit-box
                }
            }

            @supports(gap: 8px) {
                .kt-post-card-thumbnail__tags-container {
                    gap:8px
                }
            }

            @supports(gap: 8px) {
                .kt-post-card-thumbnail__tags-container>* {
                    margin-left:0
                }
            }

            @supports(padding-bottom: constant(safe-area-inset-bottom)) {
                .kt-alert__actions,.kt-modal__actions {
                    padding-bottom:calc(24px + constant(safe-area-inset-bottom))
                }
            }

            @supports(padding-bottom: env(safe-area-inset-bottom)) {
                .kt-alert__actions,.kt-modal__actions {
                    padding-bottom:calc(24px + env(safe-area-inset-bottom, 0))
                }
            }

            @supports(padding-bottom: constant(safe-area-inset-bottom)) {
                .kt-alert__actions,.kt-modal__actions {
                    padding-bottom:calc(24px + constant(safe-area-inset-bottom))
                }
            }

            @supports(padding-bottom: env(safe-area-inset-bottom)) {
                .kt-alert__actions,.kt-modal__actions {
                    padding-bottom:calc(24px + env(safe-area-inset-bottom, 0))
                }
            }

            @keyframes skeleton-loading {
                0% {
                    right: -20%
                }

                to {
                    right: 110%
                }
            }

            @keyframes kt-toggle-press {
                to {
                    transform: scale(2)
                }
            }

            @keyframes ripple-before {
                0% {
                    opacity: .6;
                    transform: scale3d(1.2,1.2,1)
                }

                50% {
                    opacity: 1;
                    transform: scale3d(1.4,1.4,1)
                }

                to {
                    opacity: .6;
                    transform: scale3d(1.2,1.2,1)
                }
            }

            @keyframes ripple-after {
                0% {
                    opacity: .32;
                    transform: scale3d(1.2,1.2,1)
                }

                50% {
                    opacity: .8;
                    transform: scale3d(1.6,1.6,1)
                }

                to {
                    opacity: .32;
                    transform: scale3d(1.2,1.2,1)
                }
            }

            @keyframes pulse-dot {
                0% {
                    transform: scaleX(1)
                }

                50% {
                    transform: scale3d(1.05,1.05,1)
                }

                to {
                    transform: scaleX(1)
                }
            }

            @supports(padding-bottom: constant(safe-area-inset-bottom)) {
                .kt-bottom-sheet {
                    padding-bottom:constant(safe-area-inset-bottom)
                }
            }

            @supports(padding-bottom: env(safe-area-inset-bottom)) {
                .kt-bottom-sheet {
                    padding-bottom:env(safe-area-inset-bottom,0)
                }
            }

            @supports(padding-bottom: constant(safe-area-inset-bottom)) {
                .kt-plate__bottom-sheet-body {
                    padding-bottom:constant(safe-area-inset-bottom)
                }
            }

            @supports(padding-bottom: env(safe-area-inset-bottom)) {
                .kt-plate__bottom-sheet-body {
                    padding-bottom:env(safe-area-inset-bottom,0)
                }
            }

            /* arcaptcha-pb-831.38bef66d.desktop.css */
            #voiceChallenge[data-v-a00616ec] {
                box-shadow: 0 3pt 6pt rgba(0,0,0,.161);
                z-index: 10000;
            }

            #voiceChallenge #loading-layer[data-v-a00616ec] {
                background-color: hsla(0,0%,100%,.7);
            }

            #guide-box[data-v-a00616ec] {
                bottom: -35px;
            }

            @media (min-width: 320px) {
                #guide-box[data-v-a00616ec] {
                    right: 120px;
                }
            }

            @media (min-width: 768px) {
                #guide-box[data-v-a00616ec] {
                    right: 380px;
                }
            }

            #loading-layer[data-v-5b4bc6c2] {
                background-color: hsla(0,0%,100%,.7);
            }

            #challenge {
                font-display: swap;
                font-family: Yekan,unset;
                position: relative;
            }

            #challenge #loading-layer {
                background-color: hsla(0,0%,100%,.7);
            }

            #challenge[data-v-03c61aac] {
                box-shadow: 0 3pt 6pt rgba(0,0,0,.161);
                z-index: 10000;
            }

            #challenge #loading-layer[data-v-03c61aac] {
                background-color: hsla(0,0%,100%,.7);
            }

            #guide-box[data-v-03c61aac] {
                bottom: -70px;
            }

            @media only screen and (min-width: 320px) {
                #guide-box[data-v-03c61aac] {
                    left: 5px;
                }
            }

            @media (min-width: 768px) {
                #guide-box[data-v-03c61aac] {
                    left: -20px;
                }
            }

            @keyframes spin {
                to {
                    transform: rotate(1turn)
                }
            }

            @supports (color: rgb(0 0 0/0)) {
                .tw-bg-emerald-600 {
                    background-color:rgb(5 150 105/var(--tw-bg-opacity,1))
                }
            }

            @supports (color: rgb(0 0 0/0)) {
                .tw-bg-red-500 {
                    background-color:rgb(239 68 68/var(--tw-bg-opacity,1))
                }
            }

            @supports (color: rgb(0 0 0/0)) {
                .tw-bg-white {
                    background-color:rgb(255 255 255/var(--tw-bg-opacity,1))
                }
            }

            @supports (color: rgb(0 0 0/0)) {
                .tw-text-orange-500 {
                    color:rgb(249 115 22/var(--tw-text-opacity,1))
                }
            }

            @supports (color: rgb(0 0 0/0)) {
                .tw-text-red-600 {
                    color:rgb(220 38 38/var(--tw-text-opacity,1))
                }
            }

            @supports (color: rgb(0 0 0/0)) {
                .tw-text-white {
                    color:rgb(255 255 255/var(--tw-text-opacity,1))
                }
            }

            @keyframes buzz-out {
                10% {
                    transform: translateX(3px) rotate(2deg)
                }

                20% {
                    transform: translateX(-3px) rotate(-2deg)
                }

                30% {
                    transform: translateX(3px) rotate(2deg)
                }

                40% {
                    transform: translateX(-3px) rotate(-2deg)
                }

                50% {
                    transform: translateX(2px) rotate(1deg)
                }

                60% {
                    transform: translateX(-2px) rotate(-1deg)
                }

                70% {
                    transform: translateX(2px) rotate(1deg)
                }

                80% {
                    transform: translateX(-2px) rotate(-1deg)
                }

                90% {
                    transform: translateX(1px) rotate(0)
                }

                to {
                    transform: translateX(-1px) rotate(0)
                }
            }

            @keyframes moveArrow-602e5489 {
                0% {
                    transform: translateX(0)
                }

                to {
                    transform: translateX(5px)
                }
            }

            @keyframes loading-18d4b056 {
                to {
                    transform: translateX(50%)
                }
            }

            /* vendors-pb-159.400a4952.desktop.css */
            .keen-slider:not([data-keen-slider-disabled]) {
                -webkit-touch-callout: none;
                -webkit-tap-highlight-color: transparent;
                align-content: flex-start;
                display: flex;
                overflow: hidden;
                position: relative;
                touch-action: pan-y;
                -webkit-user-select: none;
                -moz-user-select: none;
                -ms-user-select: none;
                user-select: none;
                -khtml-user-select: none;
                width: 100%;
            }

            .keen-slider:not([data-keen-slider-disabled]) .keen-slider__slide {
                min-height: 100%;
                overflow: hidden;
                position: relative;
                width: 100%;
            }

            .keen-slider:not([data-keen-slider-disabled])[data-keen-slider-reverse] {
                flex-direction: row-reverse;
            }

            .keen-slider:not([data-keen-slider-disabled])[data-keen-slider-v] {
                flex-wrap: wrap;
            }

            /* widget-base-183.17dd2262.desktop.css */
            .slides-dUO2O_>div {
                min-width: 100%;
            }

            .image-kclhuf {
                cursor: pointer;
            }

            .note-eLyuUj {
                display: block;
                margin: 8px 0 32px;
            }

            .container-UafEm_ {
                position: relative;
            }

            .hint-JTObjj {
                margin-top: 4px;
            }

            .hint-JTObjj {
                color: rgb(var(--content-neutral-default));
                font-size: .75rem;
            }

            /* postview-782.89280520.desktop.css */
            .expandable-box {
                max-height: 23em;
                overflow: hidden;
                transition: max-height .5s;
            }

            .expandable-box--collapsed {
                max-height: 0;
            }

            .post-actions {
                display: flex;
                margin: 16px 0;
            }

            .post-actions__share-button {
                margin-right: 8px;
            }

            .post-actions__bookmark-button {
                margin-right: auto;
            }

            .post-page__section--padded+.post-page__section--padded {
                margin-top: 16px;
            }

            /* main-792.20fa726a.desktop.css */
            .no-pointer-event {
                pointer-events: none;
            }

            .kt-text-truncate {
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            }

            .kt-base-row {
                color: #71717a;
                color: rgb(var(--content-neutral-default));
                display: flex;
                font-size: 1rem;
                font-weight: 400;
                justify-content: space-between;
                line-height: 2;
                min-height: 48px;
                padding: 8px 0;
                white-space: normal;
            }

            .kt-base-row__end,.kt-base-row__start {
                align-items: flex-start;
                display: flex;
            }

            .kt-base-row__end,.kt-base-row__start {
                min-width: 0;
            }

            .kt-base-row__start {
                flex: 1 1;
            }

            .kt-base-row__end {
                flex-shrink: 0;
                justify-content: flex-end;
                margin-right: 10px;
                max-width: 50%;
            }

            .kt-base-row__arrow {
                line-height: 1;
                margin: 4px 8px 0 0;
            }

            .kt-base-row__arrow:before {
                color: #a1a1aa;
                color: rgb(var(--content-neutral-weak));
            }

            .kt-base-row__icon {
                line-height: 1;
                margin: 4px 0 0 16px;
            }

            .kt-section-title {
                align-items: flex-start;
                display: flex;
                margin-top: 24px;
            }

            .kt-section-title--alt-padded {
                margin-bottom: 16px;
            }

            .kt-section-title__title-block {
                align-items: flex-end;
                display: flex;
            }

            .kt-section-title__title {
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
                font-size: 1.125rem;
                font-weight: 400;
                line-height: 1.5;
                margin: 0;
            }

            .kt-unexpandable-row {
                font-size: 1rem;
                overflow: hidden;
                white-space: nowrap;
            }

            .kt-unexpandable-row__title-box {
                flex: unset;
                min-width: 20%;
            }

            .kt-unexpandable-row__value-box {
                flex: unset;
                margin-right: 16px;
                max-width: calc(80% - 16px);
                min-width: 20%;
            }

            .kt-unexpandable-row__title,.kt-unexpandable-row__value {
                font-size: inherit;
                line-height: 2;
                margin: 0;
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            }

            .kt-unexpandable-row__title {
                color: #71717a;
                color: rgb(var(--content-neutral-default));
            }

            .kt-unexpandable-row__value {
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
            }

            .kt-selector-row {
                border-radius: 4px;
                outline: none;
            }

            .kt-selector-row__start {
                align-items: flex-start;
                display: flex;
                flex: 1 1;
                overflow: hidden;
            }

            .kt-selector-row__title {
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
                font-size: inherit;
                line-height: 2;
                margin: 0;
            }

            .kt-title-row {
                align-items: center;
                margin-top: 8px;
                white-space: nowrap;
            }

            .kt-title-row__title {
                font-size: inherit;
                font-weight: 700;
                line-height: 2;
                margin: 0;
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            }

            .kt-title-row__title--secondary {
                font-size: 1.125rem;
                line-height: 1.5;
            }

            .kt-title-row__row {
                align-items: center;
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
            }

            .kt-description-row {
                min-height: auto;
                padding: 0;
                position: relative;
            }

            .kt-description-row__text {
                color: #71717a;
                color: rgb(var(--content-neutral-default));
                font-weight: 400;
                line-height: 2;
                margin: 0;
                overflow-wrap: anywhere;
                white-space: pre-line;
            }

            .kt-description-row__text--primary {
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
            }

            .kt-description-row--padded {
                padding: 16px 0;
            }

            .kt-icon {
                text-rendering: auto;
                background-position: 50%;
                background-size: contain;
                display: inline-block;
                font-family: sonnat !important;
                font-size: 1.25rem;
                font-style: normal;
                font-variant: normal;
                height: 20px;
                line-height: 1;
                vertical-align: middle;
                width: 20px;
            }

            .kt-icon--xl {
                font-size: 2rem;
                height: 32px;
                width: 32px;
            }

            .kt-icon--lg {
                font-size: 1.5rem;
                height: 24px;
                width: 24px;
            }

            .kt-icon--sm {
                font-size: 1.125rem;
                height: 18px;
                width: 18px;
            }

            .kt-icon--xs {
                font-size: 1rem;
                height: 16px;
                width: 16px;
            }

            .kt-icon-elevator:before {
                content: "\e962";
            }

            .kt-icon-social-linkedin:before {
                content: "\e964";
            }

            .kt-icon-report:before {
                content: "\e967";
            }

            .kt-icon-support:before {
                content: "\e96a";
            }

            .kt-icon-social-instagram-fill:before {
                content: "\e975";
            }

            .kt-icon-chat-bubble:before {
                content: "\e997";
            }

            .kt-icon-social-twitter:before {
                content: "\e9a6";
            }

            .kt-icon-social-divar:before {
                content: "\e9a9";
            }

            .kt-icon-share-o:before {
                content: "\e9b9";
            }

            .kt-icon-place:before {
                content: "\e9c4";
            }

            .kt-icon-person:before {
                content: "\e9c9";
            }

            .kt-icon-full-screen-o:before {
                content: "\e9ce";
            }

            .kt-icon-warning:before {
                content: "\e9da";
            }

            .kt-icon-added-o:before {
                content: "\e9e6";
            }

            .kt-icon-close:before {
                content: "\e9f6";
            }

            .kt-icon-search-o:before {
                content: "\e9fc";
            }

            .kt-icon-bookmark-o:before {
                content: "\ea10";
            }

            .kt-icon-keyboard-arrow-left:before {
                content: "\ea13";
            }

            .kt-icon-keyboard-arrow-down-o:before {
                content: "\ea14";
            }

            .kt-icon-share:before {
                content: "\ea16";
            }

            .kt-icon-cabinet:before {
                content: "\ea19";
            }

            .kt-icon-parking:before {
                content: "\ea1c";
            }

            .kt-icon-social-aparat:before {
                content: "\ea34";
            }

            .kt-icon-article-magnifier:before {
                content: "\ec15";
            }

            .kt-tag {
                align-items: center;
                border-radius: 8px;
                display: inline-flex;
                font-weight: 400;
                height: auto;
                line-height: 2;
                overflow: hidden;
                padding: 0 4px 0 8px;
            }

            .kt-tag__text {
                flex: 1 1;
                margin-right: 4px;
                unicode-bidi: plaintext;
            }

            .kt-tag--flipped {
                flex-direction: row-reverse;
            }

            .kt-tag--flipped:not(.kt-tag--just-text):not(.kt-tag--just-icon) {
                padding: 0 8px 0 4px;
            }

            .kt-tag--flipped:not(.kt-tag--just-text)>.kt-tag__text {
                margin-left: 4px;
                margin-right: 0;
            }

            .kt-tag--overlay {
                background-color: rgba(0,0,0,.64);
                background-color: rgba(var(--surface-inverted-on-color),.64);
                border: 1px solid transparent;
                color: #fff;
                color: rgb(var(--content-neutral-on-color));
            }

            .kt-tag--medium {
                font-size: .875rem;
                max-height: 30px;
                min-height: 30px;
            }

            .kt-tag__icon {
                background-repeat: no-repeat;
            }

            .kt-divider {
                background-color: #e4e4e7;
                background-color: rgb(var(--border-neutral-weaker));
                border: none;
                box-sizing: border-box;
                height: 1px;
                margin: 0;
            }

            .kt-divider--padded {
                margin: 8px 0;
            }

            .kt-divider--vertical {
                display: inline-block;
                height: 1.5rem;
                width: 1px;
            }

            .kt-divider--vertical.kt-divider--padded {
                margin: 0 8px;
            }

            .kt-progress-circular,.kt-progress-snake {
                display: inline-block;
                position: relative;
                vertical-align: middle;
            }

            .kt-progress-circular--center,.kt-progress-snake--center {
                align-items: center;
                display: inline-flex;
                justify-content: center;
                width: 100%;
            }

            .kt-progress-circular--center,.kt-progress-snake--center {
                height: 100%;
            }

            .kt-progress-circular--animated .kt-progress-circular__rotate {
                animation: rotate .8s linear infinite;
                transform-box: fill-box;
                transform-origin: center;
            }

            .kt-progress-circular--animated .kt-progress-circular__moving-particle {
                animation: stroke-dash 1.6s ease-in infinite;
            }

            .kt-progress-circular__content {
                height: 20px;
                width: 20px;
            }

            .kt-progress-circular--lg .kt-progress-circular__content {
                height: 24px;
                min-height: 24px;
                min-width: 24px;
                width: 24px;
            }

            .kt-progress-circular__static-particle {
                fill: #c3c3c9;
                fill: rgb(var(--content-neutral-weaker));
            }

            .kt-progress-circular__moving-particle {
                fill: none;
                stroke: #2a2a30;
                stroke: rgb(var(--content-neutral-stronger));
                stroke-width: 2px;
                stroke-linecap: round;
                stroke-linejoin: round;
                stroke-dasharray: 67,100;
                stroke-dashoffset: 46;
                transform-origin: center;
            }

            .kt-progress-snake--primary .kt-progress-snake__node {
                background-color: #d83939;
                background-color: rgb(var(--surface-brand-strong));
            }

            .kt-progress-snake--animated .kt-progress-snake__node {
                animation: wave 1s ease-in-out infinite;
            }

            .kt-progress-snake__node {
                background-color: #e4e4e7;
                background-color: rgb(var(--surface-neutral-default));
                border-radius: 50%;
                display: inline-block;
                height: 4px;
                margin: 0 2px;
                vertical-align: middle;
                width: 4px;
            }

            .kt-progress-snake__node:nth-child(n+2) {
                animation-delay: .2s;
            }

            .kt-progress-snake__node:nth-child(n+3) {
                animation-delay: .4s;
            }

            .kt-button {
                align-items: center;
                background-color: #3f3f46;
                background-color: rgb(var(--surface-inverted-default));
                border: 1px solid transparent;
                border-radius: 4px;
                box-sizing: border-box;
                color: #fff;
                color: rgb(var(--content-neutral-on-color));
                cursor: pointer;
                display: inline-flex;
                font-size: 1rem;
                font-weight: 500;
                height: 2.5rem;
                justify-content: center;
                line-height: normal;
                min-width: 6rem;
                outline: none;
                overflow: hidden;
                padding: 0 16px;
                position: relative;
                transition: color .36s ease,background-color .36s ease,box-shadow .36s ease,border-color .36s ease,transform .36s ease;
            }

            .kt-button:focus,.kt-button:hover {
                background-color: #52525b;
                background-color: rgb(var(--surface-inverted-weak));
            }

            .kt-button:active {
                background-color: #2a2a30;
                background-color: rgb(var(--surface-inverted-strong));
            }

            .kt-button:disabled {
                background-color: #c3c3c9;
                background-color: rgb(var(--surface-neutral-strong));
                box-shadow: none;
                color: #71717a;
                color: rgb(var(--content-neutral-default));
                cursor: not-allowed;
            }

            .kt-button:disabled:focus,.kt-button:disabled:hover {
                background-color: #c3c3c9;
                background-color: rgb(var(--surface-neutral-strong));
                box-shadow: none;
                transform: none;
            }

            .kt-button:disabled:active {
                background-color: #c3c3c9;
                background-color: rgb(var(--surface-neutral-strong));
            }

            .kt-button.kt-button--primary {
                background-color: #c32e2e;
                background-color: rgb(var(--surface-brand-stronger));
                color: #fff;
                color: rgb(var(--content-neutral-on-color));
            }

            .kt-button.kt-button--primary:focus,.kt-button.kt-button--primary:hover {
                background-color: #d83939;
                background-color: rgb(var(--surface-brand-strong));
            }

            .kt-button.kt-button--primary:active {
                background-color: #8d3131;
                background-color: rgb(var(--surface-brand-strongest));
            }

            .kt-button.kt-button--primary:disabled {
                background-color: #c3c3c9;
                background-color: rgb(var(--surface-neutral-strong));
                color: #71717a;
                color: rgb(var(--content-neutral-default));
            }

            .kt-button.kt-button--primary:disabled:active,.kt-button.kt-button--primary:disabled:focus,.kt-button.kt-button--primary:disabled:hover {
                background-color: #c3c3c9;
                background-color: rgb(var(--surface-neutral-strong));
            }

            .kt-button--inlined {
                background-color: transparent;
                color: #71717a;
                color: rgb(var(--content-neutral-default));
            }

            .kt-button--inlined:focus,.kt-button--inlined:hover {
                background-color: #f4f4f5;
                background-color: rgb(var(--surface-neutral-weak));
            }

            .kt-button--inlined:active {
                background-color: #e4e4e7;
                background-color: rgb(var(--surface-neutral-default));
            }

            .kt-button--inlined:disabled {
                background-color: transparent;
                color: #a1a1aa;
                color: rgb(var(--content-neutral-weak));
            }

            .kt-button--inlined:disabled:active,.kt-button--inlined:disabled:focus,.kt-button--inlined:disabled:hover {
                background-color: transparent;
            }

            .kt-button--inlined:disabled:focus,.kt-button--inlined:disabled:hover {
                color: #a1a1aa;
                color: rgb(var(--content-neutral-weak));
            }

            .kt-button--inlined:focus,.kt-button--inlined:hover {
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
            }

            .kt-button--inlined:focus:disabled,.kt-button--inlined:hover:disabled {
                color: #a1a1aa;
                color: rgb(var(--content-neutral-weak));
            }

            .kt-button--inlined.kt-button--primary {
                background-color: transparent;
                color: #c32e2e;
                color: rgb(var(--content-brand-strong));
            }

            .kt-button--inlined.kt-button--primary:focus,.kt-button--inlined.kt-button--primary:hover {
                background-color: #fcf8f8;
                background-color: rgb(var(--surface-brand-weakest));
            }

            .kt-button--inlined.kt-button--primary:active {
                background-color: #fae7e7;
                background-color: rgb(var(--surface-brand-weaker));
            }

            .kt-button--inlined.kt-button--primary:focus,.kt-button--inlined.kt-button--primary:hover {
                color: #c32e2e;
                color: rgb(var(--content-brand-strong));
            }

            .kt-button--inlined.kt-button--primary:disabled {
                background-color: transparent;
                color: #a1a1aa;
                color: rgb(var(--content-neutral-weak));
            }

            .kt-button--inlined.kt-button--primary:disabled:active,.kt-button--inlined.kt-button--primary:disabled:focus,.kt-button--inlined.kt-button--primary:disabled:hover {
                background-color: transparent;
            }

            .kt-button--inlined {
                color: #71717a;
                color: rgb(var(--content-neutral-default));
            }

            .kt-button__icon {
                height: 1.25rem;
                margin-left: 8px;
                margin-right: -4px;
            }

            .kt-button--circular {
                border-radius: 50%;
                height: 2.5rem;
                min-width: auto;
                padding: 0;
                width: 2.5rem;
            }

            .kt-button--circular .kt-button__icon {
                margin-left: 0;
                margin-right: 0;
            }

            .kt-button-row {
                display: flex;
                justify-content: flex-end;
            }

            .kt-button-row--fullwidth>* {
                flex: 1 1;
            }

            .kt-button-row>:not(:first-child) {
                margin-right: 16px;
            }

            @media (max-width: 768px) {
                .kt-button-row--responsive>* {
                    flex: 1 1;
                }
            }

            .kt-textarea {
                display: block;
                overflow: hidden;
                position: relative;
            }

            .kt-textarea:after {
                border: 1px solid #71717a;
                border: 1px solid rgb(var(--border-neutral-strong));
                border-radius: 4px;
                bottom: 0;
                box-shadow: inset 0 0 0 0 transparent;
                content: "";
                display: block;
                left: 0;
                pointer-events: none;
                position: absolute;
                right: 0;
                top: 0;
                transition: border-color .4s ease,box-shadow .4s ease;
                z-index: 2;
            }

            .kt-textarea__field {
                background: none;
                border: none;
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
                display: block;
                font-size: 1rem;
                font-weight: 400;
                line-height: 2;
                min-height: 7.5rem;
                outline: none;
                padding: 8px 16px;
                resize: none;
                width: 100%;
            }

            .kt-textarea__field::-webkit-scrollbar {
                height: 12px;
                width: 12px;
            }

            .kt-textarea__field::-webkit-scrollbar-thumb {
                background-clip: padding-box;
                background-color: #c3c3c9;
                background-color: rgb(var(--border-neutral-weak));
                border: 4px solid transparent;
                border-radius: 12px;
            }

            .kt-textarea__field::-webkit-scrollbar-thumb:hover {
                background-color: #a1a1aa;
                background-color: rgb(var(--border-neutral-default));
            }

            .kt-textarea__field::-webkit-input-placeholder {
                color: #a1a1aa;
                color: rgb(var(--content-neutral-weak));
                font-size: 1rem;
                font-weight: 400;
                line-height: 2;
                opacity: 1;
            }

            .kt-textarea__field::placeholder {
                color: #a1a1aa;
                color: rgb(var(--content-neutral-weak));
                font-size: 1rem;
                font-weight: 400;
                line-height: 2;
                opacity: 1;
            }

            .kt-textarea__field::-webkit-resizer {
                display: none;
            }

            .kt-textarea__resize-box {
                align-items: center;
                background: #fff;
                background: rgb(var(--surface-neutral-weaker));
                bottom: 0;
                display: none;
                height: .75rem;
                justify-content: center;
                left: 0;
                pointer-events: none;
                position: absolute;
                width: .75rem;
                z-index: 1;
            }

            .kt-textarea__resize-indicator {
                background: #e4e4e7;
                background: rgb(var(--surface-neutral-default));
                height: 1px;
                transform: rotate(45deg);
                transition: background-color .4s ease;
                width: .5rem;
            }

            .kt-textarea:hover:after {
                border-color: #52525b;
                border-color: rgb(var(--border-neutral-stronger));
            }

            .kt-textarea:hover .kt-textarea__resize-indicator {
                background: #a1a1aa;
                background: rgb(var(--surface-neutral-stronger));
            }

            .kt-toast-container {
                display: flex;
                flex-direction: column;
                height: 100%;
                padding: 16px;
                pointer-events: none;
                position: fixed;
                right: 0;
                top: 0;
                width: 100%;
                z-index: 1070;
            }

            @media screen and (min-width: 768px) {
                .kt-toast-container {
                    padding: 32px;
                }
            }

            .kt-dimmer {
                height: 100vh;
                left: 0;
                opacity: 0;
                position: fixed;
                top: 0;
                transition: opacity .36s ease-in-out,visibility .36s;
                transition-duration: .24s;
                visibility: hidden;
                width: 100vw;
                z-index: 1060;
            }

            .kt-dimmer__content {
                align-items: center;
                display: flex;
                flex-direction: column;
                height: 100%;
                justify-content: center;
                left: 0;
                position: fixed;
                top: 0;
                width: 100%;
            }

            .kt-dimmer--dark {
                background-color: rgba(0,0,0,32%);
                background-color: rgba(var(--surface-dimmer-neutral-default),var(--surface-dimmer-neutral-opacity-darker));
            }

            [data-theme=dark] .kt-dimmer--dark {
                background-color: rgba(94,94,94,.32);
            }

            .kt-breadcrumbs {
                -webkit-overflow-scrolling: touch;
                align-items: center;
                display: flex;
                font-size: .75rem;
                line-height: 2;
                margin: 0;
                overflow-x: auto;
                padding: 0;
                scroll-behavior: smooth;
            }

            .kt-breadcrumbs__item {
                align-items: center;
                display: none;
            }

            .kt-breadcrumbs__item:nth-last-child(2) {
                display: flex;
                flex-direction: row-reverse;
            }

            .kt-breadcrumbs__item:nth-last-child(2) .kt-breadcrumbs__nav-icon {
                transform: rotate(180deg);
            }

            @media screen and (min-width: 768px) {
                .kt-breadcrumbs__item:nth-last-child(2) {
                    flex-direction: row;
                }

                .kt-breadcrumbs__item:nth-last-child(2) .kt-breadcrumbs__nav-icon {
                    transform: none;
                }
            }

            @media screen and (max-width: 768px) {
                .kt-breadcrumbs--extended-items-on-mobile .kt-breadcrumbs__item:nth-last-child(2) .kt-breadcrumbs__nav-icon {
                    display: none;
                }

                .kt-breadcrumbs--extended-items-on-mobile .kt-breadcrumbs__item:nth-last-child(-n+4):not(:last-child) {
                    display: flex;
                    flex-direction: row;
                }

                .kt-breadcrumbs--extended-items-on-mobile .kt-breadcrumbs__item:nth-last-child(-n+4):not(:last-child):hover .kt-breadcrumbs__nav-icon {
                    transform: rotate(180deg);
                }

                .kt-breadcrumbs--extended-items-on-mobile .kt-breadcrumbs__item:nth-last-child(-n+4):not(:last-child) .kt-breadcrumbs__nav-icon {
                    transform: rotate(0);
                }
            }

            @media screen and (min-width: 768px) {
                .kt-breadcrumbs__item {
                    display: flex;
                }
            }

            .kt-breadcrumbs__item:hover .kt-breadcrumbs__action-text,.kt-breadcrumbs__item:hover .kt-breadcrumbs__nav-icon {
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
            }

            .kt-breadcrumbs:not(.kt-breadcrumbs--single) .kt-breadcrumbs__item:last-child .kt-breadcrumbs__nav-icon {
                display: none;
            }

            .kt-breadcrumbs:not(.kt-breadcrumbs--single):not(.kt-breadcrumbs--hierarchy) .kt-breadcrumbs__item:last-child .kt-breadcrumbs__action-text,.kt-breadcrumbs:not(.kt-breadcrumbs--single):not(.kt-breadcrumbs--hierarchy) .kt-breadcrumbs__item:last-child:hover .kt-breadcrumbs__action-text {
                color: #a1a1aa;
                color: rgb(var(--content-neutral-weak));
            }

            .kt-breadcrumbs__item:hover .kt-breadcrumbs__nav-icon,.kt-breadcrumbs__item:hover~.kt-breadcrumbs__item .kt-breadcrumbs__nav-icon {
                transform: rotate(180deg);
            }

            .kt-breadcrumbs__action {
                align-items: center;
                border-radius: 4px;
                display: flex;
                margin: 4px;
                transition: color .36s ease;
            }

            .kt-breadcrumbs__nav-icon {
                transition: color .36s ease,transform .36s ease;
            }

            .kt-breadcrumbs__action-text,.kt-breadcrumbs__nav-icon {
                color: #71717a;
                color: rgb(var(--content-neutral-default));
            }

            .kt-breadcrumbs__action-text {
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            }

            .kt-breadcrumbs--padded {
                padding: 16px 0;
            }

            @media screen and (min-width: 768px) {
                .kt-breadcrumbs--padded {
                    padding: 32px 0;
                }
            }

            .kt-breadcrumbs::-webkit-scrollbar,.kt-breadcrumbs::-webkit-scrollbar-thumb,.kt-breadcrumbs::-webkit-scrollbar-thumb:hover,.kt-breadcrumbs::-webkit-scrollbar-track {
                background-color: transparent;
                display: none;
            }

            .kt-container {
                margin-left: auto;
                margin-right: auto;
                max-width: 768px;
                padding-left: 16px;
                padding-right: 16px;
                width: 100%;
            }

            @media (min-width: 960px) {
                .kt-container {
                    max-width: 960px;
                }
            }

            @media (min-width: 1024px) {
                .kt-container {
                    max-width: 1024px;
                }
            }

            .kt-row {
                display: flex;
                flex-wrap: wrap;
                margin-left: -8px;
                margin-right: -8px;
            }

            .kt-col-5,.kt-col-6 {
                padding-left: 8px;
                padding-right: 8px;
                position: relative;
                width: 100%;
            }

            .kt-col-5 {
                flex: 0 0 41.6666666667%;
                max-width: 41.6666666667%;
            }

            .kt-col-6 {
                flex: 0 0 50%;
                max-width: 50%;
            }

            .kt-offset-1 {
                margin-right: 8.3333333333%;
            }

            .kt-wrapper-row {
                align-items: flex-start;
                display: flex;
                flex-wrap: wrap;
                margin: -8px 0 0 -8px;
            }

            .kt-wrapper-row__child {
                margin: 8px 0 0 8px;
            }

            @media screen and (max-width: 767px) {
                .kt-post-card__features>i.kt-icon-chat-bubble:before {
                    content: "\e927";
                }
            }

            .kt-image-block {
                display: block;
                overflow: hidden;
                position: relative;
                width: 100%;
            }

            .kt-image-block--radius-sm {
                border-radius: 4px;
            }

            .kt-image-block__image {
                display: block;
                height: 100%;
                left: 0;
                object-fit: cover;
                position: absolute;
                top: 0;
                width: 100%;
            }

            .kt-page-title {
                display: flex;
                flex-wrap: wrap;
            }

            .kt-page-title__texts {
                flex: 1 1;
                order: 1;
            }

            .kt-page-title__title {
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
                font-size: 1.25rem;
                font-weight: 500;
                -webkit-hyphens: auto;
                hyphens: auto;
                line-height: 1.5;
                margin: 0;
                overflow-wrap: anywhere;
            }

            @media screen and (min-width: 768px) {
                .kt-page-title__title--responsive-sized {
                    font-size: 1.5rem;
                }
            }

            .kt-page-title__tags {
                display: flex;
                flex-wrap: wrap;
                margin: -16px 0 16px -8px;
                order: 3;
                padding: 0;
                width: calc(100% + 8px);
            }

            .kt-group-row {
                direction: rtl;
                display: flex;
                flex-flow: column wrap;
                padding: 16px 0;
            }

            .kt-group-row__header {
                width: 100%;
            }

            .kt-group-row__heading {
                align-items: flex-end;
                display: flex;
                white-space: nowrap;
            }

            .kt-group-row__data-row {
                align-items: flex-start;
                display: flex;
                white-space: nowrap;
            }

            .kt-group-row-item {
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
                display: flex;
                flex-basis: 33.33333%;
                flex-direction: column;
                flex-grow: 1;
                overflow: hidden;
                padding: 0;
                position: relative;
                text-align: center;
            }

            .kt-group-row-item__header {
                box-sizing: content-box;
            }

            .kt-group-row-item__header:not(:first-child):not(:nth-child(3n+1)):before {
                border-left: 1px solid #e4e4e7;
                border-left: 1px solid rgb(var(--border-neutral-weaker));
                bottom: 0;
                content: "";
                height: 20px;
                position: absolute;
                right: 0;
            }

            .kt-group-row-item__value {
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: break-spaces;
            }

            .kt-group-row-item__value:not(:first-child):not(:nth-child(3n+1)):before {
                border-left: 1px solid #e4e4e7;
                border-left: 1px solid rgb(var(--border-neutral-weaker));
                content: "";
                height: 20px;
                position: absolute;
                right: 0;
                top: 0;
            }

            .kt-group-row-item__title {
                color: #71717a;
                color: rgb(var(--content-neutral-default));
                overflow: hidden;
                padding-bottom: 4px;
                text-overflow: ellipsis;
            }

            .kt-group-row-item__icon {
                font-weight: 400;
                margin: auto;
                padding-bottom: 4px;
                width: 100%;
            }

            .kt-group-row-item--info-row {
                font-size: 1.125rem;
                font-weight: 500;
                line-height: 1.5;
            }

            .kt-dropdown-button {
                align-items: center;
                background-color: #3f3f46;
                background-color: rgb(var(--surface-inverted-default));
                border: 1px solid transparent;
                border-radius: 4px;
                box-sizing: border-box;
                color: #fff;
                color: rgb(var(--content-neutral-on-color));
                cursor: pointer;
                display: inline-flex;
                font-size: 1rem;
                font-weight: 500;
                height: 2.5rem;
                justify-content: center;
                justify-content: space-between;
                min-width: auto;
                outline: none;
                overflow: hidden;
                padding: 0 16px 0 0;
                transition: color .36s ease,background-color .36s ease,box-shadow .36s ease,border-color .36s ease,transform .36s ease;
            }

            .kt-dropdown-button:focus,.kt-dropdown-button:hover {
                background-color: #52525b;
                background-color: rgb(var(--surface-inverted-weak));
            }

            .kt-dropdown-button:active {
                background-color: #2a2a30;
                background-color: rgb(var(--surface-inverted-strong));
            }

            .kt-dropdown-button:disabled {
                background-color: #c3c3c9;
                background-color: rgb(var(--surface-neutral-strong));
                box-shadow: none;
                color: #71717a;
                color: rgb(var(--content-neutral-default));
                cursor: not-allowed;
            }

            .kt-dropdown-button:disabled:focus,.kt-dropdown-button:disabled:hover {
                background-color: #c3c3c9;
                background-color: rgb(var(--surface-neutral-strong));
                box-shadow: none;
                transform: none;
            }

            .kt-dropdown-button:disabled:active {
                background-color: #c3c3c9;
                background-color: rgb(var(--surface-neutral-strong));
            }

            .kt-dropdown-button--inlined {
                background-color: transparent;
                color: #71717a;
                color: rgb(var(--content-neutral-default));
            }

            .kt-dropdown-button--inlined:focus,.kt-dropdown-button--inlined:hover {
                background-color: #f4f4f5;
                background-color: rgb(var(--surface-neutral-weak));
            }

            .kt-dropdown-button--inlined:active {
                background-color: #e4e4e7;
                background-color: rgb(var(--surface-neutral-default));
            }

            .kt-dropdown-button--inlined:disabled {
                background-color: transparent;
                color: #a1a1aa;
                color: rgb(var(--content-neutral-weak));
            }

            .kt-dropdown-button--inlined:disabled:active,.kt-dropdown-button--inlined:disabled:focus,.kt-dropdown-button--inlined:disabled:hover {
                background-color: transparent;
            }

            .kt-dropdown-button--inlined:disabled:focus,.kt-dropdown-button--inlined:disabled:hover {
                color: #a1a1aa;
                color: rgb(var(--content-neutral-weak));
            }

            .kt-dropdown-button--inlined:focus,.kt-dropdown-button--inlined:hover {
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
            }

            .kt-dropdown-button--inlined:focus:disabled,.kt-dropdown-button--inlined:hover:disabled {
                color: #a1a1aa;
                color: rgb(var(--content-neutral-weak));
            }

            .kt-dropdown-button--inlined {
                color: #71717a;
                color: rgb(var(--content-neutral-default));
            }

            .kt-dropdown-button__arrow-icon {
                display: block;
                margin-left: 11px;
                margin-right: 8px;
                transform-origin: center;
                transition: transform .24s ease;
                will-change: transform;
            }

            .kt-dropdown-button:focus .kt-dropdown-button__arrow-icon {
                transform: rotate(180deg);
            }

            .kt-dropdown-button:focus .kt-dropdown-button__arrow-icon--closed,.kt-dropdown-button__arrow-icon--closed {
                transform: none;
            }

            .kt-dropdown-button--medium {
                font-size: .875rem;
            }

            .kt-chip {
                align-items: center;
                background-color: #f4f4f5;
                background-color: rgb(var(--surface-neutral-weak));
                border: none;
                border-radius: 2px;
                display: inline-flex;
                font-size: .875rem;
                font-weight: 400;
                height: 2rem;
                outline: none;
                padding: 0 12px;
                transition: background-color .36s ease;
            }

            .kt-chip:focus,.kt-chip:hover {
                background-color: #e4e4e7;
                background-color: rgb(var(--surface-neutral-default));
            }

            .kt-chip:active {
                background-color: #c3c3c9;
                background-color: rgb(var(--surface-neutral-strong));
            }

            .kt-chip.kt-chip {
                color: #71717a;
                color: rgb(var(--content-neutral-default));
            }

            .kt-chip--small {
                font-size: .75rem;
                height: 1.75rem;
            }

            .kt-chip--rounded {
                border-radius: 16px;
            }

            .kt-chip--outlined {
                background-color: transparent;
                border: 1px solid #c3c3c9;
                border: 1px solid rgb(var(--border-neutral-weak));
            }

            .kt-chip--outlined:focus,.kt-chip--outlined:hover {
                background-color: #f4f4f5;
                background-color: rgb(var(--surface-neutral-weak));
            }

            .kt-chip--outlined:active {
                background-color: #e4e4e7;
                background-color: rgb(var(--surface-neutral-default));
            }

            .kt-chip--has-action {
                cursor: pointer;
            }

            .kt-snackbar-container {
                height: 100%;
                left: 0;
                pointer-events: none;
                position: fixed;
                top: 0;
                width: 100%;
                z-index: 1070;
            }

            .kt-dropdown-menu {
                display: inline-block;
                position: relative;
            }

            .kt-nav-button {
                font-size: .875rem;
                line-height: 2;
                min-width: unset;
            }

            .kt-nav-button--small {
                font-size: .75rem;
            }

            .kt-visually-hidden {
                word-wrap: normal;
                clip: rect(0 0 0 0);
                border: 0;
                height: 1px;
                margin: -1px;
                overflow: hidden;
                padding: 0;
                position: absolute;
                white-space: nowrap;
                width: 1px;
            }

            .kt-nav-text-field {
                background-color: #f4f4f5;
                background-color: rgb(var(--surface-neutral-weak));
                border-radius: 4px;
                position: relative;
                transition-duration: .36s;
                transition-property: background-color,box-shadow;
            }

            .kt-nav-text-field__field {
                align-items: center;
                display: flex;
                gap: 8px;
                height: 40px;
                padding: 0 8px;
            }

            .kt-nav-text-field__icon {
                color: #a1a1aa;
                color: rgb(var(--content-neutral-weak));
                transition: color .36s;
            }

            .kt-nav-text-field__input {
                background-color: transparent;
                border: none;
                border-radius: 4px;
                box-sizing: border-box;
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
                flex: 1 1;
                font-size: .875rem;
                outline: 0;
                transition: color .36s;
            }

            .kt-nav-text-field__input::-webkit-input-placeholder {
                color: #71717a;
                color: rgb(var(--content-neutral-default));
            }

            .kt-nav-text-field__input::placeholder {
                color: #71717a;
                color: rgb(var(--content-neutral-default));
            }

            .kt-nav-text-field__dropdown {
                display: none;
                width: 100%;
            }

            .kt-nav-text-field:hover .kt-nav-text-field__icon {
                color: #71717a;
                color: rgb(var(--content-neutral-default));
            }

            .kt-new-modal {
                background-color: #fff;
                background-color: rgb(var(--surface-neutral-weaker));
                border-radius: 4px;
                display: flex;
                flex-direction: column;
                position: relative;
            }

            .kt-new-modal--default,.kt-new-modal--stickyfooter {
                max-height: 656px;
                min-height: 232px;
                width: 488px;
            }

            @media screen and (max-width: 520px) {
                .kt-new-modal--default,.kt-new-modal--stickyfooter {
                    height: 100%;
                    margin: 0;
                    min-height: 100%;
                    width: 100%;
                }
            }

            .kt-new-modal__header {
                display: flex;
                flex-direction: column;
                padding: 8px 24px;
            }

            @media screen and (max-width: 520px) {
                .kt-new-modal__header {
                    padding: 8px 16px;
                }
            }

            .kt-new-modal__header--has-divider {
                box-shadow: 0 1px 2px 0 #e4e4e7;
                box-shadow: 0 1px 2px 0 rgb(var(--border-neutral-weaker));
            }

            .kt-new-modal__title {
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
                font-size: 1rem;
                font-weight: 400;
                margin: 0;
            }

            .kt-new-modal__title-box {
                align-items: center;
                display: flex;
                justify-content: space-between;
                min-height: 56px;
            }

            .kt-new-modal__body {
                overflow-y: auto;
                padding: 8px 24px 24px;
            }

            .kt-new-modal__body::-webkit-scrollbar {
                height: 12px;
                width: 12px;
            }

            .kt-new-modal__body::-webkit-scrollbar-thumb {
                background-clip: padding-box;
                background-color: #c3c3c9;
                background-color: rgb(var(--border-neutral-weak));
                border: 4px solid transparent;
                border-radius: 12px;
            }

            .kt-new-modal__body::-webkit-scrollbar-thumb:hover {
                background-color: #a1a1aa;
                background-color: rgb(var(--border-neutral-default));
            }

            .kt-new-modal__body--consider-sticky-footer {
                margin-bottom: 72px;
            }

            @media screen and (max-width: 520px) {
                .kt-new-modal__body {
                    padding: 8px 16px 24px;
                }
            }

            .kt-new-modal__footer {
                background-color: #fff;
                background-color: rgb(var(--surface-neutral-weaker));
                border-radius: 0 0 4px 4px;
                bottom: 0;
                box-shadow: 0 -1px 2px 0 #e4e4e7;
                box-shadow: 0 -1px 2px 0 rgb(var(--border-neutral-weaker));
                padding: 16px;
                position: absolute;
                width: 100%;
            }

            .kt-new-modal__close-button {
                margin-left: -8px;
            }

            @media screen and (max-width: 520px) {
                .kt-new-modal {
                    border-radius: 0;
                }
            }

            .kt-base-carousel__button {
                border: none;
                cursor: pointer;
            }

            .kt-base-carousel__fullscreen-control {
                bottom: 16px;
                left: 16px;
                position: absolute;
            }

            .kt-base-carousel__thumbnails {
                direction: rtl;
                margin-top: 16px;
                overflow: hidden;
            }

            .kt-base-carousel__slides {
                width: 100%;
            }

            .kt-base-carousel__slide-loading-overlay {
                background-color: rgba(0,0,0,32%);
                background-color: rgba(var(--surface-dimmer-neutral-default),var(--surface-dimmer-neutral-opacity-darker));
                height: 100%;
                left: 0;
                opacity: 0;
                pointer-events: none;
                position: absolute;
                top: 0;
                transition: opacity .36s ease;
                width: 100%;
            }

            .kt-base-carousel__figure {
                height: 100%;
                margin: 0;
                pointer-events: auto;
            }

            .kt-carousel--rounded .keen-slider {
                border-radius: 4px;
            }

            .kt-carousel__thumbnails {
                display: none;
            }

            @media screen and (min-width: 960px) {
                .kt-carousel__thumbnails {
                    display: flex;
                }
            }

            .kt-caret {
                align-items: center;
                display: flex;
                height: 1.5rem;
                justify-content: center;
                width: 1.5rem;
            }

            .kt-caret__handle {
                align-items: center;
                display: flex;
                height: 100%;
                overflow: hidden;
                width: 50%;
            }

            .kt-caret__handle:before {
                background-color: #a1a1aa;
                background-color: rgb(var(--content-neutral-weak));
                border-radius: 1px;
                content: "";
                height: 2px;
                transition: transform .32s cubic-bezier(.4,0,.2,1) 0ms;
                width: .5rem;
            }

            .kt-caret__right-handle:before {
                transform: translateX(2px) rotate(45deg);
            }

            .kt-caret__left-handle {
                flex-direction: row-reverse;
            }

            .kt-caret__left-handle:before {
                transform: translateX(-2px) rotate(-45deg);
            }

            .kt-info-row {
                background: transparent;
                border: 0;
                border-radius: 4px;
                outline: 0;
                padding: 0;
                text-align: right;
                width: 100%;
            }

            .kt-info-row--has-content {
                cursor: pointer;
                -webkit-user-select: none;
                user-select: none;
            }

            .kt-info-row__title,.kt-info-row__value {
                font-size: inherit;
                line-height: 2;
                margin: 0;
                overflow: hidden;
                text-overflow: ellipsis;
            }

            .kt-info-row__title {
                color: #2a2a30;
                color: rgb(var(--content-neutral-stronger));
            }

            .kt-info-row__value {
                color: #71717a;
                color: rgb(var(--content-neutral-default));
            }

            .kt-info-row__content {
                padding: 8px 0 16px;
            }

            .kt-info-row__caret {
                margin: 4px 16px 0 0;
            }

            .kt-body,.kt-description-row__text {
                font-size: 1rem;
                font-weight: 400;
                line-height: 2;
            }

            .kt-body--stable {
                font-size: 1rem !important;
            }

            .kt-body--sm,.kt-description-row__text--small {
                font-size: .875rem;
            }

            @media screen and (max-width: 768px) {
                .kt-body,.kt-description-row__text {
                    font-size: .875rem;
                }
            }

            .full-width {
                width: 100%;
            }
        </style>
        <link data-chunk="main" rel="stylesheet" href="https://s100.divarcdn.com/web-assets/2026/09/vendors-pb-159.400a4952.desktop.css" onload="this.media='all';this.onload=null;" media="print">
        <link data-chunk="main" rel="stylesheet" href="https://s100.divarcdn.com/web-assets/2026/09/main-792.20fa726a.desktop.css" onload="this.media='all';this.onload=null;" media="print">
        <link data-chunk="bootstrap" rel="stylesheet" href="https://s100.divarcdn.com/web-assets/2026/09/widget-base-183.17dd2262.desktop.css" onload="this.media='all';this.onload=null;" media="print">
        <link data-chunk="bootstrap" rel="stylesheet" href="https://s100.divarcdn.com/web-assets/2026/09/bootstrap-547.0ea3018f.desktop.css" onload="this.media='all';this.onload=null;" media="print">
        <link data-chunk="PostView" rel="stylesheet" href="https://s100.divarcdn.com/web-assets/2026/09/postview-782.89280520.desktop.css" onload="this.media='all';this.onload=null;" media="print">
        <noscript>
            <link data-chunk="main" rel="stylesheet" href="https://s100.divarcdn.com/web-assets/2026/09/vendors-pb-159.400a4952.desktop.css">
            <link data-chunk="main" rel="stylesheet" href="https://s100.divarcdn.com/web-assets/2026/09/main-792.20fa726a.desktop.css">
            <link data-chunk="bootstrap" rel="stylesheet" href="https://s100.divarcdn.com/web-assets/2026/09/widget-base-183.17dd2262.desktop.css">
            <link data-chunk="bootstrap" rel="stylesheet" href="https://s100.divarcdn.com/web-assets/2026/09/bootstrap-547.0ea3018f.desktop.css">
            <link data-chunk="PostView" rel="stylesheet" href="https://s100.divarcdn.com/web-assets/2026/09/postview-782.89280520.desktop.css">
        </noscript>
        <style>
            .connection-banner-b55d2 {
                position: sticky;
                top: 0;
                z-index: 1040;
                display: flex;
                align-items: center;
                justify-content: center;
                width: 100%;
                height: 0;
                color: rgb(var(--content-neutral-on-color));
                font-size: .75rem;
                background-color: rgb(var(--surface-informative-strong));
                transition: height .24s ease-in-out
            }

            .connection-banner__show-d8f73 {
                height: 32px
            }

            .connection-banner__icon-cfe92 {
                margin-left: 8px
            }

            .connection-banner__offline-c277c {
                background-color: rgb(var(--surface-inverted-default))
            }

            .connection-banner__back-online-ff637 {
                font-weight: 400
            }

            .modal-fbeee {
                display: flex;
                flex-direction: column;
                align-items: center;
                height: 100%;
                padding-top: 8px;
                text-align: center
            }

            .modal__divar-logo-a605b {
                display: block;
                margin: 0 auto 16px
            }

            .modal__top-d5d3b,.modal__bottom-a8837 {
                padding: 0 16px
            }

            .modal__bottom-a8837 {
                align-self: flex-start;
                text-align: initial
            }

            .modal__add-f631a {
                color: rgb(var(--content-informative-default))
            }

            .modal--bold-text-f3d95 {
                font-weight: 500
            }

            .modal__close-button-eadb9 {
                margin-right: auto
            }

            .error-f9466 {
                padding-top: 48px;
                text-align: center
            }

            .shell--with-islands-header-c4631 {
                padding-top: 56px
            }

            .nav-bar-c7698 {
                position: sticky;
                top: 0;
                z-index: 1040;
                display: flex;
                align-items: center;
                width: 100%;
                height: 64px;
                transition: top .24s ease-in-out
            }

            .nav-bar--with-connection-banner-b70a2 {
                top: 32px
            }

            .nav-bar-c7698 {
                justify-content: center;
                background: rgb(var(--surface-neutral-weaker));
                box-shadow: 0 4px 8px rgba(0,0,0,.08)
            }

            [data-theme=dark] .nav-bar-c7698 {
                box-shadow: 0 8px 16px rgba(0,0,0,.16)
            }

            .nav-bar__content-d23b1 {
                display: flex;
                flex-grow: 1;
                align-items: center;
                max-width: 1440px;
                padding: 0 16px
            }

            .nav-bar__end-section-dabb8 {
                display: flex;
                align-items: center;
                margin-right: auto
            }

            .nav-bar__submit-btn-fbb11 {
                margin-right: 16px
            }

            .nav-bar--dimmer-active-d3758 {
                z-index: 1080
            }

            .nav-bar--dimmer-active-d3758::before {
                position: absolute;
                top: 0;
                left: 100%;
                width: 15px;
                height: 100%;
                background-color: rgb(var(--surface-neutral-weaker));
                content: ""
            }

            .nav-bar__search-container-ac88f {
                flex: 1;
                max-width: 480px;
                height: 40px;
                margin-left: 8px
            }

            .nav-bar__category-mega-box-ad06f {
                position: relative;
                display: flex;
                flex-grow: 1;
                align-items: center;
                margin-right: 16px
            }

            .nav-bar__city-button-fb19d {
                flex-shrink: 0
            }

            [data-hidden-overflow-side=left] .nav-bar--dimmer-active-d3758::before {
                right: 100%;
                left: unset
            }

            .logo-e3eeb {
                margin-left: 8px;
                vertical-align: middle
            }

            .select-city-button-d4d79 {
                max-width: 170px;
                overflow: hidden;
                text-overflow: ellipsis
            }

            .dropdown-bfba4.dropdown-bfba4 {
                position: static;
                margin-left: 8px
            }

            .dropdown__cats-button--open-c842d.dropdown__cats-button--open-c842d {
                color: rgb(var(--content-neutral-stronger))
            }

            .dropdown__menu-bcdab.dropdown__menu-bcdab {
                position: absolute;
                top: 100%;
                right: 0;
                left: 0;
                display: flex;
                flex-direction: row;
                width: 100%;
                min-height: 496px;
                max-height: 520px;
                margin-top: 4px;
                padding: 32px;
                background-color: rgb(var(--surface-neutral-weaker))
            }

            .description-a64e0.description-a64e0 {
                margin-bottom: 48px
            }

            .bookmark-icon-caca4 {
                animation: preloader-c41f0 .2s ease alternate
            }

            .bookmark-icon--loading-a2282 {
                transform: scale(0.9);
                transition: transform .2s
            }

            @keyframes preloader-c41f0 {
                100% {
                    transform: scale(1.1)
                }
            }

            .form-a9d32 {
                display: flex;
                flex-grow: 1
            }

            .form-a9d32 {
                height: 100%
            }

            .dropdown-dc2a5 {
                max-height: 528px;
                overflow-y: auto
            }

            .empty-list-a2fa9 {
                display: flex;
                justify-content: center
            }

            .progressible-content-e2c95 {
                width: 100%;
                height: 100%
            }

            .progressible-content__progress-a7872 {
                padding: 32px 0
            }

            .progressible-content__full-page-d920f {
                position: fixed;
                top: 0;
                left: 0
            }

            .queries-b4dfc {
                padding: 0 16px 16px
            }

            .queries__title-ccabe {
                margin: 16px 0;
                color: rgb(var(--content-neutral-default));
                font-size: .875rem;
                line-height: 1.75
            }

            .queries__items-bee00 {
                display: flex;
                flex-wrap: wrap;
                gap: 8px
            }

            .queries__item-c3381 {
                cursor: pointer
            }

            .widget-based-afad6 {
                width: 250px;
                padding: 0 16px;
                background-color: rgb(var(--surface-neutral-weaker))
            }

            .button-f32f0:not(:first-child) {
                margin-right: 8px
            }

            .indicator-c6af3 {
                position: absolute;
                top: 1px;
                right: 3px
            }

            .container--has-footer-d86a9 {
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                min-height: calc(100vh - 64px)
            }

            .a11y-menu__container-eac90 {
                position: fixed;
                top: 80px;
                right: 0;
                display: flex;
                flex-direction: column;
                padding: 12px 12px 0;
                transform: translateX(100%);
                z-index: 1000;
                background-color: rgb(var(--surface-neutral-weak));
                border-radius: 4px;
                box-shadow: 0px 8px 12px 0px rgba(0,0,0,.16)
            }

            .a11y-menu__container-eac90 .kt-divider-daf66 {
                background-color: rgb(var(--border-neutral-weak))
            }

            [data-theme=light] .a11y-menu__container-eac90 {
                background-color: rgb(var(--surface-neutral-weaker))
            }

            [data-theme=light] .a11y-menu__container-eac90 .kt-divider-daf66 {
                background-color: rgb(var(--border-neutral-weaker))
            }

            .a11y-menu__container--focused-f4642 {
                transform: translateX(-16px) !important
            }

            .a11y-menu__item-b4ea4 {
                margin-bottom: 12px;
                padding: 10px 16px;
                color: rgb(var(--content-neutral-default));
                font-weight: 500;
                font-size: .875rem;
                line-height: 2;
                background-color: rgb(var(--surface-neutral-weak));
                border: none;
                border-radius: 4px;
                cursor: pointer
            }

            .raw-button-cd669 {
                cursor: pointer
            }

            .plain-f1b00,button.plain-f1b00,.plain-f1b00[type],.plain-f1b00[role=button] {
                width: auto;
                margin: 0;
                padding: 0;
                overflow: visible;
                color: inherit;
                font: inherit;
                line-height: normal;
                text-align: inherit;
                background: transparent;
                border: none;
                border-radius: 0;
                -webkit-appearance: none;
                appearance: none;
                -webkit-font-smoothing: inherit;
                -moz-osx-font-smoothing: inherit
            }

            .plain-f1b00:-moz-focusring,button.plain-f1b00:-moz-focusring,.plain-f1b00[type]:-moz-focusring,.plain-f1b00[role=button]:-moz-focusring {
                outline: auto
            }

            .disabled-efff4,button.disabled-efff4,button[disabled].disabled-efff4,.disabled-efff4[disabled][role=button] {
                color: rgb(var(--content-neutral-weak));
                box-shadow: none;
                cursor: not-allowed
            }

            .disabled-efff4:hover,.disabled-efff4:focus,button.disabled-efff4:hover,button.disabled-efff4:focus,button[disabled].disabled-efff4:hover,button[disabled].disabled-efff4:focus,.disabled-efff4[disabled][role=button]:hover,.disabled-efff4[disabled][role=button]:focus {
                background-color: transparent;
                box-shadow: none;
                transform: none
            }

            .footer-fcc34 {
                z-index: 1
            }

            .link-df015 {
                margin-left: 16px
            }

            .links-container-d7e32 {
                display: flex;
                align-items: center;
                justify-content: center
            }

            .container-e7eb4 {
                display: flex;
                flex-wrap: wrap;
                align-items: center;
                justify-content: center;
                padding: 16px 0;
                font-size: .625rem;
                line-height: 2
            }

            .container-e7eb4 {
                margin-top: 128px
            }

            .logo-c189b {
                margin-left: 32px
            }

            .styled-link-d9633 {
                color: rgb(var(--content-neutral-weak));
                font-size: .75rem;
                white-space: nowrap;
                transition: 360ms ease color
            }

            .styled-link-d9633:hover {
                color: rgb(var(--content-neutral-stronger))
            }

            .links-dc796 {
                display: flex;
                align-items: center
            }

            .link-c8a3f {
                margin-right: 16px
            }

            .container-a30c5 {
                margin-top: 64px
            }

            @media screen and (min-width: 768px) {
                .modal-a5925 {
                    height:41rem
                }
            }

            .title-a774e.title-a774e {
                font-weight: 500;
                font-size: 1.125rem
            }

            .title-box-e8244 {
                min-height: unset;
                margin-top: -6px;
                margin-bottom: 8px
            }

            .header-a5d43 {
                padding: 16px;
                box-shadow: 0 1px 2px 0 rgb(var(--border-neutral-weak))
            }

            @media screen and (min-width: 520px) {
                .header-a5d43 {
                    padding:32px 32px 16px
                }
            }

            .body-b56d9.body-b56d9 {
                display: flex;
                flex-direction: column;
                height: 100%;
                margin-bottom: 4rem;
                padding: 0 16px
            }

            @media screen and (min-width: 520px) {
                .body-b56d9.body-b56d9 {
                    padding:8px 32px 0 24px
                }
            }

            .body--map-c5571.body--map-c5571 {
                padding: 0
            }

            .footer-aafd0 {
                z-index: 2;
                padding: 12px 16px
            }

            @media screen and (min-width: 520px) {
                .modal-f9b93 {
                    width:420px
                }
            }

            @media screen and (min-width: 520px) {
                .submit-e2088 {
                    flex:0 0 auto
                }
            }

            .submit-modal__body-fc3be.submit-modal__body-fc3be {
                padding-top: 24px
            }

            .ios-installation-banner-d199c {
                position: fixed;
                bottom: 0;
                display: flex;
                align-items: center;
                width: 100%;
                height: 80px;
                padding: 8px;
                background-color: rgb(var(--surface-neutral-weaker));
                border-radius: 16px 16px 0 0
            }

            .ios-installation-banner__close-icon-bc55a {
                margin-left: 8px
            }

            .ios-installation-banner__right-ecd92 {
                display: flex;
                flex: 1;
                align-items: center
            }

            .ios-installation-banner__app-logo-d3ba6 {
                margin-left: 10px;
                border: 1px solid rgb(var(--border-neutral-weaker));
                border-radius: 16px
            }

            .ios-installation-banner__title-fc8ce {
                margin: 0;
                color: rgb(var(--content-neutral-stronger));
                font-weight: 500;
                font-size: .75rem
            }

            .ios-installation-banner__subtitle-d0a5a {
                margin: 0;
                color: rgb(var(--content-neutral-default));
                font-size: .625rem
            }

            .ios-installation-banner__left-cfd5b {
                margin-left: 8px;
                padding: 8px 12px;
                color: rgb(var(--content-neutral-stronger));
                font-weight: 500;
                font-size: .875rem;
                border: 1px solid rgb(var(--content-neutral-stronger));
                border-radius: 4px
            }

            .header-c7b11 {
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 8px 0
            }

            .body-e6802 {
                display: flex;
                flex-direction: column;
                padding: 16px 0
            }

            .header-d4c4e {
                position: relative
            }

            .header-d4c4e .title-c8bc7 {
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100%;
                margin: 0;
                color: rgb(var(--content-neutral-strong));
                font-size: .875rem
            }

            .body-a11ad {
                margin-bottom: 8px;
                overflow-x: hidden
            }
        </style>
        <script data-react-helmet="true" type="application/ld+json">
            {
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "item": {
                            "@id": "https://divar.ir",
                            "name": "دیوار"
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "item": {
                            "@id": "https://divar.ir/s/tehran",
                            "name": "1"
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "item": {
                            "@id": "https://divar.ir/s/tehran/yousef-abad",
                            "name": "یوسف‌آباد"
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 4,
                        "item": {
                            "@id": "https://divar.ir/s/tehran/real-estate/yousef-abad",
                            "name": "املاک"
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 5,
                        "item": {
                            "@id": "https://divar.ir/s/tehran/buy-residential/yousef-abad",
                            "name": "فروش مسکونی"
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 6,
                        "item": {
                            "@id": "https://divar.ir/s/tehran/buy-apartment/yousef-abad",
                            "name": "فروش آپارتمان"
                        }
                    },
                    {
                        "@type": "ListItem",
                        "position": 7,
                        "item": {
                            "@id": "https://divar.ir/v/%DB%B9%DB%B7-%D9%85%D8%AA%D8%B1-%DB%B2-%D8%AE%D9%88%D8%A7%D8%A8-%D8%AF%D9%88%D9%86%D8%A8%D8%B4-%D8%AF%DB%8C%D8%AF-%D8%A7%D8%A8%D8%AF%DB%8C/gap5-Twe",
                            "name": "فروش ۹۷ متر ۲ خواب دونبش __ دید ابدی در تهران - ۲۱ شهریور ۱۴۰۵"
                        }
                    }
                ],
                "@context": "http://schema.org",
                "@type": "BreadcrumbList"
            }</script>
        <script>
            (function(w, d, s, l, i) {
                w[l] = w[l] || [];
                w[l].push({
                    'gtm.start': new Date().getTime(),
                    event: 'gtm.js'
                });
                var f = d.getElementsByTagName(s)[0]
                  , j = d.createElement(s)
                  , dl = l != 'dataLayer' ? '&l=' + l : '';
                j.defer = true;
                j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
                f.parentNode.insertBefore(j, f);
            }
            )(window, document, 'script', 'dataLayer', 'GTM-NGGBSR3');
        </script>
    </head>
    <body dir="rtl">
        <noscript>
            <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NGGBSR3" height="0" width="0" style="display:none;visibility:hidden"></iframe>
        </noscript>
        <div id=app>
            <div class="kt-dimmer kt-dimmer--dark" data-testid="dimmer">
                <div data-testid="focus-lock-container" class="kt-dimmer__content">
                    <div class="kt-visually-hidden fallback-focus-class" tabindex="-1" data-testid="focus-lock-visually-hidden-element"></div>
                    <section data-testid="new-modal-section" role="dialog" class="kt-new-modal kt-new-modal--stickyfooter">
                        <header class="kt-new-modal__header kt-new-modal__header--has-divider">
                            <div class="kt-new-modal__title-box">
                                <button class="kt-button kt-button--inlined kt-button--circular kt-new-modal__close-button modal__close-button-eadb9" type="button" tabindex="0" data-testid="new-modal-close-button" aria-label="بستن">
                                    <i class="kt-icon kt-icon-close kt-button__icon no-pointer-event" data-testid="icon" data-icon="close"></i>
                                </button>
                            </div>
                        </header>
                        <div data-testid="body" class="kt-new-modal__body kt-new-modal__body--consider-sticky-footer">
                            <div class="modal-fbeee">
                                <div class="modal__top-d5d3b">
                                    <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0ibm9uZSI+PHBhdGggZmlsbD0iI0E2MjYyNiIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNOC4zODYgMTQuNjE3SDguMjhhLjcxMi43MTIgMCAwIDEtLjU5NS0uODA2Yy40NzMtMy4xMTcuNjMtOC4wOTIuNjMtOC4xMjcuMDM1LS4zODYuMzMzLS43LjczNi0uNjgzYS43MTUuNzE1IDAgMCAxIC42ODMuNzE4YzAgLjIxLS4xNzUgNS4wOTctLjY0OCA4LjMwM2EuNy43IDAgMCAxLS43LjU5NVptMTAuMDM3IDEuMjk2YS42OTMuNjkzIDAgMCAxLS42NjYtLjQ5LjY4OC42ODggMCAwIDEgLjQ1NS0uODc2YzMuMzEtMS4wNSAzLjM2My0xLjg1NyAzLjM4MS0yLjI5NS4wMzUtLjY4My0uNDktMS41NTgtLjctMS44NTZhLjcwMS43MDEgMCAxIDEgMS4xMzgtLjgyNGMuMTA1LjE0IDEuMDUgMS40NTQuOTYzIDIuNzY4LS4wODcgMS41OTQtMS4zMTQgMi41NzUtNC4zNjEgMy41NTZhLjg0NS44NDUgMCAwIDAtLjEwNS4wMDljLS4wMzUuMDA0LS4wNy4wMDktLjEwNS4wMDlabS05LjUxMiAyLjQ3YS42NTYuNjU2IDAgMCAxLS41NDMtLjI2Mi42ODMuNjgzIDAgMCAxIC4xMjMtLjk4MWMxLjQzNi0xLjEzOSAyLjQtMi4xNTUgMy4wMy0zLjA0OC0uMzUtLjE3NS0uNzE4LS40MzgtLjkxLS44NzYtLjE3Ni0uNDAzLS4yODEtMS4wNjkuMzMyLTEuOTYyLjg3Ni0xLjI5NiAxLjc1Mi0xLjU5NCAyLjA4NC0xLjY2NGEuODcxLjg3MSAwIDAgMSAxLjAxNi42MTNjLjA4OC4zMTUuMjk4IDEuMzE0LS4zMzIgMi44MzguODQtLjAxOCAxLjUwNi0uMjQ1IDIuMDE0LS42NjYuOTgtLjc4OCAxLjAzMy0yLjEyIDEuMDMzLTIuMTM3YS43MTUuNzE1IDAgMCAxIC43MTktLjY4My43MTUuNzE1IDAgMCAxIC42ODMuNzE4YzAgLjA3LS4wNyAxLjk0NC0xLjUyNCAzLjE3LS45MTEuNzcxLTIuMTU1IDEuMTA0LTMuNjYxLjk4Mi0uNzE4IDEuMTAzLTEuODU3IDIuNC0zLjYyNiAzLjhhLjcwOC43MDggMCAwIDEtLjQzOC4xNThabTMuODAxLTcuMDc2YTMuMTM0IDMuMTM0IDAgMCAwLS42My43MzVjLS4yMjguMzUtLjI0Ni41NDMtLjIyOC41OTYuMDM1LjA4OC4yMS4xNzUuMzg1LjI0NS4zMzMtLjY2NS40MzgtMS4xOTEuNDczLTEuNTc2Wm0uMTc1IDQuOTIyYS43MS43MSAwIDAgMCAuNy42ODNoLjAzNmMuMDUzIDAgMS4yMjYtLjAzNSAyLjkwOC0uNDJhLjcwMi43MDIgMCAwIDAgLjU0My0uODQxLjcwMi43MDIgMCAwIDAtLjg0MS0uNTQzYy0xLjU2LjMzMi0yLjY2My4zODUtMi42OC4zODVhLjcwNC43MDQgMCAwIDAtLjY2Ni43MzZaTTEuMTM0IDE4LjEwM2MuMTIyLjE3NS4zNS4yOC41Ni4yOC4xNCAwIC4yOC0uMDM1LjQyLS4xMjIgNC40NS0zLjI0IDQuNjI1LTcuNDggNC42MjUtNy42NTUgMC0uMzg1LS4yOTgtLjctLjY4My0uNzE4LS4zODYtLjAxOC0uNy4yOTgtLjcxOC42ODMgMCAuMTQtLjE3NiAzLjczMS00LjA0NyA2LjU1MWEuNzAxLjcwMSAwIDAgMC0uMTU3Ljk4MVoiIGNsaXAtcnVsZT0iZXZlbm9kZCIvPjwvc3ZnPg==" alt="نشان دیوار" width="64" height="64" class="modal__divar-logo-a605b"/>
                                    <div class="kt-base-row kt-base-row--large kt-description-row kt-description-row--padded">
                                        <div class="kt-base-row__start">
                                            <p class="kt-description-row__text kt-description-row__text--primary">وب‌اپلیکیشن یا PWA دیوار سرویسی است که نصب آن، استفاده از دیوار را بدون نیاز به دانلود اپلیکیشن و به‌روز‌رسانی و تنها با کلیک روی آیکون آن فراهم می‌کند. در نسخهٔ وب‌اپلیکیشن نیازی به دانلود و به‌روزرسانی نیست و کاربران iOS و اندروید با دسترسی‌ به آیکون اپلیکیشن در کنار سایر اپ‌های موبایل خود می‌توانند از آن استفاده کنند.</p>
                                        </div>
                                    </div>
                                </div>
                                <hr data-testid="divider" class="kt-divider kt-divider--padded kt-divider--default" role="presentation"/>
                                <div class="modal__bottom-a8837">
                                    <div class="kt-base-row kt-base-row--large kt-description-row kt-description-row--padded">
                                        <div class="kt-base-row__start">
                                            <p class="kt-description-row__text kt-description-row__text--primary">
                                                ۱. در نوار پایین روی دکمهٔ <i class="kt-icon kt-icon-share-o" style="color:rgb(var(--content-informative-default))" data-testid="icon" aria-label="اشتراک‌گذاری" data-icon="share-o"></i>
                                                <span class="modal--bold-text-f3d95">share</span>
                                                بزنید.
                                            </p>
                                        </div>
                                    </div>
                                    <div class="kt-base-row kt-base-row--large kt-description-row">
                                        <div class="kt-base-row__start">
                                            <p class="kt-description-row__text kt-description-row__text--primary">
                                                ۲. در منوی باز شده، گزینهٔ <i class="kt-icon kt-icon-added-o" style="color:rgb(var(--content-informative-default))" data-testid="icon" aria-label="اضافه کردن به صفحهٔ اصلی" data-icon="added-o"></i>
                                                <span class="modal--bold-text-f3d95">Add to home screen</span>
                                                را انتخاب کنید.
                                            </p>
                                        </div>
                                    </div>
                                    <div class="kt-base-row kt-base-row--large kt-description-row kt-description-row--padded">
                                        <div class="kt-base-row__start">
                                            <p class="kt-description-row__text kt-description-row__text--primary">
                                                ۳. در قسمت بالا روی دکمهٔ <span class="modal__add-f631a">Add</span>
                                                بزنید.
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <footer class="kt-new-modal__footer">
                            <div class="kt-button-row kt-button-row--responsive">
                                <button class="kt-button kt-button--primary" type="button" tabindex="0">
                                    <span class="kt-text-truncate no-pointer-event">متوجه شدم</span>
                                </button>
                            </div>
                        </footer>
                    </section>
                </div>
            </div>
            <header class="nav-bar-c7698">
                <div id="skip-to-content-container"></div>
                <nav class="nav-bar__content-d23b1" aria-label="منو اصلی">
                    <a href="/s/tehran">
                        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0ibm9uZSI+PHBhdGggZmlsbD0iI0E2MjYyNiIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNOC4zODYgMTQuNjE3SDguMjhhLjcxMi43MTIgMCAwIDEtLjU5NS0uODA2Yy40NzMtMy4xMTcuNjMtOC4wOTIuNjMtOC4xMjcuMDM1LS4zODYuMzMzLS43LjczNi0uNjgzYS43MTUuNzE1IDAgMCAxIC42ODMuNzE4YzAgLjIxLS4xNzUgNS4wOTctLjY0OCA4LjMwM2EuNy43IDAgMCAxLS43LjU5NVptMTAuMDM3IDEuMjk2YS42OTMuNjkzIDAgMCAxLS42NjYtLjQ5LjY4OC42ODggMCAwIDEgLjQ1NS0uODc2YzMuMzEtMS4wNSAzLjM2My0xLjg1NyAzLjM4MS0yLjI5NS4wMzUtLjY4My0uNDktMS41NTgtLjctMS44NTZhLjcwMS43MDEgMCAxIDEgMS4xMzgtLjgyNGMuMTA1LjE0IDEuMDUgMS40NTQuOTYzIDIuNzY4LS4wODcgMS41OTQtMS4zMTQgMi41NzUtNC4zNjEgMy41NTZhLjg0NS44NDUgMCAwIDAtLjEwNS4wMDljLS4wMzUuMDA0LS4wNy4wMDktLjEwNS4wMDlabS05LjUxMiAyLjQ3YS42NTYuNjU2IDAgMCAxLS41NDMtLjI2Mi42ODMuNjgzIDAgMCAxIC4xMjMtLjk4MWMxLjQzNi0xLjEzOSAyLjQtMi4xNTUgMy4wMy0zLjA0OC0uMzUtLjE3NS0uNzE4LS40MzgtLjkxLS44NzYtLjE3Ni0uNDAzLS4yODEtMS4wNjkuMzMyLTEuOTYyLjg3Ni0xLjI5NiAxLjc1Mi0xLjU5NCAyLjA4NC0xLjY2NGEuODcxLjg3MSAwIDAgMSAxLjAxNi42MTNjLjA4OC4zMTUuMjk4IDEuMzE0LS4zMzIgMi44MzguODQtLjAxOCAxLjUwNi0uMjQ1IDIuMDE0LS42NjYuOTgtLjc4OCAxLjAzMy0yLjEyIDEuMDMzLTIuMTM3YS43MTUuNzE1IDAgMCAxIC43MTktLjY4My43MTUuNzE1IDAgMCAxIC42ODMuNzE4YzAgLjA3LS4wNyAxLjk0NC0xLjUyNCAzLjE3LS45MTEuNzcxLTIuMTU1IDEuMTA0LTMuNjYxLjk4Mi0uNzE4IDEuMTAzLTEuODU3IDIuNC0zLjYyNiAzLjhhLjcwOC43MDggMCAwIDEtLjQzOC4xNThabTMuODAxLTcuMDc2YTMuMTM0IDMuMTM0IDAgMCAwLS42My43MzVjLS4yMjguMzUtLjI0Ni41NDMtLjIyOC41OTYuMDM1LjA4OC4yMS4xNzUuMzg1LjI0NS4zMzMtLjY2NS40MzgtMS4xOTEuNDczLTEuNTc2Wm0uMTc1IDQuOTIyYS43MS43MSAwIDAgMCAuNy42ODNoLjAzNmMuMDUzIDAgMS4yMjYtLjAzNSAyLjkwOC0uNDJhLjcwMi43MDIgMCAwIDAgLjU0My0uODQxLjcwMi43MDIgMCAwIDAtLjg0MS0uNTQzYy0xLjU2LjMzMi0yLjY2My4zODUtMi42OC4zODVhLjcwNC43MDQgMCAwIDAtLjY2Ni43MzZaTTEuMTM0IDE4LjEwM2MuMTIyLjE3NS4zNS4yOC41Ni4yOC4xNCAwIC4yOC0uMDM1LjQyLS4xMjIgNC40NS0zLjI0IDQuNjI1LTcuNDggNC42MjUtNy42NTUgMC0uMzg1LS4yOTgtLjctLjY4My0uNzE4LS4zODYtLjAxOC0uNy4yOTgtLjcxOC42ODMgMCAuMTQtLjE3NiAzLjczMS00LjA0NyA2LjU1MWEuNzAxLjcwMSAwIDAgMC0uMTU3Ljk4MVoiIGNsaXAtcnVsZT0iZXZlbm9kZCIvPjwvc3ZnPg==" alt="نشان دیوار" width="48" height="48" class="logo-e3eeb"/>
                    </a>
                    <hr data-testid="divider" class="kt-divider kt-divider--padded kt-divider--vertical kt-divider--default" role="presentation"/>
                    <div data-testid="trigger" class="kt-rich-tooltip__trigger" data-tooltip-id="city-input-tooltip">
                        <button class="kt-button kt-button--inlined kt-nav-button select-city-button-d4d79 nav-bar__city-button-fb19d" type="button" tabindex="0">
                            <i class="kt-icon kt-icon-place kt-button__icon no-pointer-event" data-testid="icon" data-icon="place"></i>
                            <span class="kt-text-truncate no-pointer-event">تهران</span>
                        </button>
                    </div>
                    <div class="nav-bar__category-mega-box-ad06f">
                        <div data-testid="dropdown-menu" aria-haspopup="true" class="kt-dropdown-menu dropdown-bfba4">
                            <button type="button" class="kt-dropdown-button kt-dropdown-button--medium kt-dropdown-button--inlined">
                                دسته‌ها<i class="kt-icon kt-icon-keyboard-arrow-down-o kt-icon--sm kt-dropdown-button__arrow-icon kt-dropdown-button__arrow-icon--closed" data-testid="icon" data-icon="keyboard-arrow-down-o"></i>
                            </button>
                        </div>
                        <div class="nav-bar__search-container-ac88f">
                            <div class="kt-dimmer kt-dimmer--dark" data-testid="dimmer">
                                <div data-testid="focus-lock-container" class="kt-dimmer__content">
                                    <div class="kt-visually-hidden fallback-focus-class" tabindex="-1" data-testid="focus-lock-visually-hidden-element"></div>
                                    <section data-testid="new-modal-section" role="dialog" class="kt-new-modal kt-new-modal--default">
                                        <header class="kt-new-modal__header kt-new-modal__header--has-divider">
                                            <div class="kt-new-modal__title-box">
                                                <p class="kt-new-modal__title"></p>
                                                <button class="kt-button kt-button--inlined kt-button--circular kt-new-modal__close-button" type="button" tabindex="0" data-testid="new-modal-close-button" aria-label="بستن">
                                                    <i class="kt-icon kt-icon-close kt-button__icon no-pointer-event" data-testid="icon" data-icon="close"></i>
                                                </button>
                                            </div>
                                        </header>
                                        <div data-testid="body" class="kt-new-modal__body">
                                            <div class="kt-base-row kt-base-row--large kt-description-row kt-description-row--padded">
                                                <div class="kt-base-row__start">
                                                    <p class="description-a64e0 kt-description-row__text kt-description-row__text--primary"></p>
                                                </div>
                                            </div>
                                        </div>
                                        <footer class="kt-new-modal__footer">
                                            <div class="kt-button-row kt-button-row--fullwidth">
                                                <button class="kt-button kt-button--primary" type="button" tabindex="0">
                                                    <span class="kt-text-truncate no-pointer-event"></span>
                                                </button>
                                            </div>
                                        </footer>
                                    </section>
                                </div>
                            </div>
                            <div>
                                <div class="full-width kt-nav-text-field">
                                    <div class="kt-nav-text-field__field">
                                        <form class="form-a9d32">
                                            <input class="kt-nav-text-field__input" type="text" autoComplete="off" placeholder="جستجو در همهٔ آگهی‌ها" name="search" value=""/>
                                        </form>
                                        <i class="kt-icon kt-icon-search-o kt-nav-text-field__icon" data-testid="icon" data-icon="search-o"></i>
                                    </div>
                                    <div class="kt-nav-text-field__dropdown">
                                        <hr data-testid="divider" class="kt-divider kt-divider--default" role="presentation"/>
                                        <div class="dropdown-dc2a5">
                                            <div class="progressible-content-e2c95">
                                                <div class="kt-progress-snake progressible-content__progress-a7872 kt-progress-snake--primary kt-progress-snake--animated kt-progress-snake--center kt-progress-snake--lg" role="progressbar">
                                                    <span class="kt-progress-snake__node"></span>
                                                    <span class="kt-progress-snake__node"></span>
                                                    <span class="kt-progress-snake__node"></span>
                                                </div>
                                            </div>
                                            <div class="queries-b4dfc">
                                                <div class="queries__title-ccabe">بیشترین جستجوهای دیوار</div>
                                                <div class="queries__items-bee00">
                                                    <a data-testid="chip" class="kt-chip kt-chip--small kt-chip--rounded kt-chip--outlined kt-chip--has-action queries__item-c3381" role="button" tabindex="0" href="/s/tehran/car">
                                                        <span>خودروی سواری</span>
                                                    </a>
                                                    <a data-testid="chip" class="kt-chip kt-chip--small kt-chip--rounded kt-chip--outlined kt-chip--has-action queries__item-c3381" role="button" tabindex="0" href="/s/tehran/buy-apartment">
                                                        <span>فروش آپارتمان</span>
                                                    </a>
                                                    <a data-testid="chip" class="kt-chip kt-chip--small kt-chip--rounded kt-chip--outlined kt-chip--has-action queries__item-c3381" role="button" tabindex="0" href="/s/tehran/rent-apartment">
                                                        <span>اجاره آپارتمان</span>
                                                    </a>
                                                    <a data-testid="chip" class="kt-chip kt-chip--small kt-chip--rounded kt-chip--outlined kt-chip--has-action queries__item-c3381" role="button" tabindex="0" href="/s/tehran/mobile-phones">
                                                        <span>موبایل</span>
                                                    </a>
                                                    <a data-testid="chip" class="kt-chip kt-chip--small kt-chip--rounded kt-chip--outlined kt-chip--has-action queries__item-c3381" role="button" tabindex="0" href="/s/tehran/chair-bench">
                                                        <span>صندلی و نیمکت</span>
                                                    </a>
                                                    <a data-testid="chip" class="kt-chip kt-chip--small kt-chip--rounded kt-chip--outlined kt-chip--has-action queries__item-c3381" role="button" tabindex="0" href="/s/tehran/pets-animals">
                                                        <span>حیوانات</span>
                                                    </a>
                                                    <a data-testid="chip" class="kt-chip kt-chip--small kt-chip--rounded kt-chip--outlined kt-chip--has-action queries__item-c3381" role="button" tabindex="0" href="/s/tehran/personal-goods">
                                                        <span>وسایل شخصی</span>
                                                    </a>
                                                    <a data-testid="chip" class="kt-chip kt-chip--small kt-chip--rounded kt-chip--outlined kt-chip--has-action queries__item-c3381" role="button" tabindex="0" href="/s/tehran/services">
                                                        <span>خدمات</span>
                                                    </a>
                                                    <a data-testid="chip" class="kt-chip kt-chip--small kt-chip--rounded kt-chip--outlined kt-chip--has-action queries__item-c3381" role="button" tabindex="0" href="/s/tehran/jobs">
                                                        <span>استخدام</span>
                                                    </a>
                                                    <a data-testid="chip" class="kt-chip kt-chip--small kt-chip--rounded kt-chip--outlined kt-chip--has-action queries__item-c3381" role="button" tabindex="0" href="/s/tehran/tv-projector">
                                                        <span>تلویزیون</span>
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="nav-bar__end-section-dabb8">
                            <div data-testid="dropdown-menu" aria-haspopup="true" class="kt-dropdown-menu">
                                <button class="kt-button kt-button--inlined kt-nav-button button-f32f0 kt-nav-button--small" type="button" tabindex="0" aria-haspopup="true" aria-expanded="false">
                                    <i class="kt-icon kt-icon-person kt-button__icon no-pointer-event" data-testid="icon" data-icon="person"></i>
                                    <span class="kt-text-truncate no-pointer-event"> دیوار من </span>
                                </button>
                            </div>
                            <a referrerPolicy="no-referrer" rel="nofollow noopener noreferrer" class="kt-button kt-button--inlined kt-nav-button button-f32f0 kt-nav-button--small" role="button" tabindex="0" href="https://divar.ir/chat">
                                <i class="kt-icon kt-icon-chat-bubble kt-button__icon no-pointer-event" data-testid="icon" data-icon="chat-bubble"></i>
                                <span class="kt-text-truncate no-pointer-event">چت و تماس</span>
                            </a>
                            <a referrerPolicy="no-referrer" rel="noopener noreferrer" class="kt-button kt-button--inlined kt-nav-button button-f32f0 kt-nav-button--small" role="button" tabindex="0" href="https://divar.ir/help">
                                <i class="kt-icon kt-icon-support kt-button__icon no-pointer-event" data-testid="icon" data-icon="support"></i>
                                <span class="kt-text-truncate no-pointer-event"> پشتیبانی </span>
                            </a>
                            <button class="kt-button kt-button--primary kt-nav-button nav-bar__submit-btn-fbb11" type="button" tabindex="0">
                                <span class="kt-text-truncate no-pointer-event"> ثبت آگهی </span>
                            </button>
                        </div>
                    </div>
                </nav>
            </header>
            <div class="container--has-footer-d86a9 kt-container">
                <div class="">
                    <main>
                        <nav aria-label="breadcrumbs">
                            <ol class="kt-breadcrumbs kt-breadcrumbs--padded kt-breadcrumbs--extended-items-on-mobile">
                                <li class="kt-breadcrumbs__item">
                                    <a class="kt-breadcrumbs__action" tabindex="0" href="/s/tehran/real-estate">
                                        <span class="kt-breadcrumbs__action-text">املاک</span>
                                    </a>
                                    <i class="kt-icon kt-icon-keyboard-arrow-left kt-icon--xs kt-breadcrumbs__nav-icon" data-testid="icon" data-icon="keyboard-arrow-left"></i>
                                </li>
                                <li class="kt-breadcrumbs__item">
                                    <a class="kt-breadcrumbs__action" tabindex="0" href="/s/tehran/buy-residential">
                                        <span class="kt-breadcrumbs__action-text">فروش مسکونی</span>
                                    </a>
                                    <i class="kt-icon kt-icon-keyboard-arrow-left kt-icon--xs kt-breadcrumbs__nav-icon" data-testid="icon" data-icon="keyboard-arrow-left"></i>
                                </li>
                                <li class="kt-breadcrumbs__item">
                                    <a class="kt-breadcrumbs__action" tabindex="0" href="/s/tehran/buy-apartment">
                                        <span class="kt-breadcrumbs__action-text">فروش آپارتمان</span>
                                    </a>
                                    <i class="kt-icon kt-icon-keyboard-arrow-left kt-icon--xs kt-breadcrumbs__nav-icon" data-testid="icon" data-icon="keyboard-arrow-left"></i>
                                </li>
                                <li class="kt-breadcrumbs__item">
                                    <span class="kt-breadcrumbs__action">
                                        <span class="kt-breadcrumbs__action-text">۹۷ متر ۲ خواب دونبش // دید ابدی</span>
                                    </span>
                                    <i class="kt-icon kt-icon-keyboard-arrow-left kt-icon--xs kt-breadcrumbs__nav-icon" data-testid="icon" data-icon="keyboard-arrow-left"></i>
                                </li>
                            </ol>
                        </nav>
                        <article>
                            <div class="kt-row">
                                <div class="kt-col-5">
                                    <section>
                                        <div class="kt-page-title">
                                            <div class="kt-page-title__texts">
                                                <h1 class="kt-page-title__title kt-page-title__title--responsive-sized">۹۷ متر ۲ خواب دونبش // دید ابدی</h1>
                                            </div>
                                            <ul class="kt-page-title__tags"></ul>
                                        </div>
                                        <button type="button" class="kt-info-row kt-info-row--has-content" aria-expanded="false">
                                            <div class="kt-base-row kt-base-row--large">
                                                <div class="kt-base-row__start">
                                                    <p class="kt-info-row__title">ماه پیش در تهران، یوسف‌آباد، خ سی و هشتم فضل‌الهی</p>
                                                </div>
                                                <div class="kt-base-row__end">
                                                    <p class="kt-info-row__value"></p>
                                                    <span class="kt-caret kt-info-row__caret">
                                                        <div class="kt-caret__handle kt-caret__left-handle"></div>
                                                        <div class="kt-caret__handle kt-caret__right-handle"></div>
                                                    </span>
                                                </div>
                                            </div>
                                            <div class="" id="_R_b5b6ocH1_" aria-hidden="true" aria-labelledby="_R_b5b6oc_" role="region" style="box-sizing:border-box;display:none;height:0px;overflow:hidden" data-testid="collapsible-content">
                                                <div class="kt-info-row__content">
                                                    <div class="kt-base-row kt-base-row--large kt-description-row">
                                                        <div class="kt-base-row__start">
                                                            <p class="kt-description-row__text kt-description-row__text--primary kt-description-row__text--small">انتشار آگهی: ۷ مرداد ۱۴۰۵، ۱۵:۴۳
آخرین نردبان: ۲۱ شهریور ۱۴۰۵، ۱۰:۲۷
آخرین به‌روز‌رسانی: ۲۵ شهریور ۱۴۰۵، ۱۱:۰۷</p>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </button>
                                        <div class="" role="button" tabindex="0" style="cursor:pointer">
                                            <div class="kt-selector-row" data-testid="selector-row">
                                                <div class="kt-base-row kt-base-row--large kt-base-row--has-icon">
                                                    <div class="kt-base-row__start">
                                                        <i class="kt-icon kt-icon-warning kt-icon--lg kt-base-row__icon" style="color:rgb(var(--content-neutral-default))" data-testid="icon" data-icon="warning"></i>
                                                        <div class="kt-selector-row__start">
                                                            <p class="kt-selector-row__title">زنگ خطرهای قبل از معامله</p>
                                                        </div>
                                                    </div>
                                                    <div class="kt-base-row__end">
                                                        <i class="kt-icon kt-icon-keyboard-arrow-left kt-icon--lg kt-base-row__arrow" data-testid="icon" data-icon="keyboard-arrow-left"></i>
                                                    </div>
                                                </div>
                                            </div>
                                            <hr data-testid="divider" class="kt-divider kt-divider--default" role="presentation"/>
                                        </div>
                                        <div class="post-actions">
                                            <button class="kt-button kt-button--primary post-actions__get-contact" type="button" tabindex="0">
                                                <span class="kt-text-truncate no-pointer-event">اطلاعات تماس</span>
                                            </button>
                                            <div class="post-actions__bookmark-button">
                                                <div data-testid="trigger" class="kt-rich-tooltip__trigger post-actions__bookmark-button" data-tooltip-id="post-bookmark">
                                                    <button class="kt-button kt-button--inlined kt-button--circular" type="button" tabindex="0" aria-label="نشان کردن" aria-pressed="false" aria-labelledby="post-bookmark">
                                                        <i class="kt-icon kt-icon-bookmark-o kt-button__icon no-pointer-event" data-testid="icon" data-icon="bookmark-o"></i>
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="post-actions__share-button">
                                                <div data-testid="trigger" class="kt-rich-tooltip__trigger" data-tooltip-id="post-share">
                                                    <button class="kt-button kt-button--inlined kt-button--circular" type="button" tabindex="0" aria-label="اشتراک گذاری">
                                                        <i class="kt-icon kt-icon-share kt-button__icon no-pointer-event" data-testid="icon" data-icon="share"></i>
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="expandable-box expandable-box--collapsed"></div>
                                        <div class="post-page__section--padded">
                                            <table class="kt-group-row">
                                                <thead class="kt-group-row__header">
                                                    <tr class="kt-group-row__heading">
                                                        <th class="kt-group-row-item kt-group-row-item__header kt-group-row-item--info-row">
                                                            <span class="kt-group-row-item__title kt-body kt-body--sm">متراژ</span>
                                                        </th>
                                                        <th class="kt-group-row-item kt-group-row-item__header kt-group-row-item--info-row">
                                                            <span class="kt-group-row-item__title kt-body kt-body--sm">ساخت</span>
                                                        </th>
                                                        <th class="kt-group-row-item kt-group-row-item__header kt-group-row-item--info-row">
                                                            <span class="kt-group-row-item__title kt-body kt-body--sm">اتاق</span>
                                                        </th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr class="kt-group-row__data-row">
                                                        <td class="kt-group-row-item kt-group-row-item__value kt-group-row-item--info-row">۹۷</td>
                                                        <td class="kt-group-row-item kt-group-row-item__value kt-group-row-item--info-row">۱۴۰۳</td>
                                                        <td class="kt-group-row-item kt-group-row-item__value kt-group-row-item--info-row">۲</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                            <hr data-testid="divider" class="kt-divider kt-divider--default" role="presentation"/>
                                            <div class="kt-base-row kt-base-row--large kt-unexpandable-row" data-testid="unexpandable-info-row">
                                                <div class="kt-base-row__start kt-unexpandable-row__title-box">
                                                    <p class="kt-base-row__title kt-unexpandable-row__title">تصویر‌ها برای همین ملک است؟</p>
                                                </div>
                                                <div class="kt-base-row__end kt-unexpandable-row__value-box">
                                                    <p class="kt-unexpandable-row__value">خیر</p>
                                                </div>
                                            </div>
                                            <hr data-testid="divider" class="kt-divider kt-divider--default" role="presentation"/>
                                            <div class="kt-base-row kt-base-row--large kt-unexpandable-row" data-testid="unexpandable-info-row">
                                                <div class="kt-base-row__start kt-unexpandable-row__title-box">
                                                    <p class="kt-base-row__title kt-unexpandable-row__title">قیمت کل</p>
                                                </div>
                                                <div class="kt-base-row__end kt-unexpandable-row__value-box">
                                                    <p class="kt-unexpandable-row__value">‏۴۸,۵۰۰,۰۰۰,۰۰۰ تومان</p>
                                                </div>
                                            </div>
                                            <hr data-testid="divider" class="kt-divider kt-divider--default" role="presentation"/>
                                            <div class="kt-base-row kt-base-row--large kt-unexpandable-row" data-testid="unexpandable-info-row">
                                                <div class="kt-base-row__start kt-unexpandable-row__title-box">
                                                    <p class="kt-base-row__title kt-unexpandable-row__title">قیمت هر متر</p>
                                                </div>
                                                <div class="kt-base-row__end kt-unexpandable-row__value-box">
                                                    <p class="kt-unexpandable-row__value">‏۵۰۰,۰۰۰,۰۰۰ تومان</p>
                                                </div>
                                            </div>
                                            <hr data-testid="divider" class="kt-divider kt-divider--default" role="presentation"/>
                                            <div class="kt-base-row kt-base-row--large kt-unexpandable-row" data-testid="unexpandable-info-row">
                                                <div class="kt-base-row__start kt-unexpandable-row__title-box">
                                                    <p class="kt-base-row__title kt-unexpandable-row__title">طبقه</p>
                                                </div>
                                                <div class="kt-base-row__end kt-unexpandable-row__value-box">
                                                    <p class="kt-unexpandable-row__value">۵</p>
                                                </div>
                                            </div>
                                            <hr data-testid="divider" class="kt-divider kt-divider--default" role="presentation"/>
                                            <div class="kt-section-title kt-section-title--alt-padded">
                                                <div>
                                                    <div class="kt-section-title__title-block" data-testid="section-title-block">
                                                        <span class="kt-section-title__title" style="color:rgb(var(--content-neutral-stronger))">ویژگی‌ها و امکانات</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <table class="kt-group-row">
                                                <thead class="kt-group-row__header">
                                                    <tr class="kt-group-row__heading">
                                                        <th class="kt-group-row-item kt-group-row-item__header">
                                                            <i class="kt-icon kt-icon-elevator kt-icon--lg kt-group-row-item__icon" data-testid="icon" data-icon="elevator"></i>
                                                        </th>
                                                        <th class="kt-group-row-item kt-group-row-item__header">
                                                            <i class="kt-icon kt-icon-parking kt-icon--lg kt-group-row-item__icon" data-testid="icon" data-icon="parking"></i>
                                                        </th>
                                                        <th class="kt-group-row-item kt-group-row-item__header">
                                                            <i class="kt-icon kt-icon-cabinet kt-icon--lg kt-group-row-item__icon" data-testid="icon" data-icon="cabinet"></i>
                                                        </th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr class="kt-group-row__data-row">
                                                        <td class="kt-group-row-item kt-group-row-item__value kt-body kt-body--stable">آسانسور</td>
                                                        <td class="kt-group-row-item kt-group-row-item__value kt-body kt-body--stable">پارکینگ</td>
                                                        <td class="kt-group-row-item kt-group-row-item__value kt-body kt-body--stable">انباری</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                            <hr data-testid="divider" class="kt-divider kt-divider--default" role="presentation"/>
                                            <div role="button" tabindex="0" class="raw-button-cd669" aria-disabled="false">
                                                <div class="kt-selector-row" data-testid="selector-row">
                                                    <div class="kt-base-row kt-base-row--large">
                                                        <div class="kt-base-row__start">
                                                            <div class="kt-selector-row__start">
                                                                <p class="kt-selector-row__title">سایر ویژگی‌ها و امکانات</p>
                                                            </div>
                                                        </div>
                                                        <div class="kt-base-row__end">
                                                            <i class="kt-icon kt-icon-keyboard-arrow-left kt-icon--lg kt-base-row__arrow" data-testid="icon" data-icon="keyboard-arrow-left"></i>
                                                        </div>
                                                    </div>
                                                </div>
                                                <hr data-testid="divider" class="kt-divider kt-divider--default" role="presentation"/>
                                            </div>
                                            <div class="" role="button" tabindex="0" style="cursor:pointer">
                                                <div class="kt-selector-row" data-testid="selector-row">
                                                    <div class="kt-base-row kt-base-row--large kt-base-row--has-icon">
                                                        <div class="kt-base-row__start">
                                                            <i class="kt-icon kt-icon-article-magnifier kt-icon--lg kt-base-row__icon" style="color:rgb(var(--content-neutral-default))" data-testid="icon" data-icon="article-magnifier"></i>
                                                            <div class="kt-selector-row__start">
                                                                <p class="kt-selector-row__title">بررسی و کارشناسی</p>
                                                            </div>
                                                        </div>
                                                        <div class="kt-base-row__end">
                                                            <i class="kt-icon kt-icon-keyboard-arrow-left kt-icon--lg kt-base-row__arrow" data-testid="icon" data-icon="keyboard-arrow-left"></i>
                                                        </div>
                                                    </div>
                                                </div>
                                                <hr data-testid="divider" class="kt-divider kt-divider--default" role="presentation"/>
                                            </div>
                                        </div>
                                    </section>
                                    <section class="post-page__section--padded">
                                        <div class="post-page__section--padded">
                                            <div>
                                                <div class="kt-base-row kt-base-row--large kt-title-row">
                                                    <div class="kt-base-row__start kt-title-row__row kt-title-row__row--unknown">
                                                        <h2 style="color:rgb(var(--content-neutral-stronger))" class="kt-title-row__title kt-title-row__title--secondary" data-testid="title">توضیحات</h2>
                                                    </div>
                                                    <div class="kt-base-row__end"></div>
                                                </div>
                                            </div>
                                            <div class="kt-base-row kt-base-row--large kt-description-row">
                                                <div class="kt-base-row__start">
                                                    <p class="kt-description-row__text kt-description-row__text--primary">بهترین واحد در منطقه رو از دست نده! 

⚜️ ۲ خواب، دونبش، غرق نور، با دید ابدی و بدون مشرف
⚜️ نقشه عالی و سالن مربع شکل که هر جور بچینی قشنگه
⚜️ خواب‌ها استاندارد و بزرگ هستن.
⚜️ دو ساله، کلید نخورده و آماده تحویل!
⚜️ ورودی از لابی شیک و سرایدار مقیم برای امنیت بیشتر.

کارشناس فروش منطقه، REDACTED
 برای هماهنگی و بازدید، پیام بدین یا تماس بگیرین.</p>
                                                </div>
                                            </div>
                                        </div>
                                    </section>
                                    <div class="post-page__section--padded">
                                        <nav>
                                            <div class="kt-wrapper-row" data-testid="wrapper-row">
                                                <a class="" tabindex="0" href="/s/tehran/buy-apartment">
                                                    <button data-testid="chip" class="kt-chip kt-chip--has-action kt-wrapper-row__child" type="button" tabindex="0">
                                                        <span>فروش آپارتمان</span>
                                                    </button>
                                                </a>
                                                <a class="" tabindex="0" href="/s/tehran/buy-apartment/yousef-abad">
                                                    <button data-testid="chip" class="kt-chip kt-chip--has-action kt-wrapper-row__child" type="button" tabindex="0">
                                                        <span>فروش آپارتمان در یوسف‌آباد</span>
                                                    </button>
                                                </a>
                                            </div>
                                        </nav>
                                    </div>
                                </div>
                                <div class="kt-col-6 kt-offset-1">
                                    <section class="post-page__section--padded">
                                        <div class="post-page__section--padded">
                                            <div class="kt-carousel kt-carousel--rounded">
                                                <div class="keen-slider kt-base-carousel__slides slides-dUO2O_">
                                                    <span class="kt-visually-hidden" aria-live="polite">تصویر 1 از 1</span>
                                                    <div class="keen-slider__slide kt-base-carousel__slide">
                                                        <figure class="kt-base-carousel__figure" data-testid="figure-testid">
                                                            <div class="kt-base-carousel__image">
                                                                <picture class="kt-image-block" style="padding-bottom:75%" data-testid="image-block">
                                                                    <img decoding="auto" fetchPriority="auto" data-testid="image-element" class="kt-image-block__image" src="https://s100.divarcdn.com/static/photo/neda/webp_post/ctqDuy-S76vGZAxvffrTCg/43cff8b2-eb49-4012-8e90-3f565fc0ef29.webp" alt="۹۷ متر ۲ خواب دونبش // دید ابدی|فروش آپارتمان|تهران, یوسف‌آباد|دیوار"/>
                                                                </picture>
                                                            </div>
                                                        </figure>
                                                        <div class="kt-base-carousel__slide-loading-overlay"></div>
                                                    </div>
                                                    <button data-testid="tag-container" data-has-skeleton="true" class="kt-tag kt-tag--overlay kt-tag--medium kt-tag--flipped kt-base-carousel__fullscreen-control kt-base-carousel__button" type="button" aria-label="باز کردن گالری به صورت تمام‌صفحه">
                                                        <i class="kt-icon kt-icon-full-screen-o kt-icon--xs kt-tag__icon" data-testid="icon" data-icon="full-screen-o"></i>
                                                        <span data-has-skeleton="true" class="kt-tag__text kt-text-truncate">عکس‌ها: تزئینی</span>
                                                    </button>
                                                </div>
                                                <div class="kt-carousel__thumbnails">
                                                    <div class="keen-slider kt-base-carousel__thumbnails"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </section>
                                    <div class="post-page__section--padded">
                                        <div class="note-eLyuUj">
                                            <div class="container-UafEm_">
                                                <div class="kt-textarea" data-testid="textarea-wrapper">
                                                    <textarea class="kt-textarea__field" aria-invalid="false" placeholder="یادداشت شما..."></textarea>
                                                    <div class="kt-textarea__resize-box" data-testid="resize-box">
                                                        <div class="kt-textarea__resize-indicator"></div>
                                                    </div>
                                                </div>
                                            </div>
                                            <p class="hint-JTObjj">یادداشت تنها برای شما قابل دیدن است و پس از حذف آگهی، پاک خواهد شد.</p>
                                        </div>
                                    </div>
                                    <section class="post-page__section--padded">
                                        <div class="post-page__section--padded">
                                            <div class="image-kclhuf">
                                                <picture class="kt-image-block kt-image-block--radius-sm" style="padding-bottom:56.249992968750874%" data-testid="image-block">
                                                    <img decoding="auto" fetchPriority="auto" data-testid="image-element" class="kt-image-block__image" src="https://mapimage.divarcdn.com/v8/mapimage?encrypted_data=MTIzNDU2Nzg5MTIzXL_Y8SdZyazuQp-XOg7PaPpL736MLc2ODD3PkY6uBOaYTw==&amp;is_nearby=true" alt="موقعیت مکانی"/>
                                                </picture>
                                            </div>
                                        </div>
                                    </section>
                                    <section class="post-page__section--padded">
                                        <div class="post-page__section--padded">
                                            <div class="progressible-content-e2c95">
                                                <div class="kt-progress-circular progressible-content__progress-a7872 kt-progress-circular--animated kt-progress-circular--lg kt-progress-circular--center" role="progressbar">
                                                    <svg xmlns="http://www.w3.org/2000/svg" class="kt-progress-circular__content" viewBox="0 0 16 16">
                                                        <g class="kt-progress-circular__rotate">
                                                            <path class="kt-progress-circular__static-particle" d="M8,16a8,8,0,1,1,8-8A8,8,0,0,1,8,16ZM8,2a6,6,0,1,0,6,6A6,6,0,0,0,8,2Z"></path>
                                                            <circle class="kt-progress-circular__moving-particle" cx="8" cy="8" r="7"></circle>
                                                        </g>
                                                    </svg>
                                                </div>
                                            </div>
                                        </div>
                                    </section>
                                    <div class="post-page__section--padded">
                                        <div class="" role="button" tabindex="0" style="cursor:pointer">
                                            <div class="kt-selector-row" data-testid="selector-row">
                                                <div class="kt-base-row kt-base-row--large kt-base-row--has-icon">
                                                    <div class="kt-base-row__start">
                                                        <i class="kt-icon kt-icon-report kt-icon--lg kt-base-row__icon" style="color:rgb(var(--content-neutral-default))" data-testid="icon" data-icon="report"></i>
                                                        <div class="kt-selector-row__start">
                                                            <p class="kt-selector-row__title">گزارش آگهی</p>
                                                        </div>
                                                    </div>
                                                    <div class="kt-base-row__end"></div>
                                                </div>
                                            </div>
                                            <hr data-testid="divider" class="kt-divider kt-divider--default" role="presentation"/>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </article>
                    </main>
                </div>
                <footer class="container-e7eb4 footer-fcc34">
                    <div class="links-container-d7e32">
                        <a class="styled-link-d9633 logo-c189b" href="/s/tehran">
                            <i class="kt-icon kt-icon-social-divar kt-icon--xl" data-testid="icon" data-icon="social-divar"></i>
                        </a>
                        <nav class="links-dc796">
                            <a class="styled-link-d9633 link-df015" href="/about"> دربارهٔ دیوار </a>
                            <a title=" دریافت برنامه " class="styled-link-d9633 link-df015" href="/download">دریافت برنامه</a>
                            <a referrerPolicy="no-referrer" rel="noopener noreferrer" href="https://divar.news" target="_blank" class="styled-link-d9633 link-df015">اتاق خبر</a>
                        </nav>
                        <nav class="links-dc796">
                            <a referrerPolicy="no-referrer" rel="noopener noreferrer" href="https://careers.divar.ir" target="_blank" class="styled-link-d9633 link-df015">دیواری شو</a>
                            <a referrerPolicy="no-referrer" rel="noopener noreferrer" href="https://divar.ir/help" target="_blank" class="styled-link-d9633">پشتیبانی و قوانین</a>
                        </nav>
                    </div>
                    <div class="">
                        <a referrerPolicy="no-referrer" rel="noopener noreferrer nofollow" href="https://twitter.com/divar_official" target="_blank" title="دیوار در توییتر" aria-label="دیوار در توییتر" class="styled-link-d9633 link-c8a3f">
                            <i class="kt-icon kt-icon-social-twitter" data-testid="icon" data-icon="social-twitter"></i>
                        </a>
                        <a referrerPolicy="no-referrer" rel="noopener noreferrer nofollow" href="https://www.instagram.com/divar.official" target="_blank" title="دیوار در اینستاگرام" aria-label="دیوار در اینستاگرام" class="styled-link-d9633 link-c8a3f">
                            <i class="kt-icon kt-icon-social-instagram-fill" data-testid="icon" data-icon="social-instagram-fill"></i>
                        </a>
                        <a referrerPolicy="no-referrer" rel="noopener noreferrer nofollow" href="https://www.linkedin.com/company/divarofficial" target="_blank" title="دیوار در لینکداین" aria-label="دیوار در لینکداین" class="styled-link-d9633 link-c8a3f">
                            <i class="kt-icon kt-icon-social-linkedin" data-testid="icon" data-icon="social-linkedin"></i>
                        </a>
                        <a referrerPolicy="no-referrer" rel="noopener noreferrer nofollow" href="https://www.aparat.com/divar.official" target="_blank" title="دیوار در آپارات" aria-label="دیوار در آپارات" class="styled-link-d9633 link-c8a3f">
                            <i class="kt-icon kt-icon-social-aparat" data-testid="icon" data-icon="social-aparat"></i>
                        </a>
                    </div>
                </footer>
            </div>
            <div class="kt-toast-container container-a30c5"></div>
            <div class="kt-snackbar-container"></div>
            <div class="kt-dimmer kt-dimmer--dark" data-testid="dimmer">
                <div data-testid="focus-lock-container" class="kt-dimmer__content">
                    <div class="kt-visually-hidden fallback-focus-class" tabindex="-1" data-testid="focus-lock-visually-hidden-element"></div>
                    <section data-testid="new-modal-section" role="dialog" class="kt-new-modal kt-new-modal--default">
                        <header class="kt-new-modal__header kt-new-modal__header--has-divider">
                            <div class="kt-new-modal__title-box">
                                <p class="kt-new-modal__title"></p>
                                <button class="kt-button kt-button--inlined kt-button--circular kt-new-modal__close-button" type="button" tabindex="0" data-testid="new-modal-close-button" aria-label="بستن">
                                    <i class="kt-icon kt-icon-close kt-button__icon no-pointer-event" data-testid="icon" data-icon="close"></i>
                                </button>
                            </div>
                        </header>
                        <div data-testid="body" class="kt-new-modal__body">
                            <div class="kt-base-row kt-base-row--large kt-description-row kt-description-row--padded">
                                <div class="kt-base-row__start">
                                    <p class="description-a64e0 kt-description-row__text kt-description-row__text--primary"></p>
                                </div>
                            </div>
                        </div>
                        <footer class="kt-new-modal__footer">
                            <div class="kt-button-row kt-button-row--fullwidth">
                                <button class="kt-button kt-button--primary" type="button" tabindex="0">
                                    <span class="kt-text-truncate no-pointer-event"></span>
                                </button>
                            </div>
                        </footer>
                    </section>
                </div>
            </div>
            <div class="kt-dimmer kt-dimmer--dark" data-testid="dimmer">
                <div data-testid="focus-lock-container" class="kt-dimmer__content">
                    <div class="kt-visually-hidden fallback-focus-class" tabindex="-1" data-testid="focus-lock-visually-hidden-element"></div>
                    <section data-testid="new-modal-section" role="dialog" class="kt-new-modal kt-new-modal--default">
                        <header class="kt-new-modal__header kt-new-modal__header--has-divider">
                            <div class="kt-new-modal__title-box">
                                <p class="kt-new-modal__title"></p>
                                <button class="kt-button kt-button--inlined kt-button--circular kt-new-modal__close-button" type="button" tabindex="0" data-testid="new-modal-close-button" aria-label="بستن">
                                    <i class="kt-icon kt-icon-close kt-button__icon no-pointer-event" data-testid="icon" data-icon="close"></i>
                                </button>
                            </div>
                        </header>
                        <div data-testid="body" class="kt-new-modal__body">
                            <div class="kt-base-row kt-base-row--large kt-description-row kt-description-row--padded">
                                <div class="kt-base-row__start">
                                    <p class="description-a64e0 kt-description-row__text kt-description-row__text--primary"></p>
                                </div>
                            </div>
                        </div>
                        <footer class="kt-new-modal__footer">
                            <div class="kt-button-row kt-button-row--fullwidth">
                                <button class="kt-button kt-button--primary" type="button" tabindex="0">
                                    <span class="kt-text-truncate no-pointer-event"></span>
                                </button>
                            </div>
                        </footer>
                    </section>
                </div>
            </div>
        </div>
        <script>
            window.__PRELOADED_STATE__ = {
                "nb": {
                    "showNoSearchResultNotice": false,
                    "listTopWidgets": [],
                    "listWidgets": [],
                    "listBottomWidgets": [],
                    "sidebarTopWidgets": [],
                    "sidebarBottomWidgets": [],
                    "firstPostDate": null,
                    "filterChips": [],
                    "seoDetails": {},
                    "pagination": null,
                    "isLoading": false,
                    "isLoadingMore": false,
                    "showLoadMoreSkeleton": false,
                    "hasSSRUnauthorizedError": false,
                    "isPullingToRefresh": false,
                    "tabs": {},
                    "lastAttemptedFetchLocation": {
                        "pathname": "",
                        "search": ""
                    },
                    "filtersPage": {
                        "widgetList": [],
                        "isLoading": false,
                        "hasSSRUnauthorizedError": false
                    },
                    "searchBar": {},
                    "fabButton": null,
                    "mapDeferredActionLog": null,
                    "mapViewport": {
                        "isLoading": true,
                        "error": null,
                        "data": {
                            "posts": [],
                            "clusters": [],
                            "countText": ""
                        }
                    },
                    "mapData": {
                        "isEnabled": false,
                        "searchThisAreaButton": {
                            "isEnabled": false
                        },
                        "config": {
                            "style": {},
                            "layerIds": [],
                            "clusteringLayerIds": []
                        },
                        "state": {
                            "cameraInfo": {}
                        },
                        "encodedPolygonList": []
                    },
                    "isUserMapViewDisabled": false,
                    "isMapSupported": true,
                    "mapPageState": "DEFAULT",
                    "mapPostsHistory": [],
                    "shouldSyncUrl": false,
                    "suggestionCacheData": [],
                    "isListChangedByMapMove": false
                },
                "search": {
                    "rootCat": {
                        "name": "همهٔ آگهی‌ها",
                        "slug": "ROOT",
                        "icon": {},
                        "parent": null,
                        "children": [{
                            "name": "املاک",
                            "slug": "real-estate",
                            "icon": {
                                "iconColor": "rgb(var(--content-neutral-default))",
                                "iconName": "real-estate",
                                "iconURL": {
                                    "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Freal_estate.png",
                                    "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Freal_estate.png"
                                }
                            },
                            "parent": "ROOT",
                            "children": [{
                                "name": "اجارهٔ مسکونی",
                                "slug": "residential-rent",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "residential-rent",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fresidential-rent.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fresidential-rent.png"
                                    }
                                },
                                "parent": "real-estate",
                                "children": [{
                                    "name": "آپارتمان",
                                    "slug": "apartment-rent",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "apartment-rent",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fapartment-rent.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fapartment-rent.png"
                                        }
                                    },
                                    "parent": "residential-rent",
                                    "children": []
                                }, {
                                    "name": "خانه و ویلا",
                                    "slug": "house-villa-rent",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "house-villa-rent",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fhouse-villa-rent.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fhouse-villa-rent.png"
                                        }
                                    },
                                    "parent": "residential-rent",
                                    "children": []
                                }]
                            }, {
                                "name": "فروش مسکونی",
                                "slug": "residential-sell",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "residential-sell",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fresidential-sell.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fresidential-sell.png"
                                    }
                                },
                                "parent": "real-estate",
                                "children": [{
                                    "name": "آپارتمان",
                                    "slug": "apartment-sell",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "apartment-sell",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fapartment-sell.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fapartment-sell.png"
                                        }
                                    },
                                    "parent": "residential-sell",
                                    "children": []
                                }, {
                                    "name": "خانه و ویلا",
                                    "slug": "house-villa-sell",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "house-villa-sell",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fhouse-villa-sell.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fhouse-villa-sell.png"
                                        }
                                    },
                                    "parent": "residential-sell",
                                    "children": []
                                }, {
                                    "name": "زمین و ملک کلنگی",
                                    "slug": "plot-old",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "plot-old",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fplot-old.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fplot-old.png"
                                        }
                                    },
                                    "parent": "residential-sell",
                                    "children": []
                                }]
                            }, {
                                "name": "فروش اداری و تجاری",
                                "slug": "commercial-sell",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "commercial-sell",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcommercial-sell.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcommercial-sell.png"
                                    }
                                },
                                "parent": "real-estate",
                                "children": [{
                                    "name": "دفتر کار، اتاق اداری، مطب",
                                    "slug": "office-sell",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "office-sell",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Foffice-sell.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Foffice-sell.png"
                                        }
                                    },
                                    "parent": "commercial-sell",
                                    "children": []
                                }, {
                                    "name": "مغازه و غرفه",
                                    "slug": "shop-sell",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "shop-sell",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fshop-sell.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fshop-sell.png"
                                        }
                                    },
                                    "parent": "commercial-sell",
                                    "children": []
                                }, {
                                    "name": "صنعتی، کشاورزی، تجاری",
                                    "slug": "industry-agriculture-business-sell",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "industry-agriculture-business-sell",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Findustry-agriculture-business-sell.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Findustry-agriculture-business-sell.png"
                                        }
                                    },
                                    "parent": "commercial-sell",
                                    "children": []
                                }]
                            }, {
                                "name": "اجارهٔ اداری و تجاری",
                                "slug": "commercial-rent",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "commercial-rent",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcommercial-rent.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcommercial-rent.png"
                                    }
                                },
                                "parent": "real-estate",
                                "children": [{
                                    "name": "دفتر کار، اتاق اداری، مطب",
                                    "slug": "office-rent",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "office-rent",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Foffice-rent.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Foffice-rent.png"
                                        }
                                    },
                                    "parent": "commercial-rent",
                                    "children": []
                                }, {
                                    "name": "مغازه و غرفه",
                                    "slug": "shop-rent",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "shop-rent",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fshop-rent.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fshop-rent.png"
                                        }
                                    },
                                    "parent": "commercial-rent",
                                    "children": []
                                }, {
                                    "name": "صنعتی، کشاورزی، تجاری",
                                    "slug": "industry-agriculture-business-rent",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "industry-agriculture-business-rent",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Findustry-agriculture-business-rent.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Findustry-agriculture-business-rent.png"
                                        }
                                    },
                                    "parent": "commercial-rent",
                                    "children": []
                                }]
                            }, {
                                "name": "پروژه‌های ساخت‌وساز",
                                "slug": "real-estate-services",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "real-estate-services",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Freal-estate-services.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Freal-estate-services.png"
                                    }
                                },
                                "parent": "real-estate",
                                "children": [{
                                    "name": "مشارکت در ساخت",
                                    "slug": "partnership",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "partnership",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fpartnership.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fpartnership.png"
                                        }
                                    },
                                    "parent": "real-estate-services",
                                    "children": []
                                }, {
                                    "name": "پیش‌فروش",
                                    "slug": "presell",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "presell",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fpresell.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fpresell.png"
                                        }
                                    },
                                    "parent": "real-estate-services",
                                    "children": []
                                }]
                            }, {
                                "name": "اجارهٔ کوتاه‌مدت",
                                "slug": "temporary-rent",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "temporary-rent",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ftemporary-rent.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ftemporary-rent.png"
                                    }
                                },
                                "parent": "real-estate",
                                "children": [{
                                    "name": "آپارتمان و سوئیت",
                                    "slug": "suite-apartment",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "suite-apartment",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fsuite-apartment.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fsuite-apartment.png"
                                        }
                                    },
                                    "parent": "temporary-rent",
                                    "children": []
                                }, {
                                    "name": "ویلا و باغ",
                                    "slug": "villa",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "villa",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fvilla.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fvilla.png"
                                        }
                                    },
                                    "parent": "temporary-rent",
                                    "children": []
                                }, {
                                    "name": "دفتر کار و فضای آموزشی",
                                    "slug": "workspace",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "workspace",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fworkspace.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fworkspace.png"
                                        }
                                    },
                                    "parent": "temporary-rent",
                                    "children": []
                                }]
                            }]
                        }, {
                            "name": "وسایل نقلیه",
                            "slug": "vehicles",
                            "icon": {
                                "iconColor": "rgb(var(--content-neutral-default))",
                                "iconName": "cat-vehicles",
                                "iconURL": {
                                    "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcat_vehicles.png",
                                    "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcat_vehicles.png"
                                }
                            },
                            "parent": "ROOT",
                            "children": [{
                                "name": "خودرو",
                                "slug": "cars",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "cars",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcars.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcars.png"
                                    }
                                },
                                "parent": "vehicles",
                                "children": [{
                                    "name": "سواری و وانت",
                                    "slug": "light",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "light",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Flight.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Flight.png"
                                        }
                                    },
                                    "parent": "cars",
                                    "children": []
                                }, {
                                    "name": "اجاره‌ای",
                                    "slug": "rental",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "rental",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Frental.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Frental.png"
                                        }
                                    },
                                    "parent": "cars",
                                    "children": []
                                }, {
                                    "name": "کلاسیک",
                                    "slug": "classic",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "classic",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fclassic.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fclassic.png"
                                        }
                                    },
                                    "parent": "cars",
                                    "children": []
                                }, {
                                    "name": "سنگین",
                                    "slug": "heavy",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "heavy",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fheavy.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fheavy.png"
                                        }
                                    },
                                    "parent": "cars",
                                    "children": []
                                }]
                            }, {
                                "name": "موتورسیکلت",
                                "slug": "motorcycles",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "motorcycles",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmotorcycles.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmotorcycles.png"
                                    }
                                },
                                "parent": "vehicles",
                                "children": []
                            }, {
                                "name": "قطعات یدکی و لوازم جانبی",
                                "slug": "parts-accessories",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "parts-accessories",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fparts-accessories.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fparts-accessories.png"
                                    }
                                },
                                "parent": "vehicles",
                                "children": []
                            }, {
                                "name": "قایق و سایر وسایل نقلیه",
                                "slug": "boat",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "boat",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fboat.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fboat.png"
                                    }
                                },
                                "parent": "vehicles",
                                "children": []
                            }]
                        }, {
                            "name": "کالای دیجیتال",
                            "slug": "electronic-devices",
                            "icon": {
                                "iconColor": "rgb(var(--content-neutral-default))",
                                "iconName": "cat-electronic-devices",
                                "iconURL": {
                                    "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcat_electronic_devices.png",
                                    "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcat_electronic_devices.png"
                                }
                            },
                            "parent": "ROOT",
                            "children": [{
                                "name": "موبایل و تبلت",
                                "slug": "mobile-tablet",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "mobile-tablet",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmobile-tablet.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmobile-tablet.png"
                                    }
                                },
                                "parent": "electronic-devices",
                                "children": [{
                                    "name": "موبایل",
                                    "slug": "mobile-phones",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "mobile-phones",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmobile-phones.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmobile-phones.png"
                                        }
                                    },
                                    "parent": "mobile-tablet",
                                    "children": []
                                }, {
                                    "name": "تبلت",
                                    "slug": "tablet",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "tablet",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ftablet.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ftablet.png"
                                        }
                                    },
                                    "parent": "mobile-tablet",
                                    "children": []
                                }, {
                                    "name": "لوازم جانبی موبایل و تبلت",
                                    "slug": "mobile-tablet-accessories",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "mobile-tablet-accessories",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmobile-tablet-accessories.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmobile-tablet-accessories.png"
                                        }
                                    },
                                    "parent": "mobile-tablet",
                                    "children": []
                                }, {
                                    "name": "سیم‌کارت",
                                    "slug": "sim-card",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "sim-card",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fsim-card.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fsim-card.png"
                                        }
                                    },
                                    "parent": "mobile-tablet",
                                    "children": []
                                }]
                            }, {
                                "name": "رایانه",
                                "slug": "computers",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "computers",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcomputers.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcomputers.png"
                                    }
                                },
                                "parent": "electronic-devices",
                                "children": [{
                                    "name": "رایانه همراه",
                                    "slug": "laptops",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "laptops",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Flaptops.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Flaptops.png"
                                        }
                                    },
                                    "parent": "computers",
                                    "children": []
                                }, {
                                    "name": "رایانه رومیزی",
                                    "slug": "desktops",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "desktops",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fdesktops.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fdesktops.png"
                                        }
                                    },
                                    "parent": "computers",
                                    "children": []
                                }, {
                                    "name": "قطعات و لوازم جانبی",
                                    "slug": "parts-and-accessories",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "parts-and-accessories",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fparts-and-accessories.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fparts-and-accessories.png"
                                        }
                                    },
                                    "parent": "computers",
                                    "children": []
                                }, {
                                    "name": "مودم و تجهیزات شبکه",
                                    "slug": "modem-and-network-equipment",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "modem-and-network-equipment",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmodem-and-network-equipment.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmodem-and-network-equipment.png"
                                        }
                                    },
                                    "parent": "computers",
                                    "children": []
                                }, {
                                    "name": "پرینتر، اسکنر، کپی، فکس",
                                    "slug": "printer-scaner-copier",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "printer-scaner-copier",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fprinter-scaner-copier.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fprinter-scaner-copier.png"
                                        }
                                    },
                                    "parent": "computers",
                                    "children": []
                                }]
                            }, {
                                "name": "کنسول، بازی ویدئویی و آنلاین",
                                "slug": "game-consoles-and-video-games",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "game-consoles-and-video-games",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fgame-consoles-and-video-games.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fgame-consoles-and-video-games.png"
                                    }
                                },
                                "parent": "electronic-devices",
                                "children": []
                            }, {
                                "name": "صوتی و تصویری",
                                "slug": "audio-video",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "audio-video",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Faudio-video.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Faudio-video.png"
                                    }
                                },
                                "parent": "electronic-devices",
                                "children": [{
                                    "name": "فیلم و موسیقی",
                                    "slug": "movies-and-music",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "movies-and-music",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmovies-and-music.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmovies-and-music.png"
                                        }
                                    },
                                    "parent": "audio-video",
                                    "children": []
                                }, {
                                    "name": "دوربین عکاسی و فیلم‌برداری",
                                    "slug": "camera-camcoders",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "camera-camcoders",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcamera-camcoders.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcamera-camcoders.png"
                                        }
                                    },
                                    "parent": "audio-video",
                                    "children": []
                                }, {
                                    "name": "پخش‌کننده همراه",
                                    "slug": "mp3-player",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "mp3-player",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmp3-player.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmp3-player.png"
                                        }
                                    },
                                    "parent": "audio-video",
                                    "children": []
                                }, {
                                    "name": "سیستم صوتی خانگی",
                                    "slug": "stereo-surround",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "stereo-surround",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fstereo-surround.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fstereo-surround.png"
                                        }
                                    },
                                    "parent": "audio-video",
                                    "children": []
                                }, {
                                    "name": "پخش‌کننده DVD و ویدیو",
                                    "slug": "video-dvdplayer",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "video-dvdplayer",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fvideo-dvdplayer.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fvideo-dvdplayer.png"
                                        }
                                    },
                                    "parent": "audio-video",
                                    "children": []
                                }, {
                                    "name": "تلویزیون و پروژکتور",
                                    "slug": "tv-projector",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "tv-projector",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ftv-projector.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ftv-projector.png"
                                        }
                                    },
                                    "parent": "audio-video",
                                    "children": []
                                }, {
                                    "name": "دوربین مداربسته",
                                    "slug": "CCTV",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "cctv",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcctv.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcctv.png"
                                        }
                                    },
                                    "parent": "audio-video",
                                    "children": []
                                }]
                            }, {
                                "name": "تلفن رومیزی",
                                "slug": "phone",
                                "icon": {},
                                "parent": "electronic-devices",
                                "children": []
                            }]
                        }, {
                            "name": "خانه و آشپزخانه",
                            "slug": "home-kitchen",
                            "icon": {
                                "iconColor": "rgb(var(--content-neutral-default))",
                                "iconName": "cat-for-the-home",
                                "iconURL": {
                                    "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcat_for_the_home.png",
                                    "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcat_for_the_home.png"
                                }
                            },
                            "parent": "ROOT",
                            "children": [{
                                "name": "لوازم خانگی برقی",
                                "slug": "appliance",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "appliance",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fappliance.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fappliance.png"
                                    }
                                },
                                "parent": "home-kitchen",
                                "children": [{
                                    "name": "یخچال و فریزر",
                                    "slug": "refrigerator-freezer",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "refrigerator-freezer",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Frefrigerator-freezer.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Frefrigerator-freezer.png"
                                        }
                                    },
                                    "parent": "appliance",
                                    "children": []
                                }, {
                                    "name": "آب‌سردکن و تصفیه آب",
                                    "slug": "water-cooler-refinery",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "water-cooler-refinery",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fwater-cooler-refinery.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fwater-cooler-refinery.png"
                                        }
                                    },
                                    "parent": "appliance",
                                    "children": []
                                }, {
                                    "name": "ماشین لباسشویی و خشک‌کن لباس",
                                    "slug": "washing-machines",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "washing-machines",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fwashing-machines.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fwashing-machines.png"
                                        }
                                    },
                                    "parent": "appliance",
                                    "children": []
                                }, {
                                    "name": "ماشین ظرفشویی",
                                    "slug": "dishwasher",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "dishwasher",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fdishwasher.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fdishwasher.png"
                                        }
                                    },
                                    "parent": "appliance",
                                    "children": []
                                }, {
                                    "name": "جاروبرقی، جارو شارژی، بخارشو",
                                    "slug": "vacuums-cleaner",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "vacuums-cleaner",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fvacuums-cleaner.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fvacuums-cleaner.png"
                                        }
                                    },
                                    "parent": "appliance",
                                    "children": []
                                }, {
                                    "name": "اتو و لوازم اتو",
                                    "slug": "steam-iron",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "steam-iron",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fsteam-iron.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fsteam-iron.png"
                                        }
                                    },
                                    "parent": "appliance",
                                    "children": []
                                }, {
                                    "name": "آبمیوه‌گیر و آب‌مرکبات‌گیر",
                                    "slug": "juicers",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "juicers",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fjuicers.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fjuicers.png"
                                        }
                                    },
                                    "parent": "appliance",
                                    "children": []
                                }, {
                                    "name": "خردکن، آسیاب، غذاساز",
                                    "slug": "food-mill",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "food-mill",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ffood-mill.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ffood-mill.png"
                                        }
                                    },
                                    "parent": "appliance",
                                    "children": []
                                }, {
                                    "name": "سماور، چای‌ساز، قهوه‌ساز",
                                    "slug": "drink-maker",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "drink-maker",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fdrink-maker.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fdrink-maker.png"
                                        }
                                    },
                                    "parent": "appliance",
                                    "children": []
                                }, {
                                    "name": "اجاق گاز و لوازم برقی پخت‌وپز",
                                    "slug": "oven-baking-appliances",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "oven-baking-appliances",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Foven-baking-appliances.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Foven-baking-appliances.png"
                                        }
                                    },
                                    "parent": "appliance",
                                    "children": []
                                }, {
                                    "name": "هود",
                                    "slug": "range-hood",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "range-hood",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Frange-hood.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Frange-hood.png"
                                        }
                                    },
                                    "parent": "appliance",
                                    "children": []
                                }, {
                                    "name": "سایر لوازم برقی",
                                    "slug": "other-appliances",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "other-appliances",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fother-appliances.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fother-appliances.png"
                                        }
                                    },
                                    "parent": "appliance",
                                    "children": []
                                }]
                            }, {
                                "name": "ظروف و لوازم آشپزخانه",
                                "slug": "kitchen-utensils",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "kitchen-utensils",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fkitchen_utensils.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fkitchen_utensils.png"
                                    }
                                },
                                "parent": "home-kitchen",
                                "children": [{
                                    "name": "سفره، حوله، دستمال آشپزخانه",
                                    "slug": "tablecloths",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "tablecloths",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ftablecloths.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ftablecloths.png"
                                        }
                                    },
                                    "parent": "kitchen-utensils",
                                    "children": []
                                }, {
                                    "name": "آب‌چکان و نظم‌دهنده ظروف",
                                    "slug": "container-organizers",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "container-organizers",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcontainer-organizers.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcontainer-organizers.png"
                                        }
                                    },
                                    "parent": "kitchen-utensils",
                                    "children": []
                                }, {
                                    "name": "قوری، کتری، قهوه‌ساز دستی",
                                    "slug": "pot-kettle",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "pot-kettle",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fpot-kettle.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fpot-kettle.png"
                                        }
                                    },
                                    "parent": "kitchen-utensils",
                                    "children": []
                                }, {
                                    "name": "ظروف سرو و پذیرایی",
                                    "slug": "home-catering",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "home-catering",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fhome-catering.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fhome-catering.png"
                                        }
                                    },
                                    "parent": "kitchen-utensils",
                                    "children": []
                                }, {
                                    "name": "ظروف نگهدارنده، پلاستیکی، یک‌بارمصرف",
                                    "slug": "containers",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "containers",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcontainers.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcontainers.png"
                                        }
                                    },
                                    "parent": "kitchen-utensils",
                                    "children": []
                                }, {
                                    "name": "ظروف پخت‌وپز",
                                    "slug": "cooking-utensils",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "cooking-utensils",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcooking-utensils.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcooking-utensils.png"
                                        }
                                    },
                                    "parent": "kitchen-utensils",
                                    "children": []
                                }]
                            }, {
                                "name": "خوردنی و آشامیدنی",
                                "slug": "food-and-drink",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "food-and-drink",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ffood-and-drink.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ffood-and-drink.png"
                                    }
                                },
                                "parent": "home-kitchen",
                                "children": []
                            }, {
                                "name": "خیاطی و بافتنی",
                                "slug": "sewing-knitting",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "sewing-knitting",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fsewing-knitting.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fsewing-knitting.png"
                                    }
                                },
                                "parent": "home-kitchen",
                                "children": [{
                                    "name": "چرخ خیاطی و ریسندگی",
                                    "slug": "sewing-machine",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "sewing-machine",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fsewing-machine.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fsewing-machine.png"
                                        }
                                    },
                                    "parent": "sewing-knitting",
                                    "children": []
                                }, {
                                    "name": "لوازم خیاطی و بافتنی",
                                    "slug": "sewing-accessories",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "sewing-accessories",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fsewing-accessories.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fsewing-accessories.png"
                                        }
                                    },
                                    "parent": "sewing-knitting",
                                    "children": []
                                }]
                            }, {
                                "name": "مبلمان و صنایع چوب",
                                "slug": "furniture-wood",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "furniture-wood",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ffurniture-wood.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ffurniture-wood.png"
                                    }
                                },
                                "parent": "home-kitchen",
                                "children": [{
                                    "name": "مبلمان خانگی و میز عسلی",
                                    "slug": "furniture",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "furniture",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ffurniture.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ffurniture.png"
                                        }
                                    },
                                    "parent": "furniture-wood",
                                    "children": []
                                }, {
                                    "name": "میز و صندلی غذاخوری",
                                    "slug": "dining-table",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "dining-table",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fdining-table.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fdining-table.png"
                                        }
                                    },
                                    "parent": "furniture-wood",
                                    "children": []
                                }, {
                                    "name": "بوفه، ویترین، کنسول",
                                    "slug": "buffet-showcases",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "buffet-showcases",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbuffet-showcases.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbuffet-showcases.png"
                                        }
                                    },
                                    "parent": "furniture-wood",
                                    "children": []
                                }, {
                                    "name": "کتابخانه، شلف، قفسه‌های دیواری",
                                    "slug": "bookcase-shelf",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "bookcase-shelf",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbookcase-shelf.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbookcase-shelf.png"
                                        }
                                    },
                                    "parent": "furniture-wood",
                                    "children": []
                                }, {
                                    "name": "جاکفشی، کمد، دراور",
                                    "slug": "shoe-rack-drawer",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "shoe-rack-drawer",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fshoe-rack-drawer.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fshoe-rack-drawer.png"
                                        }
                                    },
                                    "parent": "furniture-wood",
                                    "children": []
                                }, {
                                    "name": "تخت و سرویس خواب",
                                    "slug": "bed-service",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "bed-service",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbed-service.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbed-service.png"
                                        }
                                    },
                                    "parent": "furniture-wood",
                                    "children": []
                                }, {
                                    "name": "میز تلفن",
                                    "slug": "phone-desk",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "phone-desk",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fphone-desk.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fphone-desk.png"
                                        }
                                    },
                                    "parent": "furniture-wood",
                                    "children": []
                                }, {
                                    "name": "میز تلویزیون",
                                    "slug": "tv-stand",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "tv-stand",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ftv-stand.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ftv-stand.png"
                                        }
                                    },
                                    "parent": "furniture-wood",
                                    "children": []
                                }, {
                                    "name": "میز تحریر و کامپیوتر",
                                    "slug": "desk",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "desk",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fdesk.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fdesk.png"
                                        }
                                    },
                                    "parent": "furniture-wood",
                                    "children": []
                                }, {
                                    "name": "مبلمان اداری",
                                    "slug": "office-decoration",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "office-decoration",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Foffice-decoration.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Foffice-decoration.png"
                                        }
                                    },
                                    "parent": "furniture-wood",
                                    "children": []
                                }, {
                                    "name": "صندلی و نیمکت",
                                    "slug": "chair-bench",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "chair-bench",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fchair-bench.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fchair-bench.png"
                                        }
                                    },
                                    "parent": "furniture-wood",
                                    "children": []
                                }]
                            }, {
                                "name": "نور و روشنایی",
                                "slug": "home-lighting",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "home-lighting",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fhome-lighting.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fhome-lighting.png"
                                    }
                                },
                                "parent": "home-kitchen",
                                "children": [{
                                    "name": "لوستر و چراغ آویز",
                                    "slug": "chandeliers",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "chandeliers",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fchandeliers.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fchandeliers.png"
                                        }
                                    },
                                    "parent": "home-lighting",
                                    "children": []
                                }, {
                                    "name": "چراغ خواب و آباژور",
                                    "slug": "lampshade",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "lampshade",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Flampshade.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Flampshade.png"
                                        }
                                    },
                                    "parent": "home-lighting",
                                    "children": []
                                }, {
                                    "name": "ریسه و چراغ تزئینی",
                                    "slug": "yarn-lights",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "yarn-lights",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fyarn-lights.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fyarn-lights.png"
                                        }
                                    },
                                    "parent": "home-lighting",
                                    "children": []
                                }, {
                                    "name": "لامپ و چراغ",
                                    "slug": "lamps",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "lamps",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Flamps.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Flamps.png"
                                        }
                                    },
                                    "parent": "home-lighting",
                                    "children": []
                                }]
                            }, {
                                "name": "فرش، گلیم، موکت",
                                "slug": "carpet-moquette",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "carpet-moquette",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcarpet-moquette.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcarpet-moquette.png"
                                    }
                                },
                                "parent": "home-kitchen",
                                "children": [{
                                    "name": "فرش",
                                    "slug": "carpet",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "carpet",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcarpet.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcarpet.png"
                                        }
                                    },
                                    "parent": "carpet-moquette",
                                    "children": []
                                }, {
                                    "name": "تابلو فرش",
                                    "slug": "pictorial-carpet",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "pictorial-carpet",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fpictorial-carpet.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fpictorial-carpet.png"
                                        }
                                    },
                                    "parent": "carpet-moquette",
                                    "children": []
                                }, {
                                    "name": "روفرشی",
                                    "slug": "rubber-carpet",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "rubber-carpet",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Frubber-carpet.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Frubber-carpet.png"
                                        }
                                    },
                                    "parent": "carpet-moquette",
                                    "children": []
                                }, {
                                    "name": "پادری",
                                    "slug": "mat",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "mat",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmat.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmat.png"
                                        }
                                    },
                                    "parent": "carpet-moquette",
                                    "children": []
                                }, {
                                    "name": "موکت",
                                    "slug": "moquette",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "moquette",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmoquette.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmoquette.png"
                                        }
                                    },
                                    "parent": "carpet-moquette",
                                    "children": []
                                }, {
                                    "name": "گلیم، جاجیم، گبه",
                                    "slug": "rugs-woolen-cloth",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "rugs-woolen-cloth",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Frugs-woolen-cloth.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Frugs-woolen-cloth.png"
                                        }
                                    },
                                    "parent": "carpet-moquette",
                                    "children": []
                                }, {
                                    "name": "پشتی",
                                    "slug": "lumbar-pillow",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "lumbar-pillow",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Flumbar-pillow.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Flumbar-pillow.png"
                                        }
                                    },
                                    "parent": "carpet-moquette",
                                    "children": []
                                }]
                            }, {
                                "name": "تشک، روتختی، رختخواب",
                                "slug": "sleep-goods",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "sleep-goods",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fsleep-goods.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fsleep-goods.png"
                                    }
                                },
                                "parent": "home-kitchen",
                                "children": [{
                                    "name": "رختخواب، بالش، پتو",
                                    "slug": "bed-pillow-blanket",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "bed-pillow-blanket",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbed-pillow-blanket.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbed-pillow-blanket.png"
                                        }
                                    },
                                    "parent": "sleep-goods",
                                    "children": []
                                }, {
                                    "name": "تشک تختخواب",
                                    "slug": "mattress",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "mattress",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmattress.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmattress.png"
                                        }
                                    },
                                    "parent": "sleep-goods",
                                    "children": []
                                }, {
                                    "name": "سرویس روتختی",
                                    "slug": "bed-sheet",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "bed-sheet",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbed-sheet.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbed-sheet.png"
                                        }
                                    },
                                    "parent": "sleep-goods",
                                    "children": []
                                }]
                            }, {
                                "name": "لوازم دکوری و تزئینی",
                                "slug": "decoration",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "decoration",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fdecoration.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fdecoration.png"
                                    }
                                },
                                "parent": "home-kitchen",
                                "children": [{
                                    "name": "پرده، رانر، رومیزی",
                                    "slug": "curtains-table-cover",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "curtains-table-cover",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcurtains-table-cover.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcurtains-table-cover.png"
                                        }
                                    },
                                    "parent": "decoration",
                                    "children": []
                                }, {
                                    "name": "آینه",
                                    "slug": "mirror",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "mirror",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmirror.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmirror.png"
                                        }
                                    },
                                    "parent": "decoration",
                                    "children": []
                                }, {
                                    "name": "ساعت دیواری و تزئینی",
                                    "slug": "wall-clock",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "wall-clock",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fwall-clock.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fwall-clock.png"
                                        }
                                    },
                                    "parent": "decoration",
                                    "children": []
                                }, {
                                    "name": "تابلو، نقاشی، عکس",
                                    "slug": "paintings-picture",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "paintings-picture",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fpaintings-picture.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fpaintings-picture.png"
                                        }
                                    },
                                    "parent": "decoration",
                                    "children": []
                                }, {
                                    "name": "مجسمه، تندیس، ماکت",
                                    "slug": "figurines",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "figurines",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ffigurines.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ffigurines.png"
                                        }
                                    },
                                    "parent": "decoration",
                                    "children": []
                                }, {
                                    "name": "گل مصنوعی",
                                    "slug": "artificial-flower",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "artificial-flower",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fartificial-flower.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fartificial-flower.png"
                                        }
                                    },
                                    "parent": "decoration",
                                    "children": []
                                }, {
                                    "name": "گل و گیاه طبیعی",
                                    "slug": "natural-plants",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "natural-plants",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fnatural-plants.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fnatural-plants.png"
                                        }
                                    },
                                    "parent": "decoration",
                                    "children": []
                                }, {
                                    "name": "صنایع دستی و سایر لوازم تزئینی",
                                    "slug": "crafts",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "crafts",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcrafts.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcrafts.png"
                                        }
                                    },
                                    "parent": "decoration",
                                    "children": []
                                }]
                            }, {
                                "name": "تهویه، سرمایش، گرمایش",
                                "slug": "ventilation-cooling-heating",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "ventilation-cooling-heating",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fventilation-cooling-heating.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fventilation-cooling-heating.png"
                                    }
                                },
                                "parent": "home-kitchen",
                                "children": [{
                                    "name": "آبگرمکن، پکیج، شوفاژ",
                                    "slug": "water-heater-package-radiator",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "water-heater-package-radiator",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fwater_heater_package_radiator.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fwater_heater_package_radiator.png"
                                        }
                                    },
                                    "parent": "ventilation-cooling-heating",
                                    "children": []
                                }, {
                                    "name": "بخاری، هیتر، شومینه",
                                    "slug": "stoves-heaters-fireplaces",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "stoves-heaters-fireplaces",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fstoves_heaters_fireplaces.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fstoves_heaters_fireplaces.png"
                                        }
                                    },
                                    "parent": "ventilation-cooling-heating",
                                    "children": []
                                }, {
                                    "name": "کولر آبی",
                                    "slug": "water-cooler",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "water-cooler",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fwater-cooler.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fwater-cooler.png"
                                        }
                                    },
                                    "parent": "ventilation-cooling-heating",
                                    "children": []
                                }, {
                                    "name": "کولر گازی و فن‌کوئل",
                                    "slug": "air-conditioning-fan-coil",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "air-conditioning-fan-coil",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fair-conditioning-fan-coil.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fair-conditioning-fan-coil.png"
                                        }
                                    },
                                    "parent": "ventilation-cooling-heating",
                                    "children": []
                                }, {
                                    "name": "پنکه و تصفیه‌کنندهٔ هوا",
                                    "slug": "fan-ventilator-humidifier",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "fan-ventilator-humidifier",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ffan-ventilator-humidifier.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ffan-ventilator-humidifier.png"
                                        }
                                    },
                                    "parent": "ventilation-cooling-heating",
                                    "children": []
                                }]
                            }, {
                                "name": "شست‌وشو و نظافت",
                                "slug": "washing-cleaning",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "washing-cleaning",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fwashing-cleaning.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fwashing-cleaning.png"
                                    }
                                },
                                "parent": "home-kitchen",
                                "children": [{
                                    "name": "مواد شوینده و دستمال کاغذی",
                                    "slug": "detergent-tissue",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "detergent-tissue",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fdetergent-tissue.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fdetergent-tissue.png"
                                        }
                                    },
                                    "parent": "washing-cleaning",
                                    "children": []
                                }, {
                                    "name": "لوازم نظافت",
                                    "slug": "cleaning-supplies",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "cleaning-supplies",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcleaning-supplies.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcleaning-supplies.png"
                                        }
                                    },
                                    "parent": "washing-cleaning",
                                    "children": []
                                }, {
                                    "name": "بندرخت و رخت‌آویز",
                                    "slug": "clothes-rack",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "clothes-rack",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fclothes-rack.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fclothes-rack.png"
                                        }
                                    },
                                    "parent": "washing-cleaning",
                                    "children": []
                                }]
                            }, {
                                "name": "حمام و سرویس بهداشتی",
                                "slug": "bathrooms",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "bathrooms",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbathrooms.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbathrooms.png"
                                    }
                                },
                                "parent": "home-kitchen",
                                "children": [{
                                    "name": "لوازم حمام",
                                    "slug": "bathroom-accessories",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "bathroom-accessories",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbathroom-accessories.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbathroom-accessories.png"
                                        }
                                    },
                                    "parent": "bathrooms",
                                    "children": []
                                }, {
                                    "name": "لوازم سرویس بهداشتی",
                                    "slug": "wc-accessories",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "wc-accessories",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fwc-accessories.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fwc-accessories.png"
                                        }
                                    },
                                    "parent": "bathrooms",
                                    "children": []
                                }]
                            }]
                        }, {
                            "name": "خدمات",
                            "slug": "services",
                            "icon": {
                                "iconColor": "rgb(var(--content-neutral-default))",
                                "iconName": "cat-services",
                                "iconURL": {
                                    "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcat_services.png",
                                    "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcat_services.png"
                                }
                            },
                            "parent": "ROOT",
                            "children": [{
                                "name": "خودرو و موتورسیکلت",
                                "slug": "car-and-motor",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "car-and-motor",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcar-and-motor.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcar-and-motor.png"
                                    }
                                },
                                "parent": "services",
                                "children": []
                            }, {
                                "name": "پذیرایی، مراسم",
                                "slug": "catering",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "catering",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcatering.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcatering.png"
                                    }
                                },
                                "parent": "services",
                                "children": []
                            }, {
                                "name": "رایانه‌ای و موبایل",
                                "slug": "computer-and-mobile",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "computer-and-mobile",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcomputer-and-mobile.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcomputer-and-mobile.png"
                                    }
                                },
                                "parent": "services",
                                "children": []
                            }, {
                                "name": "مالی، حقوقی و اداری",
                                "slug": "accounting-and-finance",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "accounting-and-finance",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Faccounting-and-finance.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Faccounting-and-finance.png"
                                    }
                                },
                                "parent": "services",
                                "children": []
                            }, {
                                "name": "حمل و نقل",
                                "slug": "transport",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "transport",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ftransport.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ftransport.png"
                                    }
                                },
                                "parent": "services",
                                "children": []
                            }, {
                                "name": "پیشه و مهارت",
                                "slug": "craftsmen",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "craftsmen",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcraftsmen.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcraftsmen.png"
                                    }
                                },
                                "parent": "services",
                                "children": []
                            }, {
                                "name": "زیبایی و سلامت",
                                "slug": "beauty-and-haircare",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "beauty-and-haircare",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbeauty-and-haircare.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbeauty-and-haircare.png"
                                    }
                                },
                                "parent": "services",
                                "children": []
                            }, {
                                "name": "نظافت",
                                "slug": "cleaning",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "cleaning",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcleaning.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcleaning.png"
                                    }
                                },
                                "parent": "services",
                                "children": []
                            }, {
                                "name": "باغبانی و درختکاری",
                                "slug": "garden-and-landscaping",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "garden-and-landscaping",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fgarden-and-landscaping.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fgarden-and-landscaping.png"
                                    }
                                },
                                "parent": "services",
                                "children": []
                            }, {
                                "name": "آموزشی",
                                "slug": "teaching",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "teaching",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fteaching.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fteaching.png"
                                    }
                                },
                                "parent": "services",
                                "children": []
                            }]
                        }, {
                            "name": "وسایل شخصی",
                            "slug": "personal",
                            "icon": {
                                "iconColor": "rgb(var(--content-neutral-default))",
                                "iconName": "cat-personal",
                                "iconURL": {
                                    "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcat_personal.png",
                                    "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcat_personal.png"
                                }
                            },
                            "parent": "ROOT",
                            "children": [{
                                "name": "کیف، کفش، لباس",
                                "slug": "clothing-and-shoes",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "clothing-and-shoes",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fclothing-and-shoes.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fclothing-and-shoes.png"
                                    }
                                },
                                "parent": "personal",
                                "children": [{
                                    "name": "کیف، کفش، کمربند",
                                    "slug": "shoes-belt-bag",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "shoes-belt-bag",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fshoes-belt-bag.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fshoes-belt-bag.png"
                                        }
                                    },
                                    "parent": "clothing-and-shoes",
                                    "children": []
                                }, {
                                    "name": "لباس",
                                    "slug": "clothing",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "clothing",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fclothing.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fclothing.png"
                                        }
                                    },
                                    "parent": "clothing-and-shoes",
                                    "children": []
                                }]
                            }, {
                                "name": "زیورآلات و اکسسوری",
                                "slug": "jewelry-and-watches",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "jewelry-and-watches",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fjewelry-and-watches.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fjewelry-and-watches.png"
                                    }
                                },
                                "parent": "personal",
                                "children": [{
                                    "name": "ساعت",
                                    "slug": "watches",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "watches",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fwatches.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fwatches.png"
                                        }
                                    },
                                    "parent": "jewelry-and-watches",
                                    "children": []
                                }, {
                                    "name": "جواهرات",
                                    "slug": "jewelry",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "jewelry",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fjewelry.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fjewelry.png"
                                        }
                                    },
                                    "parent": "jewelry-and-watches",
                                    "children": []
                                }, {
                                    "name": "بدلیجات",
                                    "slug": "rhinestones",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "rhinestones",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Frhinestones.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Frhinestones.png"
                                        }
                                    },
                                    "parent": "jewelry-and-watches",
                                    "children": []
                                }]
                            }, {
                                "name": "آرایشی، بهداشتی، درمانی",
                                "slug": "health-beauty",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "health-beauty",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fhealth-beauty.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fhealth-beauty.png"
                                    }
                                },
                                "parent": "personal",
                                "children": []
                            }, {
                                "name": "وسایل بچه و اسباب‌بازی",
                                "slug": "baby-and-toys",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "baby-and-toys",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbaby-and-toys.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbaby-and-toys.png"
                                    }
                                },
                                "parent": "personal",
                                "children": [{
                                    "name": "اسباب‌بازی بچه",
                                    "slug": "personal-toys",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "personal-toys",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fpersonal-toys.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fpersonal-toys.png"
                                        }
                                    },
                                    "parent": "baby-and-toys",
                                    "children": []
                                }, {
                                    "name": "کالسکه و لوازم جانبی",
                                    "slug": "strollers-and-accessories",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "strollers-and-accessories",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fstrollers-and-accessories.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fstrollers-and-accessories.png"
                                        }
                                    },
                                    "parent": "baby-and-toys",
                                    "children": []
                                }, {
                                    "name": "تخت و صندلی بچه",
                                    "slug": "child-car-seat",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "child-car-seat",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fchild-car-seat.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fchild-car-seat.png"
                                        }
                                    },
                                    "parent": "baby-and-toys",
                                    "children": []
                                }, {
                                    "name": "اسباب و اثاث بچه",
                                    "slug": "childrens-furniture",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "childrens-furniture",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fchildrens-furniture.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fchildrens-furniture.png"
                                        }
                                    },
                                    "parent": "baby-and-toys",
                                    "children": []
                                }]
                            }, {
                                "name": "کفش و لباس بچه",
                                "slug": "childrens-clothing-and-shoe",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "childrens-clothing-and-shoe",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fchildrens-clothing-and-shoe.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fchildrens-clothing-and-shoe.png"
                                    }
                                },
                                "parent": "personal",
                                "children": []
                            }, {
                                "name": "لوازم التحریر",
                                "slug": "stationery",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "stationery",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fstationery.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fstationery.png"
                                    }
                                },
                                "parent": "personal",
                                "children": []
                            }]
                        }, {
                            "name": "سرگرمی و فراغت",
                            "slug": "leisure-hobbies",
                            "icon": {
                                "iconColor": "rgb(var(--content-neutral-default))",
                                "iconName": "cat-leisure-hobbies",
                                "iconURL": {
                                    "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcat_leisure_hobbies.png",
                                    "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcat_leisure_hobbies.png"
                                }
                            },
                            "parent": "ROOT",
                            "children": [{
                                "name": "بلیت",
                                "slug": "ticket",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "ticket",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fticket.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fticket.png"
                                    }
                                },
                                "parent": "leisure-hobbies",
                                "children": [{
                                    "name": "کنسرت",
                                    "slug": "concert",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "concert",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fconcert.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fconcert.png"
                                        }
                                    },
                                    "parent": "ticket",
                                    "children": []
                                }, {
                                    "name": "تئاتر و سینما",
                                    "slug": "theatre-and-cinema",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "theatre-and-cinema",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ftheatre-and-cinema.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ftheatre-and-cinema.png"
                                        }
                                    },
                                    "parent": "ticket",
                                    "children": []
                                }, {
                                    "name": "کارت هدیه و تخفیف",
                                    "slug": "gift-certificate",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "gift-certificate",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fgift-certificate.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fgift-certificate.png"
                                        }
                                    },
                                    "parent": "ticket",
                                    "children": []
                                }, {
                                    "name": "مسابقه‌ها و مکان‌های ورزشی",
                                    "slug": "tickets-sports",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "tickets-sports",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ftickets-sports.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ftickets-sports.png"
                                        }
                                    },
                                    "parent": "ticket",
                                    "children": []
                                }, {
                                    "name": "ورزشی",
                                    "slug": "sport",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "sport",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fsport.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fsport.png"
                                        }
                                    },
                                    "parent": "ticket",
                                    "children": []
                                }, {
                                    "name": "اتوبوس، مترو، قطار",
                                    "slug": "bus-metro-train",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "bus-metro-train",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbus-metro-train.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbus-metro-train.png"
                                        }
                                    },
                                    "parent": "ticket",
                                    "children": []
                                }]
                            }, {
                                "name": "تور و چارتر",
                                "slug": "travel-packages",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "travel-packages",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ftravel_packages.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ftravel_packages.png"
                                    }
                                },
                                "parent": "leisure-hobbies",
                                "children": []
                            }, {
                                "name": "دوچرخه، اسکیت، اسکوتر",
                                "slug": "bicycle",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "bicycle",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbicycle.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbicycle.png"
                                    }
                                },
                                "parent": "leisure-hobbies",
                                "children": []
                            }, {
                                "name": "کتاب و مجله",
                                "slug": "book-student-literature",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "book-student-literature",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbook-student-literature.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbook-student-literature.png"
                                    }
                                },
                                "parent": "leisure-hobbies",
                                "children": [{
                                    "name": "آموزشی",
                                    "slug": "educational",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "educational",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Feducational.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Feducational.png"
                                        }
                                    },
                                    "parent": "book-student-literature",
                                    "children": []
                                }, {
                                    "name": "ادبی",
                                    "slug": "literary",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "literary",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fliterary.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fliterary.png"
                                        }
                                    },
                                    "parent": "book-student-literature",
                                    "children": []
                                }, {
                                    "name": "تاریخی",
                                    "slug": "historical",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "historical",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fhistorical.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fhistorical.png"
                                        }
                                    },
                                    "parent": "book-student-literature",
                                    "children": []
                                }, {
                                    "name": "مذهبی",
                                    "slug": "religious",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "religious",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Freligious.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Freligious.png"
                                        }
                                    },
                                    "parent": "book-student-literature",
                                    "children": []
                                }, {
                                    "name": "مجلات",
                                    "slug": "magazines",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "magazines",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmagazines.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmagazines.png"
                                        }
                                    },
                                    "parent": "book-student-literature",
                                    "children": []
                                }]
                            }, {
                                "name": "حیوانات",
                                "slug": "animals",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "animals",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fanimals.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fanimals.png"
                                    }
                                },
                                "parent": "leisure-hobbies",
                                "children": [{
                                    "name": "گربه",
                                    "slug": "cat",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "cat",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcat.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcat.png"
                                        }
                                    },
                                    "parent": "animals",
                                    "children": []
                                }, {
                                    "name": "موش و خرگوش",
                                    "slug": "rodents-rabbits",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "rodents-rabbits",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Frodents-rabbits.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Frodents-rabbits.png"
                                        }
                                    },
                                    "parent": "animals",
                                    "children": []
                                }, {
                                    "name": "خزنده",
                                    "slug": "reptile",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "reptile",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Freptile.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Freptile.png"
                                        }
                                    },
                                    "parent": "animals",
                                    "children": []
                                }, {
                                    "name": "پرنده",
                                    "slug": "birds",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "birds",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbirds.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbirds.png"
                                        }
                                    },
                                    "parent": "animals",
                                    "children": []
                                }, {
                                    "name": "ماهی",
                                    "slug": "fish",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "fish",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ffish.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ffish.png"
                                        }
                                    },
                                    "parent": "animals",
                                    "children": []
                                }, {
                                    "name": "لوازم جانبی",
                                    "slug": "accessories",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "accessories",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Faccessories.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Faccessories.png"
                                        }
                                    },
                                    "parent": "animals",
                                    "children": []
                                }, {
                                    "name": "حیوانات مزرعه",
                                    "slug": "farm-animals",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "farm-animals",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ffarm-animals.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ffarm-animals.png"
                                        }
                                    },
                                    "parent": "animals",
                                    "children": []
                                }, {
                                    "name": "سگ",
                                    "slug": "dog",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "dog",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fdog.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fdog.png"
                                        }
                                    },
                                    "parent": "animals",
                                    "children": []
                                }]
                            }, {
                                "name": "کلکسیون و سرگرمی",
                                "slug": "hobby-collectibles",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "hobby-collectibles",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fhobby-collectibles.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fhobby-collectibles.png"
                                    }
                                },
                                "parent": "leisure-hobbies",
                                "children": [{
                                    "name": "سکه، تمبر، اسکناس",
                                    "slug": "coin-stamp",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "coin-stamp",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcoin-stamp.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcoin-stamp.png"
                                        }
                                    },
                                    "parent": "hobby-collectibles",
                                    "children": []
                                }, {
                                    "name": "اشیاء عتیقه",
                                    "slug": "historical-objects",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "historical-objects",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fhistorical-objects.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fhistorical-objects.png"
                                        }
                                    },
                                    "parent": "hobby-collectibles",
                                    "children": []
                                }]
                            }, {
                                "name": "آلات موسیقی",
                                "slug": "musical-instruments",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "musical-instruments",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmusical-instruments.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmusical-instruments.png"
                                    }
                                },
                                "parent": "leisure-hobbies",
                                "children": [{
                                    "name": "گیتار، بیس، امپلیفایر",
                                    "slug": "guitar-bass-amplifier",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "guitar-bass-amplifier",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fguitar-bass-amplifier.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fguitar-bass-amplifier.png"
                                        }
                                    },
                                    "parent": "musical-instruments",
                                    "children": []
                                }, {
                                    "name": "سازهای بادی",
                                    "slug": "wind",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "wind",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fwind.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fwind.png"
                                        }
                                    },
                                    "parent": "musical-instruments",
                                    "children": []
                                }, {
                                    "name": "پیانو، کیبورد، آکاردئون",
                                    "slug": "piano-keyboard",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "piano-keyboard",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fpiano-keyboard.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fpiano-keyboard.png"
                                        }
                                    },
                                    "parent": "musical-instruments",
                                    "children": []
                                }, {
                                    "name": "سازهای سنتی",
                                    "slug": "traditional",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "traditional",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ftraditional.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ftraditional.png"
                                        }
                                    },
                                    "parent": "musical-instruments",
                                    "children": []
                                }, {
                                    "name": "درام و پرکاشن",
                                    "slug": "drums-percussion",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "drums-percussion",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fdrums-percussion.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fdrums-percussion.png"
                                        }
                                    },
                                    "parent": "musical-instruments",
                                    "children": []
                                }, {
                                    "name": "ویولن",
                                    "slug": "violins",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "violins",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fviolins.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fviolins.png"
                                        }
                                    },
                                    "parent": "musical-instruments",
                                    "children": []
                                }]
                            }, {
                                "name": "ورزش و تناسب اندام",
                                "slug": "sport-leisure",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "sport-leisure",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fsport-leisure.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fsport-leisure.png"
                                    }
                                },
                                "parent": "leisure-hobbies",
                                "children": [{
                                    "name": "ورزش‌های توپی",
                                    "slug": "ball-sports",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "ball-sports",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fball-sports.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fball-sports.png"
                                        }
                                    },
                                    "parent": "sport-leisure",
                                    "children": []
                                }, {
                                    "name": "کوهنوردی و کمپینگ",
                                    "slug": "camping-outdoor",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "camping-outdoor",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcamping-outdoor.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcamping-outdoor.png"
                                        }
                                    },
                                    "parent": "sport-leisure",
                                    "children": []
                                }, {
                                    "name": "غواصی و ورزش‌های آبی",
                                    "slug": "diving-watersports",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "diving-watersports",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fdiving-watersports.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fdiving-watersports.png"
                                        }
                                    },
                                    "parent": "sport-leisure",
                                    "children": []
                                }, {
                                    "name": "ماهیگیری",
                                    "slug": "fishing",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "fishing",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ffishing.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ffishing.png"
                                        }
                                    },
                                    "parent": "sport-leisure",
                                    "children": []
                                }, {
                                    "name": "تجهیزات ورزشی",
                                    "slug": "training",
                                    "icon": {},
                                    "parent": "sport-leisure",
                                    "children": []
                                }, {
                                    "name": "ورزش‌های زمستانی",
                                    "slug": "winter-sports",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "winter-sports",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fwinter-sports.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fwinter-sports.png"
                                        }
                                    },
                                    "parent": "sport-leisure",
                                    "children": []
                                }, {
                                    "name": "اسب و تجهیزات اسب‌سواری",
                                    "slug": "horses-equestrian",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "horses-equestrian",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fhorses-equestrian.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fhorses-equestrian.png"
                                        }
                                    },
                                    "parent": "sport-leisure",
                                    "children": []
                                }]
                            }, {
                                "name": "اسباب‌‌بازی",
                                "slug": "leisure-hobbies-toys",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "leisure-hobbies-toys",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fleisure-hobbies-toys.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fleisure-hobbies-toys.png"
                                    }
                                },
                                "parent": "leisure-hobbies",
                                "children": []
                            }]
                        }, {
                            "name": "اجتماعی",
                            "slug": "community",
                            "icon": {
                                "iconColor": "rgb(var(--content-neutral-default))",
                                "iconName": "community",
                                "iconURL": {
                                    "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcommunity.png",
                                    "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcommunity.png"
                                }
                            },
                            "parent": "ROOT",
                            "children": [{
                                "name": "رویداد",
                                "slug": "event",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "event",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fevent.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fevent.png"
                                    }
                                },
                                "parent": "community",
                                "children": [{
                                    "name": "حراج",
                                    "slug": "for-sale",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "for-sale",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ffor-sale.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ffor-sale.png"
                                        }
                                    },
                                    "parent": "event",
                                    "children": []
                                }, {
                                    "name": "گردهمایی و همایش",
                                    "slug": "conference-meeting",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "conference-meeting",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fconference-meeting.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fconference-meeting.png"
                                        }
                                    },
                                    "parent": "event",
                                    "children": []
                                }, {
                                    "name": "ورزشی",
                                    "slug": "events-sports",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "events-sports",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fevents-sports.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fevents-sports.png"
                                        }
                                    },
                                    "parent": "event",
                                    "children": []
                                }]
                            }, {
                                "name": "داوطلبانه",
                                "slug": "volunteers",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "volunteers",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fvolunteers.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fvolunteers.png"
                                    }
                                },
                                "parent": "community",
                                "children": [{
                                    "name": "سفر اشتراکی",
                                    "slug": "ride-sharing",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "ride-sharing",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fride_sharing.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fride_sharing.png"
                                        }
                                    },
                                    "parent": "volunteers",
                                    "children": []
                                }, {
                                    "name": "تحقیقاتی",
                                    "slug": "research",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "research",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fresearch.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fresearch.png"
                                        }
                                    },
                                    "parent": "volunteers",
                                    "children": []
                                }]
                            }, {
                                "name": "گم‌شده‌ها",
                                "slug": "lost-and-found",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "lost-and-found",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Flost-and-found.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Flost-and-found.png"
                                    }
                                },
                                "parent": "community",
                                "children": [{
                                    "name": "حیوانات",
                                    "slug": "lost-animals",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "lost-animals",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Flost-animals.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Flost-animals.png"
                                        }
                                    },
                                    "parent": "lost-and-found",
                                    "children": []
                                }, {
                                    "name": "اشیا",
                                    "slug": "lost-things",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "lost-things",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Flost-things.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Flost-things.png"
                                        }
                                    },
                                    "parent": "lost-and-found",
                                    "children": []
                                }]
                            }]
                        }, {
                            "name": "تجهیزات و صنعتی",
                            "slug": "tools-materials-equipment",
                            "icon": {
                                "iconColor": "rgb(var(--content-neutral-default))",
                                "iconName": "cat-businesses",
                                "iconURL": {
                                    "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcat_businesses.png",
                                    "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcat_businesses.png"
                                }
                            },
                            "parent": "ROOT",
                            "children": [{
                                "name": "مصالح و تجهیزات ساختمان",
                                "slug": "building-equipment",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "building-equipment",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbuilding-equipment.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbuilding-equipment.png"
                                    }
                                },
                                "parent": "tools-materials-equipment",
                                "children": []
                            }, {
                                "name": "ابزارآلات",
                                "slug": "toolbox",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "toolbox",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ftoolbox.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ftoolbox.png"
                                    }
                                },
                                "parent": "tools-materials-equipment",
                                "children": []
                            }, {
                                "name": "ماشین‌آلات صنعتی",
                                "slug": "industrial-machinery",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "industrial-machinery",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Findustrial-machinery.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Findustrial-machinery.png"
                                    }
                                },
                                "parent": "tools-materials-equipment",
                                "children": []
                            }, {
                                "name": "تجهیزات کسب‌وکار",
                                "slug": "work-equipment",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "work-equipment",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fwork-equipment.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fwork-equipment.png"
                                    }
                                },
                                "parent": "tools-materials-equipment",
                                "children": [{
                                    "name": "پزشکی",
                                    "slug": "medical-equipment",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "medical-equipment",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmedical-equipment.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmedical-equipment.png"
                                        }
                                    },
                                    "parent": "work-equipment",
                                    "children": []
                                }, {
                                    "name": "فروشگاه و مغازه",
                                    "slug": "shop-and-cash",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "shop-and-cash",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fshop-and-cash.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fshop-and-cash.png"
                                        }
                                    },
                                    "parent": "work-equipment",
                                    "children": []
                                }, {
                                    "name": "کافی‌شاپ و رستوران",
                                    "slug": "cafe-and-restaurant",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "cafe-and-restaurant",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcafe-and-restaurant.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcafe-and-restaurant.png"
                                        }
                                    },
                                    "parent": "work-equipment",
                                    "children": []
                                }, {
                                    "name": "آرایشگاه و سالن‌های زیبایی",
                                    "slug": "barbershop-and-beautysalon",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "barbershop-and-beautysalon",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbarbershop-and-beautysalon.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbarbershop-and-beautysalon.png"
                                        }
                                    },
                                    "parent": "work-equipment",
                                    "children": []
                                }, {
                                    "name": "دفتر کار",
                                    "slug": "offices",
                                    "icon": {
                                        "iconColor": "rgb(var(--content-neutral-default))",
                                        "iconName": "offices",
                                        "iconURL": {
                                            "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Foffices.png",
                                            "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Foffices.png"
                                        }
                                    },
                                    "parent": "work-equipment",
                                    "children": []
                                }]
                            }, {
                                "name": "عمده‌فروشی",
                                "slug": "batch",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "batch",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fbatch.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fbatch.png"
                                    }
                                },
                                "parent": "tools-materials-equipment",
                                "children": []
                            }]
                        }, {
                            "name": "استخدام و کاریابی",
                            "slug": "jobs",
                            "icon": {
                                "iconColor": "rgb(var(--content-neutral-default))",
                                "iconName": "cat-jobs",
                                "iconURL": {
                                    "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcat_jobs.png",
                                    "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcat_jobs.png"
                                }
                            },
                            "parent": "ROOT",
                            "children": [{
                                "name": "اداری و مدیریت",
                                "slug": "administration-and-hr",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "administration-and-hr",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fadministration-and-hr.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fadministration-and-hr.png"
                                    }
                                },
                                "parent": "jobs",
                                "children": []
                            }, {
                                "name": "سرایداری و نظافت",
                                "slug": "janitorial-cleaning",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "janitorial-cleaning",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fjanitorial-cleaning.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fjanitorial-cleaning.png"
                                    }
                                },
                                "parent": "jobs",
                                "children": []
                            }, {
                                "name": "معماری، عمران و ساختمانی",
                                "slug": "construction-craft",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "construction-craft",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fconstruction-craft.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fconstruction-craft.png"
                                    }
                                },
                                "parent": "jobs",
                                "children": []
                            }, {
                                "name": "خدمات فروشگاه و رستوران",
                                "slug": "shop-restaurant",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "shop-restaurant",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fshop-restaurant.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fshop-restaurant.png"
                                    }
                                },
                                "parent": "jobs",
                                "children": []
                            }, {
                                "name": "رایانه و فناوری اطلاعات",
                                "slug": "computer-and-it",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "computer-and-it",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcomputer-and-it.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcomputer-and-it.png"
                                    }
                                },
                                "parent": "jobs",
                                "children": []
                            }, {
                                "name": "مالی، حسابداری، حقوقی",
                                "slug": "accounting-finance-legal",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "accounting-finance-legal",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Faccounting-finance-legal.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Faccounting-finance-legal.png"
                                    }
                                },
                                "parent": "jobs",
                                "children": []
                            }, {
                                "name": "بازاریابی و فروش",
                                "slug": "sales-marketing",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "sales-marketing",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fsales-marketing.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fsales-marketing.png"
                                    }
                                },
                                "parent": "jobs",
                                "children": []
                            }, {
                                "name": "صنعتی، فنی، مهندسی",
                                "slug": "industrial-technology",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "industrial-technology",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Findustrial-technology.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Findustrial-technology.png"
                                    }
                                },
                                "parent": "jobs",
                                "children": []
                            }, {
                                "name": "آموزشی",
                                "slug": "education",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "education",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Feducation.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Feducation.png"
                                    }
                                },
                                "parent": "jobs",
                                "children": []
                            }, {
                                "name": "حمل و نقل",
                                "slug": "transportation",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "transportation",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Ftransportation.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Ftransportation.png"
                                    }
                                },
                                "parent": "jobs",
                                "children": []
                            }, {
                                "name": "درمانی، زیبایی، بهداشتی",
                                "slug": "care-health-beauty",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "care-health-beauty",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcare-health-beauty.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcare-health-beauty.png"
                                    }
                                },
                                "parent": "jobs",
                                "children": []
                            }, {
                                "name": "هنری و رسانه",
                                "slug": "media-advertising",
                                "icon": {
                                    "iconColor": "rgb(var(--content-neutral-default))",
                                    "iconName": "media-advertising",
                                    "iconURL": {
                                        "light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmedia-advertising.png",
                                        "dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmedia-advertising.png"
                                    }
                                },
                                "parent": "jobs",
                                "children": []
                            }]
                        }]
                    },
                    "realTimeQuery": "",
                    "categoriesHasError": false,
                    "shouldSelectCategory": null,
                    "searchData": {
                        "query": "",
                        "page": "",
                        "formData": {}
                    },
                    "showSearchAssistantSuggestion": false
                },
                "navBar": {
                    "hasSubmit": true,
                    "hasSupport": true,
                    "hasChat": true,
                    "hasSearch": true,
                    "hasNavTitle": false,
                    "hasMyDivar": true,
                    "hasCategories": true,
                    "hasSelectCity": true,
                    "hasSearchAssistant": false,
                    "hasSearchAssistantTitle": false,
                    "shouldShowShadow": true
                },
                "note": {
                    "hasNote": false,
                    "syncCount": 0
                },
                "appMeta": {
                    "cityChanged": false,
                    "isSearchEngine": false,
                    "ip": "94.182.216.58",
                    "realIP": "94.182.216.58, 127.0.0.6",
                    "isWebView": false,
                    "error": null
                },
                "currentPost": {
                    "renderPostSuccess": true,
                    "sourceType": "direct_link",
                    "getContactBlocked": false,
                    "getContactBlockedError": null,
                    "post": {
                        "seo": {
                            "title": "فروش ۹۷ متر ۲ خواب دونبش __ دید ابدی در تهران - ۲۱ شهریور ۱۴۰۵",
                            "description": "آگهی ۹۷ متر ۲ خواب دونبش __ دید ابدی در دیوار تهران",
                            "androidPackageName": "ir.divar",
                            "androidAppUrl": "android-app:\u002F\u002Fir.divar\u002Fhttp\u002Fv\u002F۹۷ متر ۲ خواب دونبش __ دید ابدی\u002Fgap5-Twe\u002F",
                            "webInfo": {
                                "title": "۹۷ متر ۲ خواب دونبش __ دید ابدی",
                                "district_persian": "یوسف‌آباد",
                                "city_persian": "تهران",
                                "category_slug_persian": "فروش آپارتمان"
                            },
                            "unavailableAfter": "2026-09-28T15:43:16.906208",
                            "breadcrumbs": [{
                                "name": "فروش آپارتمان",
                                "searchData": {
                                    "formData": {
                                        "category": {
                                            "str": {
                                                "value": "apartment-sell"
                                            }
                                        },
                                        "districts": {
                                            "repeated_string": {
                                                "value": ["90"]
                                            }
                                        }
                                    }
                                }
                            }, {
                                "name": "فروش مسکونی",
                                "searchData": {
                                    "formData": {
                                        "category": {
                                            "str": {
                                                "value": "residential-sell"
                                            }
                                        },
                                        "districts": {
                                            "repeated_string": {
                                                "value": ["90"]
                                            }
                                        }
                                    }
                                }
                            }, {
                                "name": "املاک",
                                "searchData": {
                                    "formData": {
                                        "category": {
                                            "str": {
                                                "value": "real-estate"
                                            }
                                        },
                                        "districts": {
                                            "repeated_string": {
                                                "value": ["90"]
                                            }
                                        }
                                    }
                                }
                            }, {
                                "name": "یوسف‌آباد",
                                "searchData": {
                                    "formData": {
                                        "districts": {
                                            "repeated_string": {
                                                "value": ["90"]
                                            }
                                        }
                                    }
                                }
                            }, {
                                "name": "1",
                                "searchData": {
                                    "formData": {}
                                }
                            }, {
                                "name": "دیوار",
                                "searchData": {
                                    "formData": {}
                                }
                            }],
                            "imageUrl": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fphoto\u002Fneda\u002Fpost\u002FxutSkDxwRixlf2on5wYEKA\u002F43cff8b2-eb49-4012-8e90-3f565fc0ef29.jpg"
                        },
                        "city": {
                            "id": "1",
                            "slug": "tehran",
                            "parent": "904",
                            "name": "تهران"
                        },
                        "contact": {
                            "apply_enabled": false,
                            "contact_encrypted_data": "",
                            "action_log": {
                                "server_side_info": {
                                    "info": {
                                        "@type": "type.googleapis.com\u002Faction_log.ContactInfoInfo",
                                        "post_token": "gap5-Twe",
                                        "source_view": "",
                                        "event_id": "",
                                        "method_name": "GetContactWeb",
                                        "experimental_api_enabled": false,
                                        "contact_uuid": "fa14acdb-a631-4243-9a20-2058c0258ff6",
                                        "contact_layer_experiment_id": 0,
                                        "tracker_session_id": "",
                                        "call_method": "UNKNOWN"
                                    },
                                    "item_type": {
                                        "type": "CONTACT_INFO"
                                    }
                                },
                                "enabled": true
                            },
                            "tracker_session_id": "",
                            "shopLinkEnabled": false,
                            "chatEnabled": false,
                            "chatAssistantEnabled": false,
                            "isExperimentEnabled": false,
                            "suspicionAlert": null,
                            "mainButtonOverride": {},
                            "contactUUID": "fa14acdb-a631-4243-9a20-2058c0258ff6",
                            "isSecureCallEnabled": false
                        },
                        "loading": false,
                        "token": "gap5-Twe",
                        "analytics": {
                            "cat1": "real-estate",
                            "cat2": "residential-sell",
                            "cat3": "apartment-sell",
                            "city": "tehran"
                        },
                        "sections": {
                            "BREADCRUMB": [{
                                "widgetType": "BREADCRUMB",
                                "visibilityConditions": [],
                                "uid": "5847f6e3-b569-40ff-9515-b7d102c2a0f9",
                                "normalizerId": "79f0a313-f5d9-46c8-bc1c-3685be5fd006",
                                "dto": {
                                    "widget_type": "BREADCRUMB",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.BreadcrumbData",
                                        "parent_items": [{
                                            "title": "املاک",
                                            "action": {
                                                "type": "OPEN_POSTLIST_PAGE_GRPC",
                                                "payload": {
                                                    "@type": "type.googleapis.com\u002Fwidgets.OpenPostListPageGRPCPayload",
                                                    "search_data": {
                                                        "form_data": {
                                                            "data": {
                                                                "category": {
                                                                    "str": {
                                                                        "value": "real-estate"
                                                                    }
                                                                }
                                                            },
                                                            "online_request_response_data": {}
                                                        },
                                                        "query": "",
                                                        "query_input_type": "UNKNOWN"
                                                    },
                                                    "source_view": "CATEGORY_BREAD_CRUMB",
                                                    "tooltip": "",
                                                    "refresh": false,
                                                    "source_view_str": "CATEGORY_BREAD_CRUMB",
                                                    "is_not_link": false,
                                                    "referer": "",
                                                    "navigation_type": "NAVIGATION_TYPE_UNKNOWN"
                                                },
                                                "page_pop_link": false
                                            }
                                        }, {
                                            "title": "فروش مسکونی",
                                            "action": {
                                                "type": "OPEN_POSTLIST_PAGE_GRPC",
                                                "payload": {
                                                    "@type": "type.googleapis.com\u002Fwidgets.OpenPostListPageGRPCPayload",
                                                    "search_data": {
                                                        "form_data": {
                                                            "data": {
                                                                "category": {
                                                                    "str": {
                                                                        "value": "residential-sell"
                                                                    }
                                                                }
                                                            },
                                                            "online_request_response_data": {}
                                                        },
                                                        "query": "",
                                                        "query_input_type": "UNKNOWN"
                                                    },
                                                    "source_view": "CATEGORY_BREAD_CRUMB",
                                                    "tooltip": "",
                                                    "refresh": false,
                                                    "source_view_str": "CATEGORY_BREAD_CRUMB",
                                                    "is_not_link": false,
                                                    "referer": "",
                                                    "navigation_type": "NAVIGATION_TYPE_UNKNOWN"
                                                },
                                                "page_pop_link": false
                                            }
                                        }, {
                                            "title": "فروش آپارتمان",
                                            "action": {
                                                "type": "OPEN_POSTLIST_PAGE_GRPC",
                                                "payload": {
                                                    "@type": "type.googleapis.com\u002Fwidgets.OpenPostListPageGRPCPayload",
                                                    "search_data": {
                                                        "form_data": {
                                                            "data": {
                                                                "category": {
                                                                    "str": {
                                                                        "value": "apartment-sell"
                                                                    }
                                                                }
                                                            },
                                                            "online_request_response_data": {}
                                                        },
                                                        "query": "",
                                                        "query_input_type": "UNKNOWN"
                                                    },
                                                    "source_view": "CATEGORY_BREAD_CRUMB",
                                                    "tooltip": "",
                                                    "refresh": false,
                                                    "source_view_str": "CATEGORY_BREAD_CRUMB",
                                                    "is_not_link": false,
                                                    "referer": "",
                                                    "navigation_type": "NAVIGATION_TYPE_UNKNOWN"
                                                },
                                                "page_pop_link": false
                                            }
                                        }],
                                        "current_page_title": "۹۷ متر ۲ خواب دونبش \u002F\u002F دید ابدی",
                                        "padded": true
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "5847f6e3-b569-40ff-9515-b7d102c2a0f9",
                                "__NORMALIZED_WIDGET_V2__": true
                            }],
                            "TITLE": [{
                                "widgetType": "LEGEND_TITLE_ROW",
                                "visibilityConditions": [],
                                "uid": "bfa51495-ab6a-4c46-89b9-0d80f90b2f01",
                                "normalizerId": "b108d3b5-afde-4c5c-b737-658b9c1adbaf",
                                "dto": {
                                    "widget_type": "LEGEND_TITLE_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.LegendTitleRowData",
                                        "title": "۹۷ متر ۲ خواب دونبش \u002F\u002F دید ابدی",
                                        "subtitle": "",
                                        "has_divider": false,
                                        "image_url": "",
                                        "tags": [],
                                        "show_thumbnail": false,
                                        "mobile_design": false,
                                        "high_level_heading": true,
                                        "padding": "NO_PADDING"
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "bfa51495-ab6a-4c46-89b9-0d80f90b2f01",
                                "__NORMALIZED_WIDGET_V2__": true
                            }, {
                                "widgetType": "EXPANDABLE_SECTION",
                                "visibilityConditions": [],
                                "uid": "8d7d9e05-d98e-406f-ae82-dbc894f5ee93",
                                "normalizerId": "d9f00026-cc08-4da8-93ac-13fbc2d09957",
                                "dto": {
                                    "widget_type": "EXPANDABLE_SECTION",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.ExpandableSectionData",
                                        "widget_list": [{
                                            "widget_type": "DESCRIPTION_ROW",
                                            "data": {
                                                "@type": "type.googleapis.com\u002Fwidgets.DescriptionRowData",
                                                "text": "انتشار آگهی: ۷ مرداد ۱۴۰۵، ۱۵:۴۳\nآخرین نردبان: ۲۱ شهریور ۱۴۰۵، ۱۰:۲۷\nآخرین به‌روز‌رسانی: ۲۵ شهریور ۱۴۰۵، ۱۱:۰۷",
                                                "has_divider": false,
                                                "is_primary": true,
                                                "expandable": false,
                                                "small": true,
                                                "padded": false,
                                                "preview_max_line": 0,
                                                "text_alignment": "RIGHT"
                                            },
                                            "visibility_condition": [],
                                            "uid": ""
                                        }],
                                        "title": "ماه پیش در تهران، یوسف‌آباد، خ سی و هشتم فضل‌الهی",
                                        "icon": {
                                            "image_url_dark": "",
                                            "image_url_light": "",
                                            "icon_name": "UNKNOWN",
                                            "icon_color": "UNKNOWN"
                                        },
                                        "is_expanded": false
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "8d7d9e05-d98e-406f-ae82-dbc894f5ee93",
                                "__NORMALIZED_WIDGET_V2__": true
                            }, {
                                "widgetType": "SELECTOR_ROW",
                                "visibilityConditions": [],
                                "uid": "2479cb23-516e-4807-be12-cbbc8f2e461c",
                                "normalizerId": "b56b5bcc-1c1c-4893-872e-79c81e48fe8c",
                                "dto": {
                                    "widget_type": "SELECTOR_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.SelectorRowData",
                                        "title": "زنگ خطرهای قبل از معامله",
                                        "image_url": "",
                                        "action": {
                                            "type": "OPEN_PAGE",
                                            "payload": {
                                                "@type": "type.googleapis.com\u002Fwidgets.OpenPagePayload",
                                                "request_http_method": "POST",
                                                "request_data": {
                                                    "@type": "type.googleapis.com\u002Fpost_api_v2.GetFraudAlertPageRequest.Data",
                                                    "category": "apartment-sell"
                                                },
                                                "page": "UNKNOWN_PAGE",
                                                "specification": {
                                                    "@type": "type.googleapis.com\u002Fwidgets.OpenPagePayload.SimplePageSpecification",
                                                    "has_bottom_navbar": false,
                                                    "has_search": false,
                                                    "search_placeholder": "",
                                                    "navigation_button": "BACK",
                                                    "disable_silent_fetch": false
                                                },
                                                "page_type": "SIMPLE_PAGE",
                                                "is_modal": true,
                                                "rest_request_path": "\u002Fv8\u002Fpostview\u002Ffraud-alert",
                                                "grpc_request_path": "\u002Fpost_api_v2.PostApi\u002FGetFraudAlertPage"
                                            },
                                            "page_pop_link": false
                                        },
                                        "has_divider": true,
                                        "has_notification": false,
                                        "icon": {
                                            "image_url_dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fwarning.png",
                                            "image_url_light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fwarning.png",
                                            "icon_name": "WARNING",
                                            "icon_color": "ICON_SECONDARY"
                                        },
                                        "notification_text": "",
                                        "description": "",
                                        "has_arrow": true,
                                        "small": false,
                                        "last_notification_date": "0001-01-01T00:00:00Z",
                                        "uid": "",
                                        "fullwidth": false,
                                        "truncate_title": false
                                    },
                                    "action_log": {
                                        "server_side_info": {
                                            "info": {
                                                "@type": "type.googleapis.com\u002Faction_log.PostWarningInfo",
                                                "post_token": "gap5-Twe"
                                            },
                                            "item_type": {
                                                "type": "POST_WARNING"
                                            }
                                        },
                                        "enabled": true
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "2479cb23-516e-4807-be12-cbbc8f2e461c",
                                "__NORMALIZED_WIDGET_V2__": true
                            }],
                            "DESCRIPTION": [{
                                "widgetType": "TITLE_ROW",
                                "visibilityConditions": [],
                                "uid": "572f6a69-3d7e-435a-9782-2865b831b969",
                                "normalizerId": "d558bd17-e9ee-401c-9c9e-d1f10d95831a",
                                "dto": {
                                    "widget_type": "TITLE_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.TitleRowData",
                                        "text": "توضیحات",
                                        "has_divider": false,
                                        "color": "",
                                        "text_color": "TEXT_PRIMARY",
                                        "description": "",
                                        "description_color": "UNKNOWN",
                                        "subtitle": "",
                                        "subtitle_color": "UNKNOWN",
                                        "text_type": "SECONDARY",
                                        "type": "UNKNOWN_TYPE",
                                        "show_required": false,
                                        "state": "TITLE_ROW_STATE_UNKNOWN",
                                        "is_sticky_header": false
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "572f6a69-3d7e-435a-9782-2865b831b969",
                                "__NORMALIZED_WIDGET_V2__": true
                            }, {
                                "widgetType": "DESCRIPTION_ROW",
                                "visibilityConditions": [],
                                "uid": "a06aa6a3-92c1-4a67-9e3c-1c0ea0acf433",
                                "normalizerId": "d2802389-48bc-4518-81fe-949579071002",
                                "dto": {
                                    "widget_type": "DESCRIPTION_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.DescriptionRowData",
                                        "text": "بهترین واحد در منطقه رو از دست نده! \n\n⚜️ ۲ خواب، دونبش، غرق نور، با دید ابدی و بدون مشرف\n⚜️ نقشه عالی و سالن مربع شکل که هر جور بچینی قشنگه\n⚜️ خواب‌ها استاندارد و بزرگ هستن.\n⚜️ دو ساله، کلید نخورده و آماده تحویل!\n⚜️ ورودی از لابی شیک و سرایدار مقیم برای امنیت بیشتر.\n\nکارشناس فروش منطقه، REDACTED\n برای هماهنگی و بازدید، پیام بدین یا تماس بگیرین.",
                                        "has_divider": false,
                                        "is_primary": true,
                                        "expandable": false,
                                        "small": false,
                                        "padded": false,
                                        "preview_max_line": 0,
                                        "text_alignment": "RIGHT"
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "a06aa6a3-92c1-4a67-9e3c-1c0ea0acf433",
                                "__NORMALIZED_WIDGET_V2__": true
                            }],
                            "IMAGE": [{
                                "widgetType": "IMAGE_CAROUSEL",
                                "visibilityConditions": [],
                                "uid": "70a4c1ee-9750-4f2a-8e6c-5d611292b41f",
                                "normalizerId": "f98f76f4-156f-4435-a696-83155552fe85",
                                "dto": {
                                    "widget_type": "IMAGE_CAROUSEL",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.ImageCarouselData",
                                        "items": [{
                                            "image_url": "",
                                            "image": {
                                                "url": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fphoto\u002Fneda\u002Fwebp_post\u002FctqDuy-S76vGZAxvffrTCg\u002F43cff8b2-eb49-4012-8e90-3f565fc0ef29.webp",
                                                "alt": "۹۷ متر ۲ خواب دونبش \u002F\u002F دید ابدی|فروش آپارتمان|تهران, یوسف‌آباد|دیوار",
                                                "thumbnail_url": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fphoto\u002Fneda\u002Fwebp_thumbnail\u002FuuK5NfzXt4Aa6ExBzNNOUg\u002F43cff8b2-eb49-4012-8e90-3f565fc0ef29.webp"
                                            },
                                            "video_url": ""
                                        }],
                                        "padded": false,
                                        "image_aspect_ratio": {
                                            "dynamic_aspect_ratio": {
                                                "height": 3,
                                                "width": 4
                                            }
                                        },
                                        "has_preview": true,
                                        "has_thumbnails": false,
                                        "scale_type": "CENTER_CROP",
                                        "show_tooltip": true,
                                        "tooltip_data": {
                                            "icon": {
                                                "image_url_dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Fwhite_primary\u002Fv1\u002Ffullscreen.png",
                                                "image_url_light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Fwhite_primary\u002Fv1\u002Ffullscreen.png",
                                                "icon_name": "FULLSCREEN",
                                                "icon_color": "WHITE_PRIMARY"
                                            },
                                            "text": "عکس‌ها: تزئینی"
                                        }
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "70a4c1ee-9750-4f2a-8e6c-5d611292b41f",
                                "__NORMALIZED_WIDGET_V2__": true
                            }],
                            "LIST_DATA": [{
                                "widgetType": "GROUP_INFO_ROW",
                                "visibilityConditions": [],
                                "uid": "35dfecf6-839b-4e38-8301-1f5266c7dd34",
                                "normalizerId": "ecf76768-95da-432e-b43e-d1bd54ee9216",
                                "dto": {
                                    "widget_type": "GROUP_INFO_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.GroupInfoRow",
                                        "items": [{
                                            "title": "متراژ",
                                            "value": "۹۷"
                                        }, {
                                            "title": "ساخت",
                                            "value": "۱۴۰۳"
                                        }, {
                                            "title": "اتاق",
                                            "value": "۲"
                                        }],
                                        "has_divider": true
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "35dfecf6-839b-4e38-8301-1f5266c7dd34",
                                "__NORMALIZED_WIDGET_V2__": true
                            }, {
                                "widgetType": "UNEXPANDABLE_ROW",
                                "visibilityConditions": [],
                                "uid": "5296ab72-dabf-427f-b073-e90acaea7d82",
                                "normalizerId": "67c9cf45-52b4-4adb-b80d-580c600d5f7a",
                                "dto": {
                                    "widget_type": "UNEXPANDABLE_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.UnexpandableRowData",
                                        "title": "تصویر‌ها برای همین ملک است؟",
                                        "value": "خیر",
                                        "has_divider": true,
                                        "compact": false,
                                        "has_copy_to_clipboard": false,
                                        "send_action_log_on_copy": false
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "5296ab72-dabf-427f-b073-e90acaea7d82",
                                "__NORMALIZED_WIDGET_V2__": true
                            }, {
                                "widgetType": "UNEXPANDABLE_ROW",
                                "visibilityConditions": [],
                                "uid": "b5e5f3f7-7e9e-4fc5-a939-d13337b80930",
                                "normalizerId": "356c9537-d1d0-468c-8d85-7d0979a04ddf",
                                "dto": {
                                    "widget_type": "UNEXPANDABLE_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.UnexpandableRowData",
                                        "title": "قیمت کل",
                                        "value": "‏۴۸,۵۰۰,۰۰۰,۰۰۰ تومان",
                                        "has_divider": true,
                                        "compact": false,
                                        "has_copy_to_clipboard": false,
                                        "send_action_log_on_copy": false
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "b5e5f3f7-7e9e-4fc5-a939-d13337b80930",
                                "__NORMALIZED_WIDGET_V2__": true
                            }, {
                                "widgetType": "UNEXPANDABLE_ROW",
                                "visibilityConditions": [],
                                "uid": "d0c01fe9-3384-44f1-93e2-8992d7f4ed90",
                                "normalizerId": "16544994-73e3-4f9d-8d6b-111923c1ee5d",
                                "dto": {
                                    "widget_type": "UNEXPANDABLE_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.UnexpandableRowData",
                                        "title": "قیمت هر متر",
                                        "value": "‏۵۰۰,۰۰۰,۰۰۰ تومان",
                                        "has_divider": true,
                                        "compact": false,
                                        "has_copy_to_clipboard": false,
                                        "send_action_log_on_copy": false
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "d0c01fe9-3384-44f1-93e2-8992d7f4ed90",
                                "__NORMALIZED_WIDGET_V2__": true
                            }, {
                                "widgetType": "UNEXPANDABLE_ROW",
                                "visibilityConditions": [],
                                "uid": "d39c2ad2-d257-466a-a6e4-5465a195c7a7",
                                "normalizerId": "aebb2282-1404-4e10-bff2-9310a027948b",
                                "dto": {
                                    "widget_type": "UNEXPANDABLE_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.UnexpandableRowData",
                                        "title": "طبقه",
                                        "value": "۵",
                                        "has_divider": true,
                                        "compact": false,
                                        "has_copy_to_clipboard": false,
                                        "send_action_log_on_copy": false
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "d39c2ad2-d257-466a-a6e4-5465a195c7a7",
                                "__NORMALIZED_WIDGET_V2__": true
                            }, {
                                "widgetType": "SECTION_TITLE_ROW",
                                "visibilityConditions": [],
                                "uid": "ad54705d-add8-41f9-a261-79b0fd4fa0dc",
                                "normalizerId": "b025f9a3-e5d6-409b-b4b0-2cc0894aa9f6",
                                "dto": {
                                    "widget_type": "SECTION_TITLE_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.SectionTitleRowData",
                                        "title": "ویژگی‌ها و امکانات",
                                        "subtitle": "",
                                        "image_url": "",
                                        "padded": false,
                                        "action_title": "",
                                        "title_color": "TEXT_PRIMARY",
                                        "padding": "ALT"
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "ad54705d-add8-41f9-a261-79b0fd4fa0dc",
                                "__NORMALIZED_WIDGET_V2__": true
                            }, {
                                "widgetType": "GROUP_FEATURE_ROW",
                                "visibilityConditions": [],
                                "uid": "7b9a230b-616a-4dd5-a0a9-3512b7649a13",
                                "normalizerId": "6657cb1d-4570-4bc5-882f-bf76273950ad",
                                "dto": {
                                    "widget_type": "GROUP_FEATURE_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.GroupFeatureRow",
                                        "items": [{
                                            "title": "آسانسور",
                                            "icon": {
                                                "image_url_dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Felevator.png",
                                                "image_url_light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Felevator.png",
                                                "icon_name": "ELEVATOR",
                                                "icon_color": "ICON_SECONDARY"
                                            },
                                            "available": true
                                        }, {
                                            "title": "پارکینگ",
                                            "icon": {
                                                "image_url_dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fparking.png",
                                                "image_url_light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fparking.png",
                                                "icon_name": "PARKING",
                                                "icon_color": "ICON_SECONDARY"
                                            },
                                            "available": true
                                        }, {
                                            "title": "انباری",
                                            "icon": {
                                                "image_url_dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcabinet.png",
                                                "image_url_light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcabinet.png",
                                                "icon_name": "CABINET",
                                                "icon_color": "ICON_SECONDARY"
                                            },
                                            "available": true
                                        }],
                                        "action_text": "",
                                        "has_divider": true
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "7b9a230b-616a-4dd5-a0a9-3512b7649a13",
                                "__NORMALIZED_WIDGET_V2__": true
                            }, {
                                "widgetType": "SELECTOR_ROW",
                                "visibilityConditions": [],
                                "uid": "b6709806-4050-40bd-8b40-52910de32bdf",
                                "normalizerId": "bc4cc854-de74-4e1a-939a-b911e8c1d415",
                                "dto": {
                                    "widget_type": "SELECTOR_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.SelectorRowData",
                                        "title": "سایر ویژگی‌ها و امکانات",
                                        "image_url": "",
                                        "action": {
                                            "type": "LOAD_MODAL_PAGE",
                                            "payload": {
                                                "@type": "type.googleapis.com\u002Fwidgets.LoadModalPagePayload",
                                                "modal_page": {
                                                    "title": "ویژگی‌ها و امکانات",
                                                    "widget_list": [{
                                                        "widget_type": "TITLE_ROW",
                                                        "data": {
                                                            "@type": "type.googleapis.com\u002Fwidgets.TitleRowData",
                                                            "text": "امکانات",
                                                            "has_divider": true,
                                                            "color": "",
                                                            "text_color": "TEXT_PRIMARY",
                                                            "description": "",
                                                            "description_color": "UNKNOWN",
                                                            "subtitle": "",
                                                            "subtitle_color": "UNKNOWN",
                                                            "type": "UNKNOWN_TYPE",
                                                            "show_required": false,
                                                            "state": "TITLE_ROW_STATE_UNKNOWN",
                                                            "is_sticky_header": false
                                                        },
                                                        "visibility_condition": [],
                                                        "uid": ""
                                                    }, {
                                                        "widget_type": "FEATURE_ROW",
                                                        "data": {
                                                            "@type": "type.googleapis.com\u002Fwidgets.FeatureRowData",
                                                            "title": "آسانسور",
                                                            "image_url": "",
                                                            "image_color": "UNKNOWN",
                                                            "has_divider": true,
                                                            "icon": {
                                                                "image_url_dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Felevator.png",
                                                                "image_url_light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Felevator.png",
                                                                "icon_name": "ELEVATOR",
                                                                "icon_color": "ICON_SECONDARY"
                                                            },
                                                            "disabled": false,
                                                            "text_color": "UNKNOWN"
                                                        },
                                                        "visibility_condition": [],
                                                        "uid": ""
                                                    }, {
                                                        "widget_type": "FEATURE_ROW",
                                                        "data": {
                                                            "@type": "type.googleapis.com\u002Fwidgets.FeatureRowData",
                                                            "title": "پارکینگ",
                                                            "image_url": "",
                                                            "image_color": "UNKNOWN",
                                                            "has_divider": true,
                                                            "icon": {
                                                                "image_url_dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fparking.png",
                                                                "image_url_light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fparking.png",
                                                                "icon_name": "PARKING",
                                                                "icon_color": "ICON_SECONDARY"
                                                            },
                                                            "disabled": false,
                                                            "text_color": "UNKNOWN"
                                                        },
                                                        "visibility_condition": [],
                                                        "uid": ""
                                                    }, {
                                                        "widget_type": "FEATURE_ROW",
                                                        "data": {
                                                            "@type": "type.googleapis.com\u002Fwidgets.FeatureRowData",
                                                            "title": "انباری",
                                                            "image_url": "",
                                                            "image_color": "UNKNOWN",
                                                            "has_divider": false,
                                                            "icon": {
                                                                "image_url_dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fcabinet.png",
                                                                "image_url_light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fcabinet.png",
                                                                "icon_name": "CABINET",
                                                                "icon_color": "ICON_SECONDARY"
                                                            },
                                                            "disabled": false,
                                                            "text_color": "UNKNOWN"
                                                        },
                                                        "visibility_condition": [],
                                                        "uid": ""
                                                    }],
                                                    "has_close_button": false
                                                }
                                            },
                                            "page_pop_link": false
                                        },
                                        "has_divider": true,
                                        "has_notification": false,
                                        "icon": {
                                            "image_url_dark": "",
                                            "image_url_light": "",
                                            "icon_name": "UNKNOWN",
                                            "icon_color": "UNKNOWN"
                                        },
                                        "notification_text": "",
                                        "description": "",
                                        "has_arrow": true,
                                        "small": false,
                                        "last_notification_date": "0001-01-01T00:00:00Z",
                                        "uid": "",
                                        "fullwidth": true,
                                        "truncate_title": false
                                    },
                                    "action_log": {
                                        "server_side_info": {
                                            "info": {
                                                "@type": "type.googleapis.com\u002Faction_log.ViewPostFeaturesInfo",
                                                "post_token": "gap5-Twe"
                                            },
                                            "item_type": {
                                                "type": "VIEW_POST_FEATURES"
                                            }
                                        },
                                        "enabled": true
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "b6709806-4050-40bd-8b40-52910de32bdf",
                                "__NORMALIZED_WIDGET_V2__": true
                            }, {
                                "widgetType": "SELECTOR_ROW",
                                "visibilityConditions": [],
                                "uid": "ffd5cf4d-a662-4486-8314-ba583b9b39ad",
                                "normalizerId": "43fff065-5742-4f98-afd7-672a7caec296",
                                "dto": {
                                    "widget_type": "SELECTOR_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.SelectorRowData",
                                        "title": "بررسی و کارشناسی",
                                        "image_url": "",
                                        "action": {
                                            "type": "OPEN_PAGE",
                                            "payload": {
                                                "@type": "type.googleapis.com\u002Fwidgets.OpenPagePayload",
                                                "request_http_method": "POST",
                                                "request_data": {
                                                    "@type": "type.googleapis.com\u002Fservice_providers.GetServiceProvidersPageRequest.RequestData",
                                                    "source_v2": "DEMAND_POST",
                                                    "filter": {
                                                        "service_types": ["REPORT_INSPECTION"],
                                                        "city_id": 1,
                                                        "category": "apartment-sell",
                                                        "post_token": "gap5-Twe",
                                                        "touchpoint": "DEMAND_POST",
                                                        "app_slugs": []
                                                    },
                                                    "action_data_builder": {
                                                        "conversation_id": "gap5-Twe",
                                                        "post_token": "gap5-Twe",
                                                        "ticket_uuid": "",
                                                        "return_url": "",
                                                        "user_side": "",
                                                        "business_token": "",
                                                        "touchpoint": "DEMAND_POST",
                                                        "is_bottomsheet": false,
                                                        "source": "DEMAND_POST",
                                                        "lead_source": "DEMAND"
                                                    },
                                                    "display_data": {
                                                        "page_title": "بررسی و کارشناسی",
                                                        "page_description": ""
                                                    },
                                                    "trace_id": "0fb404fd-71be-4094-98e5-f27262f7c474",
                                                    "source": "DEMAND_POST",
                                                    "lead_source": "DEMAND"
                                                },
                                                "page": "UNKNOWN_PAGE",
                                                "specification": {
                                                    "@type": "type.googleapis.com\u002Fwidgets.OpenPagePayload.SimplePageSpecification",
                                                    "has_bottom_navbar": false,
                                                    "has_search": false,
                                                    "search_placeholder": "",
                                                    "navigation_button": "UNKNOWN",
                                                    "disable_silent_fetch": false
                                                },
                                                "page_type": "SIMPLE_PAGE",
                                                "is_modal": true,
                                                "rest_request_path": "\u002Fv8\u002Fopen-platform\u002Fservice-providers",
                                                "grpc_request_path": "\u002Fservice_providers.ServiceProviders\u002FGetServiceProvidersPage"
                                            },
                                            "page_pop_link": false
                                        },
                                        "has_divider": true,
                                        "has_notification": false,
                                        "icon": {
                                            "image_url_dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Farticle-magnifier.png",
                                            "image_url_light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Farticle-magnifier.png",
                                            "icon_name": "ARTICLE_MAGNIFIER",
                                            "icon_color": "ICON_SECONDARY"
                                        },
                                        "notification_text": "",
                                        "description": "",
                                        "has_arrow": true,
                                        "small": false,
                                        "last_notification_date": "0001-01-01T00:00:00Z",
                                        "uid": "",
                                        "fullwidth": false,
                                        "truncate_title": false
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "ffd5cf4d-a662-4486-8314-ba583b9b39ad",
                                "__NORMALIZED_WIDGET_V2__": true
                            }],
                            "TAGS": [{
                                "widgetType": "WRAPPER_ROW",
                                "visibilityConditions": [],
                                "uid": "aeb37a78-a622-4418-9226-76b518e33359",
                                "normalizerId": "89f5205f-e9c7-44de-80a8-b89cd0073da8",
                                "dto": {
                                    "widget_type": "WRAPPER_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.WrapperRowData",
                                        "chip_list": {
                                            "chips": [{
                                                "text": "فروش آپارتمان",
                                                "type": "ACTION",
                                                "style": "NORMAL",
                                                "rounded": false,
                                                "small": false,
                                                "action": {
                                                    "type": "OPEN_POSTLIST_PAGE_GRPC",
                                                    "payload": {
                                                        "@type": "type.googleapis.com\u002Fwidgets.OpenPostListPageGRPCPayload",
                                                        "search_data": {
                                                            "form_data": {
                                                                "data": {
                                                                    "category": {
                                                                        "str": {
                                                                            "value": "apartment-sell"
                                                                        }
                                                                    }
                                                                },
                                                                "online_request_response_data": {}
                                                            },
                                                            "query": "",
                                                            "query_input_type": "UNKNOWN"
                                                        },
                                                        "source_view": "CATEGORY_BREAD_CRUMB",
                                                        "tooltip": "",
                                                        "refresh": false,
                                                        "source_view_str": "CATEGORY_BREAD_CRUMB",
                                                        "is_not_link": false,
                                                        "referer": "",
                                                        "navigation_type": "NAVIGATION_TYPE_UNKNOWN"
                                                    },
                                                    "page_pop_link": false
                                                },
                                                "is_active": false
                                            }, {
                                                "text": "فروش آپارتمان در یوسف‌آباد",
                                                "type": "ACTION",
                                                "style": "NORMAL",
                                                "rounded": false,
                                                "small": false,
                                                "action": {
                                                    "type": "OPEN_POSTLIST_PAGE_GRPC",
                                                    "payload": {
                                                        "@type": "type.googleapis.com\u002Fwidgets.OpenPostListPageGRPCPayload",
                                                        "search_data": {
                                                            "form_data": {
                                                                "data": {
                                                                    "category": {
                                                                        "str": {
                                                                            "value": "apartment-sell"
                                                                        }
                                                                    },
                                                                    "districts": {
                                                                        "repeated_string": {
                                                                            "value": ["90"]
                                                                        }
                                                                    }
                                                                },
                                                                "online_request_response_data": {}
                                                            },
                                                            "query": "",
                                                            "query_input_type": "UNKNOWN"
                                                        },
                                                        "source_view": "CATEGORY_BREAD_CRUMB",
                                                        "tooltip": "",
                                                        "refresh": false,
                                                        "source_view_str": "CATEGORY_BREAD_CRUMB",
                                                        "is_not_link": false,
                                                        "referer": "",
                                                        "navigation_type": "NAVIGATION_TYPE_UNKNOWN"
                                                    },
                                                    "page_pop_link": false
                                                },
                                                "is_active": false
                                            }]
                                        },
                                        "padded": false
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "aeb37a78-a622-4418-9226-76b518e33359",
                                "__NORMALIZED_WIDGET_V2__": true
                            }],
                            "MAP": [{
                                "widgetType": "MAP_ROW",
                                "visibilityConditions": [],
                                "uid": "5b8bfeb3-ca78-43d4-a6d3-b6792e1d9a5e",
                                "normalizerId": "77625fa9-feec-449b-835a-35eb1fab902b",
                                "dto": {
                                    "widget_type": "MAP_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.MapRowData",
                                        "location": {
                                            "type": "FUZZY",
                                            "fuzzy_data": {
                                                "point": {
                                                    "latitude": 35.734610425177365,
                                                    "longitude": 51.40530956635603
                                                },
                                                "radius": 500
                                            }
                                        },
                                        "image_url": "https:\u002F\u002Fmapimage.divarcdn.com\u002Fv8\u002Fmapimage?encrypted_data=MTIzNDU2Nzg5MTIzXL_Y8SdZyazuQp-XOg7PaPpL736MLc2ODD3PkY6uBOaYTw==&is_nearby=true",
                                        "preview_type": "STATIC_IMAGE"
                                    },
                                    "action_log": {
                                        "server_side_info": {
                                            "info": {
                                                "@type": "type.googleapis.com\u002Faction_log.MapInfo",
                                                "post_token": "gap5-Twe"
                                            },
                                            "item_type": {
                                                "type": "MAP"
                                            }
                                        },
                                        "enabled": true
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "5b8bfeb3-ca78-43d4-a6d3-b6792e1d9a5e",
                                "__NORMALIZED_WIDGET_V2__": true
                            }],
                            "NOTE": [{
                                "widgetType": "NOTE",
                                "visibilityConditions": [],
                                "uid": "89d8839a-ea41-4921-a2ce-4ae6960b6dd4",
                                "normalizerId": "d50d4453-c9bc-4a62-b2d6-a33d1cc1f12c",
                                "dto": {
                                    "widget_type": "NOTE",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.NoteData",
                                        "title": "یادداشت من",
                                        "button_title": "ویرایش یادداشت",
                                        "post_token": "gap5-Twe",
                                        "icon_button": {
                                            "icon": {
                                                "image_url_dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fmore_vert.png",
                                                "image_url_light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fmore_vert.png",
                                                "icon_name": "MORE_VERT",
                                                "icon_color": "ICON_SECONDARY"
                                            },
                                            "action": {
                                                "type": "LOAD_MENU",
                                                "payload": {
                                                    "@type": "type.googleapis.com\u002Fwidgets.LoadMenuPayload",
                                                    "menu": {
                                                        "title": "",
                                                        "items": [{
                                                            "text": "ویرایش یادداشت",
                                                            "icon": {
                                                                "image_url_dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Fedit.png",
                                                                "image_url_light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Fedit.png",
                                                                "icon_name": "EDIT",
                                                                "icon_color": "ICON_SECONDARY"
                                                            },
                                                            "disabled": false,
                                                            "action": {
                                                                "type": "NOTE",
                                                                "payload": {
                                                                    "@type": "type.googleapis.com\u002Fwidgets.NotePayload",
                                                                    "post_token": "gap5-Twe",
                                                                    "max_character_count": 256
                                                                },
                                                                "page_pop_link": false
                                                            },
                                                            "alignment": "RIGHT",
                                                            "state": "STATE_UNKNOWN"
                                                        }, {
                                                            "text": "حذف یادداشت",
                                                            "icon": {
                                                                "image_url_dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_primary\u002Fv1\u002Ftrash_o.png",
                                                                "image_url_light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_primary\u002Fv1\u002Ftrash_o.png",
                                                                "icon_name": "TRASH_O",
                                                                "icon_color": "ICON_PRIMARY"
                                                            },
                                                            "disabled": false,
                                                            "action": {
                                                                "type": "MAKE_NETWORK_CALL",
                                                                "payload": {
                                                                    "@type": "type.googleapis.com\u002Fwidgets.MakeNetworkCallPayload",
                                                                    "grpc_request_path": "\u002Fyaad_v2.YaadV2\u002FDeleteNoteV2",
                                                                    "rest_request_path": "\u002Fyaad\u002Fdelete-note-v2",
                                                                    "request_data": {
                                                                        "@type": "type.googleapis.com\u002Fyaad_v2.DeleteNoteV2Request.RequestData",
                                                                        "token": "gap5-Twe"
                                                                    },
                                                                    "needs_auth": true
                                                                },
                                                                "page_pop_link": false
                                                            },
                                                            "alignment": "RIGHT",
                                                            "state": "STATE_NEGATIVE"
                                                        }],
                                                        "banner": {
                                                            "title": "",
                                                            "text": "",
                                                            "image_url": ""
                                                        }
                                                    },
                                                    "display_type": "LOAD_MENU_DISPLAY_TYPE_BOTTOM_SHEET"
                                                },
                                                "page_pop_link": false
                                            },
                                            "alt_text": "",
                                            "disable": false
                                        }
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "89d8839a-ea41-4921-a2ce-4ae6960b6dd4",
                                "__NORMALIZED_WIDGET_V2__": true
                            }],
                            "STATIC": [{
                                "widgetType": "SELECTOR_ROW",
                                "visibilityConditions": [],
                                "uid": "ea826b2e-4f76-4d0f-a3ad-84091bcf586c",
                                "normalizerId": "3cfa0ef3-451e-4f05-84c6-582dcd9bd35b",
                                "dto": {
                                    "widget_type": "SELECTOR_ROW",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.SelectorRowData",
                                        "title": "گزارش آگهی",
                                        "image_url": "",
                                        "action": {
                                            "type": "OPEN_FORM_PAGE",
                                            "payload": {
                                                "@type": "type.googleapis.com\u002Fwidgets.OpenFormPagePayload",
                                                "grpc_servicer": "\u002Fpost_quality.PostQualityFeedback\u002FGetFeedbackForm",
                                                "request_data": {
                                                    "@type": "type.googleapis.com\u002Fpost_quality.GetFeedbackFormRequest.RequestData",
                                                    "post_token": "gap5-Twe"
                                                },
                                                "rest_request_path": "\u002Fv8\u002Fpost-quality\u002Ffeedback-form"
                                            },
                                            "page_pop_link": false
                                        },
                                        "has_divider": true,
                                        "has_notification": false,
                                        "icon": {
                                            "image_url_dark": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Fdark\u002Ficon_secondary\u002Fv1\u002Freport.png",
                                            "image_url_light": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fimgs\u002Fwidget-icons\u002Flight\u002Ficon_secondary\u002Fv1\u002Freport.png",
                                            "icon_name": "REPORT",
                                            "icon_color": "ICON_SECONDARY"
                                        },
                                        "notification_text": "",
                                        "description": "",
                                        "has_arrow": false,
                                        "small": false,
                                        "last_notification_date": "0001-01-01T00:00:00Z",
                                        "uid": "",
                                        "fullwidth": false,
                                        "truncate_title": false
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "ea826b2e-4f76-4d0f-a3ad-84091bcf586c",
                                "__NORMALIZED_WIDGET_V2__": true
                            }],
                            "BUSINESS_SECTION": [{
                                "widgetType": "LAZY_SECTION",
                                "visibilityConditions": [],
                                "uid": "90d6de94-a7fa-4c97-a1fe-9e22a7ec2e8a",
                                "normalizerId": "fa515b86-8034-435e-84c8-2b506cf70958",
                                "dto": {
                                    "widget_type": "LAZY_SECTION",
                                    "data": {
                                        "@type": "type.googleapis.com\u002Fwidgets.LazySectionData",
                                        "rest_request_path": "\u002Fv8\u002Fpremium-user\u002Fpost-page\u002Fbusiness-data\u002Fgap5-Twe\u002Flazy",
                                        "grpc_request_path": "\u002Fpremium_panel.PremiumPanel\u002FGetPostBusinessLazyWidgets",
                                        "request_data": {
                                            "@type": "type.googleapis.com\u002Fpremium_panel.GetPostBusinessLazyWidgetsRequest.RequestData",
                                            "post_token": "gap5-Twe",
                                            "hashed_post_owner_user_id": "0a8e25f03c178e8349f4cd5fe9cec49673d2f2f4ab5679fe8bd75d5b11327fae",
                                            "post_business_type": "premium-panel",
                                            "post_hide_phone": false
                                        }
                                    },
                                    "visibility_condition": [],
                                    "uid": ""
                                },
                                "KEY_PROP_NAME": "90d6de94-a7fa-4c97-a1fe-9e22a7ec2e8a",
                                "__NORMALIZED_WIDGET_V2__": true
                            }]
                        },
                        "share": {
                            "title": "۹۷ متر ۲ خواب دونبش __ دید ابدی",
                            "web_url": "https:\u002F\u002Fdivar.ir\u002Fv\u002Fgap5-Twe",
                            "image_url": ""
                        },
                        "webengage": {
                            "cat_3": "apartment-sell",
                            "category": "apartment-sell",
                            "district": "yousef-abad",
                            "cat_1": "real-estate",
                            "business_type": "premium-panel",
                            "business_ref": "MXYdIQan_ciZIrYqZ",
                            "image_count": 1,
                            "source_view": "",
                            "originality": "",
                            "credit": 0,
                            "cat_2": "residential-sell",
                            "city": "tehran",
                            "token": "gap5-Twe",
                            "price": 48499998720,
                            "rent": 0,
                            "gender": "",
                            "status": "",
                            "brand_model": ""
                        }
                    },
                    "hasError": false,
                    "hasSSRUnauthorizedError": false
                },
                "httpError": {
                    "is404": false,
                    "is410": false,
                    "is301": false,
                    "is302": false
                },
                "auth": {
                    "source": null,
                    "error": null,
                    "confirmSent": false,
                    "loading": false,
                    "canReplacePhone": true,
                    "resendEnabled": true,
                    "requiredUserType": null,
                    "shouldUseRwvLogin": false,
                    "autoSubmit": true
                },
                "user": {
                    "isLoggedIn": false,
                    "data": {},
                    "business": {
                        "loading": false,
                        "hasError": false
                    },
                    "showConnectionBanner": false,
                    "showIosInstallationBanner": true,
                    "isBlacklisted": null
                },
                "history": {
                    "length": 0
                },
                "chat": {
                    "hasUnreadChat": false
                },
                "modalPage": {
                    "isOpen": false,
                    "submitLoading": false,
                    "submissionButton": null,
                    "history": [],
                    "requestCache": {},
                    "currentPageIndex": -1
                },
                "multiCity": {
                    "selectedCities": [{
                        "id": 1,
                        "name": "تهران",
                        "slug": "tehran",
                        "type": "2",
                        "parent": 904
                    }],
                    "prevSelectedCities": [],
                    "subtitle": "حداقل یک شهر را انتخاب کنید.",
                    "shouldShowCityTooltip": false,
                    "onClose": null,
                    "defaultCity": {
                        "id": 1,
                        "name": "تهران",
                        "slug": "tehran",
                        "type": "2",
                        "parent": 904
                    }
                },
                "unsafeUserSelectedLocation": {},
                "searchAssistant": {
                    "messages": [],
                    "isLoading": true,
                    "isRestartLoading": false,
                    "errorMessage": null,
                    "restartErrorMessage": null,
                    "isWaiting": false,
                    "isWaitingForSuggestions": false,
                    "waitingText": "",
                    "lastAnimatedMessageTimestamp": null,
                    "isAnimating": false,
                    "scrollPosition": null,
                    "isScrollButtonVisible": false,
                    "isAutoScrollEnabled": true,
                    "suggestions": [],
                    "feedback": null,
                    "isFeedbackVisible": true,
                    "isSuggestionsVisible": true,
                    "isSTTEnabled": false,
                    "pollInterval": 1000,
                    "latestPathConversationId": null,
                    "isSelectPostsModeActive": false,
                    "selectedPosts": [],
                    "isPostSelectionEnabled": false
                },
                "bookmarks": {
                    "posts": [],
                    "searches": [],
                    "postsIsLoading": true,
                    "postsError": null,
                    "searchesIsLoading": true,
                    "searchesError": null
                },
                "premiumPanel": {
                    "landing": {
                        "pageTitle": "",
                        "isNotFound": false,
                        "initialLoading": false,
                        "initialError": null,
                        "contentLoading": false,
                        "contentError": null,
                        "loadMoreLoading": false,
                        "loadMoreError": null,
                        "headerWidgets": [],
                        "postRowWidgets": [],
                        "pagination": {
                            "hasNext": false,
                            "lastItemIdentifier": ""
                        }
                    }
                },
                "review": {
                    "skipped": false
                }
            };
        </script>
        <script>
            (function() {
                var check = document.createElement('script');
                if (!('noModule' in check) && 'onbeforeload' in check) {
                    var support = false;
                    document.addEventListener('beforeload', function(e) {
                        if (e.target === check) {
                            support = true;
                        } else if (!e.target.hasAttribute('nomodule') || !support) {
                            return;
                        }
                        e.preventDefault();
                    }, true);

                    check.type = 'module';
                    check.src = '.';
                    document.head.appendChild(check);
                    check.remove();
                }
            }());
        </script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/runtime.88fc8528.desktop.js" data-chunk="main" data-name="runtime.88fc8528.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/polyfills.b041981d.desktop.js" data-chunk="main" data-name="polyfills.b041981d.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/vendors-pb.37583302.desktop.js" data-chunk="main" data-name="vendors-pb.37583302.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/main.a472176b.desktop.js" data-chunk="main" data-name="main.a472176b.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/widget-base-183.c90455ee.desktop.js" data-chunk="bootstrap" data-name="widget-base-183.c90455ee.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/observer-pb-256.213b941a.desktop.js" data-chunk="bootstrap" data-name="observer-pb-256.213b941a.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/framework-pb-535.37f1a3ba.desktop.js" data-chunk="bootstrap" data-name="framework-pb-535.37f1a3ba.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/khesht-326.894ba0c9.desktop.js" data-chunk="bootstrap" data-name="khesht-326.894ba0c9.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/ic-pb-930.bdb80832.desktop.js" data-chunk="bootstrap" data-name="ic-pb-930.bdb80832.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/components-179.d6e1052a.desktop.js" data-chunk="bootstrap" data-name="components-179.d6e1052a.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/utils-357.29d51d34.desktop.js" data-chunk="bootstrap" data-name="utils-357.29d51d34.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/services-671.684eee20.desktop.js" data-chunk="bootstrap" data-name="services-671.684eee20.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/store-962.40538bcd.desktop.js" data-chunk="bootstrap" data-name="store-962.40538bcd.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/per-localization-94.c8aa1079.desktop.js" data-chunk="bootstrap" data-name="per-localization-94.c8aa1079.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/bootstrap-547.f4f8925c.desktop.js" data-chunk="bootstrap" data-name="bootstrap-547.f4f8925c.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/postview-782.95a6ad6a.desktop.js" data-chunk="PostView" data-name="postview-782.95a6ad6a.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/mapbox-pb-308.54d96d74.desktop.js" data-chunk="LazyPlaceSelector" data-name="mapbox-pb-308.54d96d74.desktop.js"></script>
        <script async nomodule="true" src="https://s100.divarcdn.com/web-assets/2026/09/lazyplaceselector-329.7fc2d2d6.desktop.js" data-chunk="LazyPlaceSelector" data-name="lazyplaceselector-329.7fc2d2d6.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/runtime.88fc8528.desktop.js" data-chunk="main" data-name="runtime.88fc8528.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/polyfills.b041981d.desktop.js" data-chunk="main" data-name="polyfills.b041981d.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/vendors-pb.37583302.desktop.js" data-chunk="main" data-name="vendors-pb.37583302.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/main.a472176b.desktop.js" data-chunk="main" data-name="main.a472176b.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/widget-base-183.c90455ee.desktop.js" data-chunk="bootstrap" data-name="widget-base-183.c90455ee.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/observer-pb-256.213b941a.desktop.js" data-chunk="bootstrap" data-name="observer-pb-256.213b941a.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/framework-pb-535.37f1a3ba.desktop.js" data-chunk="bootstrap" data-name="framework-pb-535.37f1a3ba.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/khesht-326.894ba0c9.desktop.js" data-chunk="bootstrap" data-name="khesht-326.894ba0c9.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/ic-pb-930.bdb80832.desktop.js" data-chunk="bootstrap" data-name="ic-pb-930.bdb80832.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/components-179.d6e1052a.desktop.js" data-chunk="bootstrap" data-name="components-179.d6e1052a.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/utils-357.29d51d34.desktop.js" data-chunk="bootstrap" data-name="utils-357.29d51d34.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/services-671.684eee20.desktop.js" data-chunk="bootstrap" data-name="services-671.684eee20.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/store-962.40538bcd.desktop.js" data-chunk="bootstrap" data-name="store-962.40538bcd.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/per-localization-94.c8aa1079.desktop.js" data-chunk="bootstrap" data-name="per-localization-94.c8aa1079.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/bootstrap-547.f4f8925c.desktop.js" data-chunk="bootstrap" data-name="bootstrap-547.f4f8925c.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/postview-782.95a6ad6a.desktop.js" data-chunk="PostView" data-name="postview-782.95a6ad6a.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/mapbox-pb-308.54d96d74.desktop.js" data-chunk="LazyPlaceSelector" data-name="mapbox-pb-308.54d96d74.desktop.js"></script>
        <script async type="module" src="https://s100.divarcdn.com/web-assets/2026/09/lazyplaceselector-329.7fc2d2d6.desktop.js" data-chunk="LazyPlaceSelector" data-name="lazyplaceselector-329.7fc2d2d6.desktop.js"></script>
        <script id="__LOADABLE_REQUIRED_CHUNKS__" type="application/json">
            [
                179,
                357,
                782,
                308,
                159,
                329
            ]</script>
        <script id="__LOADABLE_REQUIRED_CHUNKS___ext" type="application/json">
            {
                "namedChunks": [
                    "PostView",
                    "LazyPlaceSelector"
                ]
            }</script>
        <script type="application/ld+json">
            [
                {
                    "web_info": {
                        "city_persian": "تهران",
                        "district_persian": "یوسف‌آباد",
                        "category_slug_persian": "فروش آپارتمان",
                        "title": "۹۷ متر ۲ خواب دونبش \u002F\u002F دید ابدی"
                    },
                    "name": "۹۷ متر ۲ خواب دونبش \u002F\u002F دید ابدی",
                    "image": "https:\u002F\u002Fs100.divarcdn.com\u002Fstatic\u002Fphoto\u002Fneda\u002Fwebp_post\u002FctqDuy-S76vGZAxvffrTCg\u002F43cff8b2-eb49-4012-8e90-3f565fc0ef29.webp",
                    "numberOfRooms": "دو",
                    "accommodationCategory": "فروش آپارتمان",
                    "geo": {
                        "longitude": "51.405345168845",
                        "@type": "GeoCoordinates",
                        "address": "تهران, یوسف‌آباد",
                        "latitude": "35.73463475119"
                    },
                    "@context": "https:\u002F\u002Fschema.org",
                    "description": "بهترین واحد در منطقه رو از دست نده! \n\n⚜️ ۲ خواب، دونبش، غرق نور، با دید ابدی و بدون مشرف\n⚜️ نقشه عالی و سالن مربع شکل که هر جور بچینی قشنگه\n⚜️ خواب‌ها استاندارد و بزرگ هستن.\n⚜️ دو ساله، کلید نخورده و آماده تحویل!\n⚜️ ورودی از لابی شیک و سرایدار مقیم برای امنیت بیشتر.\n\nکارشناس فروش منطقه، REDACTED\n برای هماهنگی و بازدید، پیام بدین یا تماس بگیرین.",
                    "floorSize": {
                        "value": "97",
                        "unitCode": "MTK",
                        "@type": "QuantitativeValue"
                    },
                    "@type": "Apartment",
                    "url": "https:\u002F\u002Fdivar.ir\u002Fv\u002F۹۷-متر-۲-خواب-دونبش-دید-ابدی\u002Fgap5-Twe"
                }
            ]</script>
    </body>
</html>
```
