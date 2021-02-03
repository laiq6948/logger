import requests, json

WEB_HOOK_URL = "WEB_HOOK_URL"
requests.post(WEB_HOOK_URL, data = json.dumps({
    'text': u'Notifycation From Python.',
    'username': u'Bakira-Tech-Python-Bot',
    'icon_emoji': u':smile_cat:',
    'link_names': 1,
}))
