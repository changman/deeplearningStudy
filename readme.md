# 설치

## Windows 10 환경에서 prophet 설치

* 사전 준비
    [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

```bash
1. 원하는 콘다 환경 생성
#conda create --name prophet python=3.7
2. 원하는 Conda 환경 Activate
#activate prophet
3. fbprophet 설치
##conda install -c conda-forge fbprophet

4. "fbprophet importing plotly failed." 에러 발생 시
#pip install plotly

5. pandas_datareader 설치
#pip install pandas_datareader
```

* VSCode 환경에서 graph 가 보이지 않을 경우 
  * [How to show graph in Visual Studio Code itself?](https://stackoverflow.com/questions/49992300/how-to-show-graph-in-visual-studio-code-itself)

## xgboot 설치하기
* anaconda3에서 제공하는 패키징 기능으로 xgboost 설치하기. 

```bash
1. 원하는 콘다 환경 생성
#conda create --name deeplearning python=3.7
2. 원하는 Conda 환경 Activate
#activate deeplearning
3. py-xgboost 설치
#conda install -c anaconda py-xgboost

4. pandas 설치
#pip install pandas
#pip install pandas_datareader

5. matplotlib 설치
#pip install matplotlib

6. tqdm 설치 (콘솔에서 진행 바 표시, lotto.py 실행 시 필요)
#pip install tqdm

7. scikit-learn (lotto.py 실행 시 필요)
#pip install scikit-learn 
#pip install -U scikit-learn 
```

# 소스구성
* DataFrame_Tes.py
    * DataFrame sample.
* time_series_test.py
    * dataframe 을 이용한 time series 테스트.
* xgboost_test.py 
    * xgboost 를 이용한 주식 종가 예측 프로그램.
* lotto.py 
    * xgboost 를 이용한 Lotto 번호 6개 합 예측

# 참고
  * [[Python!] Prophet 알아보기 & 설치 방법](https://steemit.com/kr/@yoon/python-prophet-and)
  * [[Ai] Prophet Tutorial #1 - Installation & Quick Start](https://zamezzz.tistory.com/276)
  * [prophet 홈](https://facebook.github.io/prophet/)
