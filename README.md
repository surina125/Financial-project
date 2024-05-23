
# PIGGY

**목차**
1. 팀원 정보 및 분담 내역
2. 설계 내용(아키텍처 등) 및 실제 구현정도
3. 데이터베이스 모델링(ERD)
4. 금융 상품 추천 알고리즘에 대한 기술적 설명
5. 서비스 대표 기능들에 대한 설명
6. 프로젝트 후기(느낀점)

<br>

## 팀원 정보 밑 업무 분담 내역

- 프로젝트 기간 : 2024/05/16 ~2024/05/24(약 9일)

<br>

### 팀 프로젝트 구성 및 역할

| 이름       | 역할 및 구현기능 |
|------------|------------------|
| 정현수<br>(팀장) | **Back End** - 회원 커스터마이징, 추천 알고리즘 구현<br>**Front End** - 메인페이지, 회원가입, 로그인, 프로필 페이지, 금융상품 비교, 금융상품 추천, 데이터 시각화, AI 챗봇 |
| 고도연     | **Back End** - ERD, 금융상품 + 환율 데이터 저장, 금융상품 + 환율 + 게시판 RESTful 구현<br>**Front End** - 게시판 CRUD, 근처 은행 검색, 환율 계산기 |

<br>

## 설계 내용 (아키텍처 등) 및 실제 구현 정도

처음에 기획한 페이지 레이아웃 구성과 기능들을 다 구현하였습니다.

<br>

### 기술 스택

| 구분   | 기술 스택 |
|--------|------------|
| **front** | language - JavaScript<br>framework - Vue3, pinia (+pinia-plugin-persistedstate), axios, chart.js |
| **back**  | language - Python<br>framework - Django, Flask, OAuthlib, Requests-OAuthlib, drf-spectacular, Django-extensions, Jupyter, IPython |

<br>

## 데이터베이스 모델링(ERD)
<br>

![ERD](https://github.com/surina125/Financial-project/assets/156388715/206a7add-c17a-409d-8c5c-17dca67db368)

<br>

## API 명세서

<br>

## 금융 상품 추천 알고리즘에 대한 기술적 설명

1. 추천 알고리즘 <br>
- 프로필 정보에 입력된 나이, 연봉, 자산으로 유클리드거리 측정해서 유사도 판단하기<br>
  (1) 유저모델을 쿼리셋 형태로 불러와 필요한 컬럼만 데이터 프레임 형태로 변환합니다.<br>
  (2) 그 후 로그인한 사용자와 다른 사용자들 간의 유클리드 거리를 계산해서 sort합니다.<br>
  (3) 예금, 적금, 대출 상품들의 합이 10이상이 될 때까지, 가장 높은 유사도를 가진 사용자들부터 각각 상품 목록에 중복을 제거하여 추가합니다.<br>
  
2. 추천 알고리즘<br>
- 설문조사를 통해 금융상품 추천하기<br>
  (1) 예금의 경우: 예치기간, 최소한의 금리, 선호하는 은행 선택<br>
    1단계) 선택한 은행과 기간, 금리가 조건에 맞는 예금을 필터링합니다.<br>
    2단계) 결과가 10개 미만일 때 추가 필터링: 기간, 금리가 조건에 맞는 예금을 필터링합니다. 그 후 중복을 제거하여 추천목록에 추가합니다.<br>
    3단계) 1+2단계 결과가 10개 미만일 때 추가 필터링: 기간이 조건에 맞는 예금을 필터링하여 금리가 높은 순으로 정렬합니다. 그 후 추천예금목록에 담긴 상품들이 10개까지 될 때까지 중복을 제거하여 추천목록에 추가합니다.<br>
    4단계) 필터링된 결과를 recommendStore.deposits에 저장합니다. 그리고 선택한 기간을 recommendStore.deposits_period에 저장합니다.
 
  (2) 적금의 경우: 적금유형(전체/정기/자유), 예치기간, 최소한의 금리, 선호하는 은행 선택<br>
        1단계) 선택한 적금유형, 은행, 기간, 금리가 조건에 맞는 적금을 필터링합니다.<br>
        2단계) 결과가 10개 미만일 때 추가 필터링: 선택한 적금유형, 기간, 금리가 조건에 맞는 적금을 필터링합니다. 그 후 중복을 제거하여 추천목록에 추가합니다.<br>
        3단계) 1+2단계 결과가 10개 미만일 때 추가 필터링: 선택한 적금유형, 기간이 조건에 맞는 적금을 필터링하여 금리가 높은 순으로 정렬합니다. 그 후 추천적금목록에 담긴 상품들이 10개까지 될 때까지 중복을 제거하여 추천목록에 추가합니다.<br>
        4단계) 필터링된 결과를 recommendStore.savings에 저장합니다. 그리고 선택한 기간과 적금유형을 recommendStore.savings_period, recommendStore.savings_type에 저장합니다.
  
  (3) 주택담보대출의 경우: 담보유형(아파트/아파트외), 선호하는 보험사 선택<br>
    1단계) 선택한 담보유형(아파트/아파트외), 보험사 조건에 맞는 주택담보대출을 필터링합니다. <br>
    2단계) 결과가 10개 미만일 때 추가 필터링: 선택한 담보유형에 맞는 대출을 필터링하여 금리가 낮은 순으로 정렬하여 중복을 제거하여 추천대출목록에 추가합니다.<br>
    3단계) 필터링된 결과를 recommendStore.loas에 저장합니다. 그리고 선택한 적금유형을 recommendStore.loas_type에 저장합니다.


3. 추천 알고리즘
   - gpt를 이용하여 추천받기
     1단계) 금융상품을 추천받고 싶다고 사용자가 입력하면 [추천] => 예금, 적금, 대출 중에 어떤 상품을 원하는지 질문 <br>
     2단계) 예금, 적금, 주택담보대출 중에 사용자가 원하는 상품을 입력하면 [예금, 적금, 대출] => 선호하는 은행을 질문 <br>
     3단계) 예적금의 경우 은행명/ 적금의 경우 보험사명을 말하면 => 해당 금융회사 상품들 중 관심 상품(like_user로 판단)으로 가장 많이 등록된 상품을 추천해 줍니다. <br>

## 서비스 대표 기능들에 대한 설명

1. 메인페이지
2. 로그인 회원가입 페이지
3. 프로필 페이지
4. 금융 상품 추천 페이지
5. 금융 상품 조회 페이지
6. 환율 계산기 페이지
7. 주변 은행 검색 페이지
8. 금융 상품 추천 커뮤니티 페이지
9. 재테크 정보 페이지

<br>

## 프로젝트 후기(느낀점)

- 정현수:
- 고도연: 1학기 동안 빠르게 익혔던 Django, Vue3 내용을 활용할 수 있는 소중한 시간이었다. 각각의 프레임워크 사용에 아직 익숙치 않았기 때문에, 프로젝트 기간동안 다양한 기능을 구현하는 과정이 쉽지 않았다. 오류 투성이인 기능들을 보면서 좌절감에 빠지기도 했지만, 덕분에 백엔드와 프론트엔드 간의 전체적 흐름을 제대로 파악할 수 있었다. 특히 수업시간에 자세히 다루지 않았던 내용들을 혼자 혹은 팀원과 함께 해결해나가는 과정에서 이전에 부족했던 문제해결능력이 점차 향상되어간다는 생각이 들었다. 또한 프로젝트 진행기간이 짧았기 때문에 부가적인 기능들을 더 구현해보지 않았던 점이 아쉬웠다. 

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
