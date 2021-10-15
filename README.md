# 키비 Friendly Fitness iOS app

참고 : https://www.youtube.com/channel/UCMMitT9SCbWlEcEkemnsxQg

### Kivy 설치
```
$ python3 -m venv kivyenv(가상환경이름)

$ source kivyenv/bin/activate

(kivyenv) $ python -m pip install kivy[base] kivy_examples
```

### Failed building wheel for Kivy-Garden 에러 발생 시
```
파이썬 버전 3.7 버전으로 해결 가능

$ virtualenv kivyenv --python=python3.7
```

### python3.7 설치
```
Ubuntu 기준

$ sudo apt update
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt install python3.7
```
