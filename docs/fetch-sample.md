> نمونه‌های خام Captured از DevTools (فقط مرجع؛ این فایل را ویرایش نکنید).
> تحلیل کامل ساختار درخواست/پاسخ و نگاشت فیلدها: [`divar-api.md`](divar-api.md) — طرح کانفیگ متناظر: [`configuration.md`](configuration.md)

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
    "bottom_description_text": "آژانس ملکاتو در سعادت\u200cآباد",
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
    "bottom_description_text": "آژانس املاک آبتین در سعادت\u200cآباد",
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
    "bottom_description_text": "املاک یوسفيان      در سعادت\u200cآباد",
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
    "bottom_description_text": "مشاور اقای تهرانی در سعادت\u200cآباد",
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
    "bottom_description_text": "آژانس مسکن رازان میرداماد در دریا",
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
    "bottom_description_text": "آژانس مسکن متراژ در سعادت\u200cآباد",
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
await fetch("https://api.divar.ir/v8/postlist/w/search", {
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
    "bottom_description_text": "مشاوره تخصصی املاک نارمک محمدی در مدائن",
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
    "bottom_description_text": "آژانس گروه مشاورین املاک ایده نو نارمک در هفت حوض",
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
    "bottom_description_text": "املاک بزرگ دلتا کاسپین در دردشت",
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
    "bottom_description_text": "آژانس املاک بزرگ اسکان در هفت حوض",
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
    "bottom_description_text": "مسکن سیاوش در هفت حوض",
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
    "bottom_description_text": "مسکن پرستیژ در درختی",
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
    "bottom_description_text": "املاک بزرگ دلتا کاسپین در دردشت",
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
    "bottom_description_text": "آژانس شاهان در گلستان (شهرک راه آهن)",
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
    "bottom_description_text": "سرزمین ملکی راشا در گلستان (شهرک راه آهن)",
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
    "bottom_description_text": "مسكن نور ۰ مقدم در گلستان (شهرک راه آهن)",
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
    "bottom_description_text": "آژانس شاهان در گلستان (شهرک راه آهن)",
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
    "bottom_description_text": "آژانس خانه ايران شعبه بلوار در سعادت\u200cآباد",
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
    "bottom_description_text": "املاک بزرگ ارمان نارمک در هفت حوض",
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
    "bottom_description_text": "املاک رشید در آسمان",
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

