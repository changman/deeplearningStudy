# 설치환경

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