 

import base64, codecs
magic = 'ZnJvbSBiYW5fTWFpbGVyX1ggaW1wb3J0ICoKZnJvbSBzZW5kZXIuTWFpbCBpbXBvcnQgKgpmcm9tIHNlbmRlci5TTVN4IGltcG9ydCAqCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUKaW1wb3J0IHRpbWUKaW1wb3J0IG9zCgoKZGVmIFN0YXJ0KCk6CiAgICBvcy5zeXN0ZW0oJ2Nscycgb3IgJ2NsZWFyJykKICAgIG1pbGVyX2JhbigpCgogICAgeW91X3dhbnQgPSBpbnQoaW5wdXQoZidbe0ZvcmUuQ1lBTn0/e0ZvcmUuV0hJVEV9XSBFbnRlciBudW1iZXIgOicpKQoKICAgIGlmIHlvdV93YW50ID09IDE6CiAgICAgICAgCiAgICAgICAgb3Muc3lzdGVtKCdjbHMnIG9yICdjbGVhcicpCiAgICAgICAgbWFpbGVyXzEoKQogICAgICAgIAogICAgICAgICMgZW1haWwgc2VuZGVyCiAgICAgICAgeW91cl9tYWlsID0gc3RyKGlucHV0KGYnW3tGb3JlLkJMVUV9P3tGb3JlLldISVRFfV0gRW50ZXIgbWFpbCBzZW5kZXIgOicpKQogICAgICAgICMgcGFzc3dvcmQgZW1haWwgc2VuZGVyCiAgICAgICAgcGFzc3dvcmRfbWFpbCA9IHN0cihpbnB1dChmJ1t7Rm9yZS5CTFVFfT97Rm9yZS5XSElURX1dIEVudGVyIHBhc3N3b3JkIG1haWwgc2VuZGVyIDonKSkKICAgICAgICAjIHNlbmQgdG8KICAgICAgICBzZW5kX3RvID0gc3RyKGlucHV0KGYnW3tGb3JlLkJMVUV9P3tGb3JlLldISV'
love = 'ESsI0tEJ50MKVtoJScoPO0olN6WlxcPtbtVPNtVPNtVPZtoJImp2quPvNtVPNtVPNtoJImp2SaMFN9VUA0pvucoaO1qPuzW1g7Ez9lMF5PGSISsG97Ez9lMF5KFRyHEK1qVRIhqTIlVT1yp3AuM2HtBvpcXDbtVPNtVPNtVNbtVPNtVPNtVSAyozEmVQ0tGJScoUtbXDbtVPNtVPNtVSAyozEmYz9hMI9gLJyfXUyiqKWsoJScoPjtpTSmp3qipzEsoJScoPjtp2IhMS90oljtoJImp2SaMFxXPvNtVPOyoTyzVUyiqI93LJ50VQ09VQV6PvNtVPNtVPNtPvNtVPNtVPNto3Zhp3ymqTIgXPqwoTIupvpcPvNtVPNtVPNtoJScoTIlKmVbXDbtVPNtVPNtVNbtVPNtVPNtVPZtMJ1unJjtp2IhMTIlPvNtVPNtVPNtrJ91py9gLJyfVQ0tp3ElXTyhpUI0XTLaJ3gTo3WyYxWZIHI9C3gTo3WyYyqVFIESsI0tEJ50MKVtoJScoPOmMJ5xMKVtBvpcXDbtVPNtVPNtVPZtpTSmp3qipzDtMJ1unJjtp2IhMTIlPvNtVPNtVPNtpTSmp3qipzEsoJScoPN9VUA0pvucoaO1qPuzW1g7Ez9lMF5PGSISsG97Ez9lMF5KFRyHEK1qVRIhqTIlVUOup3A3o3WxVT1unJjtp2IhMTIlVQbaXFxXVPNtVPNtVPNwVUAyozDtqT8XVPNtVPNtVPOmMJ5xK3EiVQ0tnJ5jqKDbMvqor0MipzHhDxkIEK0/r0MipzHhI0uWIRI9KFOSoaEypvOfnKA0VTMcoTHtoJScoPN6WlxXVPNtVPNtVPNwVT1yp3AaLDbtVPNtVPNtVT1y'
god = 'c3NnYSA9IHN0cihpbnB1dChmJ1t7Rm9yZS5CTFVFfT97Rm9yZS5XSElURX1dIEVudGVyIG1lc3NhZ2UgOicpKQoKICAgICAgICBTZW5kUyA9IE1haWx4KCkKICAgICAgICBTZW5kUy5saXN0X21haWwoeW91cl9tYWlsLCBwYXNzd29yZF9tYWlsLCBzZW5kX3RvLCBtZXNzZ2EpCiAgICAgICAgCgogICAgZWxpZiB5b3Vfd2FudCA9PSAzIDoKICAgICAgICAKICAgICAgICBvcy5zeXN0ZW0oJ2NsZWFyJykKICAgICAgICBtYWlsZXJfMigpCiAgICAgICAgcHJpbnQoZid7Rm9yZS5SRUR9IHlvdSBjYW4gc2VuZCBvbmUgbWVzc2FnZSBpbiBkYXkgLi4uIHtGb3JlLldISVRFfVxuJykKICAgICAgICB0aW1lLnNsZWVwKDEpCgogICAgICAgIE51bWJlcnggPSBpbnB1dChmJ1t7Rm9yZS5DWUFOfT97Rm9yZS5XSElURX1dIEVudGVyIG51bWJlciB0YXJnZXQgOiAnKQogICAgICAgIE1lc3NhZ2V4ID0gaW5wdXQoZidbe0ZvcmUuQ1lBTn0/e0ZvcmUuV0hJVEV9XSBFbnRlciBNZXNzYWdlIDogJykKCiAgICAgICAgU2VuZCA9IFNNUyhOdW1iZXJ4LCBNZXNzYWdleCkKICAgICAgICBTZW5kLlNNU190ZXh0YmVsdCgpCgogICAgZWxpZiB5b3Vfd2FudCA9PSA0IDoKICAgICAgICAKICAgICAgICBvcy5zeXN0ZW0oJ2NsZWFyJykKICAgICAgICBtYWlsZXJfMSgpCiAgICAgICAgcHJpbn'
destiny = 'DbMvW7Ez9lMF5FEHE9VTyzVUyiqFOxo24aqPObLKMyVUE3nJkcolOaolO0olNaVTu0qUOmBv8iqUqcoTyiYzAioFNaVSkhVTShMPOmnJ5aVUIjVP57Ez9lMF5KFRyHEK0vXDbXVPNtVPNtVPOBo25yKlN9VTyhpUI0XPqpoyOlMKAmVSftEJ50MKVtKFO0olOwo250nJ51MFNhYv4tWlxXPvNtVPNtVPNtoaIgVQ0tnJ5jqKDbMvqor0MipzHhD1yOGa0/r0MipzHhI0uWIRI9KFOSoaEypvOhqJ1vMKVtqTSlM2I0VQbtWlxXVPNtVPNtVPOgMKAmVQ0tnJ5jqKDbMvqor0MipzHhD1yOGa0/r0MipzHhI0uWIRI9KFOSoaEypvOgMKAmLJqyVQbtWlxXVPNtVPNtVPOmnJDtCFOcoaO1qPuzW1g7Ez9lMF5QJHSBsG97Ez9lMF5KFRyHEK1qVRIhqTIlVSAWEPN6VPpcPvNtVPNtVPNtqT9eVQ0tnJ5jqKDbMvqor0MipzHhD1yOGa0/r0MipzHhI0uWIRI9KFOSoaEypvO0o2gyovN6VPpcPvNtVPNtVPNtrJ91pvN9VTyhpUI0XTLaJ3gTo3WyYxAMDH59C3gTo3WyYyqVFIESsI0tEJ50MKVtrJ91pvOhqJ1vMKVtBvNaXDbXVPNtVPNtVPOGEH5RVQ0tH01GXT51oFjtoJImpljtp2yxYPO0o2ffVUyiqKVcPvNtVPNtVPNtH0IBEP5GGIAsqUqcoTyiXPxXPvNtVPOyoTyzVUyiqI93LJ50VQ09VQx5VQbXVPNtVPNtVPOjpzyhqPtaE29iMPOvLKxtYv4hWlxXVPNtVPNtVPOyrTy0XPxXPyA0LKW0XPxX'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
