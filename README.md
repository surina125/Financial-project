# Financial-project
## 프로젝트 목표
#### 싸피 출신 개발자 최차윤은 드디어 취업에 성공 했습니다.
#### 결혼 후 자가마련을 위해 재테크 계획을 세우려고 합니다.
#### 그런데, 신입사원이라 은행에 갈 시간이 없어 금융 정보를 한 곳에 알 수 있는 웹 애플리케이션을 직접 만들어 보려고 합니다.




# 팀명 및 프로젝트 간략 설명

**목차**
1. 팀원 정보 및 분담 내역
2. 설계 내용(아키텍처 등) 및 실제 구현정도
3. 데이터베이스 모델링(ERD)
4. 금융 상품 추천 알고리즘에 대한 기술적 설명
5. 서비스 대표 기능들에 대한 설명
6. 프로젝트 후기(느낀점)

## 팀원 정보 밑 업무 분담 내역

- 프로젝트 기간 : 2024/05/16 ~2024/05/24(약 9일)

### 팀 프로젝트 구성 및 역할

| 이름       | 역할 및 구현기능 |
|------------|------------------|
| 정현수<br>(팀장) | **Back End** - 회원 커스터마이징, 추천 알고리즘 구현, 금융상품 URL(최종수정)<br>**Front End** - 메인페이지, 회원가입, 로그인, 프로필 페이지, 금융상품 비교, 금융상품 추천, AI 챗봇 |
| 고도연     | **Back End** - ERD, 금융상품 + 환율 데이터 저장, 금융상품 + 환율 + 게시판 RESTful 구현<br>**Front End** - 게시판 CRUD, 근처 은행 검색, 환율 계산기 |

## 설계 내용 (아키텍처 등) 및 실제 구현 정도

### 기술 스택

| 구분   | 기술 스택 |
|--------|------------|
| **front** | language - JavaScript<br>framework - Vue3, pinia (+pinia-plugin-persistedstate), axios, chart.js |
| **back**  | language - Python<br>framework - Django, Flask, OAuthlib, Requests-OAuthlib, drf-spectacular, Django-extensions, Jupyter, IPython |

## 데이터베이스 모델링(ERD)
<br>



## error

```
// accounts/serializers.py - 현수
from dj_rest_auth.serializers import UserDetailsSerializer

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        pass
```
UserDetailsSerializer가 undefined되었다고 error나왔었는데 import를 안해서 오류 났었다.
<br>
post보낼때 headers도 같이 안보내서 401에러남
<br>

#### 도연

```
# exchange/models.py  + exchange/views.py- 도연
if exchange_infos:
                # db에 데이터가 존재X, db 저장
                if not result: 
                        serializer = ExchangeSerializer(data=exchange_infos, many=True)
                        if serializer.is_valid(raise_exception=True):          
                                serializer.save()
                        return Response(serializer.data)

```
유효성 검사를 통과하지 못해서 오류 발생 + db 저장이 안됐었다.
json파일의 키 값과 모델의 필드 값이 일치하지 않았기 때문이었다.



### 강사님께 질문
1. export depault사용해야 하는지 <- 해야 한다면 마지막에 다 넣기

## 계획

5/16(목) <br>
현수: detail 페이지 완성(차트 생각 - 대출 +예적금 페이지)
<br>
도연 : 환율 데이터 저장, 데이터 조회 함수(예,적금, 대출, 환율) 작성, 금리계산 함수 작성  

5/17(금) <br>
현수: 프로필 페이지(상품 가입이랑 관심상품 저장 잘 작동하는 지 확인)조회, 디테일페이지 완성하기! + 유저 외래키로 받는 모델 하나 더 추가 
<br>
도연 : 게시판 back 코드 완성, 데이터 조회 함수 수정

5/18(토) <br>
현수: 추천알고리즘, 프로필페이지 구현
<br>
도연 : 게시판 페이지 구현, +...

### 새롭게 알게된 점
##### 현수
error문구를 많이 보다보니까 어느정도 에러에 익숙해지는 느낌이다. 에러코드랑 문구를 보고 해석하는 방법을 배우게 되었다.

##### 도연

<br>

### 평가 요소

1. 초기 아이디어를 얼마나 구현 했는지?
2. 프로젝트 명세서 요구사항을 얼마나 충족 했는지?
3. 구현된 기능은 철저한 테스트를 통해 에러없이 작동이 잘 되는지?
4. 각각의 기능은 정확한 데이터를 추출하여 제공되는지?
5. 주어진 기능을 수행하는데 사용자 중심의 UI와 동작성을 보여주는지?
6. 적절한 컴포넌트 구성과 css를 활용하여 가독성이 좋은지?
7. 사용자가 필요로 하는 유용한 정보와 기능이 사용하기 편하게 제공이 되고 있는지?
8. 발표 준비자료 그리고 발표력이 프로젝트 결과를 잘 전달하고 있는지?
9. 팀원간의 협력이 원활하고 역할분담을 적절하게 하였는지?
10. 프로젝트 주제에 적합한 실용적인 기능이 추가적으로 구현이 되었는지?
11. readme 파일 등 프로젝트에 관한 문서화를 잘 하였는지?
12. 프로젝트 결과발표를 청중들이 충분히 이해하고 공감할 수 있도록 간단 명료하게 쉽게 설명을 잘 하는지?
