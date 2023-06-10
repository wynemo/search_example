# search_example

a DRF demo, with swagger

## Quick start

install docker(with docker compose), in bash, type `sh build.sh` to run this site, then in your browser,  access http://127.0.0.1:8000/swagger/

## how I setup

1. install python requirements, using django-admin, create a django project
2. create a app 
3. create model, do migration
4. import data from csv to database

## swagger example
![](/i/dd34672e-9a78-48b6-89fa-fcad81b8892b.jpg)

## benchmark
let's request 100 candidates for a request:
```
❯ cat post_loc.txt
{
  "skill_name": "backend",
  "page": 1,
  "page_size": 100
}
```

and use this to do benchmark:
```
❯ ab -p post_loc.txt -T application/json  -c 5 -n 500 http://10.0.1.65:8000/search_candidates/
```

when cache is not enabled, you can see,  you can see, the average request time is about ~1500ms
```
Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        3    8  12.9      5     107
Processing:  1343 1794 231.3   1774    2500
Waiting:     1332 1775 231.2   1756    2487
Total:       1352 1802 231.4   1778    2504

Percentage of the requests served within a certain time (ms)
  50%   1778
  66%   1898
  75%   1958
  80%   1996
  90%   2123
  95%   2196
  98%   2334
  99%   2367
 100%   2504 (longest request)
```

when cache is enabled, you can see, the average request time is about ~100ms, this is faster.

```

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        4   11  10.9      8     122
Processing:    24   52  71.7     40    1466
Waiting:        8   22  68.5     13    1418
Total:         31   63  72.7     49    1472

Percentage of the requests served within a certain time (ms)
  50%     49
  66%     62
  75%     68
  80%     71
  90%     83
  95%    128
  98%    147
  99%    152
 100%   1472 (longest request)
```
