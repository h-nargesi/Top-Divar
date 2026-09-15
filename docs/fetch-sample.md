> نمونه‌های خام Captured از DevTools (فقط مرجع؛ این فایل را ویرایش نکنید).
> تحلیل کامل ساختار درخواست/پاسخ و نگاشت فیلدها: [`divar-api.md`](divar-api.md) — طرح کانفیگ متناظر: [`configuration.md`](configuration.md)

## search

```js
fetch("https://api.divar.ir/v8/postlist/w/search", {
  "headers": {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.8",
    "baggage": "sentry-environment=client,sentry-release=release-the-wall-matching-5260ce73,sentry-public_key=7e7d19d51ebe4bd5955fda8ab50107b1,sentry-trace_id=29782daa5ab3ccf923493dcb1db20caf,sentry-sampled=false,sentry-sample_rand=0.9305946880091628,sentry-sample_rate=0.01",
    "content-type": "application/json",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Brave\";v=\"152\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1",
    "sentry-trace": "29782daa5ab3ccf923493dcb1db20caf-4f845f37c75ca1dd-0",
    "traceparent": "00-29782daa5ab3ccf923493dcb1db20caf-4f845f37c75ca1dd-00",
    "tracestate": "sentry.sampled_not_recording=1,sentry.sample_rand=0.9305946880091628,sentry.sample_rate=0.01,sentry.url=https://api.divar.ir/v8/postlist/w/search",
    "x-render-type": "CSR",
    "x-screen-size": "2328x654",
    "x-standard-divar-error": "true",
    "x-web-serving-mode": "desktop"
  },
  "referrer": "https://divar.ir/",
  "body": "{\"source_view\":\"FILTER\",\"pagination_data\":{\"@type\":\"type.googleapis.com/post_list.PaginationData\",\"last_post_date\":\"2026-09-15T08:25:33.266302Z\",\"page\":1,\"layer_id\":1,\"search_uid\":\"45c38199-af25-401d-b638-148f013a39e5\",\"cumulative_widgets_count\":8,\"viewed_tokens\":\"H4sIAAAAAAAE/wTAsQqAIBAG4Be6JWhol1oqMJSc/8B+5CAuI/Lx+whDN60qhLldYxLCQhz6RwhzUcMthKXi3ybENX9avBBnPsZchTC3tbr8AQAA//9EZfSqRwAAAA==\",\"search_bookmark_info\":{\"search_hash\":\"7a1de9fa3c0ccce4e03702b0c5d99f52\",\"bookmark_state\":{},\"alert_state\":{}},\"first_page_viewed_at\":\"2026-09-15T19:47:18.548447651Z\",\"filters_hash\":\"eh3p+jwMzOTgNwKwxdmfUg==\"},\"disable_recommendation\":false,\"map_state\":{\"camera_info\":{\"bbox\":{}}},\"search_data\":{\"form_data\":{\"data\":{\"warehouse\":{\"boolean\":{\"value\":true}},\"elevator\":{\"boolean\":{\"value\":true}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"40\",\"654\",\"75\",\"907\",\"929\",\"992\"]}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"parking\":{\"boolean\":{\"value\":true}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"price\":{\"number_range\":{\"minimum\":\"10000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"10000000000\",\"maximum\":\"60000000000\"}}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}}}},\"server_payload\":{\"@type\":\"type.googleapis.com/widgets.SearchData.ServerPayload\",\"additional_form_data\":{\"data\":{\"sort\":{\"str\":{\"value\":\"sort_date\"}}}}}},\"city_ids\":[\"1\"],\"user_selected_location\":{\"places\":[{\"place_id\":\"1\"}]},\"previous_user_selected_location\":{\"places\":[]}}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
});
```
response:
```json
{
  "action_log": {
    "server_side_info": {
      "info": {
        "@type": "type.googleapis.com/action_log.PostListLoadPageInfo",
        "cities": ["1"],
        "current_tab": "default",
        "search_data": {
          "form_data_json": "{\"data\":{\"building-age\":{\"number_range\":{\"minimum\":\"0\",\"maximum\":\"15\",\"value\":{\"minimum\":\"0\",\"maximum\":\"15\"}}},\"category\":{\"str\":{\"value\":\"apartment-sell\"}},\"districts\":{\"repeated_string\":{\"value\":[\"198\",\"399\",\"40\",\"654\",\"75\",\"907\",\"929\",\"992\"]}},\"elevator\":{\"boolean\":{\"value\":true}},\"floor\":{\"number_range\":{\"minimum\":\"-1\",\"maximum\":\"6\",\"value\":{\"minimum\":\"-1\",\"maximum\":\"6\"}}},\"parking\":{\"boolean\":{\"value\":true}},\"price\":{\"number_range\":{\"minimum\":\"10000000000\",\"maximum\":\"60000000000\",\"value\":{\"minimum\":\"10000000000\",\"maximum\":\"60000000000\"}}},\"price_per_square\":{\"number_range\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\",\"value\":{\"minimum\":\"256000000\",\"maximum\":\"900000000\"}}},\"rebuilt\":{\"boolean\":{\"value\":true}},\"recent_ads\":{\"str\":{\"value\":\"1d\"}},\"rooms\":{\"repeated_string\":{\"value\":[\"یک\",\"دو\",\"سه\",\"چهار\"]}},\"size\":{\"number_range\":{\"minimum\":\"40\",\"maximum\":\"140\",\"value\":{\"minimum\":\"40\",\"maximum\":\"140\"}}},\"sort\":{\"str\":{\"value\":\"sort_date\"}},\"warehouse\":{\"boolean\":{\"value\":true}}}}",
          "sort": "sort_date",
          "cities": ["1"],
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
        "page": 1,
        "pelle": {
          "elastic": {}
        },
        "last_post_date_epoch": "-62135596800000000",
        "search_id": "75b6f38562312aaaad7822a9a54ac3da",
        "search_uid": "45c38199-af25-401d-b638-148f013a39e5",
        "source_view": "MAP_DISCOVERY_MAP",
        "jli": {
          "elevator": true,
          "rebuilt": true,
          "floor": {
            "min": -1,
            "max": 6
          },
          "size": {
            "min": 40,
            "max": 140
          },
          "category": {
            "value": "apartment-sell"
          },
          "districts": {
            "vacancies": ["198", "399", "40", "654", "75", "907", "929", "992"]
          },
          "warehouse": true,
          "sort": {
            "value": "sort_date"
          },
          "parking": true,
          "places": {
            "value": ["1"]
          },
          "price_per_square": {
            "min": 256000000,
            "max": 900000000
          },
          "rooms": {
            "value": ["یک", "دو", "سه", "چهار"]
          },
          "price": {
            "max": 60000000000,
            "min": 10000000000
          },
          "building-age": {
            "min": 0,
            "max": 15
          },
          "recent_ads": {
            "value": "1d"
          },
          "cities": ["1"]
        },
        "search_layer": "fulltext_t2",
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
      "layer_id": 1,
      "search_uid": "45c38199-af25-401d-b638-148f013a39e5",
      "cumulative_widgets_count": 8,
      "viewed_tokens": "H4sIAAAAAAAE/wTAsQqAIBAG4Be6JWhol1oqMJSc/8B+5CAuI/Lx+whDN60qhLldYxLCQhz6RwhzUcMthKXi3ybENX9avBBnPsZchTC3tbr8AQAA//9EZfSqRwAAAA==",
      "search_bookmark_info": {
        "search_hash": "7a1de9fa3c0ccce4e03702b0c5d99f52",
        "bookmark_state": {},
        "alert_state": {}
      },
      "first_page_viewed_at": "2026-09-15T19:47:18.548447651Z",
      "filters_hash": "dbbzhWIxKqqteCKppUrD2g=="
    }
  },
  "search_id": "75b6f38562312aaaad7822a9a54ac3da",
  "show_no_search_result_notice": true
}
```
